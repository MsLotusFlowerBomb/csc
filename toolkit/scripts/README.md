# CTF Toolkit Scripts

This directory contains useful scripts for managing your CTF learning journey.

## Available Scripts

### 🚀 setup-challenge.sh
Interactive script to set up a new challenge workspace.

**Usage:**
```bash
./toolkit/scripts/setup-challenge.sh
```

**Features:**
- Creates organized directory structure for new challenges
- Generates writeup template with pre-filled metadata
- Creates initial analysis notes
- Sets up directories for files, notes, and scripts

### 📊 progress-tracker.py
Python script to track and visualize your CTF learning progress.

**Usage:**
```bash
# Add a solved challenge
./toolkit/scripts/progress-tracker.py add "Challenge Name" web easy 100 "Platform Name"

# Show progress statistics
./toolkit/scripts/progress-tracker.py progress

# List all challenges
./toolkit/scripts/progress-tracker.py list

# Filter challenges by category
./toolkit/scripts/progress-tracker.py list --category web

# Start a learning session
./toolkit/scripts/progress-tracker.py session start --focus "web security"

# End a learning session
./toolkit/scripts/progress-tracker.py session end --id 0 --notes "Learned about SQL injection"
```

**Features:**
- Track solved challenges with metadata
- Generate progress statistics
- Manage learning sessions
- Filter and search challenges
- Export data in JSON format

## Installation

Make sure scripts are executable:
```bash
chmod +x toolkit/scripts/*.sh
chmod +x toolkit/scripts/*.py
```

## Data Storage

Progress data is stored in `toolkit/data/progress.json` and is automatically created when first used.

## Adding New Scripts

When adding new scripts to this directory:
1. Make them executable: `chmod +x script-name`
2. Add documentation to this README
3. Follow the existing naming convention
4. Include proper error handling and help text

---
*CTF Toolkit Scripts - Automating your learning journey*