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
style vkeyboard_text:
    font "fonts/Nunito-Regular.ttf"
    size 35
transform text_effect:
    linear 0.6 alpha 0.5
    linear 1.0 alpha 1
    repeat

transform text_effect2:
    linear 0.8 alpha 0.5
    linear 0.8 alpha 1
    repeat

transform text_effect3:
    linear 1.0 alpha 0.5
    linear 0.6 alpha 1
    repeat

style vkeyboard_button:
    background None  # Transparent by default
    padding (10, 5)  # Adjust padding

screen virtual_keyboard():
    frame:
        xysize (500, 300)  # Adjust size as needed
        align (0.5, 0.45)  # Center the keyboard on the screen
        background None
        vbox:
            # Displaying the entered name
            text "[persistent.player_name]" size 40 color "#ffffff" align (0.5, 0.5)

            # QWERTY keyboard layout
            vbox spacing 5:
                hbox spacing 5:
                    at text_effect

                    for letter in "qwertyuiop":
                        textbutton letter:
                            text_style "vkeyboard_text"  # Explicitly apply text style

                            style "vkeyboard_button"
                            action Function(append_letter, letter)

                hbox spacing 5:
                    at text_effect2

                    for letter in "asdfghjkl":
                        textbutton letter:
                            text_style "vkeyboard_text"  # Explicitly apply text style

                            style "vkeyboard_button"
                            action Function(append_letter, letter)

                hbox spacing 5:
                    at text_effect3

                    for letter in "zxcvbnm":
                        textbutton letter:
                            text_style "vkeyboard_text"  # Explicitly apply text style

                            style "vkeyboard_button"
                            action Function(append_letter, letter)

                hbox spacing 20:
                    
                    textbutton "Back":
                        text_style "vkeyboard_text"  # Explicitly apply text style
                        style "vkeyboard_button"
                        action Function(backspace_name)

                    textbutton "Done":
                        text_style "vkeyboard_text"  # Explicitly apply text style
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
            god "Are you sure you don't want to {color=#ff0}Name{/color} yourself?"
            menu:
               "yes":
                  "Don't you think a {color=#ff0}Name{/color}is important?"
                  with Fade(1.5, 0, 0, color="#fff")
                  $persistent.player_name = "Stranger"
                  $persistent.named = True
                  jump start
               "no":
                  pass
        elif persistent.player_name.lower() in [" fu"]:
            f0 "Hey!, That's my {color=#ff0}Name{/color}."
            god "I'm sorry, perhap choosing another {color=#ff0}Name{/color}"
        elif persistent.player_name.lower() in [" yuka"]:
            f0 """
            "Hey! You're not Yuka. There can only be one Yuka."
            """

            y0 """
            "Don't take it too seriously, Fu! People can have the same {color=#ff0}Name{/color}. Maybe their {color=#ff0}Name{/color} has a different meaning."

            "Or maybe it's just a coincidence that they have the same {color=#ff0}Name{/color} and meaning as mine. After all,[persistent.player_name] isn't that rare."
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
            god "While it might not define one’s entire {color=#ff0000}Existence{/color}"
            god "It can shape their {color=#79D021}Experiences{/color}"
            god "Are you sure that you want to be remembered as[persistent.player_name]?"
            menu:
                "Yes":
                    with Fade(1.5, 0, 0, color="#fff")
                    $persistent.named = True
                    jump start
                "No":
                    pass


