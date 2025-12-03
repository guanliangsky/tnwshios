#!/bin/bash

# Simple GitHub Setup Script
# Run this after accepting the Xcode license

echo "🌐 Setting up GitHub sync for SilenceHoldsApp..."
echo ""

# Check if Git is working
if ! git --version > /dev/null 2>&1; then
    echo "❌ Git is not working. Please accept the Xcode license first:"
    echo "   sudo xcodebuild -license accept"
    exit 1
fi

echo "✅ Git is working!"

# Get GitHub username
echo ""
echo "📝 Please enter your GitHub username:"
read -r GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ Username cannot be empty"
    exit 1
fi

echo ""
echo "🚀 Setting up repository for user: $GITHUB_USERNAME"

# Initialize Git repository
echo "📁 Initializing Git repository..."
git init

# Create .gitignore
echo "📝 Creating .gitignore..."
cat > .gitignore << 'EOF'
# Backup files
backups/
commits/
*.backup
*.tmp

# System files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log

# Temporary files
*.swp
*.swo
*~
EOF

# Add all files
echo "📦 Adding files to Git..."
git add .

# Make initial commit
echo "💾 Making initial commit..."
git commit -m "Initial commit: Complete SilenceHoldsApp with all lessons and coping skills"

# Add GitHub remote
echo "🔗 Adding GitHub remote..."
git remote add origin "https://github.com/$GITHUB_USERNAME/SilenceHoldsApp.git"

echo ""
echo "✅ Local setup complete!"
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

















