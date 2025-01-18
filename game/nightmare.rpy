##init python:
##    import random
##
##    def shoot(current_turn, player_turn):
##        probability = 2 / current_turn
##        random_value = random.random()
##        return random_value < probability
##
##    def random_family_member():
##        family_members = ["mom", "dad", "grandpa", "grandma", "brother"]
##        return random.choice(family_members)
##
##label nightmare2:
##    god "[greeting], [persistent.player_name]!"
##    f " [persistent.player_name]?"
##    window hide
##    god "Are you having fun?"
##
##    menu:
##        "Yes":
##            god "Great! Perhaps I should provide even more fun with a minigame."
##        "No":
##            god "Aw, perhaps I could brighten you up with a minigame."
##
##    god "Let's play Russian Roulette! *gun reload sound* You and 5 other precious members. And of course, you get to choose your turn."
##
##    # Choose player's turn
##    menu:
##        "Turn 1":
##            $ persistent.player_turn = 1
##        "Turn 2":
##            $ persistent.player_turn = 2
##        "Turn 3":
##            $ persistent.player_turn = 3
##        "Turn 4":
##            $ persistent.player_turn = 4
##        "Turn 5":
##            $ persistent.player_turn = 5
##        "Turn 6":
##            $ persistent.player_turn = 6
##
##    god "Oh yeah, since I don't want the game to last forever, there will be no reloading after each turn. Have fun!"
##
##    $ persistent.current_turn = 1
##
##    while persistent.current_turn <= 6:
##        $ heartbeat(persistent.player_turn, persistent.current_turn)
##
##        if not shoot(persistent.current_turn, persistent.player_turn):
##            $ gunshot(0)
##            $ persistent.current_turn += 1
##
##        elif shoot(persistent.current_turn, persistent.player_turn) and persistent.current_turn != persistent.player_turn:
##            $ family = random_family_member()
##            $ gunshot(1)
##            
##            god "Hahaha, congrats, you won!"
##            show "censored_image.png"
##            fu "{family}?"
##            break
##
##        elif shoot(persistent.current_turn, persistent.player_turn) and persistent.current_turn == persistent.player_turn:
##            $ gunshot(1)
##            show red_screen
##
##            if persistent.current_turn == 6:
##                god "Oh my, that was unlucky."
##                god "Or was it well deserved?"
##                god "Since you only think of yourself..."
##            else:
##                god "That was unlucky."
##                god "Welp, no one will remember you anyway."
##            break
##
##    return
##
