# Hardware

All hardware design files are released under the [CERN-OHL-S-2.0](LICENSE-HARDWARE) license.

## Folders

| Folder | Contents |
|--------|----------|
| [pcb/](pcb/) | Schematic and PCB layout files |
| [enclosure/](enclosure/) | 3D enclosure design files |
| [bom/](bom/) | Bill of materials |

## File formats

### PCB / schematic

OSHWA-preferred open formats:

| Format | Files | Purpose |
|--------|-------|---------|
| KiCad 8+ | `.kicad_sch`, `.kicad_pcb`, `.kicad_pro` | Source files — preferred for modification |
| Gerber + drill | `gerbers/` folder | Manufacturing — send to any PCB fab |
| PDF | `schematic.pdf` | Human-readable schematic |
| STEP | `pcb.step` | 3D model of assembled PCB |

If you do not have KiCad, the PDF schematic and Gerbers are sufficient for fabrication and review. KiCad is free and open source: https://www.kicad.org

### Enclosure (3D)

| Format | Files | Purpose |
|--------|-------|---------|
| STEP (`.step` / `.stp`) | Primary open format | Preferred for modification in any CAD tool |
| STL (`.stl`) | Print-ready | Use directly with any slicer (PrusaSlicer, Bambu Studio, Cura, etc.) |
| 3MF (`.3mf`) | Print-ready with settings | Includes slicer configuration |
| Shapr3D (`.shapr`) | Source | Original source file — requires Shapr3D |

For modification, import the `.step` file into your preferred CAD tool (Fusion 360, FreeCAD, Shapr3D, Onshape, SolidWorks, etc.).

For printing, use the `.stl` or `.3mf` files directly.

## License notice (CERN-OHL-S-2.0)

This hardware is covered by the CERN Open Hardware Licence Strongly Reciprocal v2.
Full text: https://ohwr.org/cern_ohl_s_v2.txt

If you produce hardware based on these design files, you must:
- Retain this license notice and the Source Location on any product or its documentation
- Release any modifications to the design files under the same CERN-OHL-S-2.0 license
- Make the modified source files available (the "Source" requirement in CERN-OHL-S)
