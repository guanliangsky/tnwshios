#!/bin/bash

# Advanced Auto-commit script for SilenceHoldsApp
# This script automatically commits changes every hour with detailed logging

# Configuration
PROJECT_DIR="/Users/miaguan/SilenceHoldsApp"
LOG_FILE="$PROJECT_DIR/auto_commit.log"
COMMIT_PREFIX="Auto-commit"

# Function to log with timestamp
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Change to project directory
cd "$PROJECT_DIR" || exit 1

# Get current timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
COMMIT_MSG="$COMMIT_PREFIX: $TIMESTAMP"

# Check if there are any changes
if [ -n "$(git status --porcelain)" ]; then
    log_message "Changes detected, committing..."
    
    # Get list of changed files
    CHANGED_FILES=$(git status --porcelain | wc -l)
    log_message "Found $CHANGED_FILES modified files"
    
    # Add all changes
    git add .
    
    # Commit with timestamp
    git commit -m "$COMMIT_MSG"
    
    # Get commit hash
    COMMIT_HASH=$(git rev-parse --short HEAD)
    log_message "Auto-commit completed: $COMMIT_HASH - $COMMIT_MSG"
    
    # Show file changes summary
    git show --stat --format="" HEAD | tail -n +2 | head -n -1 | while read line; do
        log_message "  $line"
    done
    
else
    log_message "No changes to commit"
fi

# Log system info
log_message "System: $(uname -s) $(uname -r)"
log_message "Git version: $(git --version)"
log_message "---"
