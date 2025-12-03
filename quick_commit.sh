#!/bin/bash

# Quick Commit Script - Super Simple Version Control
# Just run: ./quick_commit.sh "your message" "version"

echo "🚀 Quick Commit for SilenceHoldsApp"
echo "=================================="
echo ""

# Get commit message
if [ $# -ge 1 ]; then
    MESSAGE="$1"
else
    echo "📝 What did you change? (e.g., 'Added new meditation exercises')"
    read -r MESSAGE
fi

# Get version (optional)
if [ $# -ge 2 ]; then
    VERSION="$2"
else
    echo "🏷️  Version name? (optional - press Enter to skip)"
    read -r VERSION
fi

# Check if there are changes
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo ""
    echo "📋 Changes found:"
    git status --short
    
    echo ""
    echo "💾 Committing changes..."
    
    # Add all changes
    git add .
    
    # Create commit message
    if [ -n "$VERSION" ]; then
        COMMIT_MSG="$MESSAGE (Version: $VERSION)"
        echo "✅ Committing: $COMMIT_MSG"
        git commit -m "$COMMIT_MSG"
    else
        echo "✅ Committing: $MESSAGE"
        git commit -m "$MESSAGE"
    fi
    
    echo ""
    echo "🎉 Commit successful!"
    echo ""
    echo "📋 Recent commits:"
    git log --oneline -3
    
    echo ""
    echo "💡 Next steps:"
    echo "   ./github_sync.sh push    # Push to GitHub"
    echo "   ./version_control.sh log # View all versions"
    
else
    echo "❌ No changes to commit"
    echo "💡 Make some changes first, then run this script again"
fi
















