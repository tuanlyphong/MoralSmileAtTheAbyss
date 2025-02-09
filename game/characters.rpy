# Declare characters used by this game. The color argument colorizes the
# name of the character.
define f = Character("Fu",window_style="window",ctc="ctc_animation",who_color="#c0c0c0")
define y0 = Character(" Yuka ",window_style="window", who_color="#00ffff",ctc="ctc_animation")
define god = Character("", window_style="god")
define f0 = Character(" Fu ",window_style="window",who_color="#c0c0c0",ctc="ctc_animation")
define y = Character("Yuka",window_style="window",who_color="#00ffff",ctc="ctc_animation" )
define e = Character(None, window_style="window", ctc="ctc_animation")
define all =  Character("???",who_color="#fff", window_style="window")
image ctc_animation = Animation("gui/indicator0.png", 0.2,"gui/indicator1.png", 0.2, "gui/indicator2.png", 0.2, "gui/indicator3.png", 0.2, xpos=0.9, ypos=1.3, xanchor=1.0, yanchor=1.0)

