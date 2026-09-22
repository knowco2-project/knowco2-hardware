# Hardware design changes

This file records dated modifications to the KnowCO2 Covered Source. Do not remove prior applicable entries. Anyone conveying modified Covered Source should add the date and a brief description of each modification, as required by CERN-OHL-S v2 section 3.3(b).

## Unreleased

- 2026-09-22: Moved licensing CI to a dedicated AWS CodeBuild self-hosted runner managed in knowco2-cloud. Replaced the Docker licensing action with a pinned REUSE CLI, added runner-policy regression checks, and documented deployment and trusted-contributor boundaries. No geometry, BOM content, or license text changed.
- 2026-09-04: Clarified the hardware and documentation license boundaries, made the Source Location display requirement consistent, added complete license texts and machine-readable file coverage, and documented the versioned release process. No geometry or BOM content changed.

## Earlier design history

Earlier changes remain available in the repository's Git history. The first tagged hardware release should identify the exact commit used for manufacturing.
