
init python:
    import datetime
    if persistent.named is None:
        persistent.named = False

    if persistent.badend is None:
        persistent.badend = False

    if persistent.happyend is None:
        persistent.happyend = False

    if persistent.trueend is None:
        persistent.trueend = False

    if persistent.firstrun is None:
        persistent.firstrun = True
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
     
    config.has_autosave = False

