---
name: park4nigh-skill
description: Search for campsites, motorhome areas, and nature spots using the Park4night API. Use this skill when the user wants to find travel spots near GPS coordinates, check ratings, or read recent reviews.
---

# Park4night Skill (park4nigh-skill)

This skill provides a programmatic interface to explore locations from the Park4night service. All necessary Python logic is bundled within the skill.

## Core Workflows

### 1. Search for Spots near Coordinates
When asked to find places near a specific location or GPS coordinates:
- Execute the `main.py` script located in the skill's `scripts/` directory.
- Use the virtual environment Python if available, or the system `python3`.
- Require `latitude` and `longitude` as positional arguments.

**Command Pattern:**
```bash
python3 <skill_path>/scripts/main.py <lat> <lon> [--limit <n>] [--sort <type>] [--comments <n>]
```

### 2. Sorting Options (`--sort`)
- `rating`: Best rated first.
- `reviews`: Most visited first.
- `rating-reviews`: Best rated, then most reviews.
- `reviews-rating`: Most reviews, then best rated.

### 3. Detailed Reviews
- Use `--comments <n>` to fetch the latest `n` reviews for each listed spot.

## Location Types Reference
- ⛺ **Campsite** (`C`)
- 🌲 **Nature Spot (Wild)** (`OR`)
- 🚐 **Motorhome Area** (`AC`)
- 🅿️ **Parking** (`P`)
- ☀️ **Day Parking Only** (`PJ`)
- 🏠 **Private Host** (`PH`)
- 💧 **Service Point** (`DS`)

## Technical Setup
- The skill includes `client.py`, `models.py`, and `requirements.txt` in the `scripts/` folder.
- If running for the first time, dependencies from `scripts/requirements.txt` must be installed.
- Ensure the `scripts/` directory is in the `PYTHONPATH` when running `main.py`.
