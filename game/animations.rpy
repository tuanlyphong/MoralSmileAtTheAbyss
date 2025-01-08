transform highcenter:
    xalign 0.5
    yalign 3

transform fly_in_bg:
    xalign 0.5  # Keep the background horizontally centered
    yalign 0.5  # Keep the background vertically centered
    xoffset -1010  # Start with the background off-screen to the left
    linear 1.5 xoffset 0  # Animate to the original position (xoffset 0) over 1 second

transform fade_in:
    alpha 0.0
    linear 1 alpha 1.0  # Adjust 2.0 for a slower or faster fade-in

image menu_animation = Animation(
    "gui/menuanimate/frame1.png", 2,  # Fully open
    "gui/menuanimate/frame2.png", 0.2,  # About 25% closed
    "gui/menuanimate/frame3.png", 0.2,  # Half-closed
    "gui/menuanimate/frame2.png", 0.2,  # About 25% open
)

image play_animation = Animation(
    "gui/menuanimate/Start1.png", 0.1,
    "gui/menuanimate/Start2.png", 0.1,
)
