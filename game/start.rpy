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
    jump outside

image YukaWake:
    "OutsideFuHouse3"
    zoom 3 xpos 0.22 ypos 2.8
image Headache:
    "OutsideFuHouse"
    zoom 2
label outside:
    window hide
    $ quick_menu = False
    show YukaSleep
    $renpy.pause(6, hard = True)  # This ensures everything stops for 6 seconds
    window show
    $ quick_menu = True
    f "Good morning?"
    y "Mornin-"
    window hide
    $quick_menu = False
    show YukaWake with Dissolve(1)
    $renpy.pause(1, hard = True)  # This ensures everything stops for 6 seconds
    show OutsideFuHouse with vpunch
    $quick_menu = True
    y "HOW DARE YOU?!"
    return

