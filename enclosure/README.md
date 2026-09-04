# KnowCO2 Enclosure

This README is documentation licensed under [CC-BY-SA-4.0](../LICENSES/CC-BY-SA-4.0.txt). The enclosure design files and reference renders are Covered Source under the [CERN-OHL-S-2.0 project notice](../LICENSE-HARDWARE).

This folder contains the custom 3D printed enclosure files for the KnowCO2 KC2-01 hardware design.

The enclosure is designed around:

- Adafruit Feather ESP32-S3 Reverse TFT
- Adafruit SCD-40/SCD-41 CO2 Sensor Breakout
- STEMMA QT I2C cable
- USB-C power

The CO2 sensor is physically separated from the main electronics enclosure to improve airflow and reduce self-heating effects from the display, processor, and power circuitry.

## Parts

| Part | STEP | STL | Description |
|------|------|-----|-------------|
| Main case | `step/knowco2_main_case.step` | `stl/knowco2_main_case.stl` | Main body for the Feather ESP32-S3 Reverse TFT |
| Main cover | `step/knowco2_main_cover.step` | `stl/knowco2_main_cover.stl` | Front cover with display and button openings |
| Sensor case | `step/knowco2_sensor_case.step` | `stl/knowco2_sensor_case.stl` | Body for the SCD41 sensor module |
| Sensor cover | `step/knowco2_sensor_cover.step` | `stl/knowco2_sensor_cover.stl` | Cover for the SCD41 sensor enclosure |

## Images

Reference images are included in `images/`:

| Image | Description |
|-------|-------------|
| `images/knowco2_main_case.png` | Main case reference render |
| `images/knowco2_main_cover.png` | Main cover reference render |
| `images/knowco2_sensor_case.png` | Sensor case reference render |
| `images/knowco2_sensor_cover.png` | Sensor cover reference render |

## Recommended print settings

These are starting settings and may need adjustment for your printer and filament.

| Setting | Recommendation |
|---------|----------------|
| Material | PETG or PLA |
| Layer height | 0.20 mm |
| Nozzle | 0.4 mm |
| Infill | 15-25% |
| Walls/perimeters | 3 or more |
| Top/bottom layers | 4 or more |
| Supports | As needed based on orientation |

## Assembly checks

Before final assembly, confirm:

- The Feather ESP32-S3 Reverse TFT fits into the main case.
- The USB-C connector is accessible.
- The TFT aligns with the front cover opening.
- The buttons move freely and return properly.
- The SCD41 sensor breakout fits into the sensor case.
- The sensor has adequate airflow exposure.
- The STEMMA QT cable is not pinched.
- The ESP32-S3 antenna area is not blocked by metal or shielding.

## Notes

The STEP files are the preferred files for modification and manufacturing. The STL files are provided for direct 3D printing.
