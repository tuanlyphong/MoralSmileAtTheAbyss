label firstday:
    $renpy.pause(0.5)
    show room_animation with Fade(0.1,0,0, color = "#fff")
    play music "breathing.ogg"

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
    show FuRoomSad with Dissolve(2)
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

    return




