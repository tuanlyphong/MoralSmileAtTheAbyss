init python:
    def append_letter(letter):
        if len(persistent.player_name) < 30:  # Max length of 30
            if len(persistent.player_name) == 1:
                  persistent.player_name += letter.upper()  # First letter should be capitalized
            else:
                  persistent.player_name += letter.lower()  # Remaining letters should be lowercase
            renpy.play("press.ogg")
    def backspace_name():
        if len(persistent.player_name) > 1:
            persistent.player_name = persistent.player_name[:-1]
            renpy.play("press.ogg")

default persistent.player_name = " "
$ initialize_persistent_vars()

style vkeyboard_button:
    background None  # Transparent by default
    font "fonts/Nunito-Regular.ttf"  # Replace with your font path
    padding (10, 5)  # Adjust padding
    size 24  # Font size
    align (0.5, 0.5)  # Center the button text

screen virtual_keyboard():
    frame:
        xysize (500, 300)  # Adjust size as needed
        align (0.5, 0.5)  # Center the keyboard on the screen
        background None
        vbox:
            # Displaying the entered name
            text "[persistent.player_name]" size 32 color "#ffffff" align (0.5, 0.5)

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
            god "Are you sure you don't want to {color=#ff0}name{/color} yourself?"
            menu:
               "yes":
                  "Don't you think a {color=#ff0}name{/color}is important?"
                  with Fade(1.5, 0, 0, color="#fff")
                  $persistent.player_name = ""
                  $persistent.named = True
                  jump start
               "no":
                  pass
        elif persistent.player_name.lower() in [" fu"]:
            f0 "Hey!, That's my {color=#ff0}name{/color}."
            god "I'm sorry, perhap choosing another {color=#ff0}name{/color}"
        elif persistent.player_name.lower() in [" yuka"]:
            f0 """
            "Hey! You're not Yuka. There can only be one Yuka."
            """

            y0 """
            "Don't take it too seriously, Fu! People can have the same {color=#ff0}name{/color}. Maybe their {color=#ff0}name{/color} has a different meaning."

            "Or maybe it's just a coincidence that they have the same {color=#ff0}name{/color} and meaning as mine. After all,[persistent.player_name] isn't that rare."
            """
            god "Are you sure you want to be remembered as[persistent.player_name]?"
            menu:
               "Yes":
                  f0 """
                  "I don't know why you'd want to call yourself[persistent.player_name]."

                  "If you're just experimenting, {color=#ff0}Naming{/color} yourself anything doesn't change how the story goes."

                  "But if your {color=#ff0}Name{/color} really is[persistent.player_name], then that's totally okay."

                  "But if you're naming yourself[persistent.player_name] just to make me {color=#FF0000}Suffer{/color} even more..."

                  "Then you're truly the sickest among the players. Nobody is going to love you."

                  "Nobody."
                  """
                  with Fade(1.5, 0, 0, color="#fff")
                  $persistent.named = True
                  jump start
               "no":
                  pass
        elif persistent.player_name.lower() in [" fuyuka"]:
            god "I'm sorry, but this {color=#ff0}Name{/color} mean a lot to me"
        else:
            god "Naming is very important..."
            god "It can last a lifetime, you know?"
            god "While it might not define one’s entire {color=#ff0000}existence{/color}"
            god "It can shape their {color=#79D021}experiences{/color}"
            god "Are you sure that you want to be remembered as[persistent.player_name]?"
            menu:
                "Yes":
                    with Fade(1.5, 0, 0, color="#fff")
                    $persistent.named = True
                    jump start
                "No":
                    pass


