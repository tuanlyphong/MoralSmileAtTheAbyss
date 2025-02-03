image door_effect:
    "doorsad"
    alpha 0
    linear 1.5 zoom 1 alpha 1

label main_menu:

    return

label start:
    jump door

label door:
    $ quick_menu = False
    hide window
    stop music
    show door_effect
    $ renpy.pause(2, hard=True)
    if persistent.nihilism:
      jump door_choice2
    else:
      jump door_choice

label door_choice:
    menu:
        "Open":
            # Add logic for opening the door here
            pass
        "Do nothing":
            $ renpy.pause(3, hard=True)  # Pause for 2 seconds
            play music "nothing1.ogg"
            jump nothing1  # Repeat the choice without replaying the effect

    return

label door_choice2:
    menu:
        "Open":
            # Add logic for opening the door here
            pass
    return

label nothing1:
    show doorsad2 with Fade(1, 0, 0, color="#000")
    menu:
        "Open":
            # Add logic for opening the door here
            pass
        "Do nothing":
            $ renpy.pause(2, hard=True)  # Pause for 2 seconds
            jump nothing2 # Repeat the choice without replaying the effect
    return
label nothing2:
    show doorsad3 with Fade(1, 0, 0, color="#000")

    menu:
        "Open":
            # Add logic for opening the door here
            pass
        "Do nothing":
            $ renpy.pause(1, hard=True)  # Pause for 2 seconds
            play music "nothing2.ogg"
            jump nothing3  # Repeat the choice without replaying the effect
    return
label nothing3:
    show doormad with Fade(1, 0, 0, color="#000")
    menu:
      "Do nothing":
          jump nihilism
    return

label nihilism:
    stop music
    $persistent.nihilism = True
    scene black
    play sound "audio/notification_sound.ogg" 
    $renpy.pause(2)

    play music "audio/void.ogg"
    god """
    Hmm... what a horrible ending.

    I shouldn't have given you this much {color=#FFA500}power{/color}.

    It'd be pretty lame if you kept choosing to do {color=#c0c0c0}nothing{/color} like this.

    Or perhaps... you think everything is meaningless?

    That nothing is worth doing?

    ...

    I see...

    But isn't choosing to do nothing still an action?
    """
    show door_effect
    jump door_choice2
