<!-- SPDX-FileCopyrightText: 2026 KnowCO2 LLC -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Hardware repository instructions

All CI execution must use the dedicated AWS CodeBuild self-hosted runner.
Never introduce GitHub-hosted runners, a generic self-hosted fallback, or the
website deployment runner. Do not add runner image/fleet/buildspec overrides.

Runner infrastructure belongs in `knowco2-project/knowco2-cloud`, under
`ci/hardware-codebuild`. This repository owns hardware files, licensing metadata,
and `.github/workflows/compliance.yml`. Keep `Licensing compliance` as the workflow
name unless its cloud webhook filter is updated in the same reviewed change.

Keep GitHub permissions read-only, pin remote actions to full commit SHAs, disable
checkout credential persistence, and keep external PR code away from production
privileges. Do not use `pull_request_target` or skip required licensing checks.
Run the tests and checks documented in `docs/ci.md`; state honestly which ran.
Preserve license notices and update `CHANGES.md` for applicable modifications.
