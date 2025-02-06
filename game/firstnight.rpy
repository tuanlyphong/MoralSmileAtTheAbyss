

image Nightmarea:
    "bg/nightmare.png" with Dissolve(2)
    1.5
    "bg/nightmare2.png" with Dissolve(2)
    1.5
    repeat



image nightmare_effect:
    "Nightmarea"
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

    play music "nightmare1.ogg"
    $quick_menu = True
    all """
    You shouldn't have been born

    You are such a burden

    Why are you so stupid?

    He's a little bit slower than the other kids

    It's all your fault

    Don't even try

    You will fail

    And you will always fail

    You are so useless

    Why do I even raise you? It would have been much better if I raised a pig instead of you    
    
    Why can't you do anything?

    What the fuck is wrong with your brain?
    
    If you do that again, I'll beat you up
    """ 
    hide nightmare_effect
    show paranoid with Fade(0.5, 0, 0, color="#fff")
    $renpy.pause(1)
    hide paranoid with Fade(0.5, 0, 0, color="#000")

    stop music
    jump firstday

