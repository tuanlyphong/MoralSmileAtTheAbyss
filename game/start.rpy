image YukaSitPose = "YukaSitPose.png"
image OutsideFuHouse = "bg/OutsideFuHouse.png"
image OutsideFuHouse1 = "bg/OutsideFuHouse1.png"
image OutsideFuHouse2 = "bg/OutsideFuHouse2.png"
image OutsideFuHouse3 = "bg/OutsideFuHouse3.png"

image YukaSitPoseBlush = "YukaSitPoseBlush.png"
#decrease is move right,increase is move left
#                 down,                  up
#middle is xpos 0.5 ypos 1.0
image Outside:
    "OutsideFuHouse1"
    5
    "OutsideFuHouse2" with Dissolve(1)
    1
    
image YukaSleep:
    "Outside"     
    zoom 3 xpos 0.3 ypos 1.0
    linear 6 xpos 0.22 ypos 2.8
label main_menu:

    return

label start:
    stop music
    jump fight
image YukaWake:
    "OutsideFuHouse3"
    zoom 3 xpos 0.22 ypos 2.8
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
    f "Good morning?"
    y "Mornin-"
    window hide
    $quick_menu = False
    stop music
    show YukaWake with Dissolve(1)
    $renpy.pause(1, hard = True)  # This ensures everything stops for 6 seconds

image approach:
    "YukaAngry"
    ypos 1.2
    linear 1 zoom 1.2 ypos 1.4

image Close1:
    "OutsideFuHouse"
    zoom 1.5 ypos 1.5

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

image YukaDere1:
    "YukaDere"
    zoom 1.2 ypos 1.4

image YukaDere2:
    "YukaDereTalking"
    zoom 1.2 ypos 1.4
image YukaEmba:
    "YukaAngryBlush"
    pause 0.9
    "YukaDere" with Dissolve(0.1)
    pause 0.3
    "YukaDereTalking"
    pause 0.3
    "YukaDere"
image YukaAngry1:
    "YukaAngry"
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

image YukaFrown2:
    "YukaFrownTalking"
    zoom 1.2 ypos 1.4
image YukaNorm:
    "Yuka" with Dissolve (0.2)
    zoom 1.2 ypos 1.4
image Yuka GlareA:
    "YukaGlare1" with Dissolve(0.2)
    pause 0.2
    "YukaGlare2" with Dissolve(0.1)
image YukaATalk:
    "YukaAngry1" with Dissolve(0.2)
    pause 0.2
    "YukaAngry2"
    pause 0.3
    "YukaAngry1"
image YukaFTalk:
    "YukaFrown1" with Dissolve(0.2)
    pause 0.2
    "YukaFrown2"
    pause 0.3
    "YukaFrown1"
image YukaDTalk:
    "YukaDere1" with Dissolve(0.2)
    pause 0.2
    "YukaDere2"
    pause 0.3
    "YukaDere1"

label fight:
    play sound "Boom.ogg"
    $ quick_menu = True
    
    # Show Yuka close-up
    show Close1
    show Close2 with moveinbottom
    $renpy.pause(0.5)
    y "How DARE you!"
    
    
    # Fu backs off
    show Back1
    show Back2
    "Too close..."
    
    hide Back2
    show approach
    f "Urgh..."
    hide approach
    show YukaDTalk
    y "Mou!"
    show YukaATalk
    y "what took you so long?" 
    show YukaFTalk
    y "We have school today!" 
    show YukaFTalk
    y "Are you planning to make us late?"
    show YukaGlare2
    show YukaNorm
    
    y "Fu!" 
    y "Are you even listening?" 
    y "You look so pale—are you okay?"
    return

