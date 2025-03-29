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
                {font=fonts/RobotoCondensed-Regular.ttf}More than 700 000 people die by {color=#FF0000}Suicide{/color} every year, which is one person every 40 seconds
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
  elif datetime.date.today().month == 12 and datetime.date.today().day == 24:
    jump ChristmasEve
  elif datetime.date.today().month == 12 and datetime.date.today().day == 25:
    jump Christmas
  else:
    jump company

label ChristmasEve:
    scene cg4 with Dissolve(2) 

    y """
    "Mmmh..."

    "Unbelievable, I have to spend Christmas Eve eating fries."

    "You didn't keep your promise."
    """

    f """
    "Despite being forced to make that promise..."

    "I still kept my word and brought you to a restaurant."

    "Besides, you have terrible taste in clothing while you're clearly enjoying MY fries."
    """

    y """
    "If I had money to buy new clothes, I’d be eating turkey and cake instead of fries."
    """

    f """
    "Damn you, P. Why did you make us this poor?"
    """

    god """
    "Shut up. I don't even have fries for Christmas. You motherfuckers are lucky."
    """

    god """
    Whoever is playing this game on Christmas

    Besides myself, of course

    Donate, or I’ll make these two eat fries every Christmas."
    """

    fy """
    "Great. Now we’ll never get any donations. Thanks, P."
    """

    god """
    "Don't bully your creator!"
    """


    hide cg4 with Dissolve(2)

    jump company


label Christmas:
    scene cg5 with Dissolve(2)
    god """
    "MERRY CHRISTMAS! You two... or more?"
    """

    f """
    "Probably two. Who else would even be here besides you, anyway?"
    """

    god "..."

    fy """
    "Merry Christmas, P. And to anyone else... if you exist."
    """

    god "Thank you, I will never regret creating you."
    hide scene cg5 with Dissolve(2)
    jump company
