## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(scroll=None):
        frame:
            xalign 0.5
            yalign 0.5
            background None  # Optional, ensures no frame background
            padding (20, 20)  # Optional, adds padding around the content

            vbox:
                xpos 300
                ypos 50
                spacing 20  # Add spacing between sections for better appearance

                hbox:
                    box_wrap True

                    if renpy.variant("pc") or renpy.variant("web"):

                        vbox:
                            spacing 12

                            vbox:
                                style_prefix "radio"
                                label _("Display")
                                textbutton _("Fullscreen") action Preference("display", "fullscreen")
                                textbutton _("Windowed") action Preference("display", "window")

                    vbox:
                        style_prefix "check"
                        label _("Skip")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                    vbox:
                        style_prefix "radio"
                        label _("Language")
                        textbutton "English" action Language(None)
                        textbutton "Vietnamese" action Language("vietnamese")
                        textbutton "Japanese" action Language("japanese")
                    vbox:
                        style_prefix "radio"
                        label _("Website")

                        imagebutton:
                            idle "website_button.png"  # Normal state image
                            hover "website_button_hover.png"  # Hover state image
                            action OpenURL("https://fuyuka.netlify.app/")  # URL to open when clicked
                null height (4 * gui.pref_spacing)

                hbox:
                    style_prefix "slider"
                    box_wrap True

                    vbox:

                        label _("Text Speed")
                        bar value Preference("text speed")

                        label _("Auto-Forward Time")
                        bar value Preference("auto-forward time")

                    vbox:

                        if config.has_music:
                            label _("Music Volume")
                            hbox:
                                bar value Preference("music volume")

                        if config.has_sound:
                            label _("Sound Volume")
                            hbox:
                                bar value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)

                        if config.has_voice:
                            label _("Voice Volume")
                            hbox:
                                bar value Preference("voice volume")

                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice)

                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing
                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text


style pref_vbox:
    xsize 500
    xalign 0.5
    yalign 0.5
style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 450

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    frame:
        style "game_menu_content_frame"

        if scroll == "viewport":

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True


                side_yfill True

                vbox:
                    transclude

        elif scroll == "vpgrid":

            vpgrid:
                cols 1
                yinitial 1.0

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                transclude

        else:

            transclude



            ## Reserve space for the navigation section.
    imagebutton:
            idle "gui/return.png"  # Image when idle
            hover "gui/return_hover.png"  # Image when hovered
            action Return()  # Action to return to the previous screen
            xpos 100  # Center horizontally
            ypos 100 # Position at the bottom of the screen


    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar



style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

