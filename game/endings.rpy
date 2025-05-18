label happyending:
    $quick_menu = False
    scene black with Fade(0.3, 0, 0, color="#000")
    play music "void.ogg"

    god """
    Yay! A happy ending.

    Just kidding, lol. I'm kinda out of money for instant noodles...

    So, maybe consider sharing? It might help with the remaining story.

    It's kinda sad that the world revolves around clout,  
    but what else can I do?

    Anyway, see ya!
    """
    
    return

label badending:
    $quick_menu = False
    scene black with Fade(0.3, 0, 0, color="#000")
    play music "void.ogg"

    god """

    ...

    And then, Fu dies peacefully, leaving nothing behind.

    Everyone else continues to live happily ever after—until they die.

    They will be remembered, but not for long...

    Perhaps this is our only true ending.

    Some will be sad, some will be happy, and others will feel something in between...

    But what else can I do?

    Anyway, see ya!    
    """
    
    return
