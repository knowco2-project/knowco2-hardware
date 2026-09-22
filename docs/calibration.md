# Calibration Guide

Documentation license: [CC-BY-SA-4.0](../LICENSES/CC-BY-SA-4.0.txt)

---

## How CO₂ sensor calibration works

The Sensirion SCD4x uses Non-Dispersive Infrared (NDIR) to measure CO₂. Like all NDIR sensors, it can drift over time and benefits from periodic calibration against a known reference concentration.

Outdoor air is ~400 ppm CO₂ and is the standard reference for calibration.

---

## Automatic Self-Calibration (ASC) — recommended

ASC is enabled by default and is the recommended method for most environments.

**How it works:**
The sensor continuously tracks the lowest CO₂ level it measures. Over time, it uses that minimum as its fresh-air baseline (~400 ppm). The algorithm assumes the device is exposed to outdoor-level air at least once every few days.

**Timeline:**
- First adjustments: ~2 days of use
- Fully settled: ~7–9 days of normal use
- Runs continuously in the background

**Best practice:**
Expose the device to outdoor air for a few minutes every few days (e.g., near an open window). This gives ASC a reliable, consistent reference point.

**When NOT to use ASC:**
Disable ASC if the device is in a permanently occupied or sealed space where CO₂ never drops to outdoor levels (e.g., a sealed grow room, submarine, or server room). In these environments, ASC will drift low over time.

To disable ASC: open the settings portal at `http://knowco2-XXXX.local` and toggle Automatic Self-Calibration off.

---

## Forced Recalibration (FRC) — for immediate correction

Use FRC if readings are consistently wrong and you want to recalibrate immediately.

**Procedure:**
1. Take the device outdoors (or to a well-ventilated area with outdoor air) away from people, vehicles, and plants
2. Wait 3–5 minutes for the sensor to stabilize at the outdoor CO₂ level
3. Open the settings portal at `http://knowco2-XXXX.local`
4. Navigate to **Calibration** and enter a reference value of **415 ppm** (or the current outdoor CO₂ level from a trusted source)
5. Tap **Calibrate**

The device will apply the correction immediately. Readings should be accurate within a few minutes.

> Use a reference value of 400–420 ppm for typical outdoor air. If you have a reference instrument, use its reading as the reference value.

---

## Checking calibration

A well-calibrated device should read:
- **Outdoors:** 400–430 ppm
- **Ventilated room with no occupants:** 400–600 ppm
- **Normal occupied room:** 600–1000 ppm
- **Poorly ventilated occupied space:** 1000–2000 ppm

If readings are systematically high or low by a fixed offset, FRC is the correct remedy.

---

## SCD30 notes

The SCD30 uses a different calibration algorithm. ASC on the SCD30 requires the device to see outdoor-level CO₂ at least once every 7 days. FRC is supported via the same settings portal interface.
