label firstday:
    scene FuRoomEvil with Fade(0.1, 0, 0, color="#fff")
    $renpy.pause(0.5)
    show room_animation
    play music "breathing.ogg"

    menu:
        "Take the medication":
            pass
        "Don’t take the medication":
            $ quick_menu = True
            "There’s no way I can live like this. I have to take the medicine."

    stop music
    play sound "takepill.ogg"
    window hide
    $renpy.pause(4)
    show FuRoomSad
    play music "Sorrow.ogg"
    window show
    $ quick_menu = True
    """
    I can't remember the last time I slept peacefully.

    It all started when I became fully aware of the world around me.

    Every night feels like a never-ending torment. 

    No matter how hard I try

    My body remains paralyzed, and I can't call out for help.

    When it finally seems like the nightmare is over 

    I wake up with excruciating headaches and overwhelming nausea.
    """

    if persistent.badend:
      """
      Recently, things have got worse. 
      
      The space around feels distorted, warped 
      
      And the voices are becoming more frequent."
      """
    
    """
    I told my parents, and the doctor prescribed me a bunch of medications with strange names.

    They are all {color=#FF0000}antidepressants{/color}.

    Each one came with a slew of side effects.

    Lately, they've given me something new, and I find myself enjoying it more than I should.

    {color=#FFA500}Morphine{/color}.

    It numbs the pain effortlessly.

    But perhaps it's expensive, and they won't give me enough to satisfy my cravings, no matter how badly I need it.
    """

    f "But perhaps it's expensive, and they won't give me enough to satisfy my cravings, no matter how badly I need it."
    return

