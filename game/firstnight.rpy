

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
    "You are our {color=#FFA500}Pride{/color} and {color=#FFA500}Joy{/color}, Fu."

    "Fu coming in first again, as {color=#FFA500}Expected{/color}!"

    "That's my boy!"

    "You're going to be a great man."

    "What happened to you?"

    "Who cares about the meaning of life? You need to make {color=#FF0000}Money{/color}."

    "{color=#FF0000}Depression{/color}?"

    "What is that? Is this supposed to be a joke?"

    "We paid you to fix him, and you made up some disease?!"

    "What a fucking waste of {color=#FF0000}Money{/color}."

    "Look at him. Doesn’t even look people in the eyes anymore."

    "You were supposed to be better."

    "You let us down."

    "You let yourself down."

    "I want to beat you the fuck up."

    "We wasted our time and {color=#FF0000}Money{/color} on you."

    "You ruined everything."

    "What are you reading, *Beyond Good and Evil*? Isn’t it obvious? It’s {color=#FF0000}Money{/color}."

    "Why do I even raise you? It would have been better if I raised a pig."

    "You are a fucking {color=#FF0000}Burden{/color}!"

    "It’s all your fault!"

    "Why are you even {color=#FF0000}Alive{/color} in the first place?"

    """ 

    hide nightmare_effect
    show paranoid with Fade(0.5, 0, 0, color="#fff")
    hide paranoid with Fade(0.5, 0, 0, color="#000")

    stop music
    jump firstday

