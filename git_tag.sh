#!/bin/bash

# Git Tag Script - Create version tags like v0.0.1, v1.2.3, etc.
# Usage: ./git_tag.sh "v0.0.1" "commit_message"

echo "🏷️  Creating Git Version Tag"
echo "============================"
echo ""

# Get version tag
if [ $# -ge 1 ]; then
    VERSION="$1"
else
    echo "🏷️  What version? (e.g., 'v0.0.1', 'v1.2.3', 'v2.0.0')"
    read -r VERSION
fi

# Get commit message
if [ $# -ge 2 ]; then
    MESSAGE="$2"
else
    echo "📝 What did you change? (e.g., 'Initial release', 'Added new features')"
    read -r MESSAGE
fi

echo ""
echo "🚀 Creating version tag: $VERSION"
echo "📝 Message: $MESSAGE"
echo ""

# Add all changes
git add .

# Commit with version info
COMMIT_MSG="$MESSAGE (Version: $VERSION)"
git commit -m "$COMMIT_MSG"

# Create the tag
git tag -a "$VERSION" -m "Version $VERSION: $MESSAGE"

echo ""
echo "🎉 Version tag created successfully!"
echo ""
echo "📋 Current tags:"
git tag

echo ""
echo "💡 Commands to remember:"
echo "   git tag                           # See all version tags"
echo "   git checkout $VERSION            # Go to this version"
echo "   git checkout main                # Go back to main"
echo "   git log --oneline                # See commit history"
echo "   git show $VERSION                # See what's in this version"
















