init python:
    chat_partner = {
            "name": "Yuka",
            "status": "Online",
            "icon": "images/chat_partner_icon.png"
        }

    def scroll_to_bottom():
            renpy.pause(0.1)
            renpy.scroll_to("message_viewport", 0, 1.0, duration=0)

    messages = [
            {"sender": "player", "content": "Hi, how are you?"},
            {"sender": "other", "content": "I'm good, thanks for asking!"},
            {"sender": "player", "content": "Did you finish the project?"},
            {"sender": "other", "content": "Yes, it's all done. I'll send it over now."},
            {"sender": "player", "content": "Hi, how are you?"},
            {"sender": "other", "content": "I'm good, thanks for asking!"},
            {"sender": "player", "content": "Did you finish the project?"},
            {"sender": "other", "content": "Yes, it's all done. I'll send it over now."},
            {"sender": "other", "content": "I'm good, thanks for asking!"},
            {"sender": "player", "content": "Did you finish the project?"},
            {"sender": "other", "content": "Yes, it's all done. I'll send it over now."},
            {"sender": "player", "content": "Hi, how are you?"},
            {"sender": "other", "content": "I'm good, thanks for asking!"},
            {"sender": "player", "content": "Did you finish the project?"},
            {"sender": "player", "content": "Hi, how are you?"},
            {"sender": "other", "content": "I'm good, thanks for asking!"},
            {"sender": "player", "content": "Did you finish the project?"},
            {"sender": "other", "content": "Yes, it's all done. I'll send it over now."},
            {"sender": "player", "content": "Hi, how are you?"},
            {"sender": "other", "content": "I'm good, thanks for asking!"},
            {"sender": "player", "content": "Did you finish the project?"},
 
        ]
# Phone icon and notification setup
screen phone_icon():
    if phone_notify == 0:
        # Display the phone icon (no notification) as a button
        imagebutton:
            idle "images/phone_iconh.png"  # Image when the button is idle
            hover "images/phone_icon.png"  # Image when the button is hovered
            xpos 100
            ypos 980
            action Show("phone_screen")  # Show the phone screen when clicked
    elif phone_notify == 1:
        # Display the phone icon (with notification) as a button
        imagebutton:
            idle "phone_icon_notifh.png"  # Image when the button is idle
            hover "phone_icon_notif.png"  # Image when the button is hovered
            xpos 100
            ypos 980
            action Show("phone_screen")  # Show the phone screen when clicked

screen phone_screen():
    # Phone frame with the phone background
    frame:
        xalign 0.5
        yalign 0.2
        xsize 500
        ysize 855
        background "images/phone_background.png"

        # Top bar showing chat partner information
        frame:
            xalign 0.489
            yalign 0.15
            xsize 410
            ysize 80
            background "#537d90"  # Dark gray bar

            hbox:
                spacing 10
                xalign 0
                yalign 0.5

                # Profile picture of the chat partner
                image "images/chat_partner_icon.png" size (50, 50)

                # Chat partner's name and status
                vbox:
                    text chat_partner["name"] size 22 color "#ffffff" bold True
                    text chat_partner["status"] size 16 color "#90EE90"


          # Message display area
        frame:
            xalign 0.489  # Center horizontally within the phone background
            yalign 0.7  # Center vertically within the phone background
            xsize 410
            ysize 567
            background "images/message_screen.png"

            # Scrollable message container
            viewport:
                draggable True
                mousewheel True

                vbox:
                    spacing 10
                    for message in messages:
                        hbox:
                            spacing 10
                            # Adjust based on sender (e.g., left for others, right for player)
                            if message["sender"] == "player":
                                spacing 10
                                xalign 1.0  # Align to the right
                                # Player's message bubble and icon
                                frame:
                                    background Frame("images/player_bubble.png", 10, 10)
                                    xpadding 10
                                    ypadding 5
                                    text message["content"] size 20 color "#ffffff"
                            else:
                                # Other sender's message bubble and icon
                                image "images/sender_icon.png" xalign 0.0 yalign 0.5
                                frame:
                                    background Frame("images/sender_bubble.png", 10, 10)
                                    xpadding 10
                                    ypadding 5
                                    text message["content"] size 20 color "#ffffff"

        # Close button inside the phone screen at position (400, 56)
        imagebutton:
            idle "images/phonebutton.png"  # Idle image for the button
            hover "images/phonebuttonh.png"  # Hover image for the button
            xpos 400
            ypos 130
            action Hide("phone_screen")  # Close the phone when clicked on the button

        imagebutton:
            xpos 350
            ypos 130
            idle "images/video_call_icon.png"  # Idle image for the video call button
            hover "images/video_call_icon_hover.png"
            action Hide("phone_screen")  

        imagebutton:
            xpos 300
            ypos 130
            idle "images/phone_call_icon.png"  # Idle image for the phone call button
            hover "images/phone_call_icon_hover.png"
            action Hide("phone_screen")  


