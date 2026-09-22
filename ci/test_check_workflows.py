# SPDX-FileCopyrightText: 2026 KnowCO2 LLC
# SPDX-License-Identifier: CC-BY-SA-4.0
import unittest

from check_workflows import RUNNER, check_workflow

BASE = """name: Licensing compliance
on: [pull_request, push, workflow_dispatch]
permissions:
  contents: read
jobs:
  reuse:
    runs-on: ["RUNNER"]
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
        with:
          persist-credentials: false
      - run: reuse lint
""".replace("RUNNER", RUNNER)


class WorkflowPolicyTests(unittest.TestCase):
    def test_approved_workflow(self):
        self.assertEqual(check_workflow(BASE), [])

    def test_single_string_runner(self):
        self.assertEqual(check_workflow(BASE.replace(f'["{RUNNER}"]', RUNNER)), [])

    def test_blocked_runners(self):
        for runner in ("ubuntu-latest", "windows-latest", "macos-latest", "self-hosted",
                       "codebuild-knowco2-website-${{ github.run_id }}-${{ github.run_attempt }}",
                       "${{ matrix.runner }}", RUNNER + " image:ubuntu-7.0",
                       RUNNER + ", self-hosted"):
            with self.subTest(runner=runner):
                self.assertTrue(check_workflow(BASE.replace(RUNNER, runner)))

    def test_write_permissions(self):
        self.assertTrue(check_workflow(BASE.replace("contents: read", "contents: write")))

    def test_missing_permissions(self):
        self.assertTrue(check_workflow(BASE.replace("permissions:\n  contents: read\n", "")))

    def test_job_permission_override(self):
        self.assertTrue(check_workflow(BASE.replace("    steps:", "    permissions: write-all\n    steps:")))

    def test_unpinned_action(self):
        self.assertTrue(check_workflow(BASE.replace("11bd71901bbe5b1630ceea73d27597364c9af683", "v4")))

    def test_checkout_credentials(self):
        self.assertTrue(check_workflow(BASE.replace("persist-credentials: false", "persist-credentials: true")))

    def test_unsafe_events(self):
        for event in ("pull_request_target", "workflow_run"):
            with self.subTest(event=event):
                self.assertTrue(check_workflow(BASE.replace("pull_request", event)))

    def test_containers(self):
        for field in ("container: ubuntu:latest", "services: {db: {image: postgres}}"):
            with self.subTest(field=field):
                self.assertTrue(check_workflow(BASE.replace("    steps:", f"    {field}\n    steps:")))

    def test_ignored_failure(self):
        self.assertTrue(check_workflow(BASE.replace("    steps:", "    continue-on-error: true\n    steps:")))

    def test_ignored_step_failure(self):
        self.assertTrue(check_workflow(BASE.replace("      - run: reuse lint", "      - run: reuse lint\n        continue-on-error: true")))

    def test_timeout(self):
        for timeout in ("0", "11", "${{ inputs.timeout }}"):
            with self.subTest(timeout=timeout):
                self.assertTrue(check_workflow(BASE.replace("timeout-minutes: 10", f"timeout-minutes: {timeout}")))

    def test_duplicate_key(self):
        self.assertTrue(check_workflow(BASE.replace("  reuse:\n", "  reuse: {}\n  reuse:\n")))

    def test_invalid_input(self):
        for text in ("[", "[]", "null", "jobs: {}", "jobs: {bad: []}", BASE + "---\nother: doc"):
            with self.subTest(text=text):
                self.assertTrue(check_workflow(text))

    def test_reusable_workflow(self):
        self.assertTrue(check_workflow(BASE.replace("    steps:", "    uses: owner/repo/.github/workflows/job.yml@main\n    steps:")))

    def test_local_action(self):
        self.assertTrue(check_workflow(BASE.replace("actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683", "./some-action")))

    def test_malformed_steps(self):
        self.assertTrue(check_workflow(BASE.replace("      - run: reuse lint", "      - [bad]")))


if __name__ == "__main__":
    unittest.main()
