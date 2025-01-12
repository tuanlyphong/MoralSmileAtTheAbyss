image room_animation:
    "bg/FuRoomEvilLoop1.png"
    1
    "bg/FuRoomEvilLoop2.png"
    1
    repeat

label start:
##if persistent.firstrun:
  # Play the nightmare scene
  stop music
  $ quick_menu = False
  #play sound "nightmare1.ogg"
  scene Nightmare
  #$ renpy.pause(17, hard = True)
  scene FuRoomEvil with Fade(0.1, 0, 0, color="#fff")
  $renpy.pause(0.5)
  show room_animation
  play music "breathing.ogg"

  menu:
      "Take the medication":
                          stop music
                          play sound "takepill.ogg"
                          $renpy.pause(4, hard = True)
                          show FuRoomSad
                          """
                          I can't remember the last time I slept peacefully.

                          It all started when I became fully aware of the world around me.

                          Every night feels like a never-ending torment. No matter how hard I try, my body remains paralyzed, and I can't call out for help.

                          When it finally seems like the nightmare is over, I wake up with excruciating headaches and overwhelming nausea.

                          I told my parents, and the doctor prescribed me a bunch of medications with strange names.

                          They all ended in "-ine" or "-pram."

                          Each one came with a slew of side effects.

                          Lately, they've given me something new, and I find myself enjoying it more than I should.

                          {color=#FFA500}Morphine{/color}

                          It numbs the pain effortlessly.

                          But it's expensive, and they won't give me enough to satisfy my cravings, no matter how badly I need it.
                          """
      "Don’t take the medication":
                          f "What were you thinking Fu, you have to take medicine to live properly, there is no choices"
                          stop music
                          play sound "takepill.ogg"
                          $renpy.pause(4, hard = True)
                          f "Every day is the same—waking up with excruciating headaches and extreme nausea."
  
##else:
##stop music
  # Mark that the player has played the game
  $ persistent.played_before = False
  $ persistent.named = False
  $ persistent.firstrun = True
return

