#!/bin/bash

# Auto-commit script for SilenceHoldsApp
# This script automatically commits changes every hour

# Get current timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
COMMIT_MSG="Auto-commit: $TIMESTAMP"

# Check if there are any changes
if [ -n "$(git status --porcelain)" ]; then
    echo "[$TIMESTAMP] Changes detected, committing..."
    
    # Add all changes
    git add .
    
    # Commit with timestamp
    git commit -m "$COMMIT_MSG"
    
    echo "[$TIMESTAMP] Auto-commit completed: $COMMIT_MSG"
else
    echo "[$TIMESTAMP] No changes to commit"
fi
