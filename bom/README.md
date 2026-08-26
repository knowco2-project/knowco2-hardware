# Bill of Materials

Hardware license: [CERN-OHL-S-2.0](../LICENSE-HARDWARE)

The BOM is provided as a CSV file: [bom.csv](bom.csv)

Columns: `Reference`, `Quantity`, `Description`, `Manufacturer`, `MPN`, `Supplier`, `Supplier PN`, `Unit Cost (USD)`, `Notes`

## No-solder build

The simplest build requires no soldering:

1. Adafruit Feather ESP32-S3 Reverse TFT
2. Sensirion SCD41 (with STEMMA QT cable)
3. STEMMA QT / Qwiic cable (50 mm or 100 mm)
4. USB-C cable (for power)
5. Printed or purchased enclosure

The sensor connects directly to the Feather via the STEMMA QT port — no soldering, no breadboard.

## Sourcing notes

- **Adafruit Feather ESP32-S3 Reverse TFT**: Available from Adafruit (#5691) and distributors (Digi-Key, Mouser)
- **Sensirion SCD40**: Lower-cost option, ±50 ppm + 5% accuracy. Available from Digi-Key (#1649-SCD40-D-R2CT-ND)
- **Sensirion SCD41**: Higher accuracy, supports single-shot measurement. Available from Digi-Key and Mouser
- **SCD30**: Older, larger sensor, dual-channel NDIR. Supported but not recommended for new builds

All primary components are available through major distributors. No specialty sourcing required.
