# SPDX-FileCopyrightText: 2026 KnowCO2 LLC
# SPDX-License-Identifier: CC-BY-SA-4.0
"""Regression guard, not an authorization boundary; see docs/ci.md."""
from pathlib import Path
import re
import sys

import yaml

RUNNER = "codebuild-knowco2-hardware-ci-${{ github.run_id }}-${{ github.run_attempt }}"
ACTION = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_./-]+)?@[0-9a-f]{40}$")
EVENTS = {"pull_request", "push", "workflow_dispatch"}


class UniqueLoader(yaml.BaseLoader):
    """Treat YAML scalars as strings (including 'on'); reject duplicate keys."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if not isinstance(key, str) or key in result:
            raise ValueError("Duplicate or non-scalar YAML mapping key")
        result[key] = loader.construct_object(value_node, deep=True)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def check_workflow(text: str) -> list[str]:
    """Return policy violations without executing any workflow content."""
    try:
        workflow = yaml.load(text, Loader=UniqueLoader)
    except (yaml.YAMLError, ValueError) as exc:
        return [f"Invalid YAML: {exc}"]
    if not isinstance(workflow, dict):
        return ["Workflow must be a mapping"]
    errors = []
    events = workflow.get("on")
    if isinstance(events, str):
        events = [events]
    if not isinstance(events, (dict, list)) or not events or any(not isinstance(e, str) or e not in EVENTS for e in events):
        errors.append("Only pull_request, push and workflow_dispatch events are approved")
    if workflow.get("permissions") != {"contents": "read"}:
        errors.append("Workflow permissions must be exactly contents: read")
    jobs = workflow.get("jobs")
    if not isinstance(jobs, dict) or not jobs:
        return errors + ["Workflow must contain jobs"]
    for name, job in jobs.items():
        prefix = f"Job {name}: "
        if not isinstance(job, dict):
            errors.append(prefix + "job must be a mapping")
            continue
        if "uses" in job:
            errors.append(prefix + "reusable workflows need a separate runner-policy review")
        if job.get("runs-on") not in (RUNNER, [RUNNER]):
            errors.append(prefix + "only the exact dedicated CodeBuild label is allowed")
        if job.get("permissions", {"contents": "read"}) != {"contents": "read"}:
            errors.append(prefix + "permissions must remain read-only")
        if any(k in job for k in ("container", "services")):
            errors.append(prefix + "Docker containers/services are not approved")
        if job.get("continue-on-error", "false") != "false":
            errors.append(prefix + "failures must not be ignored")
        timeout = job.get("timeout-minutes", "")
        if not isinstance(timeout, str) or timeout not in {str(n) for n in range(1, 11)}:
            errors.append(prefix + "an explicit 1-10 minute timeout is required")
        steps = job.get("steps")
        if not isinstance(steps, list) or not steps:
            errors.append(prefix + "nonempty steps are required")
            continue
        for step in steps:
            if not isinstance(step, dict):
                errors.append(prefix + "step must be a mapping")
                continue
            if step.get("continue-on-error", "false") != "false":
                errors.append(prefix + "step failures must not be ignored")
            action = step.get("uses")
            if action is not None:
                if not isinstance(action, str) or ACTION.fullmatch(action) is None:
                    errors.append(prefix + "actions must be pinned to full commit SHAs")
                elif action.startswith("actions/checkout@"):
                    options = step.get("with", {})
                    if not isinstance(options, dict) or options.get("persist-credentials") != "false":
                        errors.append(prefix + "checkout must disable credential persistence")
    return errors


def main(root: Path) -> int:
    directory = root / ".github/workflows"
    paths = sorted([*directory.glob("*.yml"), *directory.glob("*.yaml")])
    if not paths:
        print("No workflow files found", file=sys.stderr)
        return 1
    failed = False
    for path in paths:
        try:
            errors = check_workflow(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as exc:
            errors = [str(exc)]
        for error in errors:
            print(f"{path.relative_to(root)}: {error}", file=sys.stderr)
            failed = True
    if not failed:
        print(f"CodeBuild-only policy passed for {len(paths)} workflow(s).")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main(Path(__file__).resolve().parents[1]))
