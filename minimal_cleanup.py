#!/usr/bin/env python3
"""
Minimal cleanup script - only removes duplicates that could cause problems
Preserves as much content as possible while fixing critical issues
"""

import re
import os

def minimal_cleanup():
    """Remove only problematic duplicates while preserving content"""
    
    print("Starting minimal cleanup - only removing problematic duplicates...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the showLessonInstructions function
    pattern = r'(function showLessonInstructions\(lessonId\) \{\s*const instructions = \{)(.*?)(\};)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("❌ Could not find showLessonInstructions function")
        return False
    
    # Extract the instructions object content
    instructions_content = match.group(2)
    
    # Find all lesson entries
    lesson_pattern = r"(\s*'[^']+': \{[^}]+\},?)"
    lessons = re.findall(lesson_pattern, instructions_content, re.DOTALL)
    
    print(f"Found {len(lessons)} lesson entries")
    
    # Create a dictionary to store unique lessons (last occurrence wins)
    unique_lessons = {}
    duplicate_count = 0
    
    for lesson in lessons:
        # Extract the lesson ID
        lesson_id_match = re.search(r"'([^']+)':", lesson)
        if lesson_id_match:
            lesson_id = lesson_id_match.group(1)
            if lesson_id in unique_lessons:
                duplicate_count += 1
                print(f"  Removing duplicate: {lesson_id}")
            unique_lessons[lesson_id] = lesson
    
    print(f"Found {len(unique_lessons)} unique lessons")
    print(f"Removed {duplicate_count} duplicates")
    
    # Rebuild the instructions object
    new_instructions = "const instructions = {\n"
    for lesson_id, lesson_content in unique_lessons.items():
        new_instructions += lesson_content + "\n"
    new_instructions += "            };"
    
    # Replace the old instructions with the cleaned version
    new_content = content.replace(
        match.group(1) + match.group(2) + match.group(3),
        match.group(1) + new_instructions
    )
    
    # Write the cleaned content back to the file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ Minimal cleanup completed successfully!")
    return True

def main():
    """Main function to perform minimal cleanup"""
    
    # Create a backup first
    print("Creating backup...")
    os.system('cp index.html index_backup_before_minimal_cleanup.html')
    
    # Perform minimal cleanup
    success = minimal_cleanup()
    
    if success:
        print("\n🎉 Minimal cleanup completed successfully!")
        print("📁 Backup saved as: index_backup_before_minimal_cleanup.html")
        print("📊 Check the file size difference:")
        os.system('ls -lh index.html index_backup_before_minimal_cleanup.html')
        
        # Check final counts
        print("\n📊 Final lesson counts:")
        os.system("grep -c \"'[^']*': {\" index.html")
        os.system("grep -c \"const instructions = {\" index.html")
    else:
        print("❌ Minimal cleanup failed!")

if __name__ == "__main__":
    main()








