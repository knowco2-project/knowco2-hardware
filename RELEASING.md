# Hardware release procedure

Use an immutable Git tag so a manufactured product can be matched to the exact Covered Source used to make it.

1. Confirm that `main` contains the intended STEP, STL, reference-image, BOM, documentation, notice, and license files.
2. Add a dated entry to `CHANGES.md` and replace the `Unreleased` heading with the release identifier.
3. Confirm the Source Location is present on the Product, its packaging, or accompanying documentation.
4. Run `reuse lint` and resolve every missing or conflicting annotation.
5. Create an annotated tag using `kc2-01-hardware-vMAJOR.MINOR.PATCH`.
6. Publish a GitHub release from that tag and identify the production model/revision in its notes.
7. Preserve the tagged source at the Source Location for at least the period required by CERN-OHL-S v2.

Do not move or replace a published tag. If a released design changes, publish a new version and add a new `CHANGES.md` entry.
