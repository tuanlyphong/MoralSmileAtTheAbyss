init python:
    import datetime
##persistent value
    if not hasattr(persistent, "named"):
       persistent.named = False
    if not hasattr(persistent, "firstrun"):
       persistent.firstrun = True
    if not hasattr(persistent, "badend"):
       persistent.badend = False
    if not hasattr(persistent, "happyend"):
       persistent.happyend = False
    if not hasattr(persistent, "trueend"):
       persistent.trueend = False       
    if not hasattr(persistent, "player"):
       persistent.player = False       

##naming
    def append_letter(letter):
        if len(persistent.player_name) < 30:  # Max length of 30
            if len(persistent.player_name) == 1:
                  persistent.player_name += letter.upper()  # First letter should be capitalized
            else:
                  persistent.player_name += letter.lower()  # Remaining letters should be lowercase
    def backspace_name():
        if len(persistent.player_name) > 1:
            persistent.player_name = persistent.player_name[:-1]

    def get_greeting():
        """Return the appropriate greeting based on the current time."""
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            return "Good morning"
        elif current_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
     
    def change_name_color():
        # Check ending states and set color accordingly
        if persistent.badend == 1 and persistent.happyend == 0 and persistent.trueend == 0:
            persistent.player_name_color = "#FF0000"  # Red color
        elif persistent.happyend == 1 and persistent.badend == 0 and persistent.trueend == 0:
            persistent.player_name_color = "#00FFFF"  # Cyan color
        elif persistent.happyend == 1 and persistent.badend == 1 and persistent.trueend == 0:
            persistent.player_name_color = "#FFFFFF"  # White color
        elif persistent.happyend == 0 and persistent.badend == 0 and persistent.trueend == 0:
            # Check persistent.player and set color accordingly
            if persistent.player == 0:
                persistent.player_name_color = "#FF0000"  # Red color
            elif persistent.player == 1:
                persistent.player_name_color = "#00FFFF"  # Cyan color
            else:
                persistent.player_name_color = "#FFFFFF"  # Default to White if no match


    messages = [
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"
        "Hey, how are you?",
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"
        "Hey, how are you?",
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"
        "Hey, how are you?",
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"
        "Hey, how are you?",
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"
        "Hey, how are you?",
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"
        "Hey, how are you?",
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"
        "Hey, how are you?",
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"
        "Hey, how are you?",
        "I'm doing great! How about you?",
        "Just working on my game. 😊",
        "That's awesome! Keep it up!"

    ]

