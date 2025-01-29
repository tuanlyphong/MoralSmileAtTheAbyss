
init python:
    import os
    import datetime
    if persistent.named is None:
        persistent.named = False
    if persistent.badend is None:
        persistent.badend = False
    if persistent.happyend is None:
        persistent.happyend = False
    if persistent.content is None:
        persistent.content = False
    if persistent.trueend is None:
        persistent.trueend = False

    if persistent.firstrun is None:
        persistent.firstrun = True

    def get_greeting():
        """Return the appropriate greeting based on the current time."""
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            return "Good morning"
        elif current_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
    hover_sound = "audio/press.ogg"    

    def delete_all_saves():
            for savegame in renpy.list_saved_games(fast=True):
                renpy.unlink_save(savegame)
