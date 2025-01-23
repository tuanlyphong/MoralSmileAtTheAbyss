## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(scroll=None, yinitial=0.0, spacing=0):
    style_prefix "game_menu"

    # Background centered
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    # Handle scrolling content placement
    if scroll == "vpgrid":
        vpgrid:
            cols 1
            yinitial yinitial
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            xalign 0.5  # Center vpgrid horizontally
            yalign 0.5  # Center vpgrid vertically
            spacing spacing
            transclude

    else:
        # No scrolling, just transclude directly
        transclude

    # Return button at the bottom center
    textbutton _("Return"):
        style "return_button"
        action Return()
        xalign 0.5  # Center horizontally
        yalign 1.0  # Align to the bottom
        yoffset -45  # Move it slightly up from the bottom



