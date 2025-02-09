label company:
    play sound "audio/fuyuka.ogg"
    show FuyukaLogo at highcenter
    with Dissolve(1.5)
    hide FuyukaLogo
    with Fade(1.5, 0, 0, color="#fff")
    stop sound
    if not persistent.content:
        play music "audio/void.ogg"
        
        god """
        {color=#FFD500}Warning{/color}: This game contains references to {color=#FF0000}Suicide{/color}, {color=#FF0000}Trauma{/color}, and other distressing themes. It also includes {color=#FF0000}Flashing lights{/color}, {color=#FF0000}Gore{/color}, and intense scenes that may not be suitable for all players. Player discretion is advised.     
        """
        
        god "Proceed?"

        menu:
            "Yes":
                $ persistent.content = True
                stop music
   
                if persistent.named:
                    return
                else:
                    jump naming

            "No":
                $renpy.quit()
    else: 
      if persistent.named:
          return
      else:
          jump naming

label splashscreen:
  if persistent.nihilism and persistent.nihilism2:
    jump nihilism
  else:
    jump company
   
