
image room_animation:
    "bg/FuRoomEvilLoop1.png" with Dissolve(2)
    1.5
    "bg/FuRoomEvilLoop2.png" with Dissolve(2)
    1.5
    "bg/FuRoomEvilLoop3.png" with Dissolve(2)
    1.5
    "bg/FuRoomEvilLoop4.png" with Dissolve(2)
    1.5
    "bg/FuRoomEvilLoop5.png" with Dissolve(2)
    1.5
    "bg/FuRoomEvilLoop6.png" with Dissolve(2)
    1.5
    "bg/FuRoomEvilLoop5.png" with Dissolve(2)
    1.5
    "bg/FuRoomEvilLoop4.png" with Dissolve(2)
    1.5
    "bg/FuRoomEvilLoop3.png" with Dissolve(2)
    1.5
    "bg/FuRoomEvilLoop2.png" with Dissolve(2)
    repeat


image room_animationscare:
    "room_animation"
    zoom 1.1 xpos 0.5 ypos 1.0
image room_animation_effect:
    "room_animation"
    alpha 0 zoom 7
    xpos 0.5 ypos 4.5
    linear 2 alpha 0.3 ypos 3.0
    linear 2 alpha 1
    pause(1)
    linear 0.5 alpha 0.2 
    linear 0.5 xpos 1.2 ypos 5.5
    linear 0.5 alpha 0.4
    pause(0.8)
    linear 0.25 alpha 0.2 

    linear 0.25 xpos 0.8 ypos 4.0
    linear 0.25 alpha 0.6
    linear 0.5 xpos 0.3 ypos 6.0
    linear 1.0 zoom 3.0 alpha 1 xpos 0.5 ypos 1.0

image room_sad_effect:
    "FuRoomSad"
    zoom 1.3 alpha 1 xpos 0.5 ypos 1.0
    linear 2 zoom 1 alpha 1 xpos 0.5 ypos 1.0
image room_sad_effectn:
    "FuRoomSad"
    zoom 1 xpos 0.5 ypos 1.0

label firstday:
    $renpy.pause(4)

    show room_animation_effect 
    $renpy.pause(0.5)
   
    play music "Hallucinate.ogg"

    window hide  # Hide window so no dialogue is visible during animation
    $quick_menu = False


    # Pause to allow animation to play. The player can skip the animation by clicking.
    $ renpy.pause(9.0)

    window show  # Show window again after animation finishes
    $quick_menu = True
    play sound "fall.ogg"
    show room_animationscare with vpunch
    stop sound 
    hide room_animation_effect
    f """
    "ARGHHHH!!!!"
    """
    hide room_animationscare with Dissolve(0.5)
    play music "breathing.ogg"
    e """
    
    ...
    
    What the fuck is wrong with me?

    It's not my fault

    I have never asked to be born 
    """
   
    f """
    "Fuck..."
    """

    $quick_menu = False


    menu:
        "Take the {color=#FFA500}Medication{/color}":
            pass
        "Don’t take the {color=#FFA500}Medication{/color}":
            $ quick_menu = True
            e "There’s no way I can live like this. I have to take the {color=#FFA500}Medicine{/color}."

    $quick_menu = False
    stop music
    play sound "takepill.ogg"
    scene black with Dissolve(2)
    show room_sad_effect with Dissolve(2)
    $renpy.pause(1)
    hide room_sad_effect
    show room_sad_effectn
  
    stop sound
    play music "emotional_sad.ogg"
    $ quick_menu = True

    e """

    I can't remember the last time I slept peacefully.

    It all started when I became truly aware of the world around me.

    The words they've said to me—they echo in my head, refusing to fade.

    Every night feels like a never-ending torment.

    No matter how hard I try, my body remains paralyzed. I can’t move. I can’t call out for help.

    And when it finally seems like the nightmare is over...

    I wake up to a pounding headache and overwhelming nausea.

    Lately, things have only gotten worse.

    The space around me warps and bends, like reality itself is unraveling.

    I see things that aren’t there. I hear voices that won’t stop.

    They grow louder. More persistent.

    Apparently, I’ve developed a case of psychotic depression.

    This time, they didn’t just ignore it.

    They agreed to pay for medicines with names I can’t even pronounce.

    But in the end, they’re all just antidepressants.

    Each one comes with its own side effects.

    Lately, they’ve given me something new—something I enjoy more than I should.

    {color=#FFA500}Morphine{/color}.

    It washes away the pain, smooth and effortless.

    I can’t imagine living a life without it.
    
    """

    window hide  # Hide the text window for a cleaner start screen
    $ quick_menu = False
    # Initialize the flag to control phone interaction flow
    $ phone_interaction_done = False  # Set to False at the start of the interaction
    
    # Simulate a phone notification to appear (trigger the notification)
    $ trigger_phone_notification()  # This sets phone_notify to True
    stop music
    play sound "audio/notification_sound.ogg" 
    if _preferences.language == "vietnamese":
        $ missed_calls = [
            {"sender": "other", "content": "{b}Cuộc gọi nhỡ{/b}\n{alpha=0.5}Nhấn để gọi lại{/alpha}"},
            {"sender": "other", "content": "{b}Cuộc gọi nhỡ{/b}\n{alpha=0.5}Nhấn để gọi lại{/alpha}"},
            {"sender": "other", "content": "{b}Cuộc gọi nhỡ{/b}\n{alpha=0.5}Nhấn để gọi lại{/alpha}"},
            {"sender": "other", "content": "Định ngủ đến bao giờ vậy???"},
            {"sender": "other", "content": "Dậy mau, đồ đần!"},
            {"sender": "other", "content": "{b}Cuộc gọi video nhỡ{/b}\n{alpha=0.5}Nhấn để gọi lại{/alpha}"},
        ]

    else: 
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
    $ renpy.pause(1)
    e """
    
    Urgh...

    She probably got tired of waiting and left for school.

    If I don’t go, she’ll be mad.

    And by mad, I don’t mean normal mad—I mean the obnoxious, annoying kind of mad.

    I already have enough paranoid thoughts to deal with.

    Handling a real one is beyond my mental limit.

    """

    $quick_menu = False

    play sound "stepping.ogg"
    hide room_sad_effectn with Dissolve(1)
    jump door





