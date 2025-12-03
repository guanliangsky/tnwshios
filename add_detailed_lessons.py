#!/usr/bin/env python3
"""
Enhanced script to add comprehensive, detailed content to lessons
This script provides much more detailed and professional content for each lesson
"""

import re
import os
import json

def create_detailed_lesson_content(lesson_id):
    """Create comprehensive, detailed content for a specific lesson"""
    
    # Define detailed lesson content templates based on categories
    detailed_lesson_contents = {
        "accept-apologies-without-grudges": {
            "title": "Accept Apologies Without Grudges",
            "content": "Learn to accept apologies genuinely and move forward without holding onto resentment. Practice forgiveness as a gift to yourself.<br><br>" +
            "<strong>🎯 Understanding Forgiveness</strong><br>" +
            "<strong>What it is:</strong> Forgiveness is choosing to let go of resentment and anger toward someone who has hurt you<br>" +
            "<strong>Why it matters:</strong> Holding grudges can harm your mental health and relationships<br>" +
            "<strong>It's a choice:</strong> You can choose to forgive even when the other person hasn't changed<br>" +
            "<strong>It's not weakness:</strong> Forgiveness is actually a sign of emotional strength and maturity<br><br>" +
            "<strong>🌟 Benefits of Accepting Apologies</strong><br>" +
            "<strong>Mental peace:</strong> Letting go of grudges reduces stress and anxiety<br>" +
            "<strong>Better relationships:</strong> Forgiveness can repair and strengthen relationships<br>" +
            "<strong>Personal growth:</strong> Forgiveness helps you grow emotionally and spiritually<br>" +
            "<strong>Freedom:</strong> You free yourself from the burden of carrying anger<br>" +
            "<strong>Improved sleep:</strong> Letting go of resentment can improve your sleep quality<br>" +
            "<strong>Better focus:</strong> Without grudges, you can focus on positive aspects of life<br><br>" +
            "<strong>💡 How to Accept Apologies Genuinely</strong><br>" +
            "<strong>Listen fully:</strong> Give the person your full attention when they apologize<br>" +
            "<strong>Look for sincerity:</strong> Notice if their words match their actions<br>" +
            "<strong>Express your feelings:</strong> Let them know how their actions affected you<br>" +
            "<strong>Set boundaries:</strong> Forgiveness doesn't mean you have to trust immediately<br>" +
            "<strong>Take your time:</strong> You don't have to forgive instantly - it's okay to process first<br>" +
            "<strong>Focus on the present:</strong> Don't let past hurts control your current relationships<br><br>" +
            "<strong>🧠 The Psychology of Forgiveness</strong><br>" +
            "<strong>It's a process:</strong> Forgiveness often happens in stages, not all at once<br>" +
            "<strong>It's about you:</strong> Forgiveness is primarily for your own peace of mind<br>" +
            "<strong>It's not forgetting:</strong> You can forgive while still remembering the lesson learned<br>" +
            "<strong>It's not approval:</strong> Forgiving doesn't mean you approve of what happened<br><br>" +
            "<strong>💭 Overcoming Challenges</strong><br>" +
            "<strong>Fear of being hurt again:</strong> Set clear boundaries to protect yourself<br>" +
            "<strong>Feeling like you're giving in:</strong> Remember that forgiveness is about your peace, not theirs<br>" +
            "<strong>Pressure to forgive quickly:</strong> Take the time you need to process your feelings<br>" +
            "<strong>Worrying about what others think:</strong> Your forgiveness journey is personal and private<br><br>" +
            "<strong>🌟 Building Your Forgiveness Practice</strong><br>" +
            "<strong>Start small:</strong> Begin with minor offenses and work up to bigger ones<br>" +
            "<strong>Practice self-forgiveness:</strong> Learn to forgive yourself for mistakes<br>" +
            "<strong>Seek support:</strong> Talk to trusted friends or a counselor about your feelings<br>" +
            "<strong>Be patient:</strong> Forgiveness is a skill that develops over time<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Accepting apologies doesn't mean you're weak - it means you're strong enough to choose peace over pain. Forgiveness is a gift you give yourself that allows you to move forward with grace and wisdom."
        },
        
        "accept-change": {
            "title": "Accept Change",
            "content": "Develop skills to accept and adapt to life changes. Learn to see change as an opportunity for growth rather than a threat.<br><br>" +
            "<strong>🔄 Understanding Change</strong><br>" +
            "<strong>What it is:</strong> Change is a natural part of life that can be planned or unexpected<br>" +
            "<strong>Why it's hard:</strong> Change often involves loss of the familiar and fear of the unknown<br>" +
            "<strong>It's inevitable:</strong> Everything changes - relationships, circumstances, and even ourselves<br>" +
            "<strong>It's often beneficial:</strong> Many of life's greatest opportunities come from change<br><br>" +
            "<strong>🌟 Benefits of Accepting Change</strong><br>" +
            "<strong>Reduced stress:</strong> Fighting change creates more stress than accepting it<br>" +
            "<strong>New opportunities:</strong> Change often brings unexpected positive outcomes<br>" +
            "<strong>Personal growth:</strong> Adapting to change builds resilience and strength<br>" +
            "<strong>Better relationships:</strong> Accepting change helps you support others through their transitions<br>" +
            "<strong>Increased flexibility:</strong> You become more adaptable to future changes<br>" +
            "<strong>Enhanced creativity:</strong> Change often requires creative problem-solving<br><br>" +
            "<strong>💡 How to Accept Change</strong><br>" +
            "<strong>Acknowledge your feelings:</strong> It's okay to feel sad, scared, or angry about change<br>" +
            "<strong>Focus on what you can control:</strong> You can't control change, but you can control your response<br>" +
            "<strong>Look for opportunities:</strong> Ask yourself what good might come from this change<br>" +
            "<strong>Take it one day at a time:</strong> You don't have to figure everything out at once<br>" +
            "<strong>Seek support:</strong> Talk to others who have experienced similar changes<br>" +
            "<strong>Maintain routines:</strong> Keep some familiar routines during times of change<br><br>" +
            "<strong>🧠 The Psychology of Change</strong><br>" +
            "<strong>Change curve:</strong> Most people go through stages: shock, denial, anger, bargaining, depression, testing, acceptance<br>" +
            "<strong>Individual differences:</strong> Everyone processes change at their own pace<br>" +
            "<strong>Past experiences:</strong> Previous change experiences influence how you handle new ones<br>" +
            "<strong>Support systems:</strong> Having support makes change much easier to navigate<br><br>" +
            "<strong>💭 Overcoming Challenges</strong><br>" +
            "<strong>Fear of the unknown:</strong> Focus on what you can learn and discover<br>" +
            "<strong>Loss of control:</strong> Identify what you can still control in the situation<br>" +
            "<strong>Nostalgia for the past:</strong> Honor the past while embracing the future<br>" +
            "<strong>Pressure to adapt quickly:</strong> Give yourself time to adjust at your own pace<br><br>" +
            "<strong>🌟 Building Your Change Acceptance Skills</strong><br>" +
            "<strong>Practice flexibility:</strong> Regularly try new things to build adaptability<br>" +
            "<strong>Develop coping strategies:</strong> Create a toolkit of strategies for handling change<br>" +
            "<strong>Build resilience:</strong> Strengthen your ability to bounce back from setbacks<br>" +
            "<strong>Stay connected:</strong> Maintain relationships during times of change<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Change is the only constant in life. By learning to accept and adapt to change, you develop the flexibility and strength to handle whatever life brings your way. Every change is an opportunity to grow and discover new aspects of yourself."
        },
        
        "anxiety-management": {
            "title": "Anxiety Management",
            "content": "Develop comprehensive strategies for managing anxiety and developing healthy coping skills.<br><br>" +
            "<strong>🎯 Understanding Anxiety</strong><br>" +
            "<strong>What it is:</strong> Anxiety is a normal human emotion that becomes problematic when it's excessive or persistent<br>" +
            "<strong>Why it happens:</strong> Anxiety is your body's natural response to perceived threats or stress<br>" +
            "<strong>It's manageable:</strong> With the right strategies, you can learn to manage anxiety effectively<br>" +
            "<strong>It's common:</strong> Anxiety disorders affect millions of people worldwide<br><br>" +
            "<strong>🌟 Benefits of Effective Anxiety Management</strong><br>" +
            "<strong>Reduced stress:</strong> Good management strategies can significantly reduce stress and anxiety<br>" +
            "<strong>Better functioning:</strong> You can maintain your daily activities and responsibilities<br>" +
            "<strong>Improved relationships:</strong> Better anxiety management helps you maintain healthy relationships<br>" +
            "<strong>Increased confidence:</strong> Successfully managing anxiety builds confidence and self-esteem<br>" +
            "<strong>Better sleep:</strong> Managing anxiety can improve your sleep quality<br>" +
            "<strong>Enhanced focus:</strong> Reduced anxiety allows you to concentrate better<br><br>" +
            "<strong>💡 How to Manage Anxiety</strong><br>" +
            "<strong>Identify triggers:</strong> Learn to recognize what triggers or worsens your anxiety<br>" +
            "<strong>Develop coping strategies:</strong> Create a toolkit of strategies that work for you<br>" +
            "<strong>Practice relaxation techniques:</strong> Deep breathing, meditation, and progressive muscle relaxation<br>" +
            "<strong>Maintain a healthy lifestyle:</strong> Regular exercise, balanced diet, and adequate sleep<br>" +
            "<strong>Challenge negative thoughts:</strong> Learn to question and reframe anxious thinking<br>" +
            "<strong>Seek professional help:</strong> Don't hesitate to get help from mental health professionals<br><br>" +
            "<strong>🧠 The Science of Anxiety</strong><br>" +
            "<strong>Fight or flight response:</strong> Anxiety activates your body's natural stress response<br>" +
            "<strong>Neurotransmitters:</strong> Imbalances in brain chemicals can contribute to anxiety<br>" +
            "<strong>Genetics:</strong> Anxiety can have a genetic component<br>" +
            "<strong>Environmental factors:</strong> Stress, trauma, and life events can trigger anxiety<br><br>" +
            "<strong>💭 Overcoming Challenges</strong><br>" +
            "<strong>Feeling overwhelmed:</strong> Break anxiety management into small, manageable steps<br>" +
            "<strong>Impatience with progress:</strong> Remember that managing anxiety takes time and practice<br>" +
            "<strong>Fear of seeking help:</strong> Professional help is a sign of strength, not weakness<br>" +
            "<strong>Perfectionism:</strong> Accept that progress isn't always linear<br><br>" +
            "<strong>🌟 Building Your Anxiety Management Toolkit</strong><br>" +
            "<strong>Breathing exercises:</strong> Practice deep breathing and box breathing techniques<br>" +
            "<strong>Grounding techniques:</strong> Use the 5-4-3-2-1 method to ground yourself in the present<br>" +
            "<strong>Mindfulness practices:</strong> Develop a regular meditation or mindfulness practice<br>" +
            "<strong>Physical activity:</strong> Regular exercise is one of the most effective anxiety treatments<br>" +
            "<strong>Social support:</strong> Build a network of supportive relationships<br>" +
            "<strong>Professional resources:</strong> Know when and how to access professional help<br><br>" +
            "<strong>💝 Encouraging Note:</strong><br>" +
            "Managing anxiety is a journey, not a destination. Be patient with yourself and celebrate small victories along the way. You have the strength and resilience to develop effective coping strategies and live a fulfilling life despite anxiety."
        }
    }
    
    # Get the detailed content or create a comprehensive default
    if lesson_id in detailed_lesson_contents:
        return detailed_lesson_contents[lesson_id]
    
    # Create comprehensive default content based on lesson type
    title = lesson_id.replace('-', ' ').title()
    
    if lesson_id.startswith('accept-'):
        return create_acceptance_lesson(lesson_id, title)
    elif lesson_id.startswith('manage-') or lesson_id.endswith('-management'):
        return create_management_lesson(lesson_id, title)
    elif lesson_id.startswith('build-') or lesson_id.startswith('develop-'):
        return create_development_lesson(lesson_id, title)
    elif lesson_id.startswith('cope-') or lesson_id.startswith('handle-'):
        return create_coping_lesson(lesson_id, title)
    else:
        return create_general_lesson(lesson_id, title)

def create_acceptance_lesson(lesson_id, title):
    """Create detailed content for acceptance-based lessons"""
    topic = lesson_id.replace('accept-', '').replace('-', ' ')
    return {
        "title": title,
        "content": f"Learn to accept {topic} and develop skills to navigate this area effectively.<br><br>" +
        "<strong>🎯 Understanding {topic.title()}</strong><br>" +
        f"<strong>What it is:</strong> {topic} is an important part of mental health and wellbeing<br>" +
        f"<strong>Why it matters:</strong> Learning to accept {topic} can reduce stress and improve your quality of life<br>" +
        "<strong>It's learnable:</strong> You can develop acceptance skills through practice and patience<br>" +
        "<strong>It's empowering:</strong> Acceptance gives you control over your response to difficult situations<br><br>" +
        f"<strong>🌟 Benefits of Accepting {topic.title()}</strong><br>" +
        "<strong>Reduced stress:</strong> Fighting against difficult realities often creates more stress than accepting them<br>" +
        "<strong>Better relationships:</strong> Acceptance helps you maintain healthier relationships<br>" +
        "<strong>Personal growth:</strong> Acceptance is a sign of emotional maturity and wisdom<br>" +
        "<strong>Inner peace:</strong> Acceptance brings a sense of peace and contentment<br>" +
        "<strong>Increased resilience:</strong> Acceptance builds your ability to handle future challenges<br>" +
        "<strong>Better decision-making:</strong> When you accept reality, you can make clearer decisions<br><br>" +
        f"<strong>💡 How to Practice Acceptance</strong><br>" +
        "<strong>Start small:</strong> Begin with accepting small things and gradually work up to bigger challenges<br>" +
        "<strong>Use mindfulness:</strong> Practice being present with your feelings about the situation<br>" +
        "<strong>Seek support:</strong> Don't try to develop acceptance alone - get help from others<br>" +
        "<strong>Be patient:</strong> Acceptance is a skill that develops over time<br>" +
        "<strong>Focus on what you can control:</strong> Accept what you can't change and focus on what you can<br>" +
        "<strong>Practice self-compassion:</strong> Be kind to yourself as you work on acceptance<br><br>" +
        "<strong>🧠 The Psychology of Acceptance</strong><br>" +
        "<strong>It's a process:</strong> Acceptance often happens in stages, not all at once<br>" +
        "<strong>It's about you:</strong> Acceptance is primarily for your own peace of mind<br>" +
        "<strong>It's not giving up:</strong> Acceptance doesn't mean you stop trying to improve things<br>" +
        "<strong>It's realistic:</strong> Acceptance means acknowledging reality as it is<br><br>" +
        "<strong>💭 Overcoming Challenges</strong><br>" +
        "<strong>Fear of change:</strong> Remember that acceptance can lead to positive change<br>" +
        "<strong>Feeling powerless:</strong> Acceptance actually gives you more power over your response<br>" +
        "<strong>Pressure to accept quickly:</strong> Take the time you need to process your feelings<br>" +
        "<strong>Worrying about what others think:</strong> Your acceptance journey is personal and private<br><br>" +
        f"<strong>🌟 Building Your Acceptance Practice</strong><br>" +
        "<strong>Daily reflection:</strong> Take time each day to practice acceptance<br>" +
        "<strong>Mindfulness meditation:</strong> Regular meditation can help develop acceptance skills<br>" +
        "<strong>Journaling:</strong> Write about your experiences with acceptance<br>" +
        "<strong>Seek professional help:</strong> Consider therapy to develop acceptance skills<br><br>" +
        "<strong>💝 Encouraging Note:</strong><br>" +
        f"Acceptance doesn't mean giving up - it means choosing peace over struggle. By learning to accept {topic}, you develop the wisdom and strength to handle life's challenges with grace and resilience."
    }

def create_management_lesson(lesson_id, title):
    """Create detailed content for management-based lessons"""
    topic = lesson_id.replace('manage-', '').replace('-management', '').replace('-', ' ')
    return {
        "title": title,
        "content": f"Learn effective strategies for managing {topic} and developing healthy coping skills.<br><br>" +
        f"<strong>🎯 Understanding {topic.title()}</strong><br>" +
        f"<strong>What it is:</strong> {topic} is a common challenge that requires specific management strategies<br>" +
        f"<strong>Why it matters:</strong> Learning to manage {topic} effectively can improve your mental health and quality of life<br>" +
        "<strong>It's manageable:</strong> With the right strategies, you can learn to manage this challenge successfully<br>" +
        "<strong>It's a skill:</strong> Management skills can be developed and improved over time<br><br>" +
        f"<strong>🌟 Benefits of Effective {topic.title()} Management</strong><br>" +
        "<strong>Reduced stress:</strong> Good management strategies can significantly reduce stress and anxiety<br>" +
        "<strong>Better functioning:</strong> You can maintain your daily activities and responsibilities<br>" +
        "<strong>Improved relationships:</strong> Better management helps you maintain healthy relationships<br>" +
        "<strong>Increased confidence:</strong> Successfully managing challenges builds confidence and self-esteem<br>" +
        "<strong>Better sleep:</strong> Effective management can improve your sleep quality<br>" +
        "<strong>Enhanced focus:</strong> Good management allows you to concentrate better<br><br>" +
        f"<strong>💡 How to Manage {topic.title()}</strong><br>" +
        "<strong>Identify your triggers:</strong> Learn to recognize what makes the situation more difficult<br>" +
        "<strong>Develop coping strategies:</strong> Create a toolkit of strategies that work for you<br>" +
        "<strong>Seek support:</strong> Don't try to manage everything alone - reach out to others for help<br>" +
        "<strong>Practice self-care:</strong> Take care of your physical and emotional needs<br>" +
        "<strong>Set realistic goals:</strong> Break down large challenges into smaller, manageable steps<br>" +
        "<strong>Monitor your progress:</strong> Keep track of what's working and what isn't<br><br>" +
        "<strong>🧠 The Science of Management</strong><br>" +
        "<strong>Problem-solving approach:</strong> Effective management involves systematic problem-solving<br>" +
        "<strong>Stress response:</strong> Understanding how stress affects your ability to manage challenges<br>" +
        "<strong>Learning and adaptation:</strong> Management skills improve with practice and experience<br>" +
        "<strong>Individual differences:</strong> What works for others may not work for you<br><br>" +
        "<strong>💭 Overcoming Challenges</strong><br>" +
        "<strong>Feeling overwhelmed:</strong> Break management into small, manageable steps<br>" +
        "<strong>Impatience with progress:</strong> Remember that developing management skills takes time<br>" +
        "<strong>Fear of seeking help:</strong> Professional help is a sign of strength, not weakness<br>" +
        "<strong>Perfectionism:</strong> Accept that progress isn't always linear<br><br>" +
        f"<strong>🌟 Building Your {topic.title()} Management Toolkit</strong><br>" +
        "<strong>Relaxation techniques:</strong> Practice deep breathing, meditation, and progressive muscle relaxation<br>" +
        "<strong>Problem-solving skills:</strong> Develop systematic approaches to addressing challenges<br>" +
        "<strong>Time management:</strong> Learn to prioritize and organize your time effectively<br>" +
        "<strong>Communication skills:</strong> Develop clear communication strategies<br>" +
        "<strong>Support networks:</strong> Build relationships with people who can help and support you<br>" +
        "<strong>Professional resources:</strong> Know when and how to access professional help<br><br>" +
        "<strong>💝 Encouraging Note:</strong><br>" +
        f"Managing {topic} is a skill that can be learned and improved over time. Be patient with yourself and remember that seeking help is a sign of strength, not weakness. You have the ability to develop effective strategies and live a fulfilling life."
    }

def create_development_lesson(lesson_id, title):
    """Create detailed content for development-based lessons"""
    topic = lesson_id.replace('build-', '').replace('develop-', '').replace('-', ' ')
    return {
        "title": title,
        "content": f"Learn how to build and develop {topic} to support your mental health and personal growth.<br><br>" +
        f"<strong>🎯 Understanding {topic.title()}</strong><br>" +
        f"<strong>What it is:</strong> {topic} is a valuable skill that can be developed through practice<br>" +
        f"<strong>Why it matters:</strong> Building {topic} can improve your mental health, relationships, and overall wellbeing<br>" +
        "<strong>It's achievable:</strong> With consistent effort, you can develop strong skills in this area<br>" +
        "<strong>It's empowering:</strong> Developing these skills gives you more control over your life<br><br>" +
        f"<strong>🌟 Benefits of Building {topic.title()}</strong><br>" +
        "<strong>Improved mental health:</strong> Strong skills support better mental health and wellbeing<br>" +
        "<strong>Better relationships:</strong> Good skills help you build and maintain healthy relationships<br>" +
        "<strong>Increased confidence:</strong> Developing skills builds confidence and self-esteem<br>" +
        "<strong>Life satisfaction:</strong> Strong skills contribute to overall life satisfaction<br>" +
        "<strong>Better decision-making:</strong> Developed skills help you make better choices<br>" +
        "<strong>Increased resilience:</strong> Strong skills help you bounce back from setbacks<br><br>" +
        f"<strong>💡 How to Build {topic.title()}</strong><br>" +
        "<strong>Start with basics:</strong> Begin with fundamental skills and gradually advance<br>" +
        "<strong>Practice regularly:</strong> Consistent practice is key to developing skills<br>" +
        "<strong>Get support:</strong> Don't try to build skills alone - seek guidance and support<br>" +
        "<strong>Be patient:</strong> Building skills takes time and consistent effort<br>" +
        "<strong>Learn from mistakes:</strong> View mistakes as learning opportunities<br>" +
        "<strong>Set realistic goals:</strong> Break down skill development into manageable steps<br><br>" +
        "<strong>🧠 The Science of Skill Development</strong><br>" +
        "<strong>Neuroplasticity:</strong> Your brain can form new connections and pathways throughout life<br>" +
        "<strong>Deliberate practice:</strong> Focused, intentional practice is more effective than casual practice<br>" +
        "<strong>Learning curves:</strong> Skill development often follows predictable patterns<br>" +
        "<strong>Individual differences:</strong> Everyone learns and develops skills at their own pace<br><br>" +
        "<strong>💭 Overcoming Challenges</strong><br>" +
        "<strong>Impatience with progress:</strong> Remember that skill development takes time and practice<br>" +
        "<strong>Fear of failure:</strong> View mistakes as learning opportunities, not failures<br>" +
        "<strong>Comparing to others:</strong> Focus on your own progress and development<br>" +
        "<strong>Lack of motivation:</strong> Find ways to make skill development enjoyable and rewarding<br><br>" +
        f"<strong>🌟 Building Your {topic.title()} Development Plan</strong><br>" +
        "<strong>Set clear goals:</strong> Define what you want to achieve and by when<br>" +
        "<strong>Create a practice schedule:</strong> Set aside regular time for skill development<br>" +
        "<strong>Find resources:</strong> Seek out books, courses, mentors, and other learning resources<br>" +
        "<strong>Track your progress:</strong> Keep a journal of your development and achievements<br>" +
        "<strong>Celebrate milestones:</strong> Acknowledge and celebrate your progress along the way<br>" +
        "<strong>Seek feedback:</strong> Get input from others to help guide your development<br><br>" +
        "<strong>💝 Encouraging Note:</strong><br>" +
        f"Building {topic} is an investment in yourself that will pay dividends throughout your life. Every step you take toward developing these skills is a step toward a happier, healthier, and more fulfilling life. You have the ability to learn and grow in amazing ways."
    }

def create_coping_lesson(lesson_id, title):
    """Create detailed content for coping-based lessons"""
    topic = lesson_id.replace('cope-', '').replace('handle-', '').replace('-', ' ')
    return {
        "title": title,
        "content": f"Learn effective strategies for coping with {topic} and developing resilience in challenging situations.<br><br>" +
        f"<strong>🎯 Understanding {topic.title()}</strong><br>" +
        f"<strong>What it is:</strong> {topic} is a common challenge that requires specific coping strategies<br>" +
        f"<strong>Why it matters:</strong> Learning to cope with {topic} effectively can improve your mental health and quality of life<br>" +
        "<strong>It's manageable:</strong> With the right strategies, you can learn to cope with this challenge successfully<br>" +
        "<strong>It's a skill:</strong> Coping skills can be developed and improved over time<br><br>" +
        f"<strong>🌟 Benefits of Effective Coping</strong><br>" +
        "<strong>Reduced stress:</strong> Good coping strategies can significantly reduce stress and anxiety<br>" +
        "<strong>Better functioning:</strong> You can maintain your daily activities and responsibilities<br>" +
        "<strong>Improved relationships:</strong> Better coping helps you maintain healthy relationships<br>" +
        "<strong>Increased resilience:</strong> Successfully coping with challenges builds resilience and strength<br>" +
        "<strong>Better sleep:</strong> Effective coping can improve your sleep quality<br>" +
        "<strong>Enhanced focus:</strong> Good coping allows you to concentrate better<br><br>" +
        f"<strong>💡 How to Cope with {topic.title()}</strong><br>" +
        "<strong>Identify your triggers:</strong> Learn to recognize what makes the situation more difficult<br>" +
        "<strong>Develop coping strategies:</strong> Create a toolkit of strategies that work for you<br>" +
        "<strong>Seek support:</strong> Don't try to cope alone - reach out to others for help<br>" +
        "<strong>Practice self-care:</strong> Take care of your physical and emotional needs<br>" +
        "<strong>Use relaxation techniques:</strong> Practice deep breathing, meditation, and other calming methods<br>" +
        "<strong>Maintain perspective:</strong> Remember that this challenge is temporary and manageable<br><br>" +
        "<strong>🧠 The Science of Coping</strong><br>" +
        "<strong>Stress response:</strong> Understanding how your body responds to stress and challenges<br>" +
        "<strong>Adaptive vs. maladaptive:</strong> Learning to distinguish between helpful and harmful coping strategies<br>" +
        "<strong>Individual differences:</strong> What works for others may not work for you<br>" +
        "<strong>Learning and growth:</strong> Coping skills improve with practice and experience<br><br>" +
        "<strong>💭 Overcoming Challenges</strong><br>" +
        "<strong>Feeling overwhelmed:</strong> Break coping into small, manageable steps<br>" +
        "<strong>Impatience with progress:</strong> Remember that developing coping skills takes time<br>" +
        "<strong>Fear of seeking help:</strong> Professional help is a sign of strength, not weakness<br>" +
        "<strong>Perfectionism:</strong> Accept that progress isn't always linear<br><br>" +
        f"<strong>🌟 Building Your {topic.title()} Coping Toolkit</strong><br>" +
        "<strong>Relaxation techniques:</strong> Practice deep breathing, meditation, and progressive muscle relaxation<br>" +
        "<strong>Distraction strategies:</strong> Develop healthy ways to take breaks from difficult thoughts<br>" +
        "<strong>Problem-solving skills:</strong> Learn systematic approaches to addressing challenges<br>" +
        "<strong>Social support:</strong> Build relationships with people who can help and support you<br>" +
        "<strong>Physical activity:</strong> Regular exercise is one of the most effective coping strategies<br>" +
        "<strong>Professional resources:</strong> Know when and how to access professional help<br><br>" +
        "<strong>💝 Encouraging Note:</strong><br>" +
        f"Coping with {topic} is a skill that can be learned and improved over time. Be patient with yourself and remember that seeking help is a sign of strength, not weakness. You have the resilience and ability to develop effective coping strategies and live a fulfilling life."
    }

def create_general_lesson(lesson_id, title):
    """Create detailed content for general lessons"""
    topic = lesson_id.replace('-', ' ')
    return {
        "title": title,
        "content": f"Learn about {topic} and develop skills to support your mental health and wellbeing.<br><br>" +
        f"<strong>🎯 Understanding {topic.title()}</strong><br>" +
        f"<strong>What it is:</strong> {topic} is an important aspect of mental health and personal development<br>" +
        f"<strong>Why it matters:</strong> Developing skills in {topic} can improve your overall quality of life<br>" +
        "<strong>It's learnable:</strong> You can develop skills in this area through practice and patience<br>" +
        "<strong>It's empowering:</strong> Developing these skills gives you more control over your life<br><br>" +
        f"<strong>🌟 Benefits of Developing {topic.title()}</strong><br>" +
        "<strong>Improved mental health:</strong> Good skills support better mental health and wellbeing<br>" +
        "<strong>Better relationships:</strong> Strong skills help you build and maintain healthy relationships<br>" +
        "<strong>Increased confidence:</strong> Developing skills builds confidence and self-esteem<br>" +
        "<strong>Life satisfaction:</strong> Strong skills contribute to overall life satisfaction<br>" +
        "<strong>Better decision-making:</strong> Developed skills help you make better choices<br>" +
        "<strong>Increased resilience:</strong> Strong skills help you bounce back from setbacks<br><br>" +
        f"<strong>💡 How to Develop {topic.title()}</strong><br>" +
        "<strong>Start small:</strong> Begin with simple exercises and gradually build your skills<br>" +
        "<strong>Be consistent:</strong> Regular practice is more important than perfect execution<br>" +
        "<strong>Seek support:</strong> Don't try to develop skills alone - get help from others<br>" +
        "<strong>Be patient:</strong> Learning new skills takes time and practice<br>" +
        "<strong>Learn from mistakes:</strong> View mistakes as learning opportunities<br>" +
        "<strong>Set realistic goals:</strong> Break down skill development into manageable steps<br><br>" +
        "<strong>🧠 The Science of Skill Development</strong><br>" +
        "<strong>Neuroplasticity:</strong> Your brain can form new connections and pathways throughout life<br>" +
        "<strong>Deliberate practice:</strong> Focused, intentional practice is more effective than casual practice<br>" +
        "<strong>Learning curves:</strong> Skill development often follows predictable patterns<br>" +
        "<strong>Individual differences:</strong> Everyone learns and develops skills at their own pace<br><br>" +
        "<strong>💭 Overcoming Challenges</strong><br>" +
        "<strong>Impatience with progress:</strong> Remember that skill development takes time and practice<br>" +
        "<strong>Fear of failure:</strong> View mistakes as learning opportunities, not failures<br>" +
        "<strong>Comparing to others:</strong> Focus on your own progress and development<br>" +
        "<strong>Lack of motivation:</strong> Find ways to make skill development enjoyable and rewarding<br><br>" +
        f"<strong>🌟 Building Your {topic.title()} Development Plan</strong><br>" +
        "<strong>Set clear goals:</strong> Define what you want to achieve and by when<br>" +
        "<strong>Create a practice schedule:</strong> Set aside regular time for skill development<br>" +
        "<strong>Find resources:</strong> Seek out books, courses, mentors, and other learning resources<br>" +
        "<strong>Track your progress:</strong> Keep a journal of your development and achievements<br>" +
        "<strong>Celebrate milestones:</strong> Acknowledge and celebrate your progress along the way<br>" +
        "<strong>Seek feedback:</strong> Get input from others to help guide your development<br><br>" +
        "<strong>💝 Encouraging Note:</strong><br>" +
        f"Developing {topic} skills is an investment in yourself that will benefit you throughout your life. Every step you take toward learning these skills is a step toward a happier, healthier, and more fulfilling life. You have the ability to learn and grow in amazing ways."
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
    """Main function to add detailed lessons"""
    
    # Read the missing lessons
    with open('missing_lesson_ids.txt', 'r') as f:
        missing_lessons = [line.strip() for line in f.readlines()]
    
    # Get the first 10 lessons for testing
    batch_lessons = missing_lessons[:10]
    
    html_file = 'index.html'
    
    print(f"Adding detailed content for {len(batch_lessons)} lessons to {html_file}")
    
    successful_additions = 0
    failed_additions = 0
    
    for i, lesson_id in enumerate(batch_lessons, 1):
        lesson_data = create_detailed_lesson_content(lesson_id)
        
        print(f"Adding detailed lesson {i}/{len(batch_lessons)}: {lesson_id}")
        
        success = add_lesson_to_instructions(
            lesson_id,
            lesson_data['title'],
            lesson_data['content'],
            html_file
        )
        
        if success:
            print(f"✓ Successfully added detailed content: {lesson_data['title']}")
            successful_additions += 1
        else:
            print(f"✗ Failed to add: {lesson_data['title']}")
            failed_additions += 1
    
    print(f"\nCompleted adding detailed content for {len(batch_lessons)} lessons.")
    print(f"Successful additions: {successful_additions}")
    print(f"Failed additions: {failed_additions}")

if __name__ == "__main__":
    main()
