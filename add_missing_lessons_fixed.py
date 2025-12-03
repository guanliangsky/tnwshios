#!/usr/bin/env python3
"""
Script to add the first batch of missing lessons (1-50) to SilenceHoldsApp
This script adds lessons to the instructions object in the showLessonInstructions function
"""

import re
import os

def create_lesson_content(lesson_id):
    """Create content for a specific lesson"""
    
    lesson_contents = {
        "accept-apologies-without-grudges": {
            "title": "Accept Apologies Without Grudges",
            "content": "Learn to accept apologies genuinely and move forward without holding onto resentment. Practice forgiveness as a gift to yourself.<br><br>" +
            "<strong>🎯 Understanding Forgiveness</strong><br>" +
            "<strong>What it is:</strong> Forgiveness is choosing to let go of resentment and anger toward someone who has hurt you<br>" +
            "<strong>Why it matters:</strong> Holding grudges can harm your mental health and relationships<br>" +
            "<strong>It's a choice:</strong> You can choose to forgive even when the other person hasn't changed<br><br>" +
            "<strong>🌟 Benefits of Accepting Apologies</strong><br>" +
            "<strong>Mental peace:</strong> Letting go of grudges reduces stress and anxiety<br>" +
            "<strong>Better relationships:</strong> Forgiveness can repair and strengthen relationships<br>" +
            "<strong>Personal growth:</strong> Forgiveness helps you grow emotionally and spiritually<br>" +
            "<strong>Freedom:</strong> You free yourself from the burden of carrying anger<br><br>" +
            "<strong>💡 How to Accept Apologies Genuinely</strong><br>" +
            "<strong>Listen fully:</strong> Give the person your full attention when they apologize<br>" +
            "<strong>Look for sincerity:</strong> Notice if their words match their actions<br>" +
            "<strong>Express your feelings:</strong> Let them know how their actions affected you<br>" +
            "<strong>Set boundaries:</strong> Forgiveness doesn't mean you have to trust immediately<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Accepting apologies doesn't mean you're weak - it means you're strong enough to choose peace over pain. Forgiveness is a gift you give yourself."
        },
        "accept-change": {
            "title": "Accept Change",
            "content": "Develop skills to accept and adapt to life changes. Learn to see change as an opportunity for growth rather than a threat.<br><br>" +
            "<strong>🔄 Understanding Change</strong><br>" +
            "<strong>What it is:</strong> Change is a natural part of life that can be planned or unexpected<br>" +
            "<strong>Why it's hard:</strong> Change often involves loss of the familiar and fear of the unknown<br>" +
            "<strong>It's inevitable:</strong> Everything changes - relationships, circumstances, and even ourselves<br><br>" +
            "<strong>🌟 Benefits of Accepting Change</strong><br>" +
            "<strong>Reduced stress:</strong> Fighting change creates more stress than accepting it<br>" +
            "<strong>New opportunities:</strong> Change often brings unexpected positive outcomes<br>" +
            "<strong>Personal growth:</strong> Adapting to change builds resilience and strength<br>" +
            "<strong>Better relationships:</strong> Accepting change helps you support others through their transitions<br><br>" +
            "<strong>💡 How to Accept Change</strong><br>" +
            "<strong>Acknowledge your feelings:</strong> It's okay to feel sad, scared, or angry about change<br>" +
            "<strong>Focus on what you can control:</strong> You can't control change, but you can control your response<br>" +
            "<strong>Look for opportunities:</strong> Ask yourself what good might come from this change<br>" +
            "<strong>Take it one day at a time:</strong> You don't have to figure everything out at once<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Change is the only constant in life. By learning to accept and adapt to change, you develop the flexibility and strength to handle whatever life brings your way."
        },
        "accept-feedback": {
            "title": "Accept Feedback",
            "content": "Learn to receive feedback constructively without taking it personally. Use feedback as a tool for personal growth and improvement.<br><br>" +
            "<strong>📝 Understanding Feedback</strong><br>" +
            "<strong>What it is:</strong> Feedback is information about your performance or behavior from others<br>" +
            "<strong>Why it's valuable:</strong> Feedback helps you see blind spots and areas for improvement<br>" +
            "<strong>It's not personal:</strong> Good feedback is about behavior, not about who you are as a person<br><br>" +
            "<strong>🌟 Benefits of Accepting Feedback</strong><br>" +
            "<strong>Personal growth:</strong> Feedback helps you identify areas where you can improve<br>" +
            "<strong>Better relationships:</strong> People appreciate when you're open to their input<br>" +
            "<strong>Increased self-awareness:</strong> Feedback helps you understand how others perceive you<br>" +
            "<strong>Professional development:</strong> Accepting feedback is crucial for success in school and work<br><br>" +
            "<strong>💡 How to Accept Feedback Constructively</strong><br>" +
            "<strong>Listen without defending:</strong> Focus on understanding, not on explaining or justifying<br>" +
            "<strong>Ask clarifying questions:</strong> If something isn't clear, ask for specific examples<br>" +
            "<strong>Thank the person:</strong> Acknowledge their effort to help you improve<br>" +
            "<strong>Reflect before responding:</strong> Take time to process the feedback before deciding how to act<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Feedback is a gift that helps you grow. The people who care about you want to see you succeed, and their feedback is meant to help you become the best version of yourself."
        },
        "accept-feelings-without-rushing-away": {
            "title": "Accept Feelings Without Rushing Away",
            "content": "Practice sitting with difficult emotions without immediately trying to fix or escape them. Learn to validate your feelings.<br><br>" +
            "<strong>💭 Understanding Emotional Acceptance</strong><br>" +
            "<strong>What it is:</strong> Allowing yourself to feel emotions without judgment or immediate action<br>" +
            "<strong>Why it's important:</strong> Suppressing emotions often makes them stronger and more persistent<br>" +
            "<strong>It's not weakness:</strong> Sitting with emotions actually takes courage and strength<br><br>" +
            "<strong>🌟 Benefits of Accepting Feelings</strong><br>" +
            "<strong>Emotional regulation:</strong> Acknowledging feelings helps you manage them better<br>" +
            "<strong>Reduced intensity:</strong> Feelings often become less intense when you don't fight them<br>" +
            "<strong>Better decision-making:</strong> You can make clearer choices when you're not fighting your emotions<br>" +
            "<strong>Increased self-awareness:</strong> Understanding your feelings helps you understand yourself better<br><br>" +
            "<strong>💡 How to Accept Feelings</strong><br>" +
            "<strong>Name the emotion:</strong> Simply identify what you're feeling - sad, angry, anxious, etc.<br>" +
            "<strong>Validate yourself:</strong> Tell yourself it's okay to feel this way<br>" +
            "<strong>Breathe through it:</strong> Use deep breathing to help you stay present with the feeling<br>" +
            "<strong>Remember it's temporary:</strong> Feelings are temporary - they will pass<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Your feelings are valid and important. By learning to sit with them instead of rushing away, you develop emotional strength and wisdom that will serve you throughout your life."
        },
        "accept-friendship-endings": {
            "title": "Accept Friendship Endings",
            "content": "Learn to gracefully accept when friendships end naturally. Understand that not all relationships are meant to last forever.<br><br>" +
            "<strong>👥 Understanding Friendship Endings</strong><br>" +
            "<strong>What it is:</strong> The natural process of friendships changing or ending as people grow and change<br>" +
            "<strong>Why it happens:</strong> People grow in different directions, have different interests, or life circumstances change<br>" +
            "<strong>It's normal:</strong> Most friendships have natural life cycles, and that's okay<br><br>" +
            "<strong>🌟 Benefits of Accepting Friendship Endings</strong><br>" +
            "<strong>Reduced stress:</strong> Fighting to maintain friendships that have run their course creates stress<br>" +
            "<strong>Space for new connections:</strong> Ending old friendships opens space for new ones<br>" +
            "<strong>Personal growth:</strong> Accepting endings helps you grow and mature emotionally<br>" +
            "<strong>Peace of mind:</strong> You can focus on relationships that are currently meaningful<br><br>" +
            "<strong>💡 How to Accept Friendship Endings</strong><br>" +
            "<strong>Allow yourself to grieve:</strong> It's normal to feel sad when friendships end<br>" +
            "<strong>Focus on the positive:</strong> Remember the good times and what you learned from the friendship<br>" +
            "<strong>Let go gracefully:</strong> Don't try to force the friendship to continue if it's not working<br>" +
            "<strong>Stay open:</strong> Be open to the friendship naturally rekindling in the future<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Friendship endings are not failures - they're often signs of growth and change. The best friendships are those that support your growth, even if that means growing apart."
        }
    }
    
    return lesson_contents.get(lesson_id, {
        "title": lesson_id.replace('-', ' ').title(),
        "content": f"Learn about {lesson_id.replace('-', ' ')} and develop skills in this area.<br><br>" +
        "<strong>🎯 Understanding This Topic</strong><br>" +
        f"<strong>What it is:</strong> {lesson_id.replace('-', ' ')} is an important skill for mental health and wellbeing<br>" +
        "<strong>Why it matters:</strong> Developing this skill can improve your overall quality of life<br>" +
        "<strong>It's learnable:</strong> You can develop this skill through practice and patience<br><br>" +
        "<strong>💡 How to Practice</strong><br>" +
        "<strong>Start small:</strong> Begin with simple exercises and gradually build your skills<br>" +
        "<strong>Be consistent:</strong> Regular practice is more important than perfect execution<br>" +
        "<strong>Be patient:</strong> Learning new skills takes time and practice<br><br>" +
        "<strong>💝 Encouraging Note:</strong><br>" +
        "Every expert was once a beginner. Be patient with yourself as you learn and grow."
    })

def add_lesson_to_instructions(lesson_id, lesson_title, lesson_content, html_file):
    """Add a lesson to the instructions object in the showLessonInstructions function"""
    
    # Create the lesson entry
    lesson_entry = f"""
                '{lesson_id}': {{
                    title: '{lesson_title}',
                    content: '{lesson_content}'
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
    """Main function to add the first batch of lessons"""
    
    # Read the missing lessons
    with open('missing_lesson_ids.txt', 'r') as f:
        missing_lessons = [line.strip() for line in f.readlines()]
    
    # Get the first 5 missing lessons for testing
    batch_lessons = missing_lessons[:5]
    
    html_file = 'index.html'
    
    print(f"Adding {len(batch_lessons)} lessons to {html_file}")
    
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
        else:
            print(f"✗ Failed to add: {lesson_data['title']}")
    
    print(f"\nCompleted adding {len(batch_lessons)} lessons to the HTML file.")

if __name__ == "__main__":
    main()
