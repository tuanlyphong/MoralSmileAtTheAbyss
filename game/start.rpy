image door_effect:
    "doorsad"
    alpha 0
    linear 1.5 zoom 1 alpha 1

label main_menu:

    return

label start:
    jump door

label door:
    show door_effect
    $ renpy.pause(2, hard=True)
    $ quick_menu = False
    jump door_choice

label door_choice:
    menu:
        "Open":
            # Add logic for opening the door here
            pass
        "Do nothing":
            $ renpy.pause(3, hard=True)  # Pause for 2 seconds
            jump door_choice  # Repeat the choice without replaying the effect

    return

