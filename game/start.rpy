image worms1 = "bg/worms1.png"
image worms2 = "bg/worms2.png"
image worms3 = "bg/worms3.png"
image life = "cg/cg3.png"
image YukaTearingA:
    zoom 1.2 ypos 1.4
    "YukaTearing.png"
    pause 1.0
    "YukaTearing1.png" with Dissolve(0.4)
    pause 0.8
    "YukaTearingTalking1.png" with Dissolve(0.4)
    pause 0.6
    "YukaTearingTalking2.png" with Dissolve(0.4)
    pause 0.4
    "YukaTearing1.png" with Dissolve(0.4)
    pause 0.3
image YukaCryingA:
    zoom 1.2 ypos 1.4
    "YukaCry.png"
    pause 0.15
    "YukaCry2.png"
    pause 0.15
    "YukaCry3.png"
    pause 0.15
   
image yukaloop:
    zoom 1.2 ypos 1.4
    "frame0000.png"
    pause 0.083  # 1/12 sec
    "frame0001.png"
    pause 0.083
    "frame0002.png"
    pause 0.083
    "frame0003.png"
    pause 0.083
    "frame0004.png"
    pause 0.083
    "frame0005.png"
    pause 0.083
    "frame0006.png"
    pause 0.083
    "frame0007.png"
    pause 0.083
    "frame0008.png"
    pause 0.083
    "frame0009.png"
    pause 0.083
    "frame0010.png"
    pause 0.083
    "frame0011.png"
    pause 0.083
    "frame0012.png"
    pause 0.083
    "frame0013.png"
    pause 0.083
    "frame0014.png"
    pause 0.083
    "frame0015.png"
    pause 0.083
    repeat

image paranoid2:

   "worms1" with Fade(0.2, 0, 0, color="#fff")
   pause 0.2
   "worms2"
   "worms3" with Fade(0.2, 0, 0, color="#000")
   pause 0.2
image DownFall1 ="bg/DownFall1.png"
image DownFall2 ="bg/DownFall2.png"
image DownFall3 ="bg/DownFall3.png"
image DownFall4 ="bg/DownFall4.png"

image OutsideFuHouseMad = "bg/OutsideFuHouseMad.png"
image OutsideFuHouseMadA:
    "OutsideFuHouseMad"
    alpha 0 zoom 7
    xpos 0.5 ypos 4.5
    linear 0.3 alpha 0.3 ypos 3.0
    linear 0.2 alpha 1
    linear 0.2 alpha 0.2 
    linear 0.2 xpos 1.2 ypos 5.5
    linear 0.2 alpha 0.4
    linear 0.15 alpha 0.2 

    linear 0.15 xpos 0.8 ypos 4.0
    linear 0.15 alpha 0.6
    linear 0.2 xpos 0.3 ypos 6.0
    linear 0.4 zoom 1.0 alpha 1 xpos 0.5 ypos 1.0

image DownFallA:
      "DownFall1" with Dissolve(0.2)
      pause 0.3
      "DownFall2" with Dissolve(0.2)
      pause 0.3
      "DownFall3" with Dissolve(0.2)
      pause 0.3
      "DownFall4" with Dissolve(0.2)
      pause 0.3
image YukaSitPose = "YukaSitPose.png"
image YukaAngryHandCoverMouth ="YukaAngryHandCoverMouth.png"
image YukaSurpriseHandCoverMouth ="YukaSurpriseHandCoverMouth.png"
image OutsideFuHouse = "bg/OutsideFuHouse.png"
image OutsideFuHouse1 = "bg/OutsideFuHouse1.png"
image OutsideFuHouse2 = "bg/OutsideFuHouse2.png"
image OutsideFuHouse3 = "bg/OutsideFuHouse3.png"
image YukaConcernPoseSurprise = "YukaConcernPoseSurprise.png"
image YukaAngryBlushYellSlap = "YukaAngryBlushYellSlap.png"
image YukaSitPoseBlush = "YukaSitPoseBlush.png"
#decrease is move right,increase is move left
#                 down,                  up
#middle is xpos 0.5 ypos 1.0
image YukaSnap = "YukaSnap.png"
image YukaSnapTalking = "YukaSnapTalking.png"
image YukaSnapEyesClosedTalking = "YukaSnapEyesClosedTalking.png"
image YukaRegret = "YukaRegret.png"
image YukaSnapEyesClosedTalking = "YukaSnapEyesClosedTalking.png"
image YukaConcernPoseTalking = "YukaConcernPoseTalking.png"
image YukaConcernPoseSadTalking = "YukaConcernPoseSadTalking.png"
image YukaAngryBlushFrustrated ="YukaAngryBlushFrustrated.png" 
image YukaAngryBlushYell ="YukaAngryBlushYell.png"
image YukaRegretDull = "YukaRegretDull.png"
image YukaSadx1 = "YukaSadx1.png"
image YukaSadx2 = "YukaSadx2.png"
image YukaCalm = "YukaCalm.png"
image YukaSadEyesClosed = "YukaSadEyesClosed.png"
image YukaC:
    "YukaCalm"
    zoom 1.2 ypos 1.4
image YukaSadEC:
    "YukaSadEyesClosed" 
    zoom 1.2 ypos 1.4
image YukaProudN:
    "YukaProud"
    zoom 1.2 ypos 1.4 
image YukaProudT:
    "YukaProudTalking"
    zoom 1.2 ypos 1.4
image YukaProudA:
    "YukaProudN" with Dissolve(0.2)
    pause 0.3
    "YukaProudT" with Dissolve(0.2)
    pause 0.3 
    "YukaProudN" with Dissolve(0.2)
    pause 0.3

image YukaRD:
    "YukaRegretDull"
    zoom 1.2 ypos 1.4  
image YukaAngryBYA:
    "YukaAngryBY" with Dissolve(0.2)
    pause 0.1
    "YukaAngryBN" with Dissolve(0.2)
    pause 0.1
#POSE
image YukaR:
  "YukaRegret"
  zoom 1.2 ypos 1.4  
image YukaSD1:
  "YukaSadDull1"
  zoom 1.2 ypos 1.4  
image YukaSadT:
  "YukaSadTalking"
  zoom 1.2 ypos 1.4  
image YukaSadS:
  "YukaSadSmile"
  zoom 1.2 ypos 1.4  
image YukaSadTGS:
  "YukaSadT" with Dissolve(0.2)
  pause 0.1
  "YukaSadG" with Dissolve(0.2)
  pause 1.0 
  "YukaSadS" with Dissolve(0.2)
  pause 1.0 
image YukaSadG:
  "YukaSadGrin"
  zoom 1.2 ypos 1.4
image YukaSadTS:
  "YukaSadT" with Dissolve(0.2)
  pause 0.1
  "YukaSadS" with Dissolve(0.2)
  pause 0.1 
image YukaSadTN:
  "YukaSadT" with Dissolve(0.2)
  pause 0.1
  "YukaS1" with Dissolve(0.2)
  pause 0.2 
image YukaBL:
  "YukaBlushLaugh" 
  zoom 1.2 ypos 1.4
image YukaBLT:
  "YukaB" with Dissolve(0.2)
  pause 0.5
  "YukaBL" with Dissolve(0.2)
  pause 0.5
  "YukaB" with Dissolve(0.2)
  pause 1.0
image YukaAIS:
  "YukaAISleep"
  zoom 1.2 ypos 1.4
image YukaAIT:
  "YukaAITalking"
  zoom 1.2 ypos 1.4
image YukaAIN:
  "YukaAI"
  zoom 1.2 ypos 1.4
image YukaAISTN:
  "YukaAIS" with Dissolve(0.2)
  pause 0.5
  "YukaAIN" with Dissolve(0.2)
  pause 0.3
  "YukaAIT" with Dissolve(0.2)
  pause 0.3

image YukaSD2:
  "YukaSadDull2"
  zoom 1.2 ypos 1.4  
image YukaSadEx1:
  "YukaSadx1"
  zoom 1.2 ypos 1.4  
 
image YukaSadEx2:
  "YukaSadx2"
  zoom 1.2 ypos 1.4  
image YukaSadExA:
  "YukaSadEx1" with Dissolve(0.2)
  pause 0.1
  "YukaSadEx2" with Dissolve(0.2)
  pause 0.1
  "YukaSadEx1" with Dissolve(0.2)
  pause 0.1

image YukaSD3:
  "YukaSadDull3"
  zoom 1.2 ypos 1.4  
image YukaSadDA:
  "YukaSD1" with Dissolve(0.1)
  pause 0.1
  "YukaSD2" with Dissolve(0.1)
  pause 0.1
  "YukaSD3" with Dissolve(0.1)
  pause 0.1

image YukaS1:
  "YukaSad"
  zoom 1.2 ypos 1.4  

image YukaS2:
  "YukaSad2"
  zoom 1.2 ypos 1.4  

image YukaS3:
  "YukaSad3"
  zoom 1.2 ypos 1.4  
image YukaSadA:
  "YukaS1" with Dissolve(0.1)
  pause 0.2
  "YukaS2" with Dissolve(0.1)
  pause 0.2
  "YukaS3" with Dissolve(0.1)
  pause 0.2

image YukaAngryBYS:
  "YukaAngryBlushYellSlap"
  zoom 1.2 ypos 1.4  


image YukaAngryBY:
  "YukaAngryBlushYell"
  zoom 1.2 ypos 1.4  
image YukaAngryBF:
  "YukaAngryBlushFrustrated"
  zoom 1.2 ypos 1.4  
image YukaAngryBN:
  "YukaAngryBlush"
  zoom 1.2 ypos 1.4  
image YukaSnapN:
  "YukaSnap"
  zoom 1.2 ypos 1.4  
image YukaSnapT:
  "YukaSnapTalking"
  zoom 1.2 ypos 1.4  
image YukaSnapECT:
  "YukaSnapEyesClosedTalking"
  zoom 1.2 ypos 1.4  
image YukaSnapL:
  "YukaSnapT" with Dissolve(0.2)
  pause 0.3
  "YukaSnapECT" with Dissolve(0.2)
  pause 0.2
  "YukaSnapN" with Dissolve(0.2)
  pause 0.2
image YukaSnapA:
  "YukaSnapN" with Dissolve(0.2)
  pause 0.4
  "YukaSnapT" with Dissolve(0.2)
  pause 0.3
  "YukaSnapN" with Dissolve(0.2)
  pause 0.2
image YukaCf:
  "YukaConfused"
  zoom 1.2 ypos 1.4
image YukaCfT:
  "YukaConfusedTalking"
  zoom 1.2 ypos 1.4
image YukaCfTA:
  "YukaCf" with Dissolve(0.2)
  pause 0.2
  "YukaCfT" with Dissolve(0.2)
  pause 0.2
image YukaI:
  "YukaInsecure" 
  zoom 1.2 ypos 1.4
image YukaIT:
  "YukaInsecureTalking"
  zoom 1.2 ypos 1.4
image YukaITA:
  "YukaI" with Dissolve(0.2)
  pause 0.3
  "YukaIT" with Dissolve(0.2)
  pause 0.3
  "YukaI" with Dissolve(0.2)
  pause 0.3

image YukaExAngry:
  "YukaAngryBN" with Dissolve(0.2) 
  pause 0.3
  "YukaAngryBF" with Dissolve(0.2)
  pause 0.3
  "YukaAngryBY" with Dissolve(0.2)
  pause 0.3
  "YukaAngryBN" with Dissolve(0.2)
image YukaAngryY:
  "YukaAngryHandCoverMouth"
  zoom 1.2 ypos 1.4  # Glare
image YukaP:
  "YukaPonder"
  zoom 1.2 ypos 1.4
image YukaPEC:
  "YukaPonderEyesClosed"
  zoom 1.2 ypos 1.4
image YukaPTEC:
  "YukaPonderTalkingEyesClosed"
  zoom 1.2 ypos 1.4
image YukaPTA2:
  "YukaPT" with Dissolve(0.2)
  pause 0.3
  "YukaPTEC" with Dissolve(0.2)
  pause 0.3
  "YukaPEC" with Dissolve(0.2)
  pause 0.3
image YukaPT:
  "YukaPonderTalking"
  zoom 1.2 ypos 1.4
image YukaPTA:
  "YukaP" with Dissolve(0.2)
  pause 0.3
  "YukaPT" with Dissolve(0.2)
  pause 0.3
  "YukaP" with Dissolve(0.2)
  pause 0.3

image YukaAHCM:
  "YukaAngryHandCoverMouth"
  zoom 1.2 ypos 1.4  # Glare
image YukaSHCM:
  "YukaSurpriseHandCoverMouth"
  zoom 1.2 ypos 1.4  # Glare
image YukaSurpriseN:
  "YukaSurprise1"
  zoom 1.2 ypos 1.4
image YukaSurpriseA:
  "YukaSurpriseN" with Dissolve(0.2)
  pause 0.3
  "YukaSHCM" with Dissolve(0.2)
  pause 0.3
#ADVANCE
image Outside:
    "OutsideFuHouse1" with Dissolve(1)
    5
    "OutsideFuHouse2" with Dissolve(1)
    1
### NEGATIVE / SERIOUS EMOTIONS

# Intense emotions like anger or frustration
image YukaGlareA:  # Glare sequence animation
    "YukaGlare1" with Dissolve(0.2)
    pause 0.5
    "YukaGlare2" with Dissolve(0.2)
image YukaGlare1: 
  "YukaGlare" 
  zoom 1.2 ypos 1.4  # Glare
image YukaGlare2: 
  "YukaGlareFrown" 
  zoom 1.2 ypos 1.4  # Glare with frown
image YukaATalk:  # Angry talking sequence
    "YukaAngry1"
    pause 0.4
    "YukaAngry2" with Dissolve(0.2)
    pause 0.5
    "YukaAngry1" with Dissolve(0.2)
image YukaAngry1: 
  "YukaAngry" 
  zoom 1.2 ypos 1.4  # Angry pose
image YukaAngry2: 
  "YukaAngryTalking" 
  zoom 1.2 ypos 1.4  # Angry talking
image approach:  # Angry zoom-in effect
    "YukaAngry"
    ypos 1.2
    linear 1 zoom 1.2 ypos 1.4
image Back3: 
  "YukaAngry" 
  zoom 1.0 ypos 1.2  # Angry retreat
image Back2: 
  "YukaAngryBlush" 
  zoom 2.0 ypos 2.2 
  linear 0.5 zoom 1.0 ypos 1.2  # Angry blush

# Sadness and concern
image YukaConcernPSadZ: 
  "YukaConcernPoseSad" 
  zoom 1.3 xpos 0.7 ypos 1.2 
  linear 1 zoom 1.4 ypos 1.3  # Sad concern zoom
image YukaConcernPSadN: 
  "YukaConcernPoseSad" 
  zoom 1.4 ypos 1.3  # Static sad concern
image YukaConcernPSadT: 
  "YukaConcernPoseSadTalking" 
  zoom 1.4 ypos 1.3  # Sad concern talking
image YukaFTalk:  # Frowning talking sequence
    "YukaFrown1"
    pause 0.4
    "YukaFrown2" with Dissolve(0.2)
    pause 0.5
    "YukaFrown1" with Dissolve(0.2)
image YukaFrown1: 
  "YukaFrown" 
  zoom 1.2 ypos 1.4  # Frown
image YukaFrown2: 
  "YukaFrownTalking" 
  zoom 1.2 ypos 1.4  # Frown while talking
image YukaFrownD:
  "YukaFrownDull"
  zoom 1.2 ypos 1.4
# Surprise / Embarrassment
image YukaSurpriseBl: 
  "YukaSurprise2" 
  zoom 1.2 ypos 1.4  # Surprised Blush

image YukaSurpriseBlG: 
  "YukaSurprise3" 
  zoom 1.2 ypos 1.4  # Surprised Blush Grin
image YukaABG:
  "YukaAngryBlushGrin"
  zoom 1.2 ypos 1.4
image DontPraise:
  "YukaSurpriseBlG" with Dissolve(0.2)
  pause 0.2
  "YukaABG" with Dissolve(0.2)
  pause 0.3
image YukaSurpriseRaise:
  "YukaSurpriseN" with Dissolve(0.2)
  pause 0.3
  "YukaSurpriseBl" with Dissolve(0.2)
  pause 0.2
  "YukaSurpriseBlG" with Dissolve(0.2)
  pause 0.1
image YukaOfferHand:
  "YukaOffer" 
  zoom 1.2 ypos 1.4
image YukaPunchN:
  "YukaPunch"
  zoom 1.2 ypos 1.4
image UltraHappy:
  "YukaAngryBlushCatSmile"
  zoom 1.2 ypos 1.4
image YukaConcernPSurprise: 
  "YukaConcernPoseSurprise" 
  zoom 1.4 xpos 0.7 ypos 1.3 
  linear 0.5 zoom 1.3 ypos 1.2  # Concern Surprise
image YukaEmba:
    "YukaAngryBlush" with Dissolve(0.2)
    pause 0.6
    "YukaDere" with Dissolve(0.2)
    pause 0.4
    "YukaDereTalking" with Dissolve(0.2)
    pause 0.3
    "YukaDere" with Dissolve(0.2)
image Close2: 
  "YukaEmba" 
  zoom 2.0 ypos 2.2  # Embarrassed Close-up
image Back1: 
  "OutsideFuHouse" 
  zoom 1.5 ypos 1.5 
  linear 0.5 zoom 1.0 ypos 1.0  # Retreat animation

### NEUTRAL / MIXED EMOTIONS

# Concerned / Thoughtful
image YukaConcernP: 
  "YukaConcernPose" 
  zoom 1.3 xpos 0.7 ypos 1.2  # Concern
image YukaConcernPT: 
  "YukaConcernPoseTalking" 
  zoom 1.3 xpos 0.7 ypos 1.2  # Concern Talking

# Neutral expressions
image YukaNorm: 
  "Yuka" 
  zoom 1.2 ypos 1.4  # Neutral
image YukaLaughN:
  "YukaLaugh"
  zoom 1.2 ypos 1.4  # Neutral

image YukaNormA:  # Neutral with subtle movement
    "YukaNorm" with Dissolve(0.2)
    pause 0.4
    "YukaNormClose" with Dissolve(0.2)
    pause 0.4
    "YukaNorm" with Dissolve(0.2)
image YukaNormClose: 
  "YukaEyesClose" 
  zoom 1.2 ypos 1.4  # Neutral with eyes closed
image YukaEyesCloseS:
  "YukaEyesCloseSmile"
  zoom 1.2 ypos 1.4
### POSITIVE EMOTIONS

# Playful / Teasing
image YukaBSmile:
  "YukaBlushSmile"
  zoom 1.2 ypos 1.4
image YukaB:
  "YukaBlush"
  zoom 1.2 ypos 1.4

image YukaMock2:
    "FunnySmile" with Dissolve(0.2)
    pause 0.4
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.4
image YukaMock:
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.4
    "FunnySmile" with Dissolve(0.2)
    pause 0.4
image YukaMock3:
    "YukaLaughN" with Dissolve(0.2)
    pause 1.0
    "FunnySmile" with Dissolve(0.2)
    pause 0.4

image YukaMock:
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.4
    "FunnySmile" with Dissolve(0.2)
    pause 0.4
image YukaThugLife:  # Cocky playful sequence
    "YukaCSmile" with Dissolve(0.2)
    pause 0.3
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.4
    "YukaCSEC" with Dissolve(0.2)
image YukaDumb:  # Dumbfounded comedic sequence
    "FunnySmile" with Dissolve(0.2)
    pause 0.5
    "FunnyLaugh" with Dissolve(0.2)
    pause 0.6
    "Smug" with Dissolve(0.2)
image YukaCSEC: 
  "YukaEyesClosedCatSmile" 
  zoom 1.2 ypos 1.4  # Playful cat smile
image YukaCSmile: 
  "YukaWinkCatSmile" 
  zoom 1.2 ypos 1.4  # Wink cat smile
image YukaWinkN:
  "YukaWink"
  zoom 1.2 ypos 1.4
# Affection / Romantic / Dere
image YukaDTalk:  # Dere Talking Animation
    "YukaDere1"
    pause 0.3
    "YukaDere2" with Dissolve(0.2)
    pause 0.6
    "YukaDere1" with Dissolve(0.2)
image YukaDere1: 
  "YukaDere" 
  zoom 1.2 ypos 1.4  # Dere pose
image YukaDere2: 
  "YukaDereTalking" 
  zoom 1.2 ypos 1.4  # Dere Talking

# Happiness / Joy
image FunnySmile: 
  "YukaEyesClosedGrin" 
  zoom 1.2 ypos 1.4  # Laughing
image FunnyLaugh: 
  "YukaEyesClosedLaugh" 
  zoom 1.2 ypos 1.4  # Laughing hard
image Smug: 
  "YukaAngrySmile" 
  zoom 1.2 ypos 1.4  # Smug smile
image YukaNSmile: 
  "YukaSmile" 
  zoom 1.2 ypos 1.4  # Natural smile
image YukaNormSmile:  # Natural to Smile
    "YukaNorm" with Dissolve(0.2)
    pause 0.4
    "YukaNSmile" with Dissolve(0.2)
    pause 0.5
image YukaWake:
    "OutsideFuHouse3"
    zoom 3 xpos 0.22 ypos 2.8
image YukaSleep:
    "Outside"     
    zoom 3 xpos 0.3 ypos 1.0
    linear 6 xpos 0.22 ypos 2.8
image Close1:
    "OutsideFuHouse"
    zoom 1.5 ypos 1.5
image Out:
    "OutsideFuHouse"
    zoom 1.0 ypos 1.0
label outside:
    window hide
    $ quick_menu = False
    play sound "open.ogg"

    hide door_effect with Fade(0.5, 0, 0, color="#fff") 
    show YukaSleep with Dissolve(1)

    $ renpy.pause(4)  # Reduced from 6 seconds for better pacing
    window show
    $ quick_menu = True
    play music "morning.ogg"
     
    f "..."
    y "Mmm..."

    f "Good morning?"

    y "Mornin-"

    window hide
    $ quick_menu = False
    stop music  # Now correctly stops before transitioning to 'fight'

    show YukaWake with Dissolve(1)
    $ renpy.pause(1, hard=True)  # Ensures transition effect is noticeable

    jump fight  # Redirects to the fight scene

label fight:

    hide YukaWake
    hide YukaSleep

    # Show Yuka close-up
    show Close1 with Dissolve(0.5)
    play sound "Boom.ogg"

    show Close2 with vpunch

    $ quick_menu = True

    y "How DARE you!"
    stop sound
    play music "fun.ogg"
    hide Close1 
    hide Close2

    # Fu backs off
    show Back1
    show Back2
    e "Whoa!"

    show Back3 with Dissolve(0.5)
    window hide
    $ quick_menu = False

    hide Back2
    hide Back1
    show Out
    hide Back3
    play sound "slowappoarch.ogg"
    show approach
    $renpy.pause(1)
    stop sound
    $ renpy.pause(1, hard=True)
    $ quick_menu = True

    f "Urgh..."

    show YukaDere1 with Dissolve(0.5)
    hide approach

    show YukaDTalk
    y "Mou!"

    show YukaAngry1 with Dissolve(0.2)
    hide YukaDTalk
    hide YukaDere1

    show YukaATalk
    hide YukaAngry1
    y "What took you so long?"

    show YukaFTalk with Dissolve(0.2)
    hide YukaATalk
    y "We have school today!"

    pause 0.2  # Helps with pacing
    show YukaFTalk with Dissolve(0.2)  # Bring back YukaFTalk before she speaks
    y "Are you planning to make us late?"
    show YukaGlare2 with Dissolve(0.2)  # Add a more intense reaction
    hide YukaFTalk

    f "..."
    pause 0.5  # Small delay for natural reaction

    show YukaNormA with Dissolve(0.2)
    hide YukaGlare2
    pause 0.7  # Makes movement feel less sudden
    play sound "move.ogg"
    hide YukaNormA with moveoutright
    stop sound
    play sound "tooclose.ogg"
    show YukaConcernP with vpunch
    e "{size=60}!!!{/size}"
    y """
    "Fu?"
    """ 
    y """
    "Are you even listening?"
    """ 
    hide YukaConcernP

    show YukaConcernPSadZ
    play sound "slowappoarch.ogg"
    y """
    "You look so pale—are you okay?"
    """
    f """
    
    "..."

    "Ku{size=40}huhuhuhuhu...{/size}"

    "KuahAhahAHa!"

    "I'm TOTALLY fine!."

    "Actually, I could never feel any BETTER in my entire life!!"

    "NOW BACK OFF,WOMAN!"
    """
    play sound "smack.ogg"
    hide YukaConcernPSadZ
    show YukaConcernPSurprise with vpunch
    y """
    "Wha—!?"
    """
    f """
    "Why on earth would you sleep in front of the door like that???"
    """
    hide YukaConcernPSurprise with Dissolve(0.5)
    show YukaSurpriseBl with Dissolve(0.5)
    f """

    "Have you ever considered what people might think?"

    "What are you?"

    "A street urchin or something?"    

    """
    show YukaFrown1 with Dissolve(0.2) 
    hide YukaSurpriseBl
    $renpy.pause(0.5)
    hide YukaFrown1
    show YukaFTalk
    y """
    
    "Mou! You startled me!,Fu!" 
     
    """
    show FunnySmile with Dissolve(0.2)
    hide YukaFTalk
    show YukaDumb
    y """

    "And for your information, I am neither a 'woman' nor a street urchin!"
    
    """
    e "???"
    hide FunnySmile
    show FunnySmile with Dissolve(0.2)
    hide YukaDumb
    show YukaDumb

    y """
    "I have told you countless times—I’m {color=#43C1E6}Yuka{/color}!!!" {fast}{size=40}{color=#43C1E6}Yuka...{/color}{/size} {w=0.2}{size=30}{color=#43C1E6}Yuka...{/color}{/size} {w=0.2}{size=25}{color=#43C1E6}Yuka...{/color}{/size} {w=0.2}{size=20}{color=#43C1E6}{alpha=0.8}Yukaaaaa.....{/alpha}{/size}
    
    """
   
    e """
    She yelled at me, then immediately launched into a rant without giving me a chance to recover from shock.

    Unquestionably, the type to talk first and think later.
    
    It’s honestly impressive how every thought she has is written all over her face.
    
    Now, what in the world is she even going on about?

    And why is she looking at me with that smug face, like she just won a debate against a goldfish?

    It’s probably a bad idea to ask what’s going on inside her head, but now I’m too curious to stop myself...
    """
    
    f """

    "What’s your point even supposed to be?"

    """ 
    show YukaNorm with Dissolve(0.2)
    hide FunnySmile
    show YukaNormSmile 
    hide YukaNorm
    hide YukaDumb
    $renpy.pause(2)
    show FunnySmile with Dissolve(0.2) 
    hide YukaNormSmile
    hide YukaDumb
    show YukaDumb
    hide FunnySmile

    y """

    "The point is..."    
    
    """
    show FunnyLaugh with Dissolve(0.2)
    show YukaMock
    hide FunnyLaugh
    hide YukaDumb

    y """

    "I have a name!"

    """
    show FunnySmile with Dissolve(0.2)
    show YukaMock2
    hide FunnySmile
    hide YukaMock

    y """

    "And urchin live in the sea, don't you know?"    

    
    """
    show YukaCSmile with Dissolve(0.2)
    hide YukaMock2
    hide FunnyLaugh
    show YukaThugLife
    hide YukaCSmile
    y """

    "You’re so lacking in knowledge, Fu."    
    
    """
    show YukaLaughN with Dissolve(0.2)
    hide YukaThugLife

    show YukaMock3
    hide YukaLaughN
    show YukaEyesCloseS with Dissolve(0.2)
    hide YukaMock3
    y """

    "How naive. You’ve got so much to learn, huh?"    
    
    """

    e """
    
    I regret expecting a proper answer.

    All that effort, only to be met with ridiculous nonsense.

    It's always like this. I always make bad decisions.

    No matter how good something seems at first, it all crumbles and ends in {color=#FF0000}Suffering{/color}.

    """
    show YukaBSmile with Dissolve(0.2)
    hide YukaEyesCloseS

    e """
    If this conversation drags on any longer, I might actually catch her stupidity like a virus.

    Just like every idiot does.

    For the sake of my already weakened sanity, I need to go back to the main subject.  
    """

    show YukaB with Dissolve(0.2)
    hide YukaBSmile

    f """
    "You know you could've just knocked on the door, right?"
    """
    show YukaSurpriseN with Dissolve(0.2)
    hide YukaB
    show YukaSurpriseA
    hide YukaSurpriseN
    #show yuka shock3

    y """ 
    "Wow, Fu, your lack of awareness is astounding. Do you seriously think I’d risk becoming a suspect?"
    """
    show YukaAHCM with Dissolve(0.2)  
    hide YukaSurpriseA
    y """
    "Do you really think I have the manners to knock on someone’s door in the morning?"
    """
    
    e """
    
    Oh-ho, so this so-called Yuka dares to challenge me?
    
    She dares challenge me with nonsense? Does she not realize I have years of arguing with my own intrusive thoughts?

    A mere mortal… against a mind in ruins? Foolish!
    
    Fine. Two can play this game. If logic won’t work, I shall descend to her level and make her taste her own medicine!
    
    """


    f """
    "Well, this is entirely your fault for not calling me! It’s not rocket science to make a phone call, right?"
    """
    show YukaSurpriseN with Dissolve(0.2)
    show YukaSurpriseRaise
    hide YukaSurpriseN
    hide YukaAHCM
    y """
    
    "WHAT!?"
    
    """
    show YukaAngryBN with Dissolve(0.2) 
    hide YukaSurpriseRaise
    show YukaExAngry
    hide YukaAngryBN
    y """

    "I DID call you!!!"

    """
    show YukaSnapN with Dissolve(0.2)
    hide YukaExAngry
    show YukaSnapA
    hide YukaSnapN
    y """
    
    " Y-you absolute walnut!!"
    
    """
    e "Shit, she's losing it"
    f "Listen, I'm Sor-"
    #show yuka angry
    show YukaSnapT with Dissolve(0.2)
    hide YukaSnapA
    show YukaSnapL
    hide YukaSnapT
    y """
    "Ahh, Fu! You suddenly became like this. No wonder we failed the high school entrance exam!"
    """
    stop music    
    e """
    
    What the hell is this girl talking about? How is her failure my fault???
    
    Why the fuck is everyone like this? Always complaining and blaming everything.

    I have never asked to become like this 
    """

    show YukaAngryBN with Dissolve(0.2)
    hide YukaSnapL

    f """
    "..."
    """
    play music "Fu.ogg"
    f """
    "Tch."

    "Whatever... School is pointless anyway."
   
    "No matter which school we go to, nothing will change."
    """

    show YukaFrown1 with Dissolve(0.2)
    hide YukaAngryBN
    #show background change
    show DownFall1 behind YukaFrown1 with Dissolve(0.2)
    $renpy.pause(0.2)
    show DownFallA behind YukaFrown1
    hide DownFall1
    show YukaFrownD with Dissolve(0.5)
    hide YukaFrown1

    $renpy.pause(1.0)

    hide Out
    show DownFall4 behind YukaFrownD
    hide DownFallA

    f """
    "Haha..."

    "You think such life can become worth living if I go to a better school?"
    
    "Like a gullible pig—"
    
    "The one who swallows whatever they're fed, only to have their throat slit the moment they stop growing or become disobedient."
    """
    show YukaSD1 with Dissolve(0.2)
    hide YukaFrownD
    show YukaSadDA
    hide YukaSD1
    f """
    "All those fancy little nicknames they give…"
    
    "Hahaha, I’m literally dying thinking about it."

    "Only after they killed me once did I realize—everyone's just full of themselves."

    "I was never their ‘joy’ or their ‘pride.’ I was their future pension, their status, their hard-earned trophy!"

    "But the moment I unable to shine, I became nothing but a burden... a mistake."

    "You don’t know what it’s like—"
    """
    show YukaRD with Dissolve(0.2)
    hide YukaSadDA
    f """
    "How hard it is to wake up, to tiptoe through your own house just to avoid your own family."
    
    "To feel pain from the gut just from the thought of talking to people."

    "And even when I try to escape into sleep… they’re still haunting me."
    
    "Every night. Every damn day."

    """
    scene black with Dissolve(0.2)
    $quick_menu = False
    stop music
    play sound "worm1.ogg"
    menu:
        "Try to {color=#00ffff}Calm{/color}":
          e "..."
          $renpy.pause(3)
          jump optimistic

        "Forfeit to {color=#ff0000}Wrath{/color}":
          all """
          {color=#ff0000}"KILL YOURSELF!!!"{/color}
          """
          jump pessimistic

label optimistic:
  $quick_menu = True
  stop music
  show YukaAngryBYS
  show Out behind YukaAngryBYS with vpunch
  show YukaAngryBY
  hide YukaAngryBYS

  show YukaAngryBYA
  hide YukaAngryBY
  play sound "smack.ogg"
  y """
  "Fu! Listen to me!"
  """
  play music "fun2.ogg"
  show YukaC
  hide YukaAngryBYA

  $renpy.pause(3)
  f """
  ...
  """
  show YukaSadEx1 with Dissolve(0.1)
  hide YukaC
  show YukaSadExA

  hide YukaSadEx1
  y """
  "Why do you always focus on the negative things?"
  """
  show YukaSadEx1 with Dissolve(0.1)
  hide YukaSadExA
  show YukaSadExA
  hide YukaSadEx1
 
  y """
  "Don’t deceive yourself like that. You know your parents never got the chance to go to school, and they regret it."
  """
  hide YukaSadExA
  show YukaSadT 
  show YukaSadTS
  hide YukaSadT

  y """
  "But you are their hope. They sacrificed so much for you, whether they wanted to or not…"
  """
  show YukaFrown1 with Dissolve(0.2)
  hide YukaSadTS
  show YukaFTalk
  hide YukaFrown1
  y """
  "You’ve always been the smart, outgoing one. I admired you."
  """
  show YukaSadEC with Dissolve(0.2)
  hide YukaFTalk
  $renpy.pause(0.4)
  show YukaSadTN
  hide YukaSadEC
  y """
  "I don’t know what happen during that summer."
  """
  show YukaSadTGS
  hide YukaSadTN
  y """
  "But when people stopped talking to you, I finally had the courage to talk to you… to be your friend."
  """
  show YukaB with Dissolve(0.2)
  hide YukaSadTGS
  show YukaBLT
  hide YukaB
  y """
  "Remember the first thing you said to me?"
  """
  show YukaAngry1 with Dissolve(0.2)
  hide YukaBLT
  
  f """
  "..."
  """
  show YukaAIN with Dissolve(0.2)
  hide YukaAngry1
  show YukaAISTN
  hide YukaAIN
  
  y """
  "We are born to suffer. Doesn’t matter more or less, we all suffer."
  """
  show YukaAIN with Dissolve(0.2)
  hide YukaAISTN
  show YukaAISTN
  hide YukaAIN

  y """
  "There is no true freedom in life—we are chained by our body and our mind."
  """
  
  show YukaAIN with Dissolve(0.2)
  hide YukaAISTN
  show YukaAISTN
  hide YukaAIN

  y """
  "It’s better never to have been."
  """
  
  show FunnySmile with Dissolve(0.2)
  hide YukaAISTN
  e "Just kill me already..."

  show YukaP with Dissolve(0.2)
  hide FunnySmile
  show YukaPTA
  hide YukaP 

  y """
  "I don’t fully remember your words..."
  """
  
  show YukaCf
  hide YukaPTA
  show YukaCfTA
  hide YukaCf

  y """
  "I didn’t really get it back then."
  """
  show YukaI
  hide YukaCfTA
  show YukaITA
  hide YukaI

  y """
  "After all, Yuka’s head isn’t that great."
  """
  hide YukaITA
  show YukaBL
  show YukaBLT
  hide yukaBL
  y """
  "But as I grew up, I started to find meaning in it."
  """
  show YukaBL with Dissolve(0.2)
  hide YukaBLT
  show YukaBLT
  hide YukaBL
  y """
  "We were all innocent when we were born, but as we live, our minds and bodies begin to control us."
  """
  
  show YukaSadEC with Dissolve(0.2)
  hide YukaBLT
  $renpy.pause(0.2)
  show YukaSadTN
  hide YukaSadEC

  y """
  "We end up doing things we don’t really want to do."
  """
  show YukaSadEC with Dissolve(0.2)
  hide YukaSadTN
  show YukaSadTN
  hide YukaSadEC

  y """
  "We cling to the idea of doing the ‘right’ thing. But maybe the line between right and wrong becomes blurrier the more we grow up."
  """
  
  show YukaS1 with Dissolve(0.2)
  hide YukaSadTN
  show YukaSadA
  hide YukaS1
  y """
  "Sometimes, doing the ‘right’ thing leaves no impact, while doing the ‘wrong’ thing might actually be more right than right."
  """
  show YukaSadEx1 with Dissolve(0.2) 
  hide YukaSadA 
  show YukaSadExA
  hide YukaSadEx1
  y """
  "Mah! Thinking about it is so frustrating that people end up not wanting to choose at all. They just… do nothing."
  """
  show FunnySmile with Dissolve(0.2)
  hide YukaSadExA
  show YukaDumb
  hide FunnySmile
  y """
  "But since we already exist, it doesn’t matter if we’re right or wrong."
  """
  show FunnySmile with Dissolve(0.2)
  hide YukaDumb
  show YukaDumb
  hide FunnySmile
  y """
  "What matters is whether we make a choice or not."
  """
  show FunnySmile with Dissolve(0.2)
  hide YukaDumb
  show YukaDumb
  hide FunnySmile
  y """
  " We can choose to accept the absurdity of life." 
  """
  show YukaCSmile with Dissolve(0.2)
  hide YukaDumb
  show YukaThugLife
  hide YukaCSmile
  y """
  "And by 'accept,' I mean to forgive life itself. Yuka believes there is one true freedom—the freedom to forgive."
  """
  show YukaSadT with Dissolve(0.2)
  hide YukaThugLife
  show YukaSadTGS
  hide YukaSadT
  y """
  "Fu… Life is full of dilemmas, but instead of staying home, isn’t it better to go to school?"
  """
  show YukaS1 with Dissolve(0.2)
  hide YukaSadTGS
  f "…"
  show YukaPT with Dissolve(0.2)
  hide YukaS1
  show YukaPTA2
  hide YukaPT
  y """
  "Besides, if you didn’t go to school, we never would have become friends. 
  """
  show YukaProudN with Dissolve(0.2)
  hide YukaPTA2
  show YukaProudA
  hide YukaProudN
  y """
  "And befriending someone as intelligent as me is a blessing!"
  """
  show YukaCSmile with Dissolve(0.2)
  hide YukaProudA
  show YukaThugLife
  hide YukaCSmile
 
  y """
  "I can help you overcome your anger issues."
  """
  show YukaNorm with Dissolve(0.2)
  hide YukaThugLife
  show YukaCSmile with Dissolve(0.2)
  hide YukaNorm
  e """
  This girl, calling herself intelligent… Just how delusional is she?
  
  And I don’t think my condition can be summarized as just ‘anger issues.’
  """
  show YukaAngry1 with Dissolve(0.2)
  hide YukaCSmile
  show YukaATalk with Dissolve(0.2)
  hide YukaAngry1
  y """
  "Mou! You can’t just leave me winking like this! Say something, Fu!"
  """
  show YukaNorm with Dissolve(0.2) 
  hide YukaATalk
  f """
  "…Thank you, I guess."
  """
  show FunnySmile with Dissolve(0.2)
  hide YukaNorm
  f """
  "Besides, even though being friends with a beautiful childhood friend like Yuka is a dilemma…"
  """
  show YukaSurpriseN with Dissolve(0.2)
  hide FunnySmile
  f """

  "it’s better than having no friends at all."

  """
  show YukaSurpriseBl with Dissolve(0.2)
  hide YukaSurpriseN
  y """
  "Mah!"
  """
  show YukaSurpriseBlG with Dissolve(0.2)   
  hide YukaSurpriseBl
  show DontPraise
  hide YukaSurpriseBlG
 
  y """
  "Don’t praise me like that! It’s not like it makes me happy or anything…"
  """
  show UltraHappy with Dissolve(0.2)  
  hide DontPraise
  e """
  I still can’t tell if she’s smart or not… but her words are worth considering.
  """
  show Smug with Dissolve(0.2)  
  hide UltraHappy
  y """
  "Stop overthinking things. Let’s go to school, okay?"
  """
  
  f """
  "…Okay."
  """
  show YukaOfferHand with Dissolve(0.2)
  hide Smug
  y """
  "Mou, come on, we are gonna be late."
  """
  hide YukaOfferHand
  show YukaPunchN with vpunch
  play sound "smack.ogg"

  y """
  "Why would you offer me your bag? You stupid tsundere!."
  """
  scene cg1 with Fade(0.3, 0, 0, color="#fff")
  $ persistent.cg1 = True
  play sound "move.ogg"
  f """
  "Fine!, let's go then."
  """
  
  e """

  She has already embarrassing me by sleeping in front of the house
  
  procceed messing with my head and hit me a couple time along with it.

  I don't want to get in any further headache,

  the best move here is just throw the tantrum and do whatever she want.

  I blindly grabbed one of her hand and drag her to school in a rush.
  """
  play music "hangout.ogg"  
  scene cg2 with Fade(0.3, 0, 0, color="#fff")
  $ persistent.cg2 = True
  e """
  
  Most students went to school 

  so it's not likely I will be caught going school late 

  hand in hand with a girl.
  
  I tell her to go in first by saying lady first.

  Fortunately, She happily goes in

  which actually helps me get out of the trouble of being mistaken as a part of a delinquent couple.

  I can already imagine her putting on this ridiculous expression for the whole day. 

  This is the reason why I don’t like to take the L even if I just pretend to. 

  People tend to think they are in control and standing on top of the world after they achive something. 

  I hate it so much to think that in the past I’m one of them. 
  """
  
  scene black with Dissolve(3)
  $renpy.pause(1.5)
  stop music
  jump happyending
label pessimistic:
  play sound "worm.ogg"
  show worms1 with Fade(0.3, 0, 0, color="#fff")
  show paranoid2  
  $renpy.pause(0.5)
  hide paranoid2
  play sound "skybreak.ogg"
  show yukaloop
  play music "Wrath.ogg"
  show OutsideFuHouseMadA behind yukaloop
  $ quick_menu = True

  all """
  {color=#ff0000} "Ψɧ@†? ₣น, ¥◎น—"{/color}
  """
  
  f """
  " GET THE FUCK AWAY FROM ME!"
  
  " DON’T TOUCH ME!"
  """
  
  show YukaTearingA 
  hide yukaloop with Dissolve(0.25)
  $renpy.pause(1.2)
  stop music

  e "Fuck,no..."
  hide YukaTearingA
  show YukaCryingA
  y "..."
  $ quick_menu = False

  scene black with Dissolve(0.2)
  play sound "runaway.ogg"
  y "You better go to school or I’m gonna beat you up!"
  $renpy.pause(13)
  stop sound
  $ quick_menu = True

  play music "suffer.ogg"
  scene DownFall2 with Dissolve(0.3)
  f "You don’t understand me, every single morning, like waking up in hell.." 
  scene cg3 with Fade(0.3, 0, 0, color="#fff")
  $ persistent.cg3 = True
  f """
  House price is unreasonably high

  If I work my entire life I still coundln’t afford one...

  Living with 5 other people in such a narrow space 

  No private room at this age…
  """
  
  $renpy.pause(5)
  e"""

  Why do I have to be so selfish… 
  
  Children out there been missing 
  
  Perphaps being killed in most unimaginable ways 
  
  Everyone...
  
  Doesn’t matter race, age, gender 
  
  Suffer more than I can imagine 
  
  And I’m standing here wining… 
  
  ...

  I’m so worthless...
  
  Why in such a world contains only suffering 
  
  Why people still forced to exist…
  """

  $renpy.pause(5)
  e"""
  Why we are all born to addicted to something… 
  
  Addiction never been a good state
  """

  $renpy.pause(5)

  e"""
  I better go to school and apology

  After all relationships exist to pass pain to others. 
  
  I can endure my pain
  
  And perhaps the pain of others
  
  But I don't want to pass it on.

  """
  
  $renpy.pause(3)
  
  e """
  Today will be the last day...

  Welp, I'm out of medication anyway...
  """
  scene black with Dissolve(3)
  $renpy.pause(1.5)
  stop music
  jump badending


