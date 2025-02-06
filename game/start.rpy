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


###BASIC
image Smug:
    "YukaAngrySmile" with Dissolve(0.25)
    zoom 1.2 ypos 1.4

image FunnyLaugh:
    "YukaEyesClosedLaugh" with Dissolve(0.3)
    zoom 1.2 ypos 1.4

image FunnySmile:
    "YukaEyesClosedGrin" with Dissolve(0.22)
    zoom 1.2 ypos 1.4

image YukaAngry1:
    "YukaAngry" with Dissolve(0.28)
    zoom 1.2 ypos 1.4

image YukaDere2:
    "YukaDereTalking" with Dissolve(0.2)
    zoom 1.2 ypos 1.4

image YukaDere1:
    "YukaDere" with Dissolve(0.27)
    zoom 1.2 ypos 1.4

image YukaCSmile:
    "YukaWinkCatSmile" with Dissolve(0.3)
    zoom 1.2 ypos 1.4

image YukaNorm:
    "Yuka" with Dissolve(0.23)
    zoom 1.2 ypos 1.4

image YukaNormClose:
    "YukaEyesClose" with Dissolve(0.29)
    zoom 1.2 ypos 1.4

image YukaAngry2:
    "YukaAngryTalking" with Dissolve(0.24)
    zoom 1.2 ypos 1.4

image YukaGlare1:
    "YukaGlare" with Dissolve(0.2)
    zoom 1.2 ypos 1.4

image YukaGlare2:
    "YukaGlareFrown" with Dissolve(0.3)
    zoom 1.2 ypos 1.4

image YukaFrown1:
    "YukaFrown" with Dissolve(0.22)
    zoom 1.2 ypos 1.4

image YukaSurpriseBl:
    "YukaSurprise2" with Dissolve(0.26)
    zoom 1.2 ypos 1.4

image YukaFrown2:
    "YukaFrownTalking" with Dissolve(0.21)
    zoom 1.2 ypos 1.4

image YukaNSmile:
    "YukaSmile" with Dissolve(0.3)
    zoom 1.2 ypos 1.4
image YukaCSEC:
    "YukaEyesClosedCatSmile" with Dissolve(0.24)
    zoom 1.2 ypos 1.4

#ADVANCE
image Outside:
    "OutsideFuHouse1"
    5
    "OutsideFuHouse2" with Dissolve(1)
    1
image YukaConcernPSurprise:
    "YukaConcernPoseSurprise"
    zoom 1.4 xpos 0.7 ypos 1.3
    linear 0.5 zoom 1.3 ypos 1.2 
image YukaConcernP:
    "YukaConcernPose"
    zoom 1.3 xpos 0.7 ypos 1.2
image YukaConcernPSad:
    "YukaConcernPoseSad"
    zoom 1.3 xpos 0.7 ypos 1.2
    linear 1 zoom 1.4 ypos 1.3
image YukaSleep:
    "Outside"     
    zoom 3 xpos 0.3 ypos 1.0
    linear 6 xpos 0.22 ypos 2.8
image YukaWake:
    "OutsideFuHouse3"
    zoom 3 xpos 0.22 ypos 2.8
image approach:
    "YukaAngry"
    ypos 1.2
    linear 1 zoom 1.2 ypos 1.4
image Close1:
    "OutsideFuHouse"
    zoom 1.5 ypos 1.5
image Out:
    "OutsideFuHouse"
    zoom 1.0 ypos 1.0

image Close2:
    "YukaEmba"
    zoom 2.0 ypos 2.2

image Back1:
    "OutsideFuHouse"
    zoom 1.5 ypos 1.5
    linear 1.0 zoom 1.0 ypos 1.0

image Back2:
    "YukaAngryBlush"
    zoom 2.0 ypos 2.2
    linear 1.0 zoom 1.0 ypos 1.2

#COMBINE
image YukaDumb:
    "FunnySmile"
    pause 0.5
    "FunnyLaugh" 
    pause 0.6
    "Smug"
image YukaMock2:
    "FunnySmile"
    pause 0.4
    "FunnyLaugh"
    pause 0.4

image YukaMock:
    "FunnyLaugh"
    pause 0.4
    "FunnySmile"
    pause 0.4
image YukaThugLife:
    "YukaCSmile"
    pause 0.5
    "FunnyLaugh"
    pause 0.4
    "YukaCSEC"
image YukaEmba:
    "YukaAngryBlush"
    pause 0.9
    "YukaDere" 
    pause 0.4
    "YukaDereTalking"
    pause 0.3
    "YukaDere"

image YukaNormA:
    "YukaNorm" 
    pause 0.4
    "YukaNormClose"
    pause 0.4
    "YukaNorm"

image YukaGlareA:
    "YukaGlare1" 
    pause 0.5
    "YukaGlare2"

image YukaATalk:
    "YukaAngry1" 
    pause 0.4
    "YukaAngry2"
    pause 0.5
    "YukaAngry1"

image YukaFTalk:
    "YukaFrown1" 
    pause 0.4
    "YukaFrown2"
    pause 0.5
    "YukaFrown1"

image YukaDTalk:
    "YukaDere1" 
    pause 0.3
    "YukaDere2"
    pause 0.6
    "YukaDere1"

image YukaNormSmile:
    "YukaNorm" 
    pause 0.4
    "YukaNSmile"
    pause 0.5

label outside:
    window hide
    $ quick_menu = False
    play sound "open.ogg"
    hide door_effect with Fade(0.5,0,0,color ="#fff") 
    show YukaSleep with Dissolve(1)
    $renpy.pause(6, hard = True)  # This ensures everything stops for 6 seconds
    window show
    $ quick_menu = True
    play music "morning.ogg"
    
    f """
    
    "..."
    
    "Good morning?"
    """

    y """

    "Mmm..."

    "Mornin-"
    
    """
    window hide
    $quick_menu = False
    stop music
    show YukaWake with Dissolve(1)
    $renpy.pause(1, hard = True)  # This ensures everything stops for 6 seconds



label fight:
    play sound "Boom.ogg"
    
    # Show Yuka close-up
    show Close1
    show Close2 with moveinbottom
    $renpy.pause(0.5,hard=True)
    $ quick_menu = True
    y """
    "How DARE you!"
    """
    
    
    # Fu backs off
    show Back1
    show Back2
    e "Whoa!"
    window hide
    $ quick_menu = False
    hide Back2
    hide Close1
    hide Close2
    hide Back1
    show Out

    show approach
    $renpy.pause(1, hard = True)
    $ quick_menu = True
    f "Urgh..."
    hide approach
    show YukaDTalk
    y """
    "Mou!"
    """
    hide YukaDTalk
    show YukaATalk
    y """
    "what took you so long?"
    """
    hide YukaATalk
    show YukaFTalk
    y """
    "We have school today!"
    """ 
    hide YukaFTalk
    show YukaFTalk
    y """
    "Are you planning to make us late?"
    """
    hide YukaFTalk
    show YukaGlare2
    f """
    "..."
    """
    hide YukaGlare2
    show YukaNormA
    $renpy.pause(1)
    hide YukaNormA with moveoutright
    show YukaConcernP with moveinright  # Show Yuka on top
    y """
    "Fu?"
    """ 
    y """
    "Are you even listening?"
    """ 
    hide YukaConcernP
    show YukaConcernPSad
    y """
    "You look so pale—are you okay?"
    """
    f """
    
    "..."

    "B-Back off woman!"
    
    """
    hide YukaConcernPSad
    show YukaConcernPSurprise
    f """
    "Don’t sit in front of the door like that"
    """
    hide YukaConcernPSurprise with moveoutright
    show YukaSurpriseBl with moveinright
    f """

    "What are you?"

    A street urchin or something?"
    
    """
    show YukaFrown1 
    $renpy.pause(0.5)
    hide YukaFrown1
    show YukaFTalk
    y """
    
    "I am NOT 'woman' or a street urchin!" 
    
    """
    hide YukaFTalk
    show YukaDumb
    y """
    
    "I’m Yuka!"
    
    """
    
    e """
    She absolutely caught me off guard, then proceeded to ramble on without giving me a {color=#FFA500}chance{/color} to speak.

    She must be the type who speaks without filtering her thoughts.

    And somehow, she manages to convey every single one of them through her expression at the same time.

    Now, what in the world is she even going on about?

    And why does she look so self-assured,

    as if her words have any real substance?   
    """
    
    f """

    "What’s your point even supposed to be?"

    """ 
    hide YukaDumb
    show YukaNormSmile
    $renpy.pause(1)
    hide YukaNormSmile
    show YukaDumb
    y """

    "The point is..."    
    
    """
    hide YukaDumb
    show YukaMock2
    y """

    "I have a name"

    
    """
    hide YukaMock
    show YukaMock
    y """

    "And urchin live in the sea, don't you know?"    

    
    """
    hide YukaMock
    show YukaThugLife
    y """

    "You’re so lacking in knowledge, Fu."    
    
    """

    hide YukaThugLife
    show YukaMock
    y """

    "How naive. You’ve got so much to learn, huh?"    
    
    """

    e """

    I don’t want to deal with this level of inanity. 

    If this conversation drags on 

    I’ll catch a case of absurdity and start assuming everyone’s a fool. 

    Just like every idiot does.
    
    """
    return

