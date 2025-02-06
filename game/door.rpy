image doorsad2 = "bg/doorsad2.png"
image doorsad3 = "bg/doorsad3.png"
image doormad = "bg/doormad.png"
image doorsad = "bg/doorsad.png"

image door_effect:

    "doorsad"
    alpha 0
    linear 3 zoom 1 alpha 1

label door:
    $ quick_menu = False
    hide window
    show door_effect with Dissolve(1)
    $ renpy.pause(2, hard=True)
    if persistent.nihilism:
      jump door_choice2
    else:
      jump door_choice

label door_choice:
    menu:
        "Open":
            stop music

            jump outside
        "Do nothing":
            $ renpy.pause(3, hard=True)  # Pause for 2 seconds
            play music "nothing1.ogg"
            jump nothing1  # Repeat the choice without replaying the effect


label door_choice2:
    menu:
        "Open":
            stop music
            jump outside

label nothing1:
    show doorsad2 with Fade(1, 0, 0, color="#000")
    menu:
        "Open":
            stop music
            jump outside
        "Do nothing":
            $ renpy.pause(2, hard=True)  # Pause for 2 seconds
            jump nothing2 # Repeat the choice without replaying the effect
    return
label nothing2:
    show doorsad3 with Fade(1, 0, 0, color="#000")

    menu:
        "Open":
            stop music
            jump outside
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
    That was a terrible ending.

    Perhaps the worst.

    Why didn’t you do anything at all?

    I regret giving you {color=#FFA500}power{/color}, only for you to choose {color=#c0c0c0}nothing{/color}.

    Don’t you think it’s pathetic to keep choosing {color=#c0c0c0}nothing{/color} like this?

    Or maybe… you think {color=#c0c0c0}nothing{/color} matters.

    That everything is {color=#c0c0c0}nothing{/color}.

    That {color=#c0c0c0}nothing{/color} is worth doing.

    …

    I see.

    If you truly feel this way, then you’re not alone.

    Many people sink into this {color=#c0c0c0}emptiness{/color}, trapped in a hollow existence.

    I have, too. Even now, I still struggle with it.

    But tell me… are you waiting for someone to save you?

    They won’t.

    And even if someone wanted to, they couldn’t.

    No one can pull you out of this but yourself.

    Because doing {color=#c0c0c0}nothing{/color} is still a choice, your choice.

    And it’s the worst one.

    If you insist on choosing {color=#c0c0c0}nothing{/color}… then why play this game at all?

    I won’t let you make that choice again. I’m taking it away.
    """
    show door_effect
    jump door_choice2


