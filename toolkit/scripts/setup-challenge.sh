#!/bin/bash

# CTF Challenge Setup Script
# This script helps set up a new challenge workspace

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to get user input
get_input() {
    local prompt="$1"
    local variable="$2"
    echo -n "$prompt: "
    read $variable
}

# Main function
main() {
    print_status "CTF Challenge Setup Script"
    echo

    # Get challenge information
    get_input "Challenge name" CHALLENGE_NAME
    echo "Select challenge category:"
    echo "1) Web"
    echo "2) Crypto"
    echo "3) Forensics"
    echo "4) PWN"
    echo "5) Rev"
    echo "6) Misc"
    get_input "Enter choice (1-6)" CATEGORY_CHOICE

    # Map choice to category
    case $CATEGORY_CHOICE in
        1) CATEGORY="web" ;;
        2) CATEGORY="crypto" ;;
        3) CATEGORY="forensics" ;;
        4) CATEGORY="pwn" ;;
        5) CATEGORY="rev" ;;
        6) CATEGORY="misc" ;;
        *) print_error "Invalid choice"; exit 1 ;;
    esac

    get_input "Platform/CTF name" PLATFORM
    get_input "Difficulty (Easy/Medium/Hard)" DIFFICULTY
    get_input "Points" POINTS

    # Create challenge directory
    CHALLENGE_DIR="challenges/${CATEGORY}/${CHALLENGE_NAME// /_}"
    
    if [ -d "$CHALLENGE_DIR" ]; then
        print_warning "Directory $CHALLENGE_DIR already exists"
        get_input "Continue anyway? (y/n)" CONTINUE
        if [ "$CONTINUE" != "y" ]; then
            print_status "Aborted"
            exit 0
        fi
    fi

    mkdir -p "$CHALLENGE_DIR"
    mkdir -p "$CHALLENGE_DIR/files"
    mkdir -p "$CHALLENGE_DIR/notes"
    mkdir -p "$CHALLENGE_DIR/scripts"

    # Create writeup from template
    WRITEUP_FILE="$CHALLENGE_DIR/README.md"
    cp "challenges/templates/challenge-writeup-template.md" "$WRITEUP_FILE"

    # Replace template placeholders
    sed -i "s/\[Web\/Crypto\/Forensics\/PWN\/Rev\/Misc\]/$CATEGORY/g" "$WRITEUP_FILE"
    sed -i "s/\[Easy\/Medium\/Hard\]/$DIFFICULTY/g" "$WRITEUP_FILE"
    sed -i "s/\[Point value\]/$POINTS/g" "$WRITEUP_FILE"
    sed -i "s/\[CTF Platform name\]/$PLATFORM/g" "$WRITEUP_FILE"
    sed -i "s/\[YYYY-MM-DD\]/$(date +%Y-%m-%d)/g" "$WRITEUP_FILE"

    # Create initial notes file
    cat > "$CHALLENGE_DIR/notes/initial-analysis.md" << EOF
# Initial Analysis - $CHALLENGE_NAME

**Date**: $(date +%Y-%m-%d)
**Time Started**: $(date +%H:%M)

## First Impressions
- 

## Tools to Try
- 

## Hypotheses
- 

## Next Steps
- [ ] 
- [ ] 
- [ ] 

---
*Notes updated: $(date)*
EOF

    print_success "Challenge workspace created at: $CHALLENGE_DIR"
    print_status "Files created:"
    print_status "  - README.md (writeup template)"
    print_status "  - files/ (for challenge files)"
    print_status "  - notes/ (for analysis notes)"
    print_status "  - scripts/ (for custom scripts)"
    
    echo
    print_status "To get started:"
    print_status "  1. cd $CHALLENGE_DIR"
    print_status "  2. Edit README.md with challenge description"
    print_status "  3. Put challenge files in files/"
    print_status "  4. Start documenting in notes/"
    
    # Optionally open the directory
    get_input "Open challenge directory? (y/n)" OPEN_DIR
    if [ "$OPEN_DIR" = "y" ]; then
        cd "$CHALLENGE_DIR"
        print_success "Changed to challenge directory: $(pwd)"
    fi
}

# Run main function
main "$@"