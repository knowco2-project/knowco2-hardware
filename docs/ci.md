# Hardware licensing CI

The hardware repository owns `.github/workflows/compliance.yml`, the license
texts, and `REUSE.toml`. Runner infrastructure belongs in **knowco2-cloud**, under
`ci/hardware-codebuild`; it is not managed in this hardware repository.
Infrastructure proposal: [knowco2-cloud PR #11](https://github.com/knowco2-project/knowco2-cloud/pull/11).

The workflow uses only the dedicated AWS CodeBuild self-hosted runner:

```yaml
runs-on:
  - codebuild-knowco2-hardware-ci-${{ github.run_id }}-${{ github.run_attempt }}
```

There is no GitHub-hosted or generic `self-hosted` fallback, and the website's
production deployment runner is not reused. GitHub still schedules and displays
jobs; execution is in AWS. A missing/disabled runner leaves the job queued, not
approved. A GitHub queue with no registered runner may need manual cancellation.

## What must pass

The existing `reuse` job checks its CodeBuild identity before checkout, refuses
external fork execution, and checks out without retaining GitHub credentials.
Checkout and Python setup are pinned to commit SHAs. It installs REUSE 6.2.0 and
PyYAML 6.0.2 in a temporary virtual environment, avoiding a Docker action and
privileged Docker. Top-level tool versions are pinned; transitive pip dependencies
are not yet hash-locked. The first AWS run must verify installation on the selected
image; do not treat local policy-test success as a completed REUSE run.

It runs the workflow policy regression tests, checks all repository workflows
against the approved runner/permissions/action-pin policy, compares `LICENSE`
byte-for-byte with `LICENSES/CERN-OHL-S-2.0.txt`, and runs `reuse lint` for file
copyright/license coverage. This does not establish legal compliance, certify
complete manufacturing source, or validate CAD geometry. Existing hardware,
documentation licenses, and production release review remain unchanged.

Local validation (Python 3.12 recommended):

```sh
python3 -m venv /tmp/knowco2-hardware-ci
/tmp/knowco2-hardware-ci/bin/python -m pip install 'reuse==6.2.0' 'PyYAML==6.0.2'
/tmp/knowco2-hardware-ci/bin/python -m unittest discover -s ci -p 'test_*.py' -v
/tmp/knowco2-hardware-ci/bin/python ci/check_workflows.py
cmp LICENSE LICENSES/CERN-OHL-S-2.0.txt
/tmp/knowco2-hardware-ci/bin/reuse lint
```

Keep the virtual environment outside the repository so it is not treated as
unlicensed source. New CI scripts use explicit SPDX headers; docs and the workflow
retain their existing REUSE annotations.

## Setup and security

Follow the cloud root's README. Its webhook is disabled by default and requires
an approved numeric GitHub actor allowlist and reviewed GitHub connection scope.
The workflow's name `Licensing compliance` must match its webhook filter.
GitHub source credentials are separate from `GITHUB_TOKEN`; a read-only workflow
does not remove the CodeBuild role's source-connection permissions. Do not use
this runner for arbitrary outside PR code or production deployments.

For an outside contribution, a maintainer reviews the exact code/workflow and
imports approved changes into a trusted branch. Do not remove the AWS actor filter,
switch to `pull_request_target`, or return a skipped green check to bypass a queue.
Re-run PR #1 after provisioning; do not merge based on a historical Ubuntu run.
Manual dispatch is available once this workflow exists on the default branch.

The policy checker is a regression guard, **not** an organization-level execution
restriction: an edited workflow can start before its own checks run. Protect the
workflow, CI scripts, and license changes with review/branch rules, restrict runner
access, and disable hosted runners in organization policy where supported. Those
administrative settings are not changed by this PR. Require a successful `reuse`
check for releases, verify its exact check name, and retain human license review.
