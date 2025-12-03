#!/bin/bash

# Script to add favorite buttons to all remaining coping skills

echo "⭐ Adding favorite buttons to remaining coping skills..."

# Add favorite buttons to all coping skills that don't have them yet
# This will add the button after the closing </div> of skill-content but before the closing </div> of coping-skill

# Pattern: Find coping-skill divs that don't have favorite-btn and add them
# We'll use a more targeted approach for each category

# Add to sadness tools
sed -i '' '/id="sadness-tools"/,/id="heartbreak-tools"/s/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

# Add to heartbreak tools
sed -i '' '/id="heartbreak-tools"/,/id="stress-tools"/s/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

# Add to stress tools
sed -i '' '/id="stress-tools"/,/id="overwhelm-tools"/s/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

# Add to overwhelm tools
sed -i '' '/id="overwhelm-tools"/,/id="physical-tools"/s/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

# Add to physical tools
sed -i '' '/id="physical-tools"/,/id="creative-tools"/s/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

# Add to creative tools
sed -i '' '/id="creative-tools"/,/id="social-tools"/s/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

# Add to social tools
sed -i '' '/id="social-tools"/,/id="mindful-tools"/s/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

# Add to mindful tools
sed -i '' '/id="mindful-tools"/,/id="favorites-tools"/s/\(<div class="coping-skill" onclick="showCopingSkillInstructions('\''[^'\'']*'\'')" data-skill="[^"]*">\)/\1\n                                <button class="favorite-btn" id="fav-\2" onclick="event.stopPropagation(); toggleFavorite('\''\2'\'')">⭐<\/button>/g' index.html

echo "✅ Favorite buttons added to all remaining coping skills!"
echo "💡 Check the file to make sure all buttons were added correctly"