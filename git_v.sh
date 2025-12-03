#!/bin/bash

# Super Simple Git Version Script
# Usage: ./git_v.sh "v0.0.1" "message"

echo "🏷️  Git Version: $1"
echo "=================="
echo ""

# Get version and message
VERSION="$1"
MESSAGE="$2"

if [ -z "$VERSION" ]; then
    echo "❌ Please provide a version (e.g., v0.0.1)"
    echo "💡 Usage: ./git_v.sh v0.0.1 \"your message\""
    exit 1
fi

if [ -z "$MESSAGE" ]; then
    echo "❌ Please provide a message"
    echo "💡 Usage: ./git_v.sh v0.0.1 \"your message\""
    exit 1
fi

echo "🚀 Creating version: $VERSION"
echo "📝 Message: $MESSAGE"
echo ""

# Add, commit, and tag
git add .
git commit -m "$MESSAGE (Version: $VERSION)"
git tag -a "$VERSION" -m "Version $VERSION: $MESSAGE"

echo ""
echo "✅ Version $VERSION created!"
echo ""
echo "📋 All versions:"
git tag
echo ""
echo "💡 Go to any version: git checkout $VERSION"
echo "💡 Back to main: git checkout main"
















