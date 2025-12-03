#!/usr/bin/env python3
import re

# Read the HTML file
with open('/Users/miaguan/SilenceHoldsApp/index.html', 'r') as f:
    content = f.read()

# Find all lesson categories
categories = re.findall(r'id="([^"]*-lessons)"', content)
print(f"Found {len(categories)} lesson categories:")
print()

# Check which lessons exist in instructions object
instructions_pattern = r"'([^']+)':\s*{"
instructions_matches = re.findall(instructions_pattern, content)
existing_lessons = set(instructions_matches)

total_lessons = 0
completed_lessons = 0
missing_lessons = 0

for i, category in enumerate(categories, 1):
    print(f"{i:2d}. {category.replace('-lessons', '').replace('-', ' ').title()}")
    
    # Find all data-skill attributes in this category
    category_section = re.search(f'id="{category}".*?(?=id="[^"]*-lessons"|$)', content, re.DOTALL)
    if category_section:
        skills = re.findall(r'data-skill="([^"]*)"', category_section.group(0))
        category_total = len(skills)
        total_lessons += category_total
        
        print(f"    Total lessons: {category_total}")
        
        # Check which ones exist in instructions
        category_completed = 0
        category_missing = []
        
        for skill in skills:
            if skill in existing_lessons:
                category_completed += 1
            else:
                category_missing.append(skill)
        
        completed_lessons += category_completed
        missing_lessons += len(category_missing)
        
        print(f"    Completed: {category_completed}")
        print(f"    Missing: {len(category_missing)}")
        
        if category_missing:
            print(f"    Missing lessons: {', '.join(category_missing[:5])}{'...' if len(category_missing) > 5 else ''}")
        print()

print(f"SUMMARY:")
print(f"Total categories: {len(categories)}")
print(f"Total lessons: {total_lessons}")
print(f"Completed lessons: {completed_lessons}")
print(f"Missing lessons: {missing_lessons}")
print(f"Completion rate: {(completed_lessons/total_lessons)*100:.1f}%")
