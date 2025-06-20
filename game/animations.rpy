transform highcenter:
    xalign 0.5
    yalign 3

transform fly_in_bg:
    xalign 0.5  # Keep the background horizontally centered
    yalign 0.5  # Keep the background vertically centered
    xoffset -1010  # Start with the background off-screen to the left
    linear 1 xoffset 0  # Animate to the original position (xoffset 0) over 1 second

transform flash:
    alpha 1.0
    linear 0.1 alpha 0.0  # Quick fade-out of white flash


image menu_animation = Animation(
    "gui/menuanimate/frame2.png", 0.8,  # About 25% closed
    "gui/menuanimate/frame3.png", 0.2,  # Half-closed
    "gui/menuanimate/frame2.png", 0.8,  # About 25% open
)

