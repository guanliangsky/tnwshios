#!/bin/bash

# Script to add favorite buttons to all remaining coping skills

echo "⭐ Adding favorite buttons to all coping skills..."

# Add favorite buttons to all coping skills that don't have them yet
# This will add the button after the closing </div> of skill-content but before the closing </div> of coping-skill

# Pattern: Find coping-skill divs that don't have favorite-btn and add them
sed -i '' 's/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

echo "✅ Favorite buttons added to all coping skills!"
echo "💡 Check the file to make sure all buttons were added correctly"
















