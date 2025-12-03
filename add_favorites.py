#!/usr/bin/env python3

import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Pattern to find coping-skill divs that don't have favorite-btn
pattern = r'(<div class="coping-skill" onclick="showCopingSkillInstructions\(\'([^\']+)\'\)" data-skill="[^"]*">[^<]*<div class="skill-content">[^<]*<span class="skill-icon">[^<]*</span>[^<]*<span class="skill-text">[^<]*</span>[^<]*</div>[^<]*</div>)'

def add_favorite_button(match):
    full_match = match.group(1)
    skill_id = match.group(2)
    
    # Check if favorite button already exists
    if 'favorite-btn' in full_match:
        return full_match
    
    # Add favorite button before the closing </div>
    favorite_button = f'<button class="favorite-btn" id="fav-{skill_id}" onclick="event.stopPropagation(); toggleFavorite(\'{skill_id}\')">⭐</button>'
    
    # Insert the button before the closing </div> of the coping-skill
    result = full_match.replace('</div>', f'{favorite_button}\n                            </div>', 1)
    return result

# Apply the replacement
new_content = re.sub(pattern, add_favorite_button, content, flags=re.DOTALL)

# Write back to file
with open('index.html', 'w') as f:
    f.write(new_content)

print("✅ Favorite buttons added to all remaining coping skills!")
















