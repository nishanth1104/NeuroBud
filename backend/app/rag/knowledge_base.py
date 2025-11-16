"""
Mental Health Knowledge Base
Contains 50 curated articles on mental wellness topics
"""

MENTAL_HEALTH_ARTICLES = [
    # ========== ANXIETY (10 articles) ==========
    {
        "id": "anxiety_001",
        "title": "Understanding Anxiety Disorders",
        "category": "anxiety",
        "content": """
        Anxiety is a normal and often healthy emotion. However, when a person regularly feels 
        disproportionate levels of anxiety, it might become a medical disorder. Anxiety disorders 
        form a category of mental health diagnoses that lead to excessive nervousness, fear, 
        apprehension, and worry.
        
        Common symptoms include:
        - Feeling nervous, restless, or tense
        - Having a sense of impending danger, panic, or doom
        - Increased heart rate
        - Rapid breathing (hyperventilation)
        - Sweating and trembling
        - Feeling weak or tired
        - Difficulty concentrating
        - Trouble sleeping
        
        Treatment options include therapy (especially CBT), medication, lifestyle changes, 
        and relaxation techniques. Most people with anxiety disorders benefit from a combination 
        of treatments.
        """
    },
    {
        "id": "anxiety_002",
        "title": "Types of Anxiety Disorders",
        "category": "anxiety",
        "content": """
        There are several types of anxiety disorders:
        
        1. Generalized Anxiety Disorder (GAD): Persistent and excessive worry about various aspects of life
        2. Panic Disorder: Recurrent unexpected panic attacks
        3. Social Anxiety Disorder: Intense fear of social situations and being judged
        4. Specific Phobias: Intense fear of specific objects or situations (heights, animals, flying)
        5. Agoraphobia: Fear of places or situations where escape might be difficult
        6. Separation Anxiety: Fear of being separated from attachment figures
        
        Each type has specific diagnostic criteria and treatment approaches. Professional diagnosis 
        is important for effective treatment. Many people experience more than one type of anxiety disorder.
        """
    },
    {
        "id": "anxiety_003",
        "title": "Physical Symptoms of Anxiety",
        "category": "anxiety",
        "content": """
        Anxiety manifests in numerous physical symptoms that can be frightening:
        
        Cardiovascular: Racing heart, chest pain, palpitations, high blood pressure
        Respiratory: Shortness of breath, rapid breathing, feeling of choking
        Gastrointestinal: Nausea, diarrhea, upset stomach, loss of appetite, IBS symptoms
        Muscular: Tension, aches, trembling, restlessness, jaw clenching
        Neurological: Dizziness, headaches, numbness, tingling, feeling faint
        Other: Sweating, fatigue, insomnia, frequent urination, dry mouth
        
        These physical symptoms are real and can be distressing. Understanding they're 
        anxiety-related can help you manage them better. However, always rule out medical 
        causes with your doctor.
        """
    },
    {
        "id": "anxiety_004",
        "title": "Anxiety Triggers and How to Identify Them",
        "category": "anxiety",
        "content": """
        Common anxiety triggers include:
        
        - Health issues or medical appointments
        - Work stress, deadlines, or performance evaluations
        - Financial concerns or major purchases
        - Relationship problems or conflicts
        - Caffeine, alcohol, and stimulants
        - Lack of sleep or poor sleep quality
        - Certain medications or supplements
        - Traumatic events or reminders of trauma
        - Major life changes (moving, job change, etc.)
        - Social situations or public speaking
        
        Identifying your triggers:
        1. Keep an anxiety journal
        2. Note what happened before anxiety increased
        3. Track patterns over time (time of day, situations, people)
        4. Rate anxiety levels (1-10)
        5. Note physical sensations and thoughts
        
        Once identified, you can develop specific coping strategies for your triggers.
        """
    },
    {
        "id": "anxiety_005",
        "title": "Managing Social Anxiety",
        "category": "anxiety",
        "content": """
        Social anxiety disorder involves intense fear of social situations where you might 
        be judged, embarrassed, or scrutinized by others.
        
        Common fears:
        - Speaking in public
        - Eating or drinking in front of others
        - Meeting new people
        - Being the center of attention
        - Making phone calls
        - Using public restrooms
        
        Coping strategies:
        - Challenge negative thoughts about social situations
        - Practice social skills in low-stakes situations
        - Use breathing exercises before social events
        - Focus on others rather than yourself
        - Set small, achievable social goals
        - Prepare conversation topics in advance
        - Remember that people notice your anxiety less than you think
        
        Professional treatment (CBT and exposure therapy) is highly effective for social anxiety.
        """
    },
    {
        "id": "anxiety_006",
        "title": "Panic Attacks: Recognition and Management",
        "category": "anxiety",
        "content": """
        A panic attack is a sudden episode of intense fear that triggers severe physical 
        reactions when there is no real danger or apparent cause.
        
        Symptoms (usually peak within 10 minutes):
        - Rapid heart rate
        - Sweating
        - Trembling or shaking
        - Shortness of breath
        - Chest pain
        - Nausea
        - Dizziness
        - Fear of losing control or dying
        
        During a panic attack:
        1. Recognize it's a panic attack (not a heart attack)
        2. Use deep breathing exercises (4-7-8 technique)
        3. Use grounding techniques (5-4-3-2-1)
        4. Focus on something in your environment
        5. Remember it will pass (usually within 20 minutes)
        6. Don't fight it - accept it's happening
        
        Prevention: Regular exercise, avoid caffeine/alcohol, practice relaxation daily, 
        get adequate sleep, consider CBT.
        """
    },
    {
        "id": "anxiety_007",
        "title": "Generalized Anxiety Disorder (GAD)",
        "category": "anxiety",
        "content": """
        GAD involves persistent and excessive worry about various aspects of daily life 
        for at least 6 months.
        
        Common worries:
        - Health (yours and loved ones)
        - Work performance
        - Finances
        - Relationships
        - Daily responsibilities
        - Future events
        
        Symptoms:
        - Difficulty controlling worry
        - Restlessness
        - Fatigue
        - Difficulty concentrating
        - Irritability
        - Muscle tension
        - Sleep problems
        
        Treatment typically includes:
        - Cognitive Behavioral Therapy (CBT)
        - Mindfulness practices
        - Relaxation techniques
        - Sometimes medication (SSRIs, SNRIs)
        - Lifestyle modifications
        
        GAD is highly treatable with proper intervention.
        """
    },
    {
        "id": "anxiety_008",
        "title": "Health Anxiety (Hypochondria)",
        "category": "anxiety",
        "content": """
        Health anxiety involves excessive worry about having or developing a serious illness, 
        despite medical reassurance.
        
        Common patterns:
        - Frequent doctor visits
        - Excessive health-related internet searches
        - Constantly checking body for signs of illness
        - Seeking repeated reassurance
        - Avoiding medical appointments (fear of bad news)
        - Misinterpreting normal body sensations
        
        Helpful strategies:
        - Limit health-related internet searches
        - Challenge catastrophic thoughts
        - Practice mindfulness
        - Reduce body checking
        - Address underlying anxiety
        - Work with a therapist specializing in health anxiety
        
        Remember: The anxiety is real even if the feared illness isn't.
        """
    },
    {
        "id": "anxiety_009",
        "title": "Performance Anxiety",
        "category": "anxiety",
        "content": """
        Performance anxiety occurs when you fear you won't perform well in specific situations.
        
        Common situations:
        - Public speaking
        - Test-taking
        - Job interviews
        - Athletic competitions
        - Musical or theatrical performances
        - Sexual performance
        
        Symptoms:
        - Racing thoughts
        - Mental blanking
        - Sweating
        - Trembling
        - Rapid heartbeat
        - Nausea
        
        Coping strategies:
        - Prepare thoroughly
        - Practice relaxation techniques beforehand
        - Use visualization (imagine success)
        - Reframe anxiety as excitement
        - Focus on the task, not the outcome
        - Accept that some anxiety is normal
        - Gradually expose yourself to performance situations
        
        Beta-blockers may help physical symptoms in some cases.
        """
    },
    {
        "id": "anxiety_010",
        "title": "Obsessive-Compulsive Disorder (OCD)",
        "category": "anxiety",
        "content": """
        OCD is characterized by unwanted, intrusive thoughts (obsessions) and repetitive 
        behaviors or mental acts (compulsions) performed to reduce anxiety.
        
        Common obsessions:
        - Fear of contamination
        - Need for symmetry or order
        - Unwanted aggressive or sexual thoughts
        - Fear of harming self or others
        - Religious or moral concerns
        
        Common compulsions:
        - Excessive cleaning or handwashing
        - Checking (locks, appliances, etc.)
        - Counting or repeating
        - Ordering or arranging
        - Seeking reassurance
        
        Treatment:
        - Exposure and Response Prevention (ERP)
        - Cognitive Behavioral Therapy (CBT)
        - Medication (SSRIs)
        - Support groups
        
        OCD is NOT about being neat or organized - it's a serious condition that requires treatment.
        """
    },

    # ========== DEPRESSION (10 articles) ==========
    {
        "id": "depression_001",
        "title": "Understanding Major Depression",
        "category": "depression",
        "content": """
        Depression (major depressive disorder) is a common and serious medical illness that 
        negatively affects how you feel, think, and act. It causes feelings of sadness and/or 
        a loss of interest in activities you once enjoyed.
        
        Symptoms (must have at least 5 for 2+ weeks):
        - Persistent sad, anxious, or empty mood
        - Loss of interest in hobbies and activities
        - Decreased energy or fatigue
        - Difficulty concentrating, remembering, or making decisions
        - Sleep disturbances (insomnia or oversleeping)
        - Appetite changes (loss or increase)
        - Feelings of worthlessness or guilt
        - Physical symptoms (aches, digestive problems)
        - Thoughts of death or suicide
        
        Depression is treatable. Between 80-90% of people with depression eventually respond 
        well to treatment. Treatment may include medication, psychotherapy, or both.
        """
    },
    {
        "id": "depression_002",
        "title": "Types of Depression",
        "category": "depression",
        "content": """
        Different forms of depression include:
        
        1. Major Depressive Disorder: Severe symptoms lasting at least 2 weeks
        2. Persistent Depressive Disorder (Dysthymia): Less severe but chronic (2+ years)
        3. Seasonal Affective Disorder (SAD): Depression related to seasonal changes (usually winter)
        4. Postpartum Depression: Occurs after childbirth, more severe than "baby blues"
        5. Premenstrual Dysphoric Disorder (PMDD): Severe mood changes before menstruation
        6. Bipolar Disorder: Alternating episodes of depression and mania
        7. Situational Depression: Triggered by specific life events (also called adjustment disorder)
        8. Atypical Depression: Mood brightens in response to positive events
        
        Each type may require different treatment approaches. Proper diagnosis is crucial 
        for effective treatment.
        """
    },
    {
        "id": "depression_003",
        "title": "Depression vs. Sadness: Key Differences",
        "category": "depression",
        "content": """
        It's important to distinguish between clinical depression and normal sadness:
        
        Normal Sadness:
        - Related to specific events
        - Improves over time
        - Doesn't significantly impair functioning
        - Can still experience joy
        - Self-esteem intact
        - Duration is proportional to the event
        
        Clinical Depression:
        - May occur without clear reason
        - Persists for weeks/months
        - Significantly impacts daily life
        - Persistent inability to feel pleasure (anhedonia)
        - Often includes feelings of worthlessness
        - May include physical symptoms
        - Doesn't improve on its own
        
        If you're experiencing symptoms for more than 2 weeks, or they're affecting your 
        daily life, consult a mental health professional.
        """
    },
    {
        "id": "depression_004",
        "title": "Behavioral Activation for Depression",
        "category": "depression",
        "content": """
        Behavioral activation is a key component of depression treatment. When depressed, 
        we tend to withdraw from activities, which worsens depression - creating a vicious cycle.
        
        The activation cycle:
        Depression → Withdrawal → Less positive experiences → More depression
        
        Breaking the cycle:
        1. Start small - even tiny actions count
        2. Schedule pleasant activities daily
        3. Break tasks into manageable steps
        4. Track your mood before and after activities
        5. Gradually increase activity levels
        6. Include social activities
        7. Don't wait to "feel like it" - action comes first, motivation follows
        
        Common activities to schedule:
        - Short walks (even 5 minutes)
        - Calling or texting a friend
        - Listening to music
        - Taking a shower
        - Light exercise or stretching
        - Preparing a healthy meal
        - Spending time in nature
        
        Remember: You don't need to enjoy it at first, just do it.
        """
    },
    {
        "id": "depression_005",
        "title": "Supporting Someone with Depression",
        "category": "depression",
        "content": """
        If someone you care about has depression, your support matters:
        
        Do:
        - Listen without judgment
        - Offer specific help ("I'm coming over to make dinner" vs. "let me know if you need anything")
        - Encourage treatment
        - Be patient - recovery takes time
        - Take care of yourself too
        - Learn about depression
        - Acknowledge their pain
        - Spend time with them
        
        Don't:
        - Say "snap out of it" or "just think positive"
        - Minimize their feelings ("it's not that bad")
        - Take their behavior personally
        - Try to "fix" them
        - Give up on them
        - Force them to do things
        - Compare their situation to others
        
        Remember: You can't cure their depression, but your support and presence matter 
        more than you might think.
        """
    },
    {
        "id": "depression_006",
        "title": "Seasonal Affective Disorder (SAD)",
        "category": "depression",
        "content": """
        SAD is a type of depression that follows a seasonal pattern, typically occurring 
        in fall and winter when there's less natural sunlight.
        
        Symptoms:
        - Oversleeping
        - Overeating (especially carbs)
        - Weight gain
        - Social withdrawal
        - Low energy
        - Depression
        
        Treatment options:
        1. Light therapy: 30 minutes daily with a 10,000 lux light box
        2. Vitamin D supplementation
        3. Regular exercise, especially outdoors
        4. Maintain consistent sleep schedule
        5. Cognitive Behavioral Therapy (CBT-SAD)
        6. Antidepressant medication
        7. Plan activities to look forward to
        
        Starting treatment before symptoms begin can prevent full-blown SAD.
        """
    },
    {
        "id": "depression_007",
        "title": "Postpartum Depression",
        "category": "depression",
        "content": """
        Postpartum depression affects 1 in 7 new mothers and is more than "baby blues."
        
        Symptoms:
        - Severe mood swings
        - Excessive crying
        - Difficulty bonding with baby
        - Withdrawing from family and friends
        - Loss of appetite or overeating
        - Inability to sleep or sleeping too much
        - Overwhelming fatigue
        - Feelings of inadequacy as a parent
        - Anxiety or panic attacks
        - Thoughts of harming yourself or baby
        
        Risk factors:
        - History of depression
        - Lack of support
        - Pregnancy/birth complications
        - Financial stress
        - Unplanned pregnancy
        
        Treatment:
        - Therapy (especially CBT and IPT)
        - Support groups
        - Medication (some are safe while breastfeeding)
        - Practical support with childcare
        
        This is a medical condition, not a character flaw. Seek help immediately.
        """
    },
    {
        "id": "depression_008",
        "title": "Depression and Physical Health",
        "category": "depression",
        "content": """
        Depression significantly affects physical health and vice versa:
        
        How depression affects the body:
        - Weakened immune system
        - Increased inflammation
        - Heart disease risk
        - Chronic pain
        - Digestive problems
        - Sleep disturbances
        - Appetite changes
        - Fatigue
        
        Physical conditions that can cause/worsen depression:
        - Chronic pain
        - Thyroid disorders
        - Heart disease
        - Diabetes
        - Cancer
        - Stroke
        - Chronic illness
        
        The mind-body connection means treating depression often improves physical health 
        and treating physical conditions can improve depression. Always discuss both with 
        your healthcare provider.
        """
    },
    {
        "id": "depression_009",
        "title": "Treatment-Resistant Depression",
        "category": "depression",
        "content": """
        Treatment-resistant depression occurs when symptoms don't improve after trying at 
        least two different antidepressants.
        
        Additional treatment options:
        1. Different medication class
        2. Combination of medications
        3. Augmentation (adding another medication)
        4. Intensive psychotherapy
        5. Electroconvulsive Therapy (ECT)
        6. Transcranial Magnetic Stimulation (TMS)
        7. Ketamine or esketamine treatment
        8. Addressing underlying conditions
        
        Important steps:
        - Verify you took medications as prescribed
        - Ensure adequate trial period (usually 6-8 weeks)
        - Check for medical conditions affecting treatment
        - Consider genetic testing for medication metabolism
        - Explore therapy options (CBT, DBT, IPT)
        - Lifestyle factors (sleep, exercise, nutrition)
        
        Don't give up - there are many treatment options available.
        """
    },
    {
        "id": "depression_010",
        "title": "Suicide Prevention and Warning Signs",
        "category": "depression",
        "content": """
        Recognizing warning signs can save lives:
        
        Warning signs:
        - Talking about wanting to die or suicide
        - Looking for ways to kill oneself
        - Talking about feeling hopeless or having no purpose
        - Saying they feel trapped
        - Increasing alcohol or drug use
        - Withdrawing from activities
        - Isolating from family and friends
        - Sleeping too much or too little
        - Visiting or calling to say goodbye
        - Giving away possessions
        - Aggression or reckless behavior
        - Extreme mood swings
        
        If you're concerned:
        - Ask directly: "Are you thinking about suicide?"
        - Listen without judgment
        - Don't leave them alone
        - Remove access to lethal means
        - Help them connect with support (988 Suicide & Crisis Lifeline)
        - Follow up regularly
        
        If immediate danger: Call 911 or go to emergency room
        
        Crisis resources:
        - 988 Suicide & Crisis Lifeline (call or text 988)
        - Crisis Text Line (text HOME to 741741)
        - Veterans Crisis Line (988 then press 1)
        """
    },

    # ========== CBT & THERAPY (10 articles) ==========
    {
        "id": "cbt_001",
        "title": "Cognitive Behavioral Therapy Fundamentals",
        "category": "therapy",
        "content": """
        Cognitive Behavioral Therapy (CBT) is an evidence-based psychotherapy that helps 
        people identify and change destructive thought patterns that negatively influence 
        behavior and emotions.
        
        Core principles:
        1. Psychological problems are based partly on faulty or unhelpful thinking patterns
        2. Psychological problems are based partly on learned patterns of unhelpful behavior
        3. People can learn better coping mechanisms to relieve symptoms
        
        Key components:
        - Identifying automatic negative thoughts
        - Recognizing cognitive distortions
        - Challenging irrational beliefs
        - Behavioral experiments
        - Exposure therapy
        - Problem-solving skills
        - Relaxation and stress reduction
        
        CBT is typically short-term (12-20 sessions), structured, and goal-oriented. 
        It's one of the most researched and effective treatments for anxiety and depression.
        """
    },
    {
        "id": "cbt_002",
        "title": "Cognitive Distortions: Common Thinking Errors",
        "category": "therapy",
        "content": """
        Cognitive distortions are irrational thought patterns that maintain negative emotions:
        
        1. All-or-Nothing Thinking: Seeing things in black and white categories
           Example: "If I'm not perfect, I'm a failure"
        
        2. Overgeneralization: Drawing broad conclusions from single events
           Example: "I failed this test, I'll never succeed at anything"
        
        3. Mental Filter: Focusing only on negatives while filtering out positives
           Example: Getting 9 compliments and 1 criticism, only remembering the criticism
        
        4. Discounting the Positive: Rejecting positive experiences
           Example: "They're just being nice, it doesn't count"
        
        5. Jumping to Conclusions:
           - Mind reading: "They think I'm stupid"
           - Fortune telling: "This will definitely end badly"
        
        6. Magnification/Minimization: Exaggerating negatives, minimizing positives
           Example: "This mistake is catastrophic" vs. "That accomplishment was nothing"
        
        7. Emotional Reasoning: Believing feelings reflect reality
           Example: "I feel worthless, therefore I am worthless"
        
        8. Should Statements: Rigid rules about how things "should" be
           Example: "I should always be happy" or "They should know what I need"
        
        9. Labeling: Assigning global labels based on specific behaviors
           Example: "I made a mistake, I'm an idiot"
        
        10. Personalization: Blaming yourself for things outside your control
            Example: "It's my fault they're upset"
        
        Identifying these patterns is the first step to changing them.
        """
    },
    {
        "id": "cbt_003",
        "title": "Thought Records: Challenging Negative Thoughts",
        "category": "therapy",
        "content": """
        Thought records are a CBT tool to identify, examine, and challenge negative thoughts:
        
        Seven-column thought record:
        1. Situation: What happened? Where? When? Who was involved?
        2. Automatic Thoughts: What went through your mind?
        3. Emotions: What did you feel? Rate intensity (0-100%)
        4. Evidence For: What supports this thought?
        5. Evidence Against: What contradicts it?
        6. Alternative/Balanced Thought: What's a more realistic view?
        7. Re-rate Emotions: How do you feel now? (0-100%)
        
        Example:
        Situation: Friend didn't respond to my text for 2 days
        Thought: "They hate me and don't want to be friends anymore"
        Emotion: Sad (85%), Anxious (75%)
        Evidence For: They didn't respond for 2 days
        Evidence Against: They've been a good friend for years, they're often busy with work, 
                          they've been slow to respond before and it wasn't about me
        Alternative: "They're probably busy with work. I'll check in tomorrow or call them."
        Re-rate: Sad (30%), Anxious (20%)
        
        Practice this regularly to make it automatic.
        """
    },
    {
        "id": "cbt_004",
        "title": "Behavioral Experiments in CBT",
        "category": "therapy",
        "content": """
        Behavioral experiments test the accuracy of negative predictions and beliefs:
        
        Steps:
        1. Identify the belief/prediction
        2. Design an experiment to test it
        3. Predict the outcome
        4. Conduct the experiment
        5. Observe what actually happens
        6. Draw conclusions
        
        Example:
        Belief: "If I speak up in meetings, everyone will think I'm stupid"
        Experiment: Share one idea in next meeting
        Prediction: Everyone will judge me negatively (80% confidence)
        Actual result: Two people engaged with my idea positively, no negative reactions observed
        Conclusion: My prediction was inaccurate; people don't judge me as harshly as I expected
        
        Common experiments:
        - Testing social predictions (people will reject me)
        - Testing perfectionism (what if I don't do it perfectly?)
        - Testing anxiety predictions (I'll have a panic attack)
        - Testing avoidance (what if I face this fear?)
        
        Start with lower-risk experiments and build up gradually.
        """
    },
    {
        "id": "cbt_005",
        "title": "Exposure Therapy for Anxiety",
        "category": "therapy",
        "content": """
        Exposure therapy involves gradually facing feared situations to reduce anxiety over time.
        
        How it works:
        - Repeated exposure to feared situations reduces anxiety response
        - You learn the feared outcome doesn't occur (or isn't as bad as expected)
        - Avoidance maintains fear; exposure reduces it
        
        Types of exposure:
        1. In vivo: Real-life exposure (facing actual feared situation)
        2. Imaginal: Imagining the feared situation in detail
        3. Interoceptive: Inducing feared physical sensations
        4. Virtual reality: Using VR to simulate feared situations
        
        Exposure hierarchy (0-100 anxiety rating):
        Start with least anxiety-provoking and gradually progress:
        - 20: Looking at pictures of dogs
        - 40: Watching videos of dogs
        - 60: Being near a small dog on a leash
        - 80: Petting a calm dog
        - 100: Being around multiple dogs
        
        Key principles:
        - Stay in situation until anxiety decreases (don't escape)
        - Practice repeatedly
        - Use coping skills during exposure
        - Gradually increase difficulty
        
        Work with a therapist for guidance, especially for severe anxiety.
        """
    },
    {
        "id": "therapy_001",
        "title": "Types of Psychotherapy",
        "category": "therapy",
        "content": """
        Different therapeutic approaches for different needs:
        
        1. Cognitive Behavioral Therapy (CBT): Focus on changing thoughts and behaviors
           Best for: Anxiety, depression, OCD, eating disorders
        
        2. Dialectical Behavior Therapy (DBT): Emotional regulation and distress tolerance
           Best for: Borderline personality disorder, self-harm, emotional dysregulation
        
        3. Acceptance and Commitment Therapy (ACT): Mindfulness and value-based living
           Best for: Chronic pain, anxiety, depression
        
        4. Psychodynamic Therapy: Exploring unconscious patterns and past experiences
           Best for: Relationship issues, long-standing patterns
        
        5. Interpersonal Therapy (IPT): Improving relationships and social functioning
           Best for: Depression, grief, relationship problems
        
        6. EMDR: Processing traumatic memories through bilateral stimulation
           Best for: PTSD, trauma, phobias
        
        7. Mindfulness-Based Therapies: Present-moment awareness and acceptance
           Best for: Stress, anxiety, chronic pain
        
        8. Humanistic/Person-Centered: Focus on self-actualization and personal growth
           Best for: Personal development, identity issues
        
        The best approach depends on your specific needs. Many therapists use integrative 
        approaches combining multiple methods.
        """
    },
    {
        "id": "therapy_002",
        "title": "How to Find the Right Therapist",
        "category": "therapy",
        "content": """
        Finding the right therapist is crucial for successful treatment:
        
        Steps:
        1. Determine your needs (anxiety, depression, trauma, relationships, etc.)
        2. Check insurance coverage or set a budget
        3. Search directories:
           - Psychology Today
           - TherapyDen
           - GoodTherapy
           - SAMHSA treatment locator
        4. Ask for recommendations from doctor, friends, or family
        5. Check credentials (licensed psychologist, LCSW, LPC, LMFT)
        6. Review specializations and treatment approaches
        7. Schedule consultations with 2-3 therapists
        8. Ask questions during consultation
        9. Trust your gut about the fit
        
        Questions to ask:
        - What's your experience with [my issue]?
        - What's your therapeutic approach?
        - How long is typical treatment?
        - What are your fees/do you take my insurance?
        - What's your availability?
        - What's your cancellation policy?
        
        Red flags:
        - Doesn't respect boundaries
        - Judgmental or dismissive
        - Promises quick fixes
        - Dual relationships (treats family members/friends)
        - Doesn't have proper credentials
        - Makes you feel uncomfortable
        
        It's okay to switch therapists if it's not working - fit matters!
        """
    },
    {
        "id": "therapy_003",
        "title": "What to Expect in Therapy",
        "category": "therapy",
        "content": """
        Understanding the therapy process helps reduce anxiety about starting:
        
        First session:
        - Intake and assessment
        - Discussion of concerns and goals
        - Review of history
        - Questions about therapy process
        - Discussion of confidentiality and limits
        - Setting expectations
        
        Typical sessions:
        - Usually 45-50 minutes
        - Weekly or bi-weekly initially
        - Structured conversation
        - Homework between sessions
        - Progress toward goals
        
        What therapy involves:
        - Talking about difficult emotions
        - Facing uncomfortable truths
        - Challenging yourself
        - Practicing new skills
        - Being vulnerable
        - Sometimes feeling worse before better
        
        Your role:
        - Be honest and open
        - Come prepared
        - Complete homework
        - Practice skills between sessions
        - Communicate about what's working/not working
        - Be patient with the process
        
        Confidentiality:
        Therapists must keep information confidential except:
        - Risk of harm to self or others
        - Child or elder abuse
        - Court order
        - You give written permission
        
        Remember: Progress isn't linear. Ups and downs are normal.
        """
    },
    {
        "id": "therapy_004",
        "title": "Dialectical Behavior Therapy (DBT) Skills",
        "category": "therapy",
        "content": """
        DBT teaches four main skill modules:
        
        1. Mindfulness:
        - Observe: Notice without judgment
        - Describe: Put words to experience
        - Participate: Be fully present
        - Non-judgmental stance
        - One-mindfully: Focus on one thing
        - Effectively: Do what works
        
        2. Distress Tolerance:
        - TIPP: Temperature, Intense exercise, Paced breathing, Paired muscle relaxation
        - ACCEPTS: Activities, Contributing, Comparisons, Emotions, Pushing away, Thoughts, Sensations
        - Self-soothe with five senses
        - IMPROVE the moment
        - Radical acceptance
        
        3. Emotion Regulation:
        - Identify and label emotions
        - Understand function of emotions
        - Reduce vulnerability (PLEASE: Physical illness, Eating, Avoid drugs, Sleep, Exercise)
        - Increase positive emotions
        - Opposite action
        - Problem-solving
        
        4. Interpersonal Effectiveness:
        - DEAR MAN: Describe, Express, Assert, Reinforce, Mindful, Appear confident, Negotiate
        - GIVE: Gentle, Interested, Validate, Easy manner
        - FAST: Fair, Apologies (no excessive), Stick to values, Truthful
        
        These skills are useful for everyone, not just those with BPD.
        """
    },
    {
        "id": "therapy_005",
        "title": "EMDR Therapy for Trauma",
        "category": "therapy",
        "content": """
        Eye Movement Desensitization and Reprocessing (EMDR) helps process traumatic memories:
        
        How it works:
        - While recalling trauma, you focus on external stimulus (eye movements, tapping, sounds)
        - This bilateral stimulation helps brain reprocess traumatic memory
        - Memory becomes less emotionally charged
        - New, adaptive information is integrated
        
        Eight phases:
        1. History taking and treatment planning
        2. Preparation and stabilization
        3. Assessment of target memory
        4. Desensitization
        5. Installation of positive belief
        6. Body scan
        7. Closure
        8. Re-evaluation
        
        What to expect:
        - Initial sessions focus on preparation and coping skills
        - During processing, you recall trauma while tracking therapist's hand movements
        - May experience strong emotions during processing
        - Memories may surface between sessions
        - Typical treatment: 6-12 sessions
        
        Best for:
        - PTSD
        - Single-incident trauma
        - Complex trauma
        - Phobias
        - Panic attacks
        - Performance anxiety
        
        EMDR is evidence-based and recognized by WHO and APA for PTSD treatment.
        """
    },

    # ========== COPING SKILLS (10 articles) ==========
    {
        "id": "breathing_001",
        "title": "Deep Breathing Techniques",
        "category": "coping",
        "content": """
        Deep breathing activates the parasympathetic nervous system, triggering relaxation:
        
        4-7-8 Breathing:
        1. Exhale completely through mouth
        2. Close mouth, inhale through nose for 4 counts
        3. Hold breath for 7 counts
        4. Exhale completely through mouth for 8 counts
        5. Repeat 3-4 times
        Best for: Sleep, calming panic
        
        Box Breathing (Square Breathing):
        1. Breathe in for 4 counts
        2. Hold for 4 counts
        3. Breathe out for 4 counts
        4. Hold for 4 counts
        5. Repeat
        Best for: Focus, stress management
        
        Diaphragmatic Breathing:
        1. Place one hand on chest, one on belly
        2. Breathe in through nose, letting belly expand (not chest)
        3. Exhale slowly through mouth
        4. Repeat for 5-10 minutes
        Best for: General relaxation, reducing physical tension
        
        Alternate Nostril Breathing:
        1. Close right nostril, inhale through left
        2. Close left nostril, exhale through right
        3. Inhale through right
        4. Exhale through left
        5. Repeat
        Best for: Balance, mental clarity
        
        Practice these daily when calm so they're easier to use during stress.
        """
    },
    {
        "id": "grounding_001",
        "title": "Grounding Techniques",
        "category": "coping",
        "content": """
        Grounding helps you stay connected to the present during anxiety, panic, or dissociation:
        
        5-4-3-2-1 Technique (Most popular):
        - 5 things you can SEE (look around the room)
        - 4 things you can TOUCH (feel textures)
        - 3 things you can HEAR (focus on sounds)
        - 2 things you can SMELL (notice scents)
        - 1 thing you can TASTE (or name favorite food)
        
        Physical Grounding:
        - Plant feet firmly on ground, press into floor
        - Hold ice cubes
        - Splash cold water on face
        - Touch something with texture (fuzzy blanket, rough tree bark)
        - Clench and release fists
        - Stretch arms or legs
        - Do wall push-ups
        - Jump up and down
        
        Mental Grounding:
        - Count backwards from 100 by 7s
        - Name objects in the room
        - Describe your surroundings in detail
        - Name countries, cities, or animals alphabetically
        - Recite poem, song lyrics, or prayer
        
        Emotional Grounding:
        - Name your emotions: "I'm feeling anxious"
        - Remind yourself: "I'm safe right now"
        - List 3 things you're grateful for
        - Think of favorite place in detail
        
        Practice when calm to make it easier during distress.
        """
    },
    {
        "id": "progressive_relaxation_001",
        "title": "Progressive Muscle Relaxation (PMR)",
        "category": "coping",
        "content": """
        PMR reduces physical tension by systematically tensing and relaxing muscle groups:
        
        Basic technique:
        1. Find quiet space, get comfortable (sitting or lying)
        2. Take few deep breaths
        3. Starting with feet, tense muscles for 5-7 seconds
        4. Release and notice relaxation for 10-15 seconds
        5. Move up through body
        6. Practice 15-20 minutes
        
        Muscle group sequence:
        1. Feet and toes (curl toes tightly)
        2. Calves (point toes toward shin)
        3. Thighs (squeeze thighs together)
        4. Buttocks (tighten)
        5. Stomach (pull navel toward spine)
        6. Chest (take deep breath and hold)
        7. Hands (make tight fists)
        8. Arms (flex biceps)
        9. Shoulders (raise to ears)
        10. Neck (gently tilt head back)
        11. Face (scrunch face, then release)
        
        Tips:
        - Don't tense so hard it hurts
        - Breathe normally during tension
        - Really notice the difference between tension and relaxation
        - Can do seated version at work
        - Skip areas with injuries
        
        Benefits:
        - Reduces physical tension
        - Improves sleep
        - Lowers blood pressure
        - Reduces headaches
        - Increases body awareness
        
        Most effective with daily practice.
        """
    },
    {
        "id": "distraction_001",
        "title": "Healthy Distraction Techniques",
        "category": "coping",
        "content": """
        Distraction is a valid coping skill when emotions are too intense to process productively:
        
        Mental Distractions:
        - Count backwards by 7s from 100
        - Name countries/cities/animals alphabetically
        - Recite song lyrics, poems, or quotes
        - Do mental math problems
        - Play word games (find 5 things starting with 'B')
        - Describe an object in extreme detail
        
        Physical Distractions:
        - Go for walk or jog
        - Do jumping jacks or dance
        - Clean or organize a space
        - Garden or do yard work
        - Take a shower or bath
        - Do yoga or stretch
        
        Creative Distractions:
        - Draw, color, or paint
        - Write in journal
        - Play an instrument
        - Do crafts or puzzles
        - Cook or bake
        - Photography
        - Build something
        
        Social Distractions:
        - Call or text a friend
        - Join online community
        - Play with a pet
        - Help someone else
        - Watch comedy
        
        When to use distraction:
        - Emotions too intense to process
        - Waiting for therapy appointment
        - During crisis period
        - When you need a break from difficult emotions
        - To prevent rumination
        
        When NOT to use:
        - As only coping strategy
        - To completely avoid dealing with problems
        - Instead of addressing serious issues
        
        Balance distraction with processing emotions at appropriate times.
        """
    },
    {
        "id": "journaling_001",
        "title": "Therapeutic Journaling",
        "category": "coping",
        "content": """
        Journaling helps process emotions, gain insights, and track patterns:
        
        Types of journaling:
        
        1. Stream of consciousness: Write whatever comes to mind for 10-15 minutes
        
        2. Gratitude journal: List 3-5 things you're grateful for daily
        
        3. Emotion journal: Track emotions, triggers, and responses
        
        4. Problem-solving: Write about problem from different perspectives
        
        5. Dialogue journal: Write conversation between different parts of yourself
        
        6. Letter writing: Write unsent letters to express feelings
        
        7. Bullet journal: Track habits, moods, tasks
        
        Prompts:
        - What am I feeling right now?
        - What triggered these feelings?
        - What do I need right now?
        - What went well today?
        - What did I learn today?
        - What am I worried about?
        - What am I proud of?
        - What pattern am I noticing?
        
        Tips:
        - No judgment - write freely
        - Don't worry about grammar or spelling
        - Be honest
        - Keep it private if needed
        - Try different styles
        - Make it a routine (same time/place)
        - Re-read periodically to notice patterns
        
        Benefits:
        - Reduces stress
        - Improves mood
        - Enhances self-awareness
        - Tracks progress
        - Processes difficult emotions
        - Problem-solving
        """
    },
    {
        "id": "visualization_001",
        "title": "Guided Imagery and Visualization",
        "category": "coping",
        "content": """
        Visualization uses mental imagery to promote relaxation and positive states:
        
        Safe place visualization:
        1. Close eyes, take deep breaths
        2. Imagine a place you feel completely safe
        3. Engage all senses:
           - What do you see? (colors, light, surroundings)
           - What do you hear? (sounds, silence)
           - What do you smell?
           - What do you feel? (temperature, textures)
           - What emotions do you experience?
        4. Stay in this space for 5-10 minutes
        5. Know you can return anytime
        
        Progressive relaxation imagery:
        - Imagine warm light moving through body, relaxing each part
        - Visualize tension melting away like ice
        - Picture stress flowing out with each breath
        
        Goal visualization:
        - Imagine successfully achieving a goal
        - See yourself confident and capable
        - Feel the emotions of success
        - Notice details of the experience
        
        Nature scenes:
        - Beach (waves, sand, sun)
        - Forest (trees, birds, fresh air)
        - Mountain (vastness, peace, clarity)
        - Garden (flowers, butterflies, serenity)
        
        Tips:
        - Find quiet space
        - Use guided recordings if helpful
        - Make imagery as vivid as possible
        - Practice regularly
        - Create personal visualizations
        
        Effective for: Anxiety, stress, pain management, sleep, performance enhancement
        """
    },
    {
        "id": "self_compassion_001",
        "title": "Self-Compassion Practices",
        "category": "coping",
        "content": """
        Self-compassion means treating yourself with the same kindness you'd show a good friend:
        
        Three components (Kristin Neff):
        
        1. Self-Kindness vs. Self-Judgment:
        - Speak to yourself kindly
        - Recognize mistakes are part of being human
        - Be gentle with yourself during failures
        
        2. Common Humanity vs. Isolation:
        - Remember everyone struggles
        - Suffering is part of human experience
        - You're not alone in your challenges
        
        3. Mindfulness vs. Over-Identification:
        - Acknowledge pain without exaggerating
        - Observe feelings without being consumed
        - Balance - don't suppress or ruminate
        
        Self-compassion break (use during difficulty):
        1. Mindfulness: "This is a moment of suffering" or "This is hard"
        2. Common humanity: "Suffering is part of life" or "I'm not alone"
        3. Self-kindness: "May I be kind to myself" or place hand on heart
        
        Practices:
        - Supportive touch (hand on heart, hug yourself)
        - Self-compassion letter (write to yourself as a friend would)
        - Change critical self-talk to supportive
        - Acknowledge your efforts, not just outcomes
        - Treat mistakes as learning opportunities
        
        Benefits:
        - Reduced anxiety and depression
        - Increased resilience
        - Better motivation
        - Improved relationships
        - Greater life satisfaction
        
        Research shows self-compassion is more beneficial than self-esteem.
        """
    },
    {
        "id": "crisis_tools_001",
        "title": "Crisis Coping Tools",
        "category": "coping",
        "content": """
        Tools for acute distress or crisis moments:
        
        TIPP Skills (DBT - for intense emotions):
        
        T - Temperature: Change body temperature
        - Splash cold water on face
        - Hold ice cubes
        - Take cold shower
        - Step outside in cold air
        
        I - Intense Exercise: Get heart rate up
        - Run in place
        - Jumping jacks
        - Dance vigorously
        - Go for run
        
        P - Paced Breathing: Slow your breathing
        - Breathe in for 4, out for 6
        - Focus on exhalations
        - Continue for several minutes
        
        P - Paired Muscle Relaxation: Tense and release
        - Tense muscles while inhaling
        - Release while exhaling
        - Notice the relaxation
        
        STOP Skill:
        S - Stop: Freeze, don't react
        T - Take a step back: Get perspective
        O - Observe: Notice what's happening
        P - Proceed mindfully: Choose effective action
        
        Crisis survival kit:
        Physical items:
        - Ice pack
        - Stress ball
        - Comfort object
        - Soothing scents
        - Photos of loved ones
        
        List of:
        - Reasons to live
        - People to contact
        - Coping strategies that work
        - Emergency numbers
        - Grounding techniques
        
        When to seek immediate help:
        - Thoughts of self-harm or suicide
        - Feeling unable to cope
        - Losing touch with reality
        - Call 988 Suicide & Crisis Lifeline
        """
    },
    {
        "id": "anger_management_001",
        "title": "Anger Management Techniques",
        "category": "coping",
        "content": """
        Healthy anger management prevents destructive expressions of anger:
        
        Recognize warning signs:
        - Physical: Tense muscles, racing heart, clenched fists, hot face
        - Mental: Racing thoughts, difficulty concentrating
        - Emotional: Frustration building, feeling disrespected
        
        In the moment:
        1. Take a timeout: Leave situation if possible
        2. Use deep breathing: 4-7-8 technique
        3. Count to 10 (or 100 if needed)
        4. Use self-talk: "Stay calm," "I can handle this"
        5. Physical release: Walk, exercise, squeeze stress ball
        
        Express anger constructively:
        - Use "I" statements: "I feel angry when..."
        - Be specific about behavior, not person
        - Stay focused on current issue
        - Listen to other perspective
        - Look for solutions
        - Take breaks if escalating
        
        Long-term strategies:
        - Identify triggers
        - Challenge angry thoughts
        - Practice relaxation daily
        - Improve communication skills
        - Address underlying issues (fear, hurt, frustration)
        - Exercise regularly
        - Get adequate sleep
        
        Cognitive restructuring:
        Instead of: "This is awful, I can't stand it!"
        Try: "This is frustrating, but I can handle it"
        
        When to seek help:
        - Anger is frequent and intense
        - Leading to violence or threats
        - Damaging relationships
        - Causing legal problems
        - Feeling out of control
        
        Anger is a valid emotion - it's about expressing it healthily.
        """
    },
    {
        "id": "assertiveness_001",
        "title": "Assertiveness Skills",
        "category": "coping",
        "content": """
        Assertiveness means expressing needs and boundaries respectfully:
        
        Communication styles:
        
        Passive: Avoid conflict, people-please, ignore own needs
        - "Whatever you want is fine"
        
        Aggressive: Demanding, hostile, violates others' rights
        - "Do it my way or else!"
        
        Passive-Aggressive: Indirect hostility, sarcasm
        - Says yes but acts resentful
        
        Assertive: Clear, respectful, honors both parties
        - "I understand your view, and I need..."
        
        Assertive techniques:
        
        1. DEAR MAN (DBT):
        D - Describe situation objectively
        E - Express feelings using "I" statements
        A - Assert needs clearly
        R - Reinforce benefits of compliance
        M - Mindful (stay focused)
        A - Appear confident
        N - Negotiate if needed
        
        2. Broken Record:
        - Calmly repeat your position
        - Don't get sidetracked
        - Stay consistent
        
        3. Fogging:
        - Agree with possible truth
        - Don't argue or defend
        - "You might be right"
        
        Practice scenarios:
        - Saying no to requests
        - Asking for what you need
        - Expressing disagreement
        - Setting boundaries
        - Giving and receiving feedback
        
        Body language:
        - Maintain eye contact
        - Stand/sit upright
        - Speak clearly and calmly
        - Use neutral facial expression
        - Respect personal space
        
        Remember: You have the right to assert yourself, and so do others.
        """
    },

    # ========== MINDFULNESS (5 articles) ==========
    {
        "id": "mindfulness_001",
        "title": "Introduction to Mindfulness",
        "category": "mindfulness",
        "content": """
        Mindfulness is purposely focusing attention on the present moment without judgment.
        
        Core elements:
        - Present-moment awareness
        - Non-judgmental observation
        - Acceptance of what is
        - Beginner's mind (curiosity)
        - Letting go
        
        Benefits (research-backed):
        - Reduced stress and anxiety
        - Improved focus and concentration
        - Better emotional regulation
        - Decreased rumination
        - Enhanced self-awareness
        - Improved relationships
        - Better sleep
        - Reduced chronic pain
        - Lower blood pressure
        
        Basic practices:
        
        1. Mindful Breathing:
        - Focus on breath
        - Notice inhale and exhale
        - When mind wanders, gently return
        - 5-10 minutes daily
        
        2. Body Scan:
        - Systematically focus on body parts
        - Notice sensations without judgment
        - 15-30 minutes
        
        3. Mindful Observation:
        - Choose an object
        - Focus all attention on it
        - Notice details, colors, textures
        - 5 minutes
        
        4. Mindful Listening:
        - Focus completely on sounds
        - Notice different layers
        - Don't judge or analyze
        - 5-10 minutes
        
        Start with 5 minutes daily and gradually increase. Consistency matters more than duration.
        """
    },
    {
        "id": "mindfulness_002",
        "title": "Mindful Eating",
        "category": "mindfulness",
        "content": """
        Mindful eating transforms relationship with food:
        
        How to practice:
        1. Eliminate distractions (no TV, phone, reading)
        2. Start with small portions
        3. Before eating:
           - Notice colors, shapes, smells
           - Express gratitude for food
           - Notice hunger level (1-10)
        4. While eating:
           - Take small bites
           - Chew slowly (20-30 times)
           - Notice textures and flavors
           - Put utensil down between bites
           - Pause mid-meal
        5. After eating:
           - Notice fullness level
           - Reflect on experience
           - Avoid immediate judgment
        
        Raisin meditation (classic exercise):
        1. Hold raisin, observe it closely
        2. Notice texture, color, smell
        3. Place on tongue, don't chew yet
        4. Notice sensations
        5. Chew slowly, notice flavors
        6. Notice impulse to swallow
        7. Swallow mindfully
        8. Reflect on experience
        
        Benefits:
        - Better digestion
        - Natural portion control
        - Reduced emotional eating
        - Greater food enjoyment
        - Improved relationship with food
        - Awareness of hunger/fullness cues
        
        Start with one mindful meal or snack per day.
        """
    },
    {
        "id": "mindfulness_003",
        "title": "Body Scan Meditation",
        "category": "mindfulness",
        "content": """
        Body scan promotes relaxation and body awareness:
        
        Full body scan (20-30 minutes):
        1. Lie down comfortably on back
        2. Close eyes, take deep breaths
        3. Start at toes of left foot
        4. Notice sensations (warmth, tingling, tension, numbness)
        5. Breathe into area, release on exhale
        6. Move attention up gradually:
           - Toes → foot → ankle → calf → knee → thigh
           - Repeat with right leg
           - Pelvis → lower back → abdomen → chest
           - Fingers → hands → arms → shoulders
           - Neck → jaw → face → scalp
        7. Notice whole body
        8. Take few deep breaths
        9. Slowly return awareness to room
        
        Short body scan (5-10 minutes):
        - Feet
        - Legs
        - Torso
        - Arms
        - Head/neck
        
        Tips:
        - Don't try to relax or change anything
        - Simply notice what's there
        - If mind wanders, gently return to body
        - No right or wrong way to feel
        - Can do sitting or lying down
        
        When to practice:
        - Before sleep (helps insomnia)
        - During anxiety (grounds you)
        - For pain management
        - To increase body awareness
        
        Great for: Sleep issues, chronic pain, anxiety, disconnection from body
        """
    },
    {
        "id": "mindfulness_004",
        "title": "Walking Meditation",
        "category": "mindfulness",
        "content": """
        Walking meditation combines mindfulness with gentle movement:
        
        How to practice:
        1. Find quiet path or space (10-30 feet)
        2. Stand still, feel feet on ground
        3. Begin walking very slowly
        4. Notice each component:
           - Lifting foot
           - Moving foot forward
           - Placing foot down
           - Shifting weight
        5. Feel sensations in feet and legs
        6. Notice body movement
        7. When mind wanders, return to sensations of walking
        8. Practice 10-20 minutes
        
        Variations:
        
        Fast-paced walking:
        - Walk at normal pace
        - Notice whole body movement
        - Feel rhythm of steps
        - Sync with breathing
        
        Nature walking:
        - Walk in nature mindfully
        - Notice surroundings
        - Engage all senses
        - Feel connection to environment
        
        Urban walking:
        - Practice in city
        - Notice sounds, sights
        - Stay present despite distractions
        - Use as daily practice (commute)
        
        Benefits:
        - Combines meditation with exercise
        - Good for restless minds
        - Can be done anywhere
        - Grounds in physical sensations
        - Breaks up sitting meditation
        - Accessible for beginners
        
        Great for: People who struggle sitting still, anxiety, need for movement
        """
    },
    {
        "id": "mindfulness_005",
        "title": "RAIN Technique for Emotions",
        "category": "mindfulness",
        "content": """
        RAIN is a mindfulness tool for working with difficult emotions:
        
        R - Recognize what's happening:
        - Pause and acknowledge the emotion
        - Name it: "This is anger," "This is fear," "This is sadness"
        - Notice where you feel it in body
        
        A - Allow the experience to be there:
        - Don't try to fix, change, or push it away
        - Let it be present
        - Say: "It's okay to feel this"
        - Resist urge to distract or avoid
        
        I - Investigate with kindness:
        - Get curious about the experience
        - Where do you feel it in your body?
        - What thoughts accompany it?
        - What does it need?
        - Investigate with compassion, not analysis
        
        N - Non-identification (or Nurture):
        - Realize you are not your emotion
        - It's a passing experience
        - You are the awareness observing it
        - Offer yourself compassion
        
        Example:
        Feeling anxious before presentation:
        R: "I'm feeling anxiety right now"
        A: "It's okay to feel anxious. I don't need to fight it"
        I: "I feel tightness in chest, racing thoughts about failing. I need reassurance"
        N: "I am not this anxiety. It will pass. May I be kind to myself"
        
        Benefits:
        - Creates space from emotions
        - Reduces reactivity
        - Builds emotional intelligence
        - Develops self-compassion
        - Prevents emotional overwhelm
        
        Use RAIN when: Feeling overwhelmed, stuck in emotion, reactive, or need self-compassion
        """
    },

    # ========== SELF-CARE (5 articles) ==========
    {
        "id": "selfcare_001",
        "title": "Comprehensive Self-Care Guide",
        "category": "self-care",
        "content": """
        Self-care is deliberate action to maintain mental, emotional, and physical health:
        
        Physical self-care:
        - Regular exercise (150 min/week)
        - Balanced, nutritious diet
        - Adequate sleep (7-9 hours)
        - Regular medical check-ups
        - Taking medications as prescribed
        - Limiting alcohol
        - Avoiding harmful substances
        
        Emotional self-care:
        - Journaling
        - Therapy or counseling
        - Saying no to protect energy
        - Processing emotions (not suppressing)
        - Allowing yourself to cry
        - Creative expression
        - Practicing self-compassion
        
        Mental self-care:
        - Reading for pleasure
        - Learning new skills
        - Limiting news/social media
        - Engaging in hobbies
        - Puzzles or brain games
        - Time for reflection
        - Creative pursuits
        
        Social self-care:
        - Quality time with loved ones
        - Setting healthy boundaries
        - Joining groups with shared interests
        - Asking for help when needed
        - Limiting toxic relationships
        - Cultivating supportive friendships
        
        Spiritual self-care:
        - Meditation or prayer
        - Time in nature
        - Practicing gratitude
        - Engaging in meaningful activities
        - Connecting with values
        - Contemplation
        
        Remember: Self-care isn't selfish - it's necessary for wellbeing.
        """
    },
    {
        "id": "sleep_001",
        "title": "Sleep Hygiene for Mental Health",
        "category": "self-care",
        "content": """
        Quality sleep is foundational for mental health:
        
        Sleep hygiene basics:
        
        1. Consistent schedule:
        - Same bedtime and wake time daily (even weekends)
        - Allow 7-9 hours for sleep
        - Avoid sleeping in to "catch up"
        
        2. Bedroom environment:
        - Cool (60-67°F ideal)
        - Dark (blackout curtains or eye mask)
        - Quiet (earplugs or white noise)
        - Comfortable mattress and pillows
        - Reserve bed for sleep and intimacy only
        
        3. Pre-bed routine:
        - Start winding down 1 hour before bed
        - Dim lights
        - Avoid screens (blue light suppresses melatonin)
        - Relaxing activities (reading, bath, stretching)
        - Light snack if hungry (avoid heavy meals)
        
        4. Daytime habits:
        - Exercise regularly (but not 3 hours before bed)
        - Get natural sunlight exposure
        - Limit naps (20 min max, before 3 PM)
        - No caffeine after 2 PM
        - Limit alcohol (disrupts sleep quality)
        
        If can't sleep:
        - Don't lie awake more than 20 minutes
        - Get up, do quiet activity in dim light
        - Return to bed when sleepy
        - Avoid clock-watching
        
        When to seek help:
        - Insomnia lasting >3 weeks
        - Excessive daytime sleepiness
        - Snoring or breathing pauses
        - Difficulty staying awake
        
        Poor sleep worsens depression and anxiety - prioritize it!
        """
    },
    {
        "id": "nutrition_001",
        "title": "Nutrition and Mental Health",
        "category": "self-care",
        "content": """
        Diet significantly impacts mood, energy, and mental health:
        
        Foods that support mental health:
        
        Omega-3 fatty acids (brain health):
        - Fatty fish (salmon, mackerel, sardines)
        - Walnuts, flaxseed, chia seeds
        - Aim: 2-3 servings fish per week
        
        Complex carbohydrates (stable blood sugar):
        - Whole grains (oats, quinoa, brown rice)
        - Vegetables (especially leafy greens)
        - Legumes (beans, lentils)
        
        Lean proteins (neurotransmitter production):
        - Chicken, turkey, fish
        - Eggs
        - Tofu, tempeh
        - Greek yogurt
        
        B vitamins (energy and mood):
        - Leafy greens, avocados
        - Eggs, poultry
        - Fortified cereals
        
        Probiotics (gut-brain connection):
        - Yogurt, kefir
        - Sauerkraut, kimchi
        - Kombucha
        
        Antioxidants (reduce inflammation):
        - Berries, dark chocolate
        - Colorful vegetables
        - Green tea
        
        Foods to limit:
        - Excessive caffeine (anxiety, sleep issues)
        - Alcohol (depression, sleep disruption)
        - Processed foods (blood sugar spikes)
        - High sugar (mood swings)
        - Trans fats (inflammation)
        
        Eating patterns:
        - Regular meals (don't skip breakfast)
        - Balanced macros (protein, carbs, fat)
        - Stay hydrated (8 glasses water)
        - Limit restrictive dieting
        
        Gut-brain axis: Gut health impacts mental health - prioritize fiber and probiotics
        """
    },
    {
        "id": "exercise_001",
        "title": "Exercise for Mental Health",
        "category": "self-care",
        "content": """
        Exercise is one of the most effective interventions for mental health:
        
        Mental health benefits:
        - Reduces anxiety (immediate and long-term)
        - Alleviates depression (as effective as medication for mild-moderate)
        - Improves self-esteem
        - Better sleep quality
        - Increased energy
        - Enhanced cognitive function
        - Reduced stress
        - Natural mood elevator (endorphins)
        
        Recommendations:
        - 150 minutes moderate aerobic activity per week
        - Or 75 minutes vigorous activity
        - Strength training 2x per week
        - Any amount is better than none
        
        Types of exercise:
        
        Aerobic (mood and anxiety):
        - Walking, jogging, running
        - Swimming, cycling
        - Dancing, aerobics
        - Sports
        
        Strength training (self-esteem, confidence):
        - Weight lifting
        - Resistance bands
        - Bodyweight exercises
        - Rock climbing
        
        Mind-body (stress and mindfulness):
        - Yoga
        - Tai chi
        - Pilates
        - Qigong
        
        Starting small:
        - 10-minute walks
        - Stretch breaks
        - Desk exercises
        - Gardening
        - Playing with pets/kids
        - Taking stairs
        
        Making it sustainable:
        - Choose activities you enjoy
        - Exercise with others
        - Set realistic goals
        - Track progress
        - Mix it up
        - Schedule it
        - Start gradually
        
        Best exercise = the one you'll actually do consistently!
        """
    },
    {
        "id": "boundaries_001",
        "title": "Setting Healthy Boundaries",
        "category": "self-care",
        "content": """
        Boundaries are guidelines for how you want to be treated:
        
        Types of boundaries:
        
        Physical:
        - Personal space needs
        - Touch preferences
        - Privacy needs
        - Physical safety
        
        Emotional:
        - What you'll share and with whom
        - Emotional labor limits
        - Not taking on others' emotions
        
        Time:
        - How you spend your time
        - Work-life balance
        - Availability to others
        - Time for self-care
        
        Material:
        - Money (lending, borrowing)
        - Possessions
        - Resources
        
        Mental:
        - Your thoughts and values
        - Right to your opinions
        - Mental energy limits
        
        How to set boundaries:
        1. Identify your limits (what feels okay vs. not okay)
        2. Be clear and direct: "I'm not available after 8 PM"
        3. Start small (practice with lower-stakes situations)
        4. Be consistent (don't cave to pressure)
        5. Don't apologize excessively for your boundaries
        6. Be prepared for pushback (especially if you've had weak boundaries)
        7. Seek support if needed
        
        Common boundary statements:
        - "I'm not comfortable with that"
        - "I need time to think about it"
        - "No, I can't do that"
        - "I need some space right now"
        - "That doesn't work for me"
        - "I'm not discussing that topic"
        
        Signs you need better boundaries:
        - Resentment toward others
        - Feeling taken advantage of
        - Difficulty saying no
        - Putting others' needs before your own constantly
        - Feeling drained by relationships
        
        Remember: Healthy boundaries improve all relationships, including with yourself.
        """
    },

    # ========== STRESS & CRISIS (5 articles) ==========
    {
        "id": "stress_001",
        "title": "Understanding and Managing Stress",
        "category": "stress",
        "content": """
        Stress is the body's response to challenges or demands:
        
        Types of stress:
        
        Acute stress: Short-term, immediate response
        - Meeting deadlines
        - Arguments
        - Near-miss accidents
        - Usually resolves quickly
        
        Chronic stress: Long-term, ongoing
        - Relationship problems
        - Financial difficulties
        - Work stress
        - Health problems
        - Can lead to serious health issues
        
        Eustress: Positive stress
        - New job
        - Getting married
        - Moving to new place
        - Still requires adaptation
        
        Physical symptoms:
        - Headaches, muscle tension
        - Fatigue, sleep problems
        - Digestive issues
        - Weakened immune system
        - High blood pressure
        - Chest pain, rapid heartbeat
        
        Emotional symptoms:
        - Anxiety, irritability
        - Depression, mood swings
        - Feeling overwhelmed
        - Difficulty concentrating
        
        Quick stress relievers:
        - Deep breathing (4-7-8)
        - Take a walk
        - Call supportive friend
        - Listen to calming music
        - Progressive muscle relaxation
        - Visualization
        
        Long-term management:
        - Regular exercise
        - Healthy diet
        - Adequate sleep
        - Time management
        - Setting boundaries
        - Social support
        - Relaxation practices
        - Addressing problems directly
        - Professional help when needed
        
        Chronic stress requires intervention - don't ignore it.
        """
    },
    {
        "id": "burnout_001",
        "title": "Recognizing and Recovering from Burnout",
        "category": "stress",
        "content": """
        Burnout is physical, emotional, and mental exhaustion from prolonged stress:
        
        Three dimensions (Maslach):
        
        1. Exhaustion:
        - Chronic fatigue
        - Physical depletion
        - Difficulty getting out of bed
        - Frequent illness
        
        2. Cynicism/Detachment:
        - Negative feelings about work/responsibilities
        - Emotional numbness
        - Loss of enjoyment
        - Withdrawal from others
        
        3. Inefficacy:
        - Reduced performance
        - Difficulty concentrating
        - Mistakes increase
        - Feelings of incompetence
        
        Additional signs:
        - Irritability, mood swings
        - Loss of motivation
        - Decreased satisfaction
        - Physical symptoms (headaches, stomach issues)
        - Using food/alcohol to cope
        - Procrastination
        
        Recovery strategies:
        
        Immediate:
        - Take time off if possible
        - Reduce commitments
        - Ask for help
        - Set strict boundaries
        - Rest and recovery
        
        Long-term:
        - Re-evaluate priorities
        - Set sustainable limits
        - Build recovery time into schedule
        - Practice stress management
        - Address underlying issues
        - Consider job change if needed
        - Regular self-care
        - Therapy
        
        Prevention:
        - Regular breaks
        - Clear work-life boundaries
        - Delegate when possible
        - Say no to additional demands
        - Maintain interests outside work
        - Social connection
        - Purpose and meaning
        
        Recovery takes time - be patient with yourself. Burnout is a sign to make changes.
        """
    },
    {
        "id": "trauma_001",
        "title": "Understanding Trauma and PTSD",
        "category": "trauma",
        "content": """
        Trauma is response to deeply distressing or disturbing events:
        
        Types of trauma:
        - Acute: Single incident (accident, assault)
        - Chronic: Repeated/prolonged (abuse, war)
        - Complex: Multiple traumatic events
        - Developmental: Childhood trauma
        
        Common trauma responses:
        
        Fight: Anger, irritability, controlling
        Flight: Anxiety, panic, restlessness
        Freeze: Numbness, dissociation, stuck
        Fawn: People-pleasing, difficulty saying no
        
        PTSD symptoms (DSM-5 criteria):
        
        Intrusion:
        - Flashbacks
        - Nightmares
        - Intrusive thoughts
        - Physical reactions to reminders
        
        Avoidance:
        - Avoiding trauma reminders
        - Avoiding thoughts/feelings
        - Emotional numbness
        
        Negative changes:
        - Negative beliefs about self/world
        - Blame, guilt, shame
        - Loss of interest
        - Detachment from others
        
        Arousal changes:
        - Hypervigilance
        - Exaggerated startle
        - Irritability
        - Sleep problems
        - Concentration difficulties
        - Reckless behavior
        
        Treatment options:
        - Trauma-focused CBT
        - EMDR (Eye Movement Desensitization)
        - Prolonged Exposure therapy
        - CPT (Cognitive Processing Therapy)
        - Medication (SSRIs)
        - Support groups
        
        Self-help:
        - Grounding techniques
        - Self-compassion
        - Safe environment
        - Gradual exposure
        - Self-care
        - Social support
        
        Healing is possible with proper support and treatment.
        """
    },
    {
        "id": "crisis_001",
        "title": "Mental Health Crisis: When to Seek Help",
        "category": "crisis",
        "content": """
        A mental health crisis requires immediate attention:
        
        Warning signs - seek help if experiencing:
        
        Immediate danger:
        - Suicidal thoughts with plan/intent
        - Self-harm urges or actions
        - Thoughts of harming others
        - Severe psychosis (hallucinations, delusions)
        - Severe disorientation
        - Unable to care for basic needs
        
        Urgent concerns:
        - Overwhelming anxiety or panic
        - Severe depression preventing function
        - Rapid mood changes
        - Extreme agitation
        - Alcohol/drug withdrawal
        - Trauma response
        
        Where to get help:
        
        Emergency (immediate danger):
        - 911
        - Emergency room
        - Crisis mobile team
        - Police (ask for CIT officer)
        
        Crisis lines (24/7):
        - 988 Suicide & Crisis Lifeline (call or text)
        - Crisis Text Line (text HOME to 741741)
        - Veterans Crisis Line (988 then press 1)
        - SAMHSA National Helpline (1-800-662-4357)
        
        Non-emergency:
        - Contact therapist
        - Call psychiatrist
        - Walk-in crisis clinic
        - Urgent care mental health
        
        Supporting someone in crisis:
        - Stay calm
        - Listen without judgment
        - Don't leave them alone
        - Remove access to means of harm
        - Call for help
        - Don't promise confidentiality if safety risk
        - Take all threats seriously
        
        After crisis:
        - Follow-up care crucial
        - Safety plan
        - Remove means
        - Increase support
        - Consider hospitalization if needed
        
        Crisis is temporary - help is available. Always err on side of caution.
        """
    },
    {
        "id": "safety_planning_001",
        "title": "Creating a Safety Plan",
        "category": "crisis",
        "content": """
        A safety plan helps manage suicidal thoughts and self-harm urges:
        
        Step 1: Warning signs
        - Thoughts, images, moods that precede crisis
        - Behavioral signs
        Examples: "Thinking 'I can't go on'", "Isolating", "Increased substance use"
        
        Step 2: Internal coping strategies
        - Things you can do without contacting anyone
        Examples:
        - Deep breathing
        - Going for walk
        - Listening to music
        - Journaling
        - Taking shower
        
        Step 3: Social contacts and settings
        - People/places for distraction
        Examples:
        - Coffee with friend
        - Visit family member
        - Go to public place (library, mall)
        - Attend group/meeting
        
        Step 4: People to ask for help
        List with phone numbers:
        - Supportive friends/family
        - Therapist
        - Sponsor/mentor
        - Clergy
        
        Step 5: Professionals to contact
        - Therapist: [name, number]
        - Psychiatrist: [name, number]
        - Local crisis line: [number]
        - Hospital emergency: [address]
        
        Step 6: Make environment safe
        - Remove or secure:
        - Medications (lock up, give to trusted person)
        - Weapons
        - Alcohol/drugs
        - Sharp objects
        - Other means
        
        Additional elements:
        - Reasons for living
        - Things worth living for
        - Coping strategies that work
        - Self-soothing activities
        
        Crisis numbers:
        - 988 Suicide & Crisis Lifeline
        - Crisis Text Line: HOME to 741741
        - Emergency: 911
        
        Keep safety plan:
        - In phone
        - Written copy accessible
        - Share with therapist/trusted person
        - Review and update regularly
        
        Having a plan reduces risk - create one when stable.
        """
    },

    # ========== RELATIONSHIPS (5 articles) ==========
    {
        "id": "communication_001",
        "title": "Effective Communication in Relationships",
        "category": "relationships",
        "content": """
        Good communication is foundation of healthy relationships:
        
        Active listening:
        - Give full, undivided attention
        - Make eye contact
        - Don't interrupt
        - Avoid planning your response while they talk
        - Use body language (nod, lean in)
        - Reflect back: "So you're saying..."
        - Ask clarifying questions
        - Validate feelings: "That makes sense"
        
        "I" statements (vs. "You" statements):
        
        Instead of: "You never listen to me!"
        Try: "I feel unheard when I'm interrupted"
        
        Formula: "I feel [emotion] when [behavior] because [reason]"
        
        Examples:
        - "I feel hurt when plans change last minute because I value our time together"
        - "I feel anxious when I don't hear from you because I worry"
        
        Communication tips:
        - Choose right time/place (not during conflict)
        - Stay calm (take breaks if escalating)
        - Be specific, not general
        - Focus on present, not past
        - One issue at a time
        - Listen to understand, not to win
        - Look for compromise
        - Express appreciation
        
        Non-verbal communication:
        - Tone of voice
        - Body language
        - Facial expressions
        - Eye contact
        - Personal space
        (Often matters more than words)
        
        Avoid:
        - Criticism ("You always/never...")
        - Contempt (sarcasm, name-calling)
        - Defensiveness
        - Stonewalling (shutting down)
        - Mind-reading ("You think...")
        - Kitchen-sinking (bringing up everything)
        
        Practice: Start with small, low-stakes conversations to build skills.
        """
    },
    {
        "id": "social_support_001",
        "title": "Building Social Support Networks",
        "category": "relationships",
        "content": """
        Strong social connections are vital for mental health and longevity:
        
        Benefits:
        - Reduced stress, anxiety, depression
        - Increased sense of belonging
        - Improved self-esteem
        - Better coping with trauma
        - Longer lifespan
        - Better immune function
        
        Types of support:
        
        Emotional: Empathy, love, trust
        - Someone who listens
        - Provides comfort
        - Shows they care
        
        Instrumental: Tangible help
        - Practical assistance
        - Resources
        - Financial help
        
        Informational: Advice, guidance
        - Sharing knowledge
        - Offering suggestions
        - Providing information
        
        Companionship: Belonging
        - Shared activities
        - Sense of community
        - Fun and relaxation
        
        Building connections:
        - Join clubs/groups (interests, hobbies)
        - Volunteer
        - Take classes
        - Attend community events
        - Reconnect with old friends
        - Be a good friend to others
        - Use online communities mindfully
        - Regular contact (quality > quantity)
        - Accept invitations
        - Invite others
        
        Maintaining relationships:
        - Regular check-ins
        - Be present and engaged
        - Show appreciation
        - Offer support
        - Be reliable
        - Share vulnerably
        - Resolve conflicts
        - Reciprocity
        
        Quality over quantity:
        - A few close relationships > many superficial
        - Deep connections matter most
        - Invest in relationships that energize you
        
        If building connections feels difficult, therapy can help with social skills.
        """
    },
    {
        "id": "loneliness_001",
        "title": "Coping with Loneliness",
        "category": "relationships",
        "content": """
        Loneliness is subjective feeling of isolation or lack of meaningful connection:
        
        Loneliness vs. Being Alone:
        - Can feel lonely in a crowd
        - Can feel content while alone
        - Loneliness is about quality, not quantity
        
        Types of loneliness:
        
        Emotional: Lack of close attachments
        - Missing intimate relationships
        - Absence of confidant
        
        Social: Lack of social network
        - Missing sense of community
        - No broader social connections
        
        Existential: Fundamental separation
        - Feeling disconnected from others
        - Sense of not being understood
        
        Health impacts:
        - Increased depression and anxiety
        - Higher stress levels
        - Sleep problems
        - Weakened immune system
        - Increased mortality risk
        - Comparable to smoking 15 cigarettes/day
        
        Coping strategies:
        
        Reconnect:
        - Reach out to someone you trust
        - Join support groups (in-person or online)
        - Volunteer (helps you and others)
        - Take classes
        - Join hobby groups
        
        Quality over quantity:
        - Focus on meaningful connections
        - Deepen existing relationships
        - Be vulnerable and authentic
        - Share your feelings
        
        Self-connection:
        - Practice self-compassion
        - Engage in meaningful activities
        - Pursue interests and passions
        - Journaling
        - Mindfulness
        
        Reframe:
        - Being alone can be peaceful
        - Opportunity for self-discovery
        - Time for personal growth
        
        Limit:
        - Social media (can increase loneliness)
        - Passive consumption
        - Comparisons to others
        
        Consider:
        - Therapy
        - Pet adoption (if appropriate)
        - Moving to more social environment
        
        Remember: Many people feel lonely - you're not alone in feeling alone.
        """
    },
    {
        "id": "conflict_resolution_001",
        "title": "Healthy Conflict Resolution",
        "category": "relationships",
        "content": """
        Conflict is normal - it's how you handle it that determines relationship health:
        
        Healthy vs. Unhealthy conflict:
        
        Healthy:
        - Respectful communication
        - Focus on issue, not person
        - Both feel heard
        - Compromise sought
        - Leads to resolution or understanding
        
        Unhealthy:
        - Personal attacks
        - Yelling, threats
        - Stonewalling
        - Bringing up past issues
        - Winner/loser mentality
        
        Steps for resolution:
        
        1. Cool down first
        - Don't engage when highly emotional
        - Take 20+ minute break
        - Self-soothe
        - Return when calm
        
        2. Choose right time/place
        - Private setting
        - When both available
        - Not late at night
        - Not in public
        
        3. Use "I" statements
        - "I feel hurt when..."
        - Not "You always..."
        
        4. Listen actively
        - Truly hear their perspective
        - Don't just wait to talk
        - Reflect back understanding
        - Validate feelings (even if disagree)
        
        5. Stay focused
        - One issue at a time
        - Current situation only
        - No "you always/never"
        - Avoid bringing up past
        
        6. Take responsibility
        - Own your part
        - Apologize if appropriate
        - Don't just defend
        
        7. Look for compromise
        - Both give something
        - Creative solutions
        - Win-win when possible
        
        8. Take breaks if needed
        - If escalating, pause
        - Agree to continue later
        - Don't storm off
        
        Repair attempts:
        - Humor (appropriate)
        - Physical affection
        - Acknowledging your role
        - Showing empathy
        
        After conflict:
        - Follow through on agreements
        - Let it go (don't hold grudges)
        - Appreciate resolution
        - Learn from it
        
        When to seek help:
        - Conflicts always escalate
        - Same issues repeatedly
        - Violence or threats
        - One person shuts down
        - Can't resolve on own
        
        Consider couples/family therapy.
        """
    },
    {
        "id": "toxic_relationships_001",
        "title": "Recognizing Toxic Relationships",
        "category": "relationships",
        "content": """
        Toxic relationships harm your wellbeing and should be addressed:
        
        Signs of toxicity:
        
        Control:
        - Dictates who you see, what you do
        - Monitors phone, social media
        - Makes all decisions
        - Isolates you from others
        
        Manipulation:
        - Guilt-tripping
        - Gaslighting (making you doubt reality)
        - Playing victim
        - Twisting words
        
        Disrespect:
        - Put-downs, insults
        - Public humiliation
        - Dismissing feelings
        - Violating boundaries
        
        Volatility:
        - Unpredictable mood swings
        - Walking on eggshells
        - Explosive anger
        - Silent treatment
        
        One-sidedness:
        - Always their needs first
        - No reciprocity
        - You do all compromising
        - Constant giving, no receiving
        
        Dishonesty:
        - Frequent lying
        - Breaking promises
        - Infidelity
        - Hidden agendas
        
        How you feel:
        - Drained, exhausted
        - Anxious around them
        - Loss of self-esteem
        - Changing yourself to please them
        - Feeling trapped
        - Worse about yourself
        
        What to do:
        
        If salvageable:
        - Set clear boundaries
        - Communicate concerns
        - Couples/family therapy
        - See if they're willing to change
        - Give specific timeline
        
        If not salvageable:
        - Plan safe exit (especially if abuse)
        - Build support system
        - Therapy for yourself
        - Document if needed
        - Gradual distance or clean break
        - Block if necessary
        - Grieve the loss
        
        Red flags on first dates:
        - Love bombing
        - Moving too fast
        - Isolation attempts
        - Crossing boundaries
        - Disrespect to others
        
        Remember: You deserve respect, kindness, and support. Leaving toxic relationships 
        is self-care, not selfishness.
        """
    }
]

def get_all_articles():
    """Return all knowledge base articles"""
    return MENTAL_HEALTH_ARTICLES

def get_articles_by_category(category):
    """Get articles filtered by category"""
    return [article for article in MENTAL_HEALTH_ARTICLES if article["category"] == category]

def get_article_by_id(article_id):
    """Get specific article by ID"""
    for article in MENTAL_HEALTH_ARTICLES:
        if article["id"] == article_id:
            return article
    return None

def get_categories():
    """Get list of all categories"""
    categories = set(article["category"] for article in MENTAL_HEALTH_ARTICLES)
    return sorted(list(categories))

def get_article_count():
    """Return total number of articles"""
    return len(MENTAL_HEALTH_ARTICLES)

def search_articles(query):
    """Simple search through articles"""
    query = query.lower()
    results = []
    for article in MENTAL_HEALTH_ARTICLES:
        if (query in article["title"].lower() or 
            query in article["content"].lower() or 
            query in article["category"].lower()):
            results.append(article)
    return results

def get_category_counts():
    """Get article count per category"""
    from collections import Counter
    categories = [article["category"] for article in MENTAL_HEALTH_ARTICLES]
    return dict(Counter(categories))