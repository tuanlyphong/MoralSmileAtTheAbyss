image nightmare_effect:
    "Nightmare"
    alpha 0.2 zoom 7
    xpos 0.5 ypos 4.5

    linear 7 zoom 1 alpha 1 xpos 0.5 ypos 1.0

label start:
    stop music
    $quick_menu = False
    show nightmare_effect with Fade(0.2, 0, 0, color="#fff")
    play sound "nightmare1.ogg"
    $ renpy.pause(17)
    hide nightmare_effect with Fade(0.2, 0, 0, color="#fff")
    stop sound
    jump firstday

