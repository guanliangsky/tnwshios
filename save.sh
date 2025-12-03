#!/bin/bash

# Super Simple Save Script
# Just run: ./save.sh

echo "💾 Quick Save for SilenceHoldsApp"
echo "================================"
echo ""

# Get what they changed
echo "📝 What did you change? (e.g., 'new lessons', 'fixed bugs', 'better design')"
read -r CHANGE

# Get version
echo "🏷️  Version? (e.g., 'v1.1', 'v2.0', 'beta', or just press Enter)"
read -r VERSION

# Save everything
git add .
git commit -m "Updated: $CHANGE${VERSION:+ (Version: $VERSION)}"

echo ""
echo "✅ Saved! Your changes are now safe."
echo ""
echo "💡 Want to push to GitHub? (y/n)"
read -r PUSH

if [ "$PUSH" = "y" ] || [ "$PUSH" = "Y" ]; then
    git push origin main
    echo "🚀 Pushed to GitHub!"
fi

echo ""
echo "🎉 All done!"
















