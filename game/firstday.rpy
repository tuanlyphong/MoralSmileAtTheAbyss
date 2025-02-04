
image room_animation:
    "bg/FuRoomEvilLoop1.png"
    0.2
    "bg/FuRoomEvilLoop2.png"
    0.1
    "bg/FuRoomEvilLoop3.png"
    0.2
    "bg/FuRoomEvilLoop4.png"
    0.3
    "bg/FuRoomEvilLoop5.png"
    0.1
    "bg/FuRoomEvilLoop6.png"
    0.2
    "bg/FuRoomEvilLoop5.png"
    0.3
    "bg/FuRoomEvilLoop4.png"
    0.2
    "bg/FuRoomEvilLoop3.png"
    0.1
    "bg/FuRoomEvilLoop2.png"
    repeat



image room_animation_effect:
    "room_animation"
    alpha 0.2 zoom 7
    xpos 0.5 ypos 4.5
    linear 2 ypos 3.0
    linear 2 alpha 1
    pause(1)
    linear 0.5 alpha 0.2 
    linear 0.5 xpos 1.2 ypos 5.5
    linear 0.5 alpha 0.4
    pause(0.8)
    linear 0.25 alpha 0.2 

    linear 0.25 xpos 0.8 ypos 4.0
    linear 0.25 alpha 0.6
    linear 6 zoom 1.3 alpha 1 xpos 0.5 ypos 1.0

image room_sad_effect:
    "FuRoomSad"
    zoom 1.3 alpha 1 xpos 0.5 ypos 1.0
    linear 2 zoom 1 alpha 1 xpos 0.5 ypos 1.0

label firstday:
    $renpy.pause(0.5)

    show room_animation_effect
    window hide  # Hide window so no dialogue is visible during animation

    play music "breathing.ogg"

    # Pause to allow animation to play. The player can skip the animation by clicking.
    $ renpy.pause(13.0,hard = True)

    window show  # Show window again after animation finishes

    f "Fucking hell..."    
    menu:
        "Take the medication":
            pass
        "Don’t take the medication":
            $ quick_menu = True
            "There’s no way I can live like this. I have to take the medicine."

    $quick_menu = False
    stop music
    play sound "takepill.ogg"
    scene black with Dissolve(2)
    show room_sad_effect with Dissolve(2)
    stop sound
    play music "emotional_sad.ogg"
    $ quick_menu = True
    e """
    I can't remember the last time I slept peacefully.

    It all started when I became fully aware of the world around me.

    Every night feels like a never-ending torment. 

    No matter how hard I try

    My body remains paralyzed, and I can't call out for help.

    When it finally seems like the nightmare is over 

    I wake up with excruciating headaches and overwhelming nausea.
    """

    if persistent.badend:
      e """
      Recently, things have got worse. 
      
      The space around feels distorted, warped 
      
      And the voices are becoming more frequent."
      """
    
    e """
    I told my parents, and the doctor prescribed me a bunch of medications with strange names.

    They are all {color=#FF0000}antidepressants{/color}.

    Each one came with a slew of side effects.

    Lately, they've given me something new, and I find myself enjoying it more than I should.

    {color=#FFA500}Morphine{/color}.

    It numbs the pain effortlessly.

    But perhaps it's expensive, and they won't give me enough to satisfy my cravings, no matter how badly I need it.
    """
    window hide  # Hide the text window for a cleaner start screen
    $ quick_menu = False
    # Initialize the flag to control phone interaction flow
    $ phone_interaction_done = False  # Set to False at the start of the interaction
    
    # Simulate a phone notification to appear (trigger the notification)
    $ trigger_phone_notification()  # This sets phone_notify to True
    stop music
    play sound "audio/notification_sound.ogg" 

    # Example conversation messages
    $ missed_calls = [
        {"sender": "other", "content": "{b}Missed audio call{/b}\n{alpha=0.5}Tap to call back{/alpha}"},
        {"sender": "other", "content": "{b}Missed audio call{/b}\n{alpha=0.5}Tap to call back{/alpha}"},
        {"sender": "other", "content": "{b}Missed audio call{/b}\n{alpha=0.5}Tap to call back{/alpha}"},
        {"sender": "other", "content": "Like how long are you planning to sleep???"},
        {"sender": "other", "content": "Wake up!,Dummy"},
        {"sender": "other", "content": "{b}Missed video call{/b}\n{alpha=0.5}Tap to call back{/alpha}"},
    ]
    $ persistent.current_messages = missed_calls  

    $ messages = []
    $ message_index = 0  # Start at the first message in the conversation
    
    # Show phone icon screen (and make sure player clicks it to proceed)
    show screen phone_icon_screen     
    # Wait for the player to complete the phone interaction before proceeding
    while not phone_interaction_done:
        $ renpy.pause(0.1)  # Keep checking if the phone interaction is complete
    $ quick_menu =True
    f "Urggh..."
    play sound "stepping.ogg"
    hide FuRoomSad with Dissolve(1)
    jump door





