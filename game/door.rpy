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
            hide door_effect with Dissolve(1) 
            $ renpy.pause(2)  # Pause for 2 seconds
            play music "nothing1.ogg"
            jump nothing1  # Repeat the choice without replaying the effect


label door_choice2:
    stop music
    menu:
        "Open":
            stop music
            jump outside

label nothing1:
    show paranoid with Fade(0.5, 0, 0, color="#000")
    hide paranoid with Fade(0.5, 0, 0, color="#fff")
    show doorsad
    show doorsad2 with Dissolve(0.5)
    menu:
        "Open":
            stop music
            jump outside
        "Do nothing":
            hide door_effect with Dissolve(1)
            $ renpy.pause(2, hard=True)  # Pause for 2 seconds
            jump nothing2 # Repeat the choice without replaying the effect
    return
label nothing2:
    show paranoid with Fade(0.5, 0, 0, color="#000")
    hide paranoid with Fade(0.5, 0, 0, color="#fff")

    show doorsad3 with Dissolve(0.5) 
    menu:
        "Open":
            stop music
            jump outside
        "Do nothing":
            hide doorsad2
            hide doorsad
            hide doorsad3 with Dissolve(1)
            $ renpy.pause(1, hard=True)  # Pause for 2 seconds
            play music "nothing2.ogg"
            jump nothing3  # Repeat the choice without replaying the effect
    return
label nothing3:
    show paranoid with Fade(0.5, 0, 0, color="#000")
    hide paranoid with Fade(0.5, 0, 0, color="#fff")

    show doormad with Fade(0.5, 0, 0, color="#ff0000")
    menu:
      "{color=#ff0000}Do nothing{/color}":
          $persistent.nihilism = True
          $persistent.nihilism2 = True

          $renpy.quit()
    return

label nihilism:
    stop music
    play sound "audio/notification_sound.ogg" 
    $renpy.pause(2)

    play music "audio/void.ogg"
    
    $renpy.pause(2)
    god """

    That was...

    A {color=#ff0000}Terrible{/color} ending.


    Perhaps the {color=#ff0000}Worst{/color}.

    Why didn’t you do anything at all?

    I regret giving you {color=#FFA500}Power{/color}, only for you to choose {color=#c0c0c0}Nothing{/color}.

    Don’t you think it’s pathetic to keep choosing {color=#c0c0c0}Nothing{/color} like this?

    Or maybe… you think {color=#c0c0c0}Nothing{/color} matters.

    That everything is {color=#c0c0c0}Nothing{/color}.

    That {color=#c0c0c0}Nothing{/color} is worth doing.

    …

    I see.

    If you truly feel this way, then you’re truly {color=#c0c0c0}Alone{/color}.

    Many people sink into this {color=#c0c0c0}Emptiness{/color}, trapped in a hollow {color=#ff0000}existence{/color}.

    I have, too. Even now, I still struggle with it.

    But tell me… are you waiting for someone to {color=#FFA500}Save{/color} you?

    They won’t.

    And even if someone wanted to, they couldn’t.

    No one can pull you out of this but yourself.

    Doing {color=#c0c0c0}Nothing{/color} is a choice...

    Your choice.

    And it’s the {color=#ff0000}Worst{/color} one.

    If you insist on choosing {color=#c0c0c0}Nothing{/color}… then why play this game at all?

    I won’t let you make that choice again. I’m taking it away.
    """
    $persistent.nihilism2 = False
    show door_effect
    jump door_choice2


