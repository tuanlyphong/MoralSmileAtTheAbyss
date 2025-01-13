default persistent.player_name = " "

style vkeyboard_button:
    idle_background "#000000"  # Color when the button is idle
    hover_background "#000000"  # Color when the button is hovered
    insensitive_background "#ffffff"  # Color when the button is disabled
    background None  # Transparent by default
    color "#ffffff"  # Text color
    font "fonts/Nunito-Regular.ttf"  # Replace with your font path
    padding (10, 5)  # Adjust padding
    size 24  # Font size
    align (0.5, 0.5)  # Center the button text

screen virtual_keyboard():
    frame:
        xysize (800, 400)  # Adjust size as needed
        align (0.66, 0.66)  # Center the keyboard on the screen
        background None  # No visible frame background

        vbox:
            # Displaying the entered name
            text "[persistent.player_name]" size 32 color "#B22222" align (0.5, 0.5)

            # QWERTY keyboard layout
            vbox spacing 5:
                hbox spacing 5:
                    for letter in "qwertyuiop":
                        textbutton letter:
                            style "vkeyboard_button"
                            action Function(append_letter, letter)

                hbox spacing 5:
                    for letter in "asdfghjkl":
                        textbutton letter:
                            style "vkeyboard_button"
                            action Function(append_letter, letter)

                hbox spacing 5:
                    for letter in "zxcvbnm":
                        textbutton letter:
                            style "vkeyboard_button"
                            action Function(append_letter, letter)

                hbox spacing 20:
                    textbutton "Back":
                        style "vkeyboard_button"
                        action Function(backspace_name)

                    textbutton "Done":
                        style "vkeyboard_button"
                        action Return(True)


# Label to ask for the player's name
label naming:
    $ persistent.player_name = " "  # Reset the name
    god "Hi Stranger!"
    god "What should I call you?"
    while True:
        call screen virtual_keyboard
        if  persistent.player_name.lower() in [" "]:
            god "Are you sure you don't want to name yourself?"
            menu:
               "yes":
                  "Don't you think a name is important?"
                  with Fade(1.5, 0, 0, color="#fff")
                  $persistent.player_name = ""
                  $persistent.named = True
                  jump start
               "no":
                  pass
        elif persistent.player_name.lower() in [" fu"]:
            f0 "Hey!, That's my name."
            god "I'm sorry, perhap choosing another name"
        elif persistent.player_name.lower() in [" yuka"]:
            f0 "Hey! You're not Yuka. There can only be one Yuka."
            y0 "Don't take it too seriously, Fu! People can have the same name. Maybe their name has a different meaning."
            y0 "Or maybe it's just a coincidence that they have the same name and meaning as mine. After all,[persistent.player_name] isn't that rare."
            god "Are you sure you want to be remembered as[persistent.player_name]?"
            menu:
               "Yes":
                  f0 "I don't know why you'd want to call yourself[persistent.player_name]."
                  f0 "If you're just experimenting, naming yourself anything doesn't change how the story goes."
                  f0 "But if your name really is[persistent.player_name], then that's totally okay."
                  f0 "But if you're naming yourself[persistent.player_name] just to make me suffer even more..."
                  f0 "Then you're truly the sickest among the players. Nobody is going to love you."
                  f0 "Nobody."
                  with Fade(1.5, 0, 0, color="#fff")
                  $persistent.named = True
                  jump start
               "no":
                  pass
        elif persistent.player_name.lower() in [" fuyuka"]:
            god "I'm sorry, but this name mean a lot to me"
        else:
            god "Naming is very important..."
            god "It can last a lifetime, you know?"
            god "While it might not define one’s entire existence"
            god "It can shape their experiences"
            god "Are you sure that you want to be remembered as[persistent.player_name]?"
            menu:
                "Yes":
                    with Fade(1.5, 0, 0, color="#fff")
                    $persistent.named = True
                    jump start
                "No":
                    pass


