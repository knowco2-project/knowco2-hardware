# Assembly Instructions

Documentation license: [CC-BY-SA-4.0](../LICENSE)

## Overview

The knowco2 device requires no soldering for the standard build. The CO₂ sensor connects to the Feather via a STEMMA QT cable, and the whole assembly slides into the 3D-printed enclosure.

**Estimated time:** 15–30 minutes (not including print time)

---

## What you need

See the full [bill of materials](../bom/bom.csv).

**Required**
- Adafruit Feather ESP32-S3 Reverse TFT
- Sensirion SCD40 or SCD41 breakout board
- STEMMA QT / Qwiic cable (50 mm or 100 mm)
- USB-C cable (for power)
- 3D-printed enclosure (see [hardware/enclosure/](../knowco2-hardware/enclosure/))

**Tools**
- Computer with a browser (for initial setup)
- Optional: soldering iron (only if attaching headers for a custom PCB)

---

## Step 1 — Flash CircuitPython

1. Download the latest `.uf2` for the Adafruit Feather ESP32-S3 Reverse TFT from:
   https://circuitpython.org/board/adafruit_feather_esp32s3_reverse_tft/
2. Double-tap the reset button on the Feather quickly. The board will enter the UF2 bootloader and a drive called `FTHRS3BOOT` will appear on your computer.
3. Drag the `.uf2` file onto `FTHRS3BOOT`. The board will reboot automatically.
4. A drive called `CIRCUITPY` should now appear.

> If `FTHRS3BOOT` does not appear, try double-tapping faster. The LED will turn green when in bootloader mode.

---

## Step 2 — Copy firmware files

1. Download the latest firmware release from:
   https://github.com/knowco2-project/firmware-releases/releases
2. Copy `code.py` to the root of `CIRCUITPY`
3. Copy the `lib/` folder to the root of `CIRCUITPY`
4. Safely eject the `CIRCUITPY` drive

The device will reboot and the display will show a startup screen.

---

## Step 3 — Connect the sensor

1. Connect one end of the STEMMA QT cable to the sensor breakout
2. Connect the other end to the STEMMA QT port on the Feather (the small JST SH connector on the short edge, near the USB port)

No soldering is required. The connector is keyed — it only goes in one way.

---

## Step 4 — Fit into the enclosure

1. Slide the Feather board into the main body of the enclosure with the display facing the front opening
2. Route the STEMMA QT cable and position the sensor in the sensor bay
3. Check that the three buttons (A, B, C) align with the button cutouts
4. Check that the USB-C port aligns with the side cutout
5. Fit the lid and press it closed

> The display rotation is `180°` — the board is installed upside-down relative to the Feather's silkscreen labels. This is correct.

---

## Step 5 — First power-on and Wi-Fi setup

1. Connect a USB-C cable to power the device
2. The display will show the knowco2 startup screen, then the AP info screen
3. On your phone or computer, connect to the Wi-Fi network named `knowco2-XXXX` (no password)
4. Open a browser and navigate to `http://192.168.4.1`
5. Enter your Wi-Fi network name (SSID) and password, then save
6. The device will reboot and connect to your network
7. Once connected, the Wi-Fi icon appears on the status bar

The device is now ready to use. It will be accessible on your local network at `http://knowco2-XXXX.local`.

---

## Troubleshooting

**`CIRCUITPY` drive doesn't appear after flashing**
- Check that CircuitPython was flashed successfully (step 1)
- Hold the middle button (B) while plugging in USB to force drive mode

**Device shows "No sensor" or no CO₂ readings**
- Check the STEMMA QT cable is fully seated on both ends
- Check that the cable is not pinched inside the enclosure

**Display is upside-down**
- This is normal if you are looking at the firmware source. The `display.rotation = 180` setting in `code.py` is intentional.

**Device won't connect to Wi-Fi**
- Confirm your network is 2.4 GHz (5 GHz is not supported)
- Hold the top button (C) for ~2 seconds to return to AP mode
