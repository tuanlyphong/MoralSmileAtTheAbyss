label start2:
    
    window hide
    $ quick_menu = False
    play music "audio/void.ogg"
    if persistent.firstrun:
        $ greeting = get_greeting()
        god "[greeting],[persistent.player_name]!"
        god "Do you have faith in humanity?"
        menu:
            "No":
                god """
                
                Great! 
                
                You came to the right place. 
                
                Here, you can ruin someone's life without any consequences!
                
                Have fun!
                """
            "Yes":
                god """
                
                Great!
                
                You came to the right place.
                
                Here, you can help someone’s messed-up life become better!
                
                "Have fun!"

                """
        $ persistent.firstrun = False
        jump firstnight
    else:
        if not persistent.badend and not persistent.happyend and not persistent.trueend:
            god """
            
            Why all of a sudden,[persistent.player_name]?
            
            Already regretting your choices? 
            
            Or perhaps...
            
            Did you forget to save the game? 
            
            Or worse...
            
            Did you misclick???
            
            Do you actually want to start a new game?
            """
            menu:
                "Yes":
                    $ reset_messages()
                    jump firstday
                "No": 
                    return
        elif persistent.badend and not persistent.happyend and not persistent.trueend:
            god "[greeting],{color=#ff0000}[persistent.player_name]{/color}! Did you enjoy the outcome of your decisions?"
            menu:
                "Yes":
                    god """
                    
                    Great! It’s always fun messing with people's lives, isn’t it? 
                    
                    Perhaps you want to enjoy torturing Fu more?
                    
                    Have fun!
                    """
                "No":
                    god """
                    
                    Aw, how come?
                    
                    Do you regret your choices?
                    """
                    menu:
                        "Yes":
                            god """
                            
                            I see... You shouldn't have gone down this path then.
                            
                            Welp, we are human after all; can't live without hypocrisy.
                            
                            I'm joking,[color=#ff0000]{persistent.player_name}[/color].
                            
                            As I said, there are no consequences.
                            
                            Have fun!
                            """
                        "No":
                            god """
                            
                            Oh...
                            
                            Perhaps this game isn’t as good as you expected.
                            
                            Or maybe you're just tired of torturing Fu over and over again.
                            
                            Have fun!
                            """
            $ reset_messages()
            jump firstday
        elif persistent.happyend and not persistent.badend and not persistent.trueend:
            god "[greeting],[color=#00ffff]{persistent.player_name}[/color]! Did you enjoy the outcome of your decisions?"
            menu:
                "Yes":
                    god """
                    
                    Great! It’s always fun helping people, isn’t it? 
                    
                    Perhaps you want to enjoy helping Fu more?
                    """
                "No":
                    god """
                    
                    Great! You can always start again to explore different parts of the game. 
                    
                    There will be no consequences! After all, it’s just a game.
                    """
            $ reset_messages()
            jump firstday
        elif persistent.happyend and persistent.badend and not persistent.trueend:
            god """
            
            Interesting,[color=#ffffff]{persistent.player_name}[/color]. Don’t you have anything better to do?
            
            Life is a game with infinite choices itself. 
            
            You should consider entertaining yourself with various kinds of media since we have very limited time to live. 
            
            Don’t let others decide or limit your decisions, or you’ll end up being a game character just like Fu.
            """
            f0 "You know that I’m based on you in real life? The only difference is I have Yuka and you do not."
            god """
            
            ...
            
            What? You actually just want to play the game again?
            
            I understand, but don’t be too obsessed with the game.
            
            If you want to talk with me in person, perhaps join my Discord. I’m all ears to hear your story.
            """
            $ persistent.trueend = True
            $ reset_messages()
            jump firstday
        elif persistent.happyend and persistent.badend and persistent.trueend:
            god """
            
            [color=#ffffff]{persistent.player_name}[/color], you’re actually enjoying this piece of media, aren’t you?
            
            If you’ve struggled enough to find this dialogue, let me tell you—I like you as a person.
            
            It's fun watching you try all the options to reach the completion of such a meaningless game.
            
            Congratulations! You’ve earned the respect of someone who hates everything, even himself.
            
            Enjoy yourself, my friend. Together, we’ll face the horrors of life.
            """
            $ reset_messages()
            jump credit

