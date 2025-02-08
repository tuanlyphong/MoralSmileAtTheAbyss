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
    "YukaAngrySmile"
    zoom 1.2 ypos 1.4

image FunnyLaugh:
    "YukaEyesClosedLaugh"
    zoom 1.2 ypos 1.4

image FunnySmile:
    "YukaEyesClosedGrin"
    zoom 1.2 ypos 1.4

image YukaAngry1:
    "YukaAngry"
    zoom 1.2 ypos 1.4

image YukaDere2:
    "YukaDereTalking"
    zoom 1.2 ypos 1.4

image YukaDere1:
    "YukaDere"
    zoom 1.2 ypos 1.4

image YukaCSmile:
    "YukaWinkCatSmile"
    zoom 1.2 ypos 1.4

image YukaNorm:
    "Yuka"
    zoom 1.2 ypos 1.4

image YukaNormClose:
    "YukaEyesClose"
    zoom 1.2 ypos 1.4

image YukaAngry2:
    "YukaAngryTalking"
    zoom 1.2 ypos 1.4

image YukaGlare1:
    "YukaGlare"
    zoom 1.2 ypos 1.4

image YukaGlare2:
    "YukaGlareFrown"
    zoom 1.2 ypos 1.4

image YukaFrown1:
    "YukaFrown"
    zoom 1.2 ypos 1.4

image YukaSurpriseBl:
    "YukaSurprise2"
    zoom 1.2 ypos 1.4

image YukaFrown2:
    "YukaFrownTalking"
    zoom 1.2 ypos 1.4

image YukaNSmile:
    "YukaSmile"
    zoom 1.2 ypos 1.4

image YukaCSEC:
    "YukaEyesClosedCatSmile"
    zoom 1.2 ypos 1.4

#ADVANCE
image Outside:
    "OutsideFuHouse1" with Dissolve(1)
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
    linear 0.5 zoom 1.0 ypos 1.0

image Back2:
    "YukaAngryBlush"
    zoom 2.0 ypos 2.2
    linear 0.5 zoom 1.0 ypos 1.2
image Back3:
    "YukaAngry"
    zoom 1.0 ypos 1.2

#COMBINE
image YukaDumb:
    "FunnySmile" with Dissolve(0.2)
    pause 0.5
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.6
    "Smug" with Dissolve(0.2)

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

image YukaThugLife:
    "YukaCSmile" with Dissolve(0.2)
    pause 0.5
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.4
    "YukaCSEC" with Dissolve(0.2)

image YukaEmba:
    "YukaAngryBlush" with Dissolve(0.2)
    pause 0.9
    "YukaDere" with Dissolve(0.2)
    pause 0.4
    "YukaDereTalking" with Dissolve(0.2)
    pause 0.3
    "YukaDere" with Dissolve(0.2)

image YukaNormA:
    "YukaNorm" with Dissolve(0.2)
    pause 0.4
    "YukaNormClose" with Dissolve(0.2)
    pause 0.4
    "YukaNorm" with Dissolve(0.2)

image YukaGlareA:
    "YukaGlare1" with Dissolve(0.2)
    pause 0.5
    "YukaGlare2" with Dissolve(0.2)

image YukaATalk:
    "YukaAngry1"
    pause 0.4
    "YukaAngry2" with Dissolve(0.2)
    pause 0.5
    "YukaAngry1" with Dissolve(0.2)

image YukaFTalk:
    "YukaFrown1"
    pause 0.4
    "YukaFrown2" with Dissolve(0.2)
    pause 0.5
    "YukaFrown1" with Dissolve(0.2)

image YukaDTalk:
    "YukaDere1"
    pause 0.3
    "YukaDere2" with Dissolve(0.2)
    pause 0.6
    "YukaDere1" with Dissolve(0.2)

image YukaNormSmile:
    "YukaNorm" with Dissolve(0.2)
    pause 0.4
    "YukaNSmile" with Dissolve(0.2)
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
    hide YukaWake
    hide YukaSleep
    # Show Yuka close-up
    show Close1 with Dissolve(1)
    show Close2 with vpunch
    $renpy.pause(0.5,hard=True)
    $ quick_menu = True
    y """
    "How DARE you!"
    """
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
    show approach
    $renpy.pause(1, hard = True)
    $ quick_menu = True
    f "Urgh..."
    show YukaDere1 with Dissolve(0.5)
    hide approach
    show YukaDTalk
    hide YukaDere1
    y """
    "Mou!"
    """
    show YukaAngry1 with Dissolve(0.2)
    hide YukaDTalk
    show YukaATalk
    hide YukaAngry1
    y """
    "what took you so long?"
    """
    show YukaFrown1 with Dissolve(0.2)
    hide YukaATalk
    show YukaFTalk
    hide YukaFrown1
    y """
    "We have school today!"
    """ 
    show YukaFrown1 with Dissolve(0.2)
    hide YukaFTalk
    show YukaFTalk
    hide YukaFrown1
    y """
    "Are you planning to make us late?"
    """
    show YukaGlare2 with Dissolve(0.2)
    hide YukaFTalk
    f """
    "..."
    """
    show YukaNormA with Dissolve(0.2)
    hide YukaGlare2
    $renpy.pause(1)
    hide YukaNormA with moveoutright
    show YukaConcernP with hpunch
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

    "Ku{size=40}huhuhuhuhu...{/size}"

    "KuahAhahAHa!"

    "I'm totally fine!."

    "Actually, I could never feel any better in my entire life!!"

    "NOW BACK OFF,WOMAN!"
    """
    
    hide YukaConcernPSad
    show YukaConcernPSurprise with vpunch
    f """
    "Why on earth would you sleep in front of the door like that???"
    """
    hide YukaConcernPSurprise with moveoutright
    show YukaSurpriseBl with moveinright
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
    
    "Mou!,You startled me!,Fu!" 
     
    """

    hide YukaFTalk
    show YukaDumb
    y """

    "And for your information, I am neither a 'woman' nor a street urchin!"
    
    """
    hide FunnySmile
    show FunnySmile with Dissolve(0.2)
    hide YukaDumb
    show YukaDumb

    y """
    
    "I have told you countless times, I’m {color=#43C1E6}Yuka{/color}!"
    
    """
    
    e """
    She startled me first, then proceeded to ramble on without giving me a {color=#FFA500}chance{/color} to speak.

    Unquestionably, a typical type who speaks without filtering any thoughts.

    It's impressive that her thoughts are all written on her face.

    Now, what in the world is she even going on about?

    And why is she even looking at me with that smug face,like she defeated me in a competition?

    It's probably a bad idea to ask what she has on her head,but I'm {color=#FFFF00}Curious{/color}.
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

    "I have a {color=#ff0}Name{/color}"

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
    
    I regret {color=#FFA500}expecting{/color} a proper answer.

    All the effort I put in, just to receive ridiculous insults.

    It's always like this. I always make bad decisions.

    No matter how good it seems from the start, it all falls apart and ends in {color=#FF0000}Suffering{/color}.

    I don’t want to deal with this level of inanity.

    If this conversation drags on, I’ll catch a case of absurdity and start assuming everyone’s a fool.

    Just like this idiot does.

    For the purpose of minimizing {color=#FF0000}Lost{/color}, better change the subject.    

    """

    return

