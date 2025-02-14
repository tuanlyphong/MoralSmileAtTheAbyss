image worms1 = "bg/worms1.png"
image worms2 = "bg/worms2.png"
image worms3 = "bg/worms3.png"
image paranoid2:
   "worms1" with Fade(0.3, 0, 0, color="#fff")
   "worms2" with Dissolve(0.2)
   "worms3" with Fade(0.5, 0, 0, color="#000")

image YukaSitPose = "YukaSitPose.png"

image OutsideFuHouse = "bg/OutsideFuHouse.png"
image OutsideFuHouse1 = "bg/OutsideFuHouse1.png"
image OutsideFuHouse2 = "bg/OutsideFuHouse2.png"
image OutsideFuHouse3 = "bg/OutsideFuHouse3.png"
image YukaConcernPoseSurprise = "YukaConcernPoseSurprise.png"
image YukaSitPoseBlush = "YukaSitPoseBlush.png"
#decrease is move right,increase is move left
#                 down,                  up
#middle is xpos 0.5 ypos 1.0

image YukaConcernPoseTalking = "YukaConcernPoseTalking.png"
image YukaConcernPoseSadTalking = "YukaConcernPoseSadTalking.png"

#ADVANCE
image Outside:
    "OutsideFuHouse1" with Dissolve(1)
    5
    "OutsideFuHouse2" with Dissolve(1)
    1
### NEGATIVE / SERIOUS EMOTIONS

# Intense emotions like anger or frustration
image YukaGlareA:  # Glare sequence animation
    "YukaGlare1" with Dissolve(0.2)
    pause 0.5
    "YukaGlare2" with Dissolve(0.2)
image YukaGlare1: 
  "YukaGlare" 
  zoom 1.2 ypos 1.4  # Glare
image YukaGlare2: 
  "YukaGlareFrown" 
  zoom 1.2 ypos 1.4  # Glare with frown
image YukaATalk:  # Angry talking sequence
    "YukaAngry1"
    pause 0.4
    "YukaAngry2" with Dissolve(0.2)
    pause 0.5
    "YukaAngry1" with Dissolve(0.2)
image YukaAngry1: 
  "YukaAngry" 
  zoom 1.2 ypos 1.4  # Angry pose
image YukaAngry2: 
  "YukaAngryTalking" 
  zoom 1.2 ypos 1.4  # Angry talking
image approach:  # Angry zoom-in effect
    "YukaAngry"
    ypos 1.2
    linear 1 zoom 1.2 ypos 1.4
image Back3: 
  "YukaAngry" 
  zoom 1.0 ypos 1.2  # Angry retreat
image Back2: 
  "YukaAngryBlush" 
  zoom 2.0 ypos 2.2 
  linear 0.5 zoom 1.0 ypos 1.2  # Angry blush

# Sadness and concern
image YukaConcernPSadZ: 
  "YukaConcernPoseSad" 
  zoom 1.3 xpos 0.7 ypos 1.2 
  linear 1 zoom 1.4 ypos 1.3  # Sad concern zoom
image YukaConcernPSadN: 
  "YukaConcernPoseSad" 
  zoom 1.4 ypos 1.3  # Static sad concern
image YukaConcernPSadT: 
  "YukaConcernPoseSadTalking" 
  zoom 1.4 ypos 1.3  # Sad concern talking
image YukaFTalk:  # Frowning talking sequence
    "YukaFrown1"
    pause 0.4
    "YukaFrown2" with Dissolve(0.2)
    pause 0.5
    "YukaFrown1" with Dissolve(0.2)
image YukaFrown1: 
  "YukaFrown" 
  zoom 1.2 ypos 1.4  # Frown
image YukaFrown2: 
  "YukaFrownTalking" 
  zoom 1.2 ypos 1.4  # Frown while talking

# Surprise / Embarrassment
image YukaSurpriseBl: 
  "YukaSurprise2" 
  zoom 1.2 ypos 1.4  # Surprised Blush
image YukaConcernPSurprise: 
  "YukaConcernPoseSurprise" 
  zoom 1.4 xpos 0.7 ypos 1.3 
  linear 0.5 zoom 1.3 ypos 1.2  # Concern Surprise
image YukaEmba:
    "YukaAngryBlush" with Dissolve(0.2)
    pause 0.6
    "YukaDere" with Dissolve(0.2)
    pause 0.4
    "YukaDereTalking" with Dissolve(0.2)
    pause 0.3
    "YukaDere" with Dissolve(0.2)
image Close2: 
  "YukaEmba" 
  zoom 2.0 ypos 2.2  # Embarrassed Close-up
image Back1: 
  "OutsideFuHouse" 
  zoom 1.5 ypos 1.5 
  linear 0.5 zoom 1.0 ypos 1.0  # Retreat animation

### NEUTRAL / MIXED EMOTIONS

# Concerned / Thoughtful
image YukaConcernP: 
  "YukaConcernPose" 
  zoom 1.3 xpos 0.7 ypos 1.2  # Concern
image YukaConcernPT: 
  "YukaConcernPoseTalking" 
  zoom 1.3 xpos 0.7 ypos 1.2  # Concern Talking

# Neutral expressions
image YukaNorm: 
  "Yuka" 
  zoom 1.2 ypos 1.4  # Neutral
image YukaLaughN:
  "YukaLaugh"
  zoom 1.2 ypos 1.4  # Neutral

image YukaNormA:  # Neutral with subtle movement
    "YukaNorm" with Dissolve(0.2)
    pause 0.4
    "YukaNormClose" with Dissolve(0.2)
    pause 0.4
    "YukaNorm" with Dissolve(0.2)
image YukaNormClose: 
  "YukaEyesClose" 
  zoom 1.2 ypos 1.4  # Neutral with eyes closed
image YukaEyesCloseS:
  "YukaEyesCloseSmile"
  zoom 1.2 ypos 1.4
### POSITIVE EMOTIONS

# Playful / Teasing
image YukaMock2:
    "FunnySmile" with Dissolve(0.2)
    pause 0.4
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.4
image YukaMock:
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.4
    "FunnySmile" with Dissolve(0.2)
    pause 0.4
image YukaMock3:
    "YukaLaughN" with Dissolve(0.2)
    pause 1.0
    "FunnySmile" with Dissolve(0.2)
    pause 0.4

image YukaMock:
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.4
    "FunnySmile" with Dissolve(0.2)
    pause 0.4
image YukaThugLife:  # Cocky playful sequence
    "YukaCSmile" with Dissolve(0.2)
    pause 0.3
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.4
    "YukaCSEC" with Dissolve(0.2)
image YukaDumb:  # Dumbfounded comedic sequence
    "FunnySmile" with Dissolve(0.2)
    pause 0.5
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.6
    "Smug" with Dissolve(0.2)
image YukaCSEC: 
  "YukaEyesClosedCatSmile" 
  zoom 1.2 ypos 1.4  # Playful cat smile
image YukaCSmile: 
  "YukaWinkCatSmile" 
  zoom 1.2 ypos 1.4  # Wink cat smile
image YukaWinkN:
  "YukaWink"
  zoom 1.2 ypos 1.4
# Affection / Romantic / Dere
image YukaDTalk:  # Dere Talking Animation
    "YukaDere1"
    pause 0.3
    "YukaDere2" with Dissolve(0.2)
    pause 0.6
    "YukaDere1" with Dissolve(0.2)
image YukaDere1: 
  "YukaDere" 
  zoom 1.2 ypos 1.4  # Dere pose
image YukaDere2: 
  "YukaDereTalking" 
  zoom 1.2 ypos 1.4  # Dere Talking

# Happiness / Joy
image FunnySmile: 
  "YukaEyesClosedGrin" 
  zoom 1.2 ypos 1.4  # Laughing
image FunnyLaugh: 
  "YukaEyesClosedLaugh" 
  zoom 1.2 ypos 1.4  # Laughing hard
image Smug: 
  "YukaAngrySmile" 
  zoom 1.2 ypos 1.4  # Smug smile
image YukaNSmile: 
  "YukaSmile" 
  zoom 1.2 ypos 1.4  # Natural smile
image YukaNormSmile:  # Natural to Smile
    "YukaNorm" with Dissolve(0.2)
    pause 0.4
    "YukaNSmile" with Dissolve(0.2)
    pause 0.5
image YukaWake:
    "OutsideFuHouse3"
    zoom 3 xpos 0.22 ypos 2.8
image YukaSleep:
    "Outside"     
    zoom 3 xpos 0.3 ypos 1.0
    linear 6 xpos 0.22 ypos 2.8
image Close1:
    "OutsideFuHouse"
    zoom 1.5 ypos 1.5
image Out:
    "OutsideFuHouse"
    zoom 1.0 ypos 1.0
label outside:
    window hide
    $ quick_menu = False
    play sound "open.ogg"

    hide door_effect with Fade(0.5, 0, 0, color="#fff") 
    show YukaSleep with Dissolve(1)

    $ renpy.pause(4, hard=True)  # Reduced from 6 seconds for better pacing
    window show
    $ quick_menu = True
    play music "morning.ogg"
     
    f "..."
    f "Good morning?"

    y "Mmm..."
    y "Mornin-"

    window hide
    $ quick_menu = False
    stop music  # Now correctly stops before transitioning to 'fight'

    show YukaWake with Dissolve(1)
    $ renpy.pause(1, hard=True)  # Ensures transition effect is noticeable

    jump fight  # Redirects to the fight scene

label fight:

    hide YukaWake
    hide YukaSleep

    # Show Yuka close-up
    show Close1 with Dissolve(1)
    play sound "Boom.ogg"

    show Close2 with vpunch

    $ renpy.pause(0.5, hard=True)
    $ quick_menu = True

    y "How DARE you!"
    stop sound
    play music "fun.ogg"
    hide Close1 
    hide Close2

    # Fu backs off
    show Back1
    show Back2
    e "Whoa!"

    show Back3 with Dissolve(0.5)
    window hide
    $ quick_menu = False

    hide Back2
    hide Back1
    show Out
    hide Back3
    play sound "slowappoarch.ogg"
    show approach
    $renpy.pause(1)
    stop sound
    $ renpy.pause(1, hard=True)
    $ quick_menu = True

    f "Urgh..."

    show YukaDere1 with Dissolve(0.5)
    hide approach

    show YukaDTalk
    y "Mou!"

    show YukaAngry1 with Dissolve(0.2)
    hide YukaDTalk
    hide YukaDere1

    show YukaATalk
    hide YukaAngry1
    y "What took you so long?"

    show YukaFTalk with Dissolve(0.2)
    hide YukaATalk
    y "We have school today!"

    pause 0.2  # Helps with pacing
    show YukaFTalk with Dissolve(0.2)  # Bring back YukaFTalk before she speaks
    y "Are you planning to make us late?"
    show YukaGlare2 with Dissolve(0.2)  # Add a more intense reaction
    hide YukaFTalk

    f "..."
    pause 0.5  # Small delay for natural reaction

    show YukaNormA with Dissolve(0.2)
    hide YukaGlare2
    pause 0.7  # Makes movement feel less sudden
    play sound "move.ogg"
    hide YukaNormA with moveoutright
    stop sound
    play sound "tooclose.ogg"
    show YukaConcernP with vpunch
    e "{size=60}!!!{/size}"
    y """
    "Fu?"
    """ 
    y """
    "Are you even listening?"
    """ 
    hide YukaConcernP

    show YukaConcernPSadZ

    y """
    "You look so pale—are you okay?"
    """
    f """
    
    "..."

    "Ku{size=40}huhuhuhuhu...{/size}"

    "KuahAhahAHa!"

    "I'm TOTALLY fine!."

    "Actually, I could never feel any BETTER in my entire life!!"

    "NOW BACK OFF,WOMAN!"
    """
    
    hide YukaConcernPSadZ
    show YukaConcernPSurprise with vpunch
    y """
    "Wha—!?"
    """
    f """
    "Why on earth would you sleep in front of the door like that???"
    """
    hide YukaConcernPSurprise with Dissolve(0.5)
    show YukaSurpriseBl with Dissolve(0.5)
    f """

    "Have you ever considered what people might think?"

    "What are you?"

    "A street urchin or something?"    

    """
    show YukaFrown1 with Dissolve(0.2) 
    hide YukaSurpriseBl
    $renpy.pause(0.5)
    hide YukaFrown1
    show YukaFTalk
    y """
    
    "Mou! You startled me!,Fu!" 
     
    """
    show FunnySmile with Dissolve(0.2)
    hide YukaFTalk
    show YukaDumb
    y """

    "And for your information, I am neither a 'woman' nor a street urchin!"
    
    """
    e "???"
    hide FunnySmile
    show FunnySmile with Dissolve(0.2)
    hide YukaDumb
    show YukaDumb

    y """
    "I have told you countless times—I’m {color=#43C1E6}Yuka{/color}!!!" {fast}{size=40}{color=#43C1E6}Yuka...{/color}{/size} {w=0.2}{size=30}{color=#43C1E6}Yuka...{/color}{/size} {w=0.2}{size=25}{color=#43C1E6}Yuka...{/color}{/size} {w=0.2}{size=20}{color=#43C1E6}{alpha=0.8}Yukaaaaa.....{/alpha}{/size}
    
    """
   
    e """
    She yelled at me, then immediately launched into a rant without giving me a chance to recover from shock.

    Unquestionably, the type to talk first and think later.
    
    It’s honestly impressive how every thought she has is written all over her face.
    
    Now, what in the world is she even going on about?

    And why is she looking at me with that smug face, like she just won a debate against a goldfish?

    It’s probably a bad idea to ask what’s going on inside her head, but now I’m too curious to stop myself...
    """
    
    f """

    "What’s your point even supposed to be?"

    """ 
    show YukaNorm with Dissolve(0.2)
    hide FunnySmile
    show YukaNormSmile 
    hide YukaNorm
    hide YukaDumb
    $renpy.pause(2)
    show FunnySmile with Dissolve(0.2) 
    hide YukaNormSmile
    hide YukaDumb
    show YukaDumb
    hide FunnySmile

    y """

    "The point is..."    
    
    """
    show FunnyLaugh with Dissolve(0.2)
    show YukaMock
    hide FunnyLaugh
    hide YukaDumb

    y """

    "I have a name!"

    """
    show FunnySmile with Dissolve(0.2)
    show YukaMock2
    hide FunnySmile
    hide YukaMock

    y """

    "And urchin live in the sea, don't you know?"    

    
    """
    show YukaCSmile with Dissolve(0.2)
    hide YukaMock2
    hide FunnyLaugh
    show YukaThugLife
    hide YukaCSmile
    y """

    "You’re so lacking in knowledge, Fu."    
    
    """
    show YukaLaughN with Dissolve(0.2)
    hide YukaThugLife

    show YukaMock3
    hide YukaLaughN
    show YukaEyesCloseS with Dissolve(0.2)
    hide YukaMock3
    y """

    "How naive. You’ve got so much to learn, huh?"    
    
    """

    e """
    
    I regret expecting a proper answer.

    All that effort, only to be met with ridiculous nonsense.

    It's always like this. I always make bad decisions.

    No matter how good something seems at first, it all crumbles and ends in {color=#FF0000}Suffering{/color}.

    If this conversation drags on any longer, I might actually catch her stupidity like a virus.

    Just like every idiot does.

    For the sake of my already weakened sanity, I need to change the subject.  
    """

    f """
    "You know you could've just knocked on the door, right?"
    """
    show yuka shock3

    y """ 
    "Wow, Fu, your lack of awareness is astounding. Do you seriously think I’d risk becoming a suspect?"
    """
    
    y """
    "Do you really think I have the manners to knock on someone’s door in the morning?"
    """
    
    e """
    
    Oh-ho, so this so-called Yuka dares to challenge me?
    
    She dares challenge me with nonsense? Does she not realize I have years of arguing with my own intrusive thoughts?

    A mere mortal… against a mind in ruins? Foolish!
    
    Fine. Two can play this game. If logic won’t work, I shall descend to her level and make her taste her own medicine!
    
    """

    f """
    "Well, this is entirely your fault for not calling me! It’s not rocket science to make a phone call, right?"
    """
    
    #show yuka shock with flail

    y """
    "WHAT!?, I DID call you, y-you absolute walnut!!"
    """

    
    #show yuka angry
    y """
    "Ahh, Fu! You’ve always been like this. No wonder we failed the high school entrance exam!"
    """
    
    e """
    
    What the hell is this girl talking about? How is her failure my fault???
    
    Why the fuck is everyone like this? Always blaming someone else.
    
    """
    #show yuka frown

    f """
    "..."

    "Tch."

    "Whatever... School is pointless anyway."
   
    "No matter which school we go to, nothing will change."
    """
    $show yuka sad
    f """
    "Haha..."

    "You think I'll be 'fixed' if I go to a better school?"
    
    "Like that gullible pig—"
    
    "The one who swallows whatever they’re fed, just to get their throat slit the moment they stop growing."

    "All those fancy little nicknames they give the pig…"
    
    "Hahaha, I’m literally dying thinking about it."

    "Only after they killed me once did I realize—everyone's just full of themselves."

    "I was never their ‘joy’ or their ‘pride.’ I was their future pension, their status, their hard-earned trophy!"

    "But the moment I unable to shine, I became nothing but a burden... their mistake."

    "You don’t know what it’s like—"
    
    "How hard it is to wake up, to tiptoe through your own house just to avoid your own family."
    
    "To feel sick just from the thought of talking to people."

    "And even when I try to escape into sleep… they’re still there."
    
    "Every night. Every damn day."

    """
    #show yuka angry
    y "Fu! Listen to me!"

    return

