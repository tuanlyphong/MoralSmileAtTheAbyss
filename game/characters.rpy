# Declare characters used by this game. The color argument colorizes the
# name of the character.
define f = Character("Fu",window_style="window",ctc="ctc_animation",who_color="#c0c0c0",ctc_position="fixed")
define y0 = Character(" Yuka ",window_style="window", who_color="#00ffff",ctc_position="fixed",ctc="ctc_animation")
define god = Character("", window_style="god")
define f0 = Character(" Fu ",window_style="window",who_color="#c0c0c0",ctc="ctc_animation", ctc_position="fixed")
define y = Character("Yuka",window_style="window",who_color="#00ffff",ctc="ctc_animation", ctc_position="fixed")
define e = Character(None, window_style="window", ctc="ctc_animation", ctc_position="fixed")
define all =  Character("???",who_color="#fff", window_style="window",ctc="ctc_animation", ctc_position="fixed")
image ctc_animation = Animation("gui/indicator0.png", 0.2,"gui/indicator1.png", 0.2, "gui/indicator2.png", 0.2, "gui/indicator3.png", 0.2, xpos=0.8, ypos=0.97, xanchor=1.0, yanchor=1.0)
define fy = Character("Fu & Yuka",window_style="window",who_color="#000",ctc="ctc_animation", ctc_position="fixed")

