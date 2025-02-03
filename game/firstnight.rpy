image nightmare_effect:
    "Nightmare"
    alpha 1 zoom 7
    xpos 1 ypos 4.5
    linear 2 ypos 3.0
    linear 2 alpha 1
    linear 1 alpha 0.2 
    linear 1 xpos 1.2 ypos 5.5
    linear 1 alpha 0.4
    linear 1 alpha 0.2 

    linear 1 xpos 0.8 ypos 4.0
    linear 1 alpha 0.6
    linear 5 zoom 1.3 alpha 1 xpos 0.5 ypos 1.0

label firstnight:
    stop music
    $quick_menu = False
    show nightmare_effect with Fade(0.2, 0, 0, color="#fff")
    play sound "nightmare1.ogg"
    $ renpy.pause(16,hard = True)
    hide nightmare_effect with Fade(0.2, 0, 0, color="#fff")
    stop sound
    jump firstday

