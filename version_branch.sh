#!/bin/bash

# Version Branch Script - Create new branch for each version
# Usage: ./version_branch.sh "version_name" "commit_message"

echo "🌿 Creating Version Branch"
echo "========================="
echo ""

# Get version name
if [ $# -ge 1 ]; then
    VERSION="$1"
else
    echo "🏷️  What version? (e.g., 'v1.1', 'v2.0', 'beta', 'release')"
    read -r VERSION
fi

# Get commit message
if [ $# -ge 2 ]; then
    MESSAGE="$2"
else
    echo "📝 What did you change? (e.g., 'Added new meditation exercises')"
    read -r MESSAGE
fi

# Create branch name
BRANCH_NAME="version-$VERSION"

echo ""
echo "🚀 Creating branch: $BRANCH_NAME"
echo "📝 Message: $MESSAGE"
echo ""

# Check if branch already exists
if git show-ref --verify --quiet refs/heads/$BRANCH_NAME; then
    echo "⚠️  Branch $BRANCH_NAME already exists!"
    echo "💡 Switching to existing branch..."
    git checkout $BRANCH_NAME
else
    # Create new branch
    git checkout -b $BRANCH_NAME
    echo "✅ Created new branch: $BRANCH_NAME"
fi

# Add all changes
git add .

# Commit with version info
COMMIT_MSG="$MESSAGE (Version: $VERSION)"
git commit -m "$COMMIT_MSG"

echo ""
echo "🎉 Version branch created successfully!"
echo ""
echo "📋 Current branches:"
git branch

echo ""
echo "💡 Commands to remember:"
echo "   git checkout main           # Go back to main branch"
echo "   git checkout $BRANCH_NAME  # Go to this version"
echo "   git branch                  # See all versions"
echo "   git log --oneline           # See commit history"
