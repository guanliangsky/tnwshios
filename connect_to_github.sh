#!/bin/bash

echo "🌐 Connecting to GitHub..."
echo ""

# Get GitHub username
echo "📝 Please enter your GitHub username:"
read -r GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ Username cannot be empty"
    exit 1
fi

echo ""
echo "🔗 Adding GitHub remote for user: $GITHUB_USERNAME"

# Add GitHub remote
git remote add origin "https://github.com/$GITHUB_USERNAME/SilenceHoldsApp.git"

echo "✅ GitHub remote added!"
echo ""
echo "📋 Next steps:"
echo "1. Go to: https://github.com/new"
echo "2. Repository name: SilenceHoldsApp"
echo "3. Description: A comprehensive mental health app with bite-sized lessons and coping skills"
echo "4. Make it Public"
echo "5. Don't check any boxes (README, .gitignore, license)"
echo "6. Click 'Create repository'"
echo ""
echo "7. Then run: git push -u origin main"
echo ""
echo "🎉 After that, you can use:"
echo "   ./github_sync.sh push    # Push changes"
echo "   ./github_sync.sh status  # Check status"

















