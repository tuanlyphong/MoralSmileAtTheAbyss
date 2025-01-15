##label nightmare2:
##    god "[greeting], [persistent.player_name]!"
##    fu " [persistent.player_name]?"
##
##    god "Are you having fun?"
##
##    menu:
##        "Yes":
##            god """
##            Great! Perhaps I should provide even more fun with a minigame.
##            """
##        "No":
##            god """
##            Aw, perhaps I could brighten you up with a minigame.
##            """
##        
##    god """
##    Let's play Russian Roulette! *gun reload sound*
##    You and 5 other precious members.
##    And of course, you get to choose your turn.
##    """
##    
##    # Show the turn choices (1 to 6)
##    menu:
##        "Turn 1":
##            # Add the corresponding action for turn 1
##            pass
##        "Turn 2":
##            # Add the corresponding action for turn 2
##            pass
##        "Turn 3":
##            # Add the corresponding action for turn 3
##            pass
##        "Turn 4":
##            # Add the corresponding action for turn 4
##            pass
##        "Turn 5":
##            # Add the corresponding action for turn 5
##            pass
##        "Turn 6":
##            # Add the corresponding action for turn 6
##            pass
##
##    god """
##    Oh yeah, since I don't want the game to last forever,
##    there will be no reloading after each turn.
##    Have fun!
##    """
##
##    # Game mechanic for when the player pulls the trigger
##    # Player's heart rate increases as their turn gets closer
##    # If shot → gunshot sound, if empty → clicking sound
##    if turn_is_player:  # When it's the player's turn
##        $ play_sound("gun_reloading")  # Play gun reload sound
##        # Add code for heart rate increase and sound effects
##
##    # If others die:
##    if others_die:
##        god "Hahaha, congrats, you won!"
##        show "censored_image.png"  # Show censor image
##        fu "[random_family_member]"  # Random family member mention
##
##    # If Fu dies:
##    if fu_dies:
##        show red_screen  # Red screen effect
##
##    # If it's the 6th turn:
##    if turn_is_6:
##        god "Oh my, that was unlucky."
##        god "Or was it well deserved?"
##        god "Since you only think of yourself..."
##
##    # If no one dies after all the turns:
##    else:
##        god "That was unlucky."
##        god "Welp, no one will remember you anyway."
#####
