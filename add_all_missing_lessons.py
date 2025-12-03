#!/usr/bin/env python3
"""
Comprehensive script to add all missing lessons to SilenceHoldsApp
This script adds lessons to the instructions object in the showLessonInstructions function
"""

import re
import os
import json

def create_lesson_content(lesson_id):
    """Create comprehensive content for a specific lesson"""
    
    # Define lesson content templates based on categories
    lesson_templates = {
        # Acceptance and Change
        "accept": {
            "template": "Learn to accept {topic} and develop skills to navigate this area effectively.<br><br>" +
            "<strong>🎯 Understanding {topic_title}</strong><br>" +
            "<strong>What it is:</strong> {topic} is an important part of mental health and wellbeing<br>" +
            "<strong>Why it matters:</strong> Learning to accept {topic} can reduce stress and improve your quality of life<br>" +
            "<strong>It's learnable:</strong> You can develop acceptance skills through practice and patience<br><br>" +
            "<strong>🌟 Benefits of Accepting {topic_title}</strong><br>" +
            "<strong>Reduced stress:</strong> Fighting against {topic} often creates more stress than accepting it<br>" +
            "<strong>Better relationships:</strong> Acceptance helps you maintain healthier relationships<br>" +
            "<strong>Personal growth:</strong> Acceptance is a sign of emotional maturity and wisdom<br>" +
            "<strong>Inner peace:</strong> Acceptance brings a sense of peace and contentment<br><br>" +
            "<strong>💡 How to Practice Acceptance</strong><br>" +
            "<strong>Start small:</strong> Begin with accepting small things and gradually work up to bigger challenges<br>" +
            "<strong>Use mindfulness:</strong> Practice being present with your feelings about {topic}<br>" +
            "<strong>Seek support:</strong> Don't try to develop acceptance alone - get help from others<br>" +
            "<strong>Be patient:</strong> Acceptance is a skill that develops over time<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Acceptance doesn't mean giving up - it means choosing peace over struggle. By learning to accept {topic}, you develop the wisdom and strength to handle life's challenges with grace."
        },
        
        # Management and Coping
        "management": {
            "template": "Learn effective strategies for managing {topic} and developing healthy coping skills.<br><br>" +
            "<strong>🎯 Understanding {topic_title}</strong><br>" +
            "<strong>What it is:</strong> {topic} is a common challenge that many people face<br>" +
            "<strong>Why it matters:</strong> Learning to manage {topic} effectively can improve your mental health and quality of life<br>" +
            "<strong>It's manageable:</strong> With the right strategies, you can learn to cope with {topic} effectively<br><br>" +
            "<strong>🌟 Benefits of Effective Management</strong><br>" +
            "<strong>Reduced stress:</strong> Good management strategies can significantly reduce stress and anxiety<br>" +
            "<strong>Better functioning:</strong> You can maintain your daily activities and responsibilities<br>" +
            "<strong>Improved relationships:</strong> Better management helps you maintain healthy relationships<br>" +
            "<strong>Increased confidence:</strong> Successfully managing {topic} builds confidence and self-esteem<br><br>" +
            "<strong>💡 How to Manage {topic_title}</strong><br>" +
            "<strong>Identify triggers:</strong> Learn to recognize what triggers or worsens {topic}<br>" +
            "<strong>Develop coping strategies:</strong> Create a toolkit of strategies that work for you<br>" +
            "<strong>Seek professional help:</strong> Don't hesitate to get help from mental health professionals<br>" +
            "<strong>Build support networks:</strong> Surround yourself with people who understand and support you<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Managing {topic} is a journey, not a destination. Be patient with yourself and celebrate small victories along the way."
        },
        
        # Building and Development
        "build": {
            "template": "Learn how to build and develop {topic} to support your mental health and personal growth.<br><br>" +
            "<strong>🎯 Understanding {topic_title}</strong><br>" +
            "<strong>What it is:</strong> {topic} is a valuable skill that can be developed through practice<br>" +
            "<strong>Why it matters:</strong> Building {topic} can improve your mental health, relationships, and overall wellbeing<br>" +
            "<strong>It's achievable:</strong> With consistent effort, you can develop strong {topic} skills<br><br>" +
            "<strong>🌟 Benefits of Building {topic_title}</strong><br>" +
            "<strong>Improved mental health:</strong> Strong {topic} skills support better mental health and wellbeing<br>" +
            "<strong>Better relationships:</strong> Good {topic} skills help you build and maintain healthy relationships<br>" +
            "<strong>Increased confidence:</strong> Developing {topic} skills builds confidence and self-esteem<br>" +
            "<strong>Life satisfaction:</strong> Strong {topic} skills contribute to overall life satisfaction<br><br>" +
            "<strong>💡 How to Build {topic_title}</strong><br>" +
            "<strong>Start with basics:</strong> Begin with fundamental {topic} skills and gradually advance<br>" +
            "<strong>Practice regularly:</strong> Consistent practice is key to developing {topic} skills<br>" +
            "<strong>Get support:</strong> Don't try to build {topic} alone - seek guidance and support<br>" +
            "<strong>Be patient:</strong> Building {topic} skills takes time and consistent effort<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Building {topic} is an investment in yourself that will pay dividends throughout your life. Every step you take toward developing these skills is a step toward a happier, healthier you."
        },
        
        # Coping and Handling
        "cope": {
            "template": "Learn effective strategies for coping with {topic} and developing resilience in challenging situations.<br><br>" +
            "<strong>🎯 Understanding {topic_title}</strong><br>" +
            "<strong>What it is:</strong> {topic} is a common challenge that requires specific coping strategies<br>" +
            "<strong>Why it matters:</strong> Learning to cope with {topic} effectively can improve your mental health and quality of life<br>" +
            "<strong>It's manageable:</strong> With the right strategies, you can learn to cope with {topic} successfully<br><br>" +
            "<strong>🌟 Benefits of Effective Coping</strong><br>" +
            "<strong>Reduced stress:</strong> Good coping strategies can significantly reduce stress and anxiety<br>" +
            "<strong>Better functioning:</strong> You can maintain your daily activities and responsibilities<br>" +
            "<strong>Improved relationships:</strong> Better coping helps you maintain healthy relationships<br>" +
            "<strong>Increased resilience:</strong> Successfully coping with {topic} builds resilience and strength<br><br>" +
            "<strong>💡 How to Cope with {topic_title}</strong><br>" +
            "<strong>Identify your triggers:</strong> Learn to recognize what makes {topic} more difficult<br>" +
            "<strong>Develop coping strategies:</strong> Create a toolkit of strategies that work for you<br>" +
            "<strong>Seek support:</strong> Don't try to cope alone - reach out to others for help<br>" +
            "<strong>Practice self-care:</strong> Take care of your physical and emotional needs<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Coping with {topic} is a skill that can be learned and improved over time. Be patient with yourself and remember that seeking help is a sign of strength, not weakness."
        },
        
        # Default template for other lessons
        "default": {
            "template": "Learn about {topic} and develop skills to support your mental health and wellbeing.<br><br>" +
            "<strong>🎯 Understanding {topic_title}</strong><br>" +
            "<strong>What it is:</strong> {topic} is an important aspect of mental health and personal development<br>" +
            "<strong>Why it matters:</strong> Developing skills in {topic} can improve your overall quality of life<br>" +
            "<strong>It's learnable:</strong> You can develop {topic} skills through practice and patience<br><br>" +
            "<strong>🌟 Benefits of Developing {topic_title}</strong><br>" +
            "<strong>Improved mental health:</strong> Good {topic} skills support better mental health and wellbeing<br>" +
            "<strong>Better relationships:</strong> Strong {topic} skills help you build and maintain healthy relationships<br>" +
            "<strong>Increased confidence:</strong> Developing {topic} skills builds confidence and self-esteem<br>" +
            "<strong>Life satisfaction:</strong> Strong {topic} skills contribute to overall life satisfaction<br><br>" +
            "<strong>💡 How to Develop {topic_title}</strong><br>" +
            "<strong>Start small:</strong> Begin with simple exercises and gradually build your skills<br>" +
            "<strong>Be consistent:</strong> Regular practice is more important than perfect execution<br>" +
            "<strong>Seek support:</strong> Don't try to develop {topic} skills alone - get help from others<br>" +
            "<strong>Be patient:</strong> Learning new skills takes time and practice<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Developing {topic} skills is an investment in yourself that will benefit you throughout your life. Every step you take toward learning these skills is a step toward a happier, healthier you."
        }
    }
    
    # Determine which template to use based on the lesson ID
    if lesson_id.startswith('accept-'):
        template_key = 'accept'
        topic = lesson_id.replace('accept-', '').replace('-', ' ')
    elif lesson_id.startswith('manage-') or lesson_id.endswith('-management'):
        template_key = 'management'
        topic = lesson_id.replace('manage-', '').replace('-management', '').replace('-', ' ')
    elif lesson_id.startswith('build-') or lesson_id.startswith('develop-'):
        template_key = 'build'
        topic = lesson_id.replace('build-', '').replace('develop-', '').replace('-', ' ')
    elif lesson_id.startswith('cope-') or lesson_id.startswith('handle-'):
        template_key = 'cope'
        topic = lesson_id.replace('cope-', '').replace('handle-', '').replace('-', ' ')
    else:
        template_key = 'default'
        topic = lesson_id.replace('-', ' ')
    
    # Get the template
    template = lesson_templates[template_key]
    
    # Create the title
    title = lesson_id.replace('-', ' ').title()
    topic_title = topic.title()
    
    # Format the content
    content = template['template'].format(topic=topic, topic_title=topic_title)
    
    return {
        "title": title,
        "content": content
    }

def add_lesson_to_instructions(lesson_id, lesson_title, lesson_content, html_file):
    """Add a lesson to the instructions object in the showLessonInstructions function"""
    
    # Escape quotes in the content
    escaped_content = lesson_content.replace("'", "\\'").replace('\n', '\\n')
    
    # Create the lesson entry
    lesson_entry = f"""
                '{lesson_id}': {{
                    title: '{lesson_title}',
                    content: '{escaped_content}'
                }},"""
    
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the instructions object and add the lesson
    # Look for the pattern where we can insert the new lesson
    pattern = r"(const instructions = \{[^}]*'telling-friend': \{[^}]*\},)"
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # Insert the new lesson before the existing lessons
        new_content = content.replace(
            match.group(1),
            match.group(1) + lesson_entry
        )
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    # Alternative approach: find the end of the instructions object
    pattern2 = r"(const instructions = \{.*?)(\};)"
    match2 = re.search(pattern2, content, re.DOTALL)
    if match2:
        # Insert before the closing brace
        new_content = content.replace(
            match2.group(2),
            lesson_entry + "\n            " + match2.group(2)
        )
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    """Main function to add all missing lessons"""
    
    # Read the missing lessons
    with open('missing_lesson_ids.txt', 'r') as f:
        missing_lessons = [line.strip() for line in f.readlines()]
    
    # Get all missing lessons
    batch_lessons = missing_lessons
    
    html_file = 'index.html'
    
    print(f"Adding {len(batch_lessons)} lessons to {html_file}")
    print("This may take a while...")
    
    successful_additions = 0
    failed_additions = 0
    
    for i, lesson_id in enumerate(batch_lessons, 1):
        lesson_data = create_lesson_content(lesson_id)
        
        print(f"Adding lesson {i}/{len(batch_lessons)}: {lesson_id}")
        
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
        
        # Add a small delay to prevent overwhelming the system
        if i % 10 == 0:
            print(f"Progress: {i}/{len(batch_lessons)} lessons processed")
    
    print(f"\nCompleted adding lessons to the HTML file.")
    print(f"Successful additions: {successful_additions}")
    print(f"Failed additions: {failed_additions}")
    print(f"Total lessons processed: {len(batch_lessons)}")

if __name__ == "__main__":
    main()
