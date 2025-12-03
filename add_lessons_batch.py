#!/usr/bin/env python3
"""
Script to add lessons in batches to avoid overwhelming the system
"""

import sys
import os

def add_lessons_batch(start_index, batch_size):
    """Add a batch of lessons starting from start_index"""
    
    # Read the missing lessons
    with open('missing_lesson_ids.txt', 'r') as f:
        missing_lessons = [line.strip() for line in f.readlines()]
    
    # Get the batch of lessons
    end_index = min(start_index + batch_size, len(missing_lessons))
    batch_lessons = missing_lessons[start_index:end_index]
    
    print(f"Adding lessons {start_index+1} to {end_index} ({len(batch_lessons)} lessons)")
    
    # Import the lesson addition function
    from add_all_missing_lessons import create_lesson_content, add_lesson_to_instructions
    
    html_file = 'index.html'
    successful_additions = 0
    failed_additions = 0
    
    for i, lesson_id in enumerate(batch_lessons, 1):
        lesson_data = create_lesson_content(lesson_id)
        
        print(f"Adding lesson {start_index + i}: {lesson_id}")
        
        success = add_lesson_to_instructions(
            lesson_id,
            lesson_data['title'],
            lesson_data['content'],
            html_file
        )
        
        if success:
            print(f"✓ Successfully added: {lesson_data['title']}")
            successful_additions += 1
        else:
            print(f"✗ Failed to add: {lesson_data['title']}")
            failed_additions += 1
    
    print(f"\nBatch completed:")
    print(f"Successful additions: {successful_additions}")
    print(f"Failed additions: {failed_additions}")
    print(f"Total lessons in batch: {len(batch_lessons)}")
    
    return successful_additions, failed_additions

def main():
    """Main function to add lessons in batches"""
    
    if len(sys.argv) != 3:
        print("Usage: python3 add_lessons_batch.py <start_index> <batch_size>")
        print("Example: python3 add_lessons_batch.py 0 10")
        sys.exit(1)
    
    start_index = int(sys.argv[1])
    batch_size = int(sys.argv[2])
    
    print(f"Starting batch from index {start_index} with size {batch_size}")
    
    successful, failed = add_lessons_batch(start_index, batch_size)
    
    print(f"\nBatch summary:")
    print(f"Start index: {start_index}")
    print(f"Batch size: {batch_size}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    main()
