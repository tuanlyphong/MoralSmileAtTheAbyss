label firstnight:
    scene Nightmare with Fade(0.1, 0, 0, color="#fff")
    play sound "nightmare1.ogg"
    $ renpy.pause(17)
    stop sound
    jump firstday

