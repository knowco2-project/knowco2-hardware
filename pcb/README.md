# PCB Design Files

Hardware license: [CERN-OHL-S-2.0](../enclosure/LICENSE-HARDWARE)

## Contents

| File / Folder | Description |
|---------------|-------------|
| `knowco2.kicad_pro` | KiCad project file |
| `knowco2.kicad_sch` | Schematic source |
| `knowco2.kicad_pcb` | PCB layout source |
| `schematic.pdf` | PDF export of schematic |
| `pcb.step` | 3D STEP model of PCB |
| `gerbers/` | Gerber files + drill file for fabrication |

> Note: PCB files will be added here. If you are waiting on the source files and need to fabricate now, contact us at knowco2.com/contact.html

## Fabrication

The Gerber files in `gerbers/` can be submitted directly to any PCB manufacturer (JLCPCB, PCBWay, OSH Park, etc.). Typical specs:

- Layers: 2
- Board thickness: 1.6 mm
- Surface finish: HASL or ENIG
- Copper weight: 1 oz

## Schematic

The PDF schematic is the fastest way to review the circuit without KiCad.

## Modifying the design

1. Install [KiCad 8+](https://www.kicad.org) (free, open source, available on macOS / Windows / Linux)
2. Open `knowco2.kicad_pro`
3. Any modifications must be released under CERN-OHL-S-2.0

## License notice

SPDX-License-Identifier: CERN-OHL-S-2.0
Source Location: https://github.com/knowco2-project/knowco2
