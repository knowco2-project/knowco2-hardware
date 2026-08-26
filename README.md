# KnowCO2 Hardware

This repository contains the open hardware design files and mechanical references for the KnowCO2 indoor air quality monitor.

All original KnowCO2 hardware design files in this repository are released under the [CERN-OHL-S-2.0](LICENSE-HARDWARE) license.

## Hardware overview

The current KnowCO2 KC2-01 hardware design is built around third-party Adafruit modules and a custom KnowCO2 3D printed enclosure.

| Item | Description | Source |
|------|-------------|--------|
| Adafruit Feather ESP32-S3 Reverse TFT | Main controller, display, Wi-Fi, USB-C power | Third-party module |
| Adafruit SCD-40/SCD-41 CO2 Sensor Breakout | CO2, temperature, and humidity sensor | Third-party module |
| STEMMA QT cable | I2C connection between Feather and sensor | Third-party cable |
| KnowCO2 enclosure | Custom 3D printed enclosure | Original KnowCO2 design files in this repository |

## Folders

| Folder                  | Contents                          |
|-------------------------|-----------------------------------|
| [enclosure/](enclosure/) | KnowCO2 3D enclosure design files |
| [docs/](docs/)          | Documentation                     |
| [bom/](bom/)            | Bill of materials                 |

## Third-party PCB/module CAD references

The Adafruit PCB/module CAD files are not maintained by KnowCO2. They are linked as mechanical references for fit checks, connector clearance, display alignment, button placement, sensor placement, and assembly planning.

- Adafruit Feather ESP32-S3 Reverse TFT:  
  https://github.com/adafruit/Adafruit_CAD_Parts/tree/main/5691%20Feather%20ESP32%20S3%20Reverse%20TFT

- Adafruit SCD-40/SCD-41 CO2 Sensor Breakout:  
  https://github.com/adafruit/Adafruit_CAD_Parts/tree/main/5187%20SCD-40%20C02%20Sensor

Third-party CAD files, board designs, product names, and trademarks remain the property of their respective owners.

## KnowCO2 enclosure files

The custom KnowCO2 enclosure files are included under [enclosure/](enclosure/).

The current enclosure design includes four printed parts:

| Part                     | Purpose |
|--------------------------|---------|
| Main case                | Main body for the Feather ESP32-S3 Reverse TFT |
| Main cover / front panel | Cover with display/button access for the main unit |
| Sensor case              | Remote/secondary enclosure body for the SCD41 sensor module |
| Sensor cover             | Cover for the SCD41 sensor enclosure |

## File formats

### Enclosure / 3D printed parts

| Format | Purpose |
|--------|---------|
| STEP (`.step` / `.stp`) | Preferred open CAD exchange format for modification and manufacturing |
| STL (`.stl`) | Print-ready mesh format for slicers |
| Shapr3D (`.shapr`) | Original source file, if included |
| PNG/JPG | Reference renders or assembly images |

For modification, import the `.step` files into a CAD tool such as FreeCAD, Shapr3D, Fusion 360, Onshape, or SolidWorks.

For printing, use the `.stl` files directly in a slicer such as PrusaSlicer, Bambu Studio, Cura, or OrcaSlicer.

### PCB / schematic

KnowCO2 KC2-01 currently uses third-party Adafruit modules rather than a custom KnowCO2 PCB. See [reference-cad/](reference-cad/) for the mechanical CAD references used by the enclosure design.

If a future KnowCO2 custom PCB is added, this repository should include open source PCB design files such as KiCad source files, Gerbers, drill files, schematic PDFs, and board STEP exports.

## Assembly notes

Before printing or assembling the enclosure, verify:

- The Feather ESP32-S3 Reverse TFT fits the main case.
- The USB-C connector is accessible.
- The TFT display aligns with the front opening.
- The buttons move freely and return properly.
- The SCD41 sensor module fits the sensor enclosure.
- The SCD41 has adequate airflow exposure.
- The STEMMA QT cable is not pinched.
- The ESP32-S3 antenna area is not blocked by metal or shielding.

## License notice (CERN-OHL-S-2.0)

This hardware is covered by the CERN Open Hardware Licence Strongly Reciprocal v2.
Full text: https://ohwr.org/cern_ohl_s_v2.txt

If you produce hardware based on these design files, you must:

- Retain this license notice and the Source Location on any product or its documentation.
- Release any modifications to the design files under the same CERN-OHL-S-2.0 license.
- Make the modified source files available, satisfying the Source requirement in CERN-OHL-S.
