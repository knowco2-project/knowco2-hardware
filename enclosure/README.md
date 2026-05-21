# Enclosure Design Files

Hardware license: [CERN-OHL-S-2.0](../LICENSE-HARDWARE)

## Files

| File | Format | Use |
|------|--------|-----|
| `knowco2-enclosure.step` | STEP | Modify in any CAD tool |
| `knowco2-enclosure-main.stl` | STL | Print the main body |
| `knowco2-enclosure-lid.stl` | STL | Print the lid |
| `knowco2-enclosure.3mf` | 3MF | Print with slicer settings included |
| `knowco2-enclosure.shapr` | Shapr3D source | Original source file |

> Design files will be placed here. For now, see the `knowco2-3d-models/` folder at the root of this project for current versions.

## Current design versions

The enclosure has gone through multiple design iterations. The current production version is **version 10** (`knowco2-main-version10.step`).

Key design decisions:
- Designed around the Adafruit Feather ESP32-S3 Reverse TFT (34.8 mm × 22.9 mm)
- Sensor opening sized for Sensirion SCD4x
- USB-C access cutout on the short edge
- Three button cutouts aligned with Feather A / B / C buttons

## Printing recommendations

| Setting | Value |
|---------|-------|
| Material | PLA or PETG |
| Layer height | 0.2 mm |
| Infill | 15–20% |
| Supports | None required (designed to print without) |
| Perimeters | 3 |

## Modifying the design

Import the `.step` file into your preferred CAD tool:
- [FreeCAD](https://www.freecad.org) (free, open source)
- Fusion 360 (free for personal/hobby use)
- Shapr3D (original source format)
- Onshape, SolidWorks, etc.

Any modifications must be released under CERN-OHL-S-2.0.

## License notice

SPDX-License-Identifier: CERN-OHL-S-2.0
Source Location: https://github.com/knowco2-project/knowco2
