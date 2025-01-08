label start:
##if persistent.firstrun:


##else:
  stop music
  y "Hi Fu"
  # Mark that the player has played the game
  $ persistent.played_before = False
  $ persistent.named = False
  $ persistent.firstrun = True
return

