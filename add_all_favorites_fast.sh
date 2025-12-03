#!/bin/bash

# Fast script to add favorite buttons to ALL remaining coping skills

echo "⚡ Adding favorite buttons to ALL remaining coping skills quickly..."

# Add favorite buttons to all coping skills that don't have them yet
# This will add the button after the closing </div> of skill-content but before the closing </div> of coping-skill

# Use a simple pattern to find all coping-skill divs without favorite-btn and add them
sed -i '' 's/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

echo "✅ Favorite buttons added to ALL remaining coping skills!"
echo "💡 Check the file to make sure all buttons were added correctly"
















