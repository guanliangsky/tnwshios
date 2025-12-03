#!/bin/bash

# Add Anything Script - Super Simple
# Just run: ./add_anything.sh

echo "🎯 Add Anything to SilenceHoldsApp"
echo "================================="
echo ""

# Show current status
echo "📋 Current changes:"
git status --short
echo ""

# Get what they want to add
echo "📝 What do you want to add/change? (e.g., 'new meditation exercises', 'fixed bugs', 'better colors')"
read -r WHAT

# Get version if they want one
echo "🏷️  Version name? (optional - like 'v1.1', 'v2.0', 'beta', etc.)"
read -r VERSION

# Add everything
echo ""
echo "📦 Adding all changes..."
git add .

# Create commit
if [ -n "$VERSION" ]; then
    COMMIT_MSG="Added: $WHAT (Version: $VERSION)"
else
    COMMIT_MSG="Added: $WHAT"
fi

echo "💾 Committing: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

echo ""
echo "🎉 Success! Your changes are saved!"
echo ""
echo "📋 Recent commits:"
git log --oneline -3

echo ""
echo "💡 Want to push to GitHub?"
echo "   Type 'y' to push, or press Enter to skip"
read -r PUSH

if [ "$PUSH" = "y" ] || [ "$PUSH" = "Y" ]; then
    echo "🚀 Pushing to GitHub..."
    git push origin main
    echo "✅ Pushed to GitHub!"
else
    echo "💾 Changes saved locally. Push later with: git push origin main"
fi
















