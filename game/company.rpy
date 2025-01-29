label splashscreen:
    if not persistent.content:
      play music "audio/void.ogg"
      god "{color=#FFD500}Warning{/color} This game contains references to topics such as {color=#FF0000}suicide{/color} and {color=#FF0000}trauma{/color} which some players may find distressing"
      $persistent.content = True
    
    stop music
    play sound "audio/fuyuka.ogg"
    show FuyukaLogo at highcenter
    with Dissolve(1.5)
    hide FuyukaLogo
    with Fade(1.5, 0, 0, color="#fff")
    stop sound
    if persistent.named:
       return
    else:
       jump naming


