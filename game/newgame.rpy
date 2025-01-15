label start:
    window hide
    $ quick_menu = False
    stop music
    if persistent.firstrun:
        $ greeting = get_greeting()
        god "[greeting],[persistent.player_name]!"
        god "Do you have fate in humanity?"
        menu:
            "No":
                god """
                Great! 

                You came to the right place. 

                Here you can ruin someone's life without any consequences!

                Have fun!
                """
            "Yes":
                $ persistent.player = True

                god """
                Great!

                You came to the right place.

                Here you can help someone’s messed-up life become better!
                """

        "Have fun!"
        $ persistent.firstrun = False
        $ change_name_color()
        jump firstnight

    elif persistent.firstrun == 0:
        if persistent.badend == 0 and persistent.happyend == 0 and persistent.trueend == 0:
            god """
            Why, all of a sudden,[color={player_name_color}]{persistent.player_name}[/color]?

            Already regret your choices? 

            Or perhaps...

            Did you forget to save the game? 

            Or worse...

            Did you misclick???

            Do you actually want to start a new game?
            """
            menu:
                "Yes": 
                    jump firstday
                "No": 
                    return
        elif persistent.badend == 1 and persistent.happyend == 0 and persistent.trueend == 0:
            $ change_name_color()
            god "[greeting],[color={player_name_color}]{persistent.player_name}[/color]! Did you enjoy your decisions' outcome?"
            menu:
                "Yes":
                    god "Great! It’s always fun messing with people's lives, isn’t it? Perhaps you want to enjoy torturing Fu more?"
                    god "Have fun!"
                "No":
                    god "Aw, how come?"
                    god "Do you regret your choices?"
                    menu:
                        "Yes":
                            god "I see... You shouldn't have gone down this path then."
                            god "Welp, we are human after all; can't live without hypocrisy."
                            god "I'm joking,[color={player_name_color}]{persistent.player_name}[/color]."
                            god "As I said, there are no consequences."
                            god "Have fun!"
                        "No":
                            god "Oh..."
                            god "Perhaps this game isn’t as good as you expected."
                            god "Or maybe you're just tired of torturing Fu over and over again."
                            god "Have fun!"
            jump firstday

        elif persistent.happyend == 1 and persistent.badend == 0 and persistent.trueend == 0:
            $ change_name_color()      
            god "[greeting],[color={player_name_color}]{persistent.player_name}[/color]! Did you enjoy your decisionsns' outcome?"
            menu:
                "Yes":
                    god "Great! It’s always fun helping people, isn’t it? Perhaps you want to enjoy helping Fu more?"
                "No":
                    god "Great! You can always start again to explore different parts of the game. There will be no consequences! After all, it’s just a game."
            jump firstday

        elif persistent.happyend == 1 and persistent.badend == 1 and persistent.trueend == 0:
            $ change_name_color()        
            god "Interesting,[color={player_name_color}]{persistent.player_name}[/color]. Don’t you have anything better to do?"
            god """
            Life is a game with infinite choices itself. 

            You should consider entertaining yourself with various kinds of media since we have very limited time to live. 

            Don’t let others decide or limit your decisions, or you’ll end up being a game character just like Fu.
            """
            f0 "You know that I’m based on you in real life? The only difference is I have Yuka and you do not."
            god """
            ...

            What? You actually just want to play the game again?

            I understand, but don’t be too obsessed with the game.

            If you want to talk with me in person, perhap joining my discord, I’m all ear to hear your story.
            """
            $ persistent.trueend = True
            jump firstday
        
        elif persistent.happyend == 1 and persistent.badend == 1 and persistent.trueend == 1:
            $ change_name_color()
            god """
            [color={player_name_color}]{persistent.player_name}[/color], you’re actually enjoying this piece of media, aren’t you?

            If you’ve struggled enough to find this dialogue, let me tell you—I like you as a person.
            
            It's fun watching you try all the options to reach the completion of such a meaningless game.

            Congratulations! You’ve earned the respect of someone who hates everything, even himself.
            
            Enjoy yourself, my friend. Together, we’ll face the horrors of life.

            """
            
            jump credit

