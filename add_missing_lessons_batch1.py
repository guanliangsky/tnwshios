#!/usr/bin/env python3
"""
Script to add the first batch of missing lessons (1-50) to SilenceHoldsApp
"""

import re
import os

def add_lesson_to_html(lesson_id, lesson_title, lesson_content, html_file):
    """Add a lesson to the HTML file"""
    
    # Create the lesson HTML structure
    lesson_html = f'''
    <div class="lesson-card" data-lesson-id="{lesson_id}">
        <div class="lesson-header">
            <h3 class="lesson-title">{lesson_title}</h3>
            <div class="lesson-actions">
                <button class="favorite-btn" data-lesson-id="{lesson_id}">
                    <span class="heart">♡</span>
                </button>
            </div>
        </div>
        <div class="lesson-content">
            <div class="lesson-description">
                {lesson_content}
            </div>
            <div class="lesson-actions">
                <button class="start-lesson-btn" data-lesson-id="{lesson_id}">Start Lesson</button>
            </div>
        </div>
    </div>
    '''
    
    # Find the lessons container and add the lesson
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the lessons container
    lessons_container_pattern = r'(<div class="lessons-container"[^>]*>)(.*?)(</div>)'
    match = re.search(lessons_container_pattern, content, re.DOTALL)
    
    if match:
        # Add the lesson before the closing div
        new_content = content.replace(
            match.group(2),
            match.group(2) + lesson_html
        )
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def create_lesson_content(lesson_id):
    """Create content for a specific lesson"""
    
    lesson_contents = {
        "accept-apologies-without-grudges": {
            "title": "Accept Apologies Without Grudges",
            "content": "Learn to accept apologies genuinely and move forward without holding onto resentment. Practice forgiveness as a gift to yourself."
        },
        "accept-change": {
            "title": "Accept Change",
            "content": "Develop skills to accept and adapt to life changes. Learn to see change as an opportunity for growth rather than a threat."
        },
        "accept-feedback": {
            "title": "Accept Feedback",
            "content": "Learn to receive feedback constructively without taking it personally. Use feedback as a tool for personal growth and improvement."
        },
        "accept-feelings-without-rushing-away": {
            "title": "Accept Feelings Without Rushing Away",
            "content": "Practice sitting with difficult emotions without immediately trying to fix or escape them. Learn to validate your feelings."
        },
        "accept-friendship-endings": {
            "title": "Accept Friendship Endings",
            "content": "Learn to gracefully accept when friendships end naturally. Understand that not all relationships are meant to last forever."
        },
        "accept-growth-can-feel-messy": {
            "title": "Accept Growth Can Feel Messy",
            "content": "Understand that personal growth isn't always linear or neat. Embrace the messy, imperfect process of becoming who you're meant to be."
        },
        "adapt-change": {
            "title": "Adapt to Change",
            "content": "Develop resilience and flexibility to adapt to life's changes. Learn practical strategies for navigating transitions."
        },
        "adapt-new-environment": {
            "title": "Adapt to New Environment",
            "content": "Build skills to adapt to new environments, whether it's a new school, job, or living situation. Create comfort in unfamiliar places."
        },
        "add-playfulness-to-day": {
            "title": "Add Playfulness to Your Day",
            "content": "Incorporate play and joy into your daily routine. Learn to balance responsibility with fun and spontaneity."
        },
        "adhd-management": {
            "title": "ADHD Management",
            "content": "Develop strategies to manage ADHD symptoms effectively. Learn organization, focus, and self-regulation techniques."
        },
        "advocate-for-needs": {
            "title": "Advocate for Your Needs",
            "content": "Learn to speak up for your needs and boundaries. Develop assertiveness skills while maintaining healthy relationships."
        },
        "aging-acceptance": {
            "title": "Aging Acceptance",
            "content": "Learn to accept and embrace the aging process. Develop a positive relationship with getting older and the changes it brings."
        },
        "aging-advocacy": {
            "title": "Aging Advocacy",
            "content": "Learn to advocate for yourself and others as you age. Understand your rights and how to access resources and support."
        },
        "aging-boundaries": {
            "title": "Aging Boundaries",
            "content": "Set and maintain healthy boundaries as you age. Learn to protect your energy and well-being while staying connected."
        },
        "aging-health": {
            "title": "Aging Health",
            "content": "Focus on maintaining physical and mental health as you age. Learn about age-appropriate health practices and when to seek help."
        },
        "aging-hope": {
            "title": "Aging Hope",
            "content": "Maintain hope and optimism about the future as you age. Learn to see aging as a time of wisdom and new possibilities."
        },
        "aging-identity": {
            "title": "Aging Identity",
            "content": "Explore and maintain your sense of identity as you age. Learn to embrace new aspects of yourself while honoring your history."
        },
        "aging-purpose": {
            "title": "Aging Purpose",
            "content": "Find and maintain a sense of purpose as you age. Learn to contribute meaningfully to your community and relationships."
        },
        "aging-relationships": {
            "title": "Aging Relationships",
            "content": "Navigate relationships and social connections as you age. Learn to maintain friendships and form new connections."
        },
        "aging-resources": {
            "title": "Aging Resources",
            "content": "Learn about resources and support available as you age. Understand how to access help and maintain independence."
        },
        "aging-support": {
            "title": "Aging Support",
            "content": "Build and maintain a support network as you age. Learn to ask for help and offer support to others."
        },
        "aging-wellness": {
            "title": "Aging Wellness",
            "content": "Maintain overall wellness as you age. Learn about physical, mental, and emotional health practices for older adults."
        },
        "anxiety-journal-safely": {
            "title": "Anxiety Journal Safely",
            "content": "Learn to journal about anxiety in a way that helps rather than increases worry. Use writing as a tool for processing and healing."
        },
        "anxiety-management": {
            "title": "Anxiety Management",
            "content": "Develop comprehensive strategies for managing anxiety. Learn breathing techniques, grounding exercises, and cognitive strategies."
        },
        "anxiety-tricking-body": {
            "title": "Anxiety: Tricking Your Body",
            "content": "Learn techniques to calm your body's anxiety response. Use physical strategies to reduce anxiety symptoms."
        },
        "apologize-sincerely-hurt-someone": {
            "title": "Apologize Sincerely When You Hurt Someone",
            "content": "Learn to give genuine, meaningful apologies. Understand the components of a sincere apology and how to make amends."
        },
        "apologizing-effectively": {
            "title": "Apologizing Effectively",
            "content": "Master the art of effective apologies. Learn when and how to apologize in a way that promotes healing and understanding."
        },
        "appreciate-body-functions": {
            "title": "Appreciate Body Functions",
            "content": "Learn to appreciate what your body does for you. Focus on function over appearance and develop body gratitude."
        },
        "appreciate-small-moments": {
            "title": "Appreciate Small Moments",
            "content": "Practice mindfulness and gratitude for small, everyday moments. Learn to find joy in simple pleasures."
        },
        "approach-groups-conversations": {
            "title": "Approach Groups and Conversations",
            "content": "Build confidence in group settings and conversations. Learn strategies for joining discussions and making connections."
        },
        "art-therapy": {
            "title": "Art Therapy",
            "content": "Use art as a therapeutic tool for expression and healing. Learn various art techniques for processing emotions."
        },
        "ask-academic-accommodations": {
            "title": "Ask for Academic Accommodations",
            "content": "Learn to advocate for academic accommodations you need. Understand your rights and how to communicate with educators."
        },
        "ask-for-space": {
            "title": "Ask for Space",
            "content": "Learn to request space and time when you need it. Practice setting boundaries around your personal time and energy."
        },
        "ask-teacher-help": {
            "title": "Ask Teacher for Help",
            "content": "Build confidence in asking teachers for help. Learn effective communication strategies for academic support."
        },
        "asking-help-without-guilt": {
            "title": "Asking for Help Without Guilt",
            "content": "Learn to ask for help without feeling guilty or burdensome. Understand that asking for help is a sign of strength."
        },
        "authentic-living": {
            "title": "Authentic Living",
            "content": "Learn to live authentically and true to yourself. Develop the courage to be genuine in all areas of your life."
        },
        "avoid-comparing-life-online": {
            "title": "Avoid Comparing Your Life Online",
            "content": "Learn to resist the urge to compare your life to what you see online. Develop strategies for healthy social media use."
        },
        "balance-dreaming-realistic": {
            "title": "Balance Dreaming and Realistic",
            "content": "Learn to balance big dreams with realistic planning. Find the sweet spot between ambition and achievable goals."
        },
        "balance-family-friend-priorities": {
            "title": "Balance Family and Friend Priorities",
            "content": "Learn to balance time and energy between family and friends. Develop strategies for maintaining all important relationships."
        },
        "balance-gaming-other-activities": {
            "title": "Balance Gaming and Other Activities",
            "content": "Learn to balance gaming with other important activities. Develop healthy gaming habits and time management."
        },
        "balance-individuality-with-belonging": {
            "title": "Balance Individuality with Belonging",
            "content": "Learn to maintain your individuality while feeling like you belong. Find the balance between being yourself and fitting in."
        },
        "balance-rest-activity": {
            "title": "Balance Rest and Activity",
            "content": "Learn to balance rest and activity for optimal health. Understand the importance of both rest and movement."
        },
        "balance-schoolwork-downtime": {
            "title": "Balance Schoolwork and Downtime",
            "content": "Learn to balance academic responsibilities with relaxation and fun. Develop time management skills for school-life balance."
        },
        "balanced-thinking": {
            "title": "Balanced Thinking",
            "content": "Learn to think in balanced, realistic ways. Challenge all-or-nothing thinking and develop more flexible thought patterns."
        },
        "beginner-meditation": {
            "title": "Beginner Meditation",
            "content": "Learn the basics of meditation for beginners. Start with simple techniques and build a meditation practice."
        },
        "believe-healing-possible": {
            "title": "Believe Healing is Possible",
            "content": "Develop hope and belief in your ability to heal and grow. Learn to maintain optimism during difficult times."
        },
        "bipolar-management": {
            "title": "Bipolar Management",
            "content": "Learn strategies for managing bipolar disorder. Develop skills for mood stability and symptom management."
        },
        "block-unfollow-harmful-accounts": {
            "title": "Block and Unfollow Harmful Accounts",
            "content": "Learn to protect your mental health by curating your social media feed. Remove harmful influences from your digital environment."
        },
        "body-acceptance": {
            "title": "Body Acceptance",
            "content": "Learn to accept your body as it is. Develop a positive relationship with your body and challenge negative body image."
        },
        "body-appreciation": {
            "title": "Body Appreciation",
            "content": "Learn to appreciate your body for what it does. Focus on gratitude for your body's functions and capabilities."
        }
    }
    
    return lesson_contents.get(lesson_id, {
        "title": lesson_id.replace('-', ' ').title(),
        "content": f"Learn about {lesson_id.replace('-', ' ')} and develop skills in this area."
    })

def main():
    """Main function to add the first batch of lessons"""
    
    # Read the missing lessons
    with open('missing_lesson_ids.txt', 'r') as f:
        missing_lessons = [line.strip() for line in f.readlines()]
    
    # Get the first 50 missing lessons
    batch_lessons = missing_lessons[:50]
    
    html_file = 'index.html'
    
    print(f"Adding {len(batch_lessons)} lessons to {html_file}")
    
    for i, lesson_id in enumerate(batch_lessons, 1):
        lesson_data = create_lesson_content(lesson_id)
        
        print(f"Adding lesson {i}/50: {lesson_id}")
        
        success = add_lesson_to_html(
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
