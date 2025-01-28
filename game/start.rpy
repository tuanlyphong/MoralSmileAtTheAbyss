
label start2:
    stop music
    window hide  # Hide the text window for a cleaner start screen
    $ quick_menu = False
    # Initialize the flag to control phone interaction flow
    $ phone_interaction_done = False  # Set to False at the start of the interaction
    
    # Simulate a phone notification to appear (trigger the notification)
    $ trigger_phone_notification()  # This sets phone_notify to True
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
    show screen phone_icon_screen with moveinbottom

    # Wait for the player to complete the phone interaction before proceeding
    while not phone_interaction_done:
        $ renpy.pause(0.1)  # Keep checking if the phone interaction is complete
    f "Urggh..."
    jump firstday

