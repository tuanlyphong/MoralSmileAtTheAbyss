init python:
##persistent value
    if not hasattr(persistent, "played_before"):
       persistent.played_before = False
    if not hasattr(persistent, "named"):
       persistent.named = False
    if not hasattr(persistent, "firstrun"):
       persistent.firstrun = False
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


