---
name: park4night-skill
description: Search for campsites, motorhome areas, and nature spots using the Park4night API. Use this skill when the user wants to find travel spots near GPS coordinates, check ratings, or read recent reviews.
---

# Park4night Skill (park4night-skill)

This skill provides a programmatic interface to explore locations from the Park4night service. All necessary Python logic is bundled within the skill.

## Core Workflows

### 1. Search for Spots near Coordinates
When asked to find places near a specific location or GPS coordinates:
- Execute the `main.py` script located in the skill's `scripts/` directory.
- Use `python3` to run the script.
- Require `latitude` and `longitude` as positional arguments.

**Command Pattern:**
```bash
PYTHONPATH=<skill_path>/scripts python3 <skill_path>/scripts/main.py <lat> <lon> [--limit <n>] [--sort <type>] [--type <code>] [--comments <n>]
```

### 2. Filtering and Sorting
- `--type <code>`: Filter by type (e.g., `C`, `OR`, `PN`).
- `--sort <type>`: Options are `rating`, `reviews`, `rating-reviews`, `reviews-rating`.

### 3. Detailed Reviews
- Use `--comments <n>` to fetch the latest `n` reviews for each listed spot.

## Location Types Reference
- ⛺ **Campsite** (`C`)
- 🌲 **Nature Spot (Wild)** (`OR`)
- 🌲 **Nature Spot** (`PN`)
- 🚐 **Motorhome Area** (`AC`)
- 🅿️ **Parking** (`P`)
- ☀️ **Day Parking Only** (`PJ`)
- 🏠 **Private Host** (`PH`)
- 💧 **Service Point** (`DS`)
- ☕ **Rest Area** (`AR`)
- 🚜 **Farm** (`F`)

## Technical Setup
- The skill includes `client.py`, `models.py`, and `requirements.txt` in the `scripts/` folder.
- Ensure the `scripts/` directory is in the `PYTHONPATH` when running `main.py`.
