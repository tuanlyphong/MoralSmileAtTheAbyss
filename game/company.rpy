label company:
    play sound "audio/fuyuka.ogg"
    show FuyukaLogo at highcenter
    with Dissolve(1.5)
    hide FuyukaLogo
    with Fade(1.5, 0, 0, color="#fff")
    stop sound
    if not persistent.content:
        god """
        {font=fonts/RobotoCondensed-Regular.ttf}{color=#FFD500}Warning{/color}: This game contains references to {color=#FF0000}Suicide{/color}, {color=#FF0000}Trauma{/color}, and other distressing themes. It also includes {color=#FF0000}Flashing lights{/color}, {color=#FF0000}Gore{/color}, and intense scenes that may not be suitable for all players. Player discretion is advised.{/font}     
        """
        
        god "{font=fonts/RobotoCondensed-Regular.ttf}Proceed?{/font}"
#ES:More than 700 000 people die by suicide every year, which is one person every 40 seconds

        menu:
            "Yes":
                $ persistent.content = True
                stop music
                god """
                {font=fonts/RobotoCondensed-Regular.ttf}According to data from the Ministry of Health, approximately 40,000 people die by {color=#FF0000}Suicide{/color} in Vietnam each year—four times the number of fatal {color=#FF0000}traffic accidents{/color}.{/font}
                {font=fonts/RobotoCondensed-Regular.ttf}A significant proportion of them are {color=#FF0000}students{/color} and young people.{/font}

                {font=fonts/RobotoCondensed-Regular.ttf}Many still perceive these mental health conditions as signs of weakness or a lack of willpower, leading to stigma and discrimination against those who suffer from them.{/font}
                """
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
    return
  else:
    jump company
   
