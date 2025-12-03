#!/usr/bin/env python3
"""
Final comprehensive cleanup script to remove ALL duplicates and merge into single object
This will handle all edge cases and create a single clean instructions object
"""

import re
import os

def cleanup_duplicates_final_v6():
    """Remove ALL duplicates and create single clean instructions object"""
    
    print("Starting final comprehensive duplicate cleanup...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find ALL lesson entries in the entire file
    lesson_pattern = r"(\s*'[^']+': \{[^}]+\},?)"
    all_lessons = re.findall(lesson_pattern, content, re.DOTALL)
    
    print(f"Found {len(all_lessons)} total lesson entries")
    
    # Create a dictionary to store unique lessons (last occurrence wins)
    unique_lessons = {}
    duplicate_count = 0
    
    for lesson in all_lessons:
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
    
    # Find the showLessonInstructions function and replace it completely
    pattern = r'(function showLessonInstructions\(lessonId\) \{\s*const instructions = \{)(.*?)(\};)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        # Create the new clean instructions object
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
        
        print("✅ Final cleanup completed successfully!")
        return True
    else:
        print("❌ Could not find showLessonInstructions function")
        return False

def main():
    """Main function to clean up duplicates"""
    
    # Create a backup first
    print("Creating backup...")
    os.system('cp index.html index_backup_before_final_v6_cleanup.html')
    
    # Clean up duplicates
    success = cleanup_duplicates_final_v6()
    
    if success:
        print("\n🎉 Final cleanup completed successfully!")
        print("📁 Backup saved as: index_backup_before_final_v6_cleanup.html")
        print("📊 Check the file size difference:")
        os.system('ls -lh index.html index_backup_before_final_v6_cleanup.html')
        
        # Check final counts
        print("\n📊 Final lesson counts:")
        os.system("grep -c \"'[^']*': {\" index.html")
        os.system("grep -c \"const instructions = {\" index.html")
    else:
        print("❌ Final cleanup failed!")

if __name__ == "__main__":
    main()








