## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            xalign 1.0  # Align to the right
            yalign 1.0  # Align to the bottom
            spacing 10  # Optional, adds space between buttons

            # First column (buttons 1, 2)
            vbox:
                spacing 10
                textbutton _("History") action ShowMenu('history') hover_sound hover_sound
                textbutton _("Save") action ShowMenu('save') hover_sound hover_sound
                textbutton _("Q.Save") action QuickSave() hover_sound hover_sound
                textbutton _("Q.Load") action QuickLoad() hover_sound hover_sound

            # Second column (buttons 3, 4)
            vbox:
                spacing 10
                textbutton _("Auto") action Preference("auto-forward", "toggle") hover_sound hover_sound
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) hover_sound hover_sound
                textbutton _("Prefs") action ShowMenu('preferences') hover_sound hover_sound

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")

