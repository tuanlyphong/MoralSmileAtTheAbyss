init python:
    phone_notify = False  # Set to True when you want the icon to appear
    chat_partner = {
        "name": "Yuka",
        "status": "Online",
        "icon": "images/chat_partner_icon.png"
    }

    if not hasattr(persistent, "messages"):
        persistent.messages = []


    def add_player_message(content):
        persistent.messages.append({"sender": "player", "content": content})
        
    def add_other_message(content):
        persistent.messages.append({"sender": "other", "content": content})
    default_messages = []

    # If messages already exist in persistent, load them
    if not hasattr(persistent, "messages"):
        persistent.messages = default_messages

    def reset_messages():
        persistent.messages = default_messages

    def trigger_phone_notification():
        """Set phone_notify to True when a new message is received."""
        global phone_notify
        phone_notify = True  # This would be triggered when you get a new message

    def reset_phone_notification():
        """Reset the notification once the phone screen is opened."""
        global phone_notify
        phone_notify = False  # Reset to False after the player clicks to open the phone screen



screen phone_icon_screen():
    # Check if there's a phone notification
    if phone_notify:
        # Display the phone icon with notification
        imagebutton:
            idle "phone_icon_notifh"  # Image when idle
            hover "phone_icon_notif"  # Image when hovered
            xpos 300
            ypos 980
            action Show("phone_screen")  # Show the phone screen when clicked
    else:
        # No phone icon if no notification
        pass



screen phone_screen():
    frame:
        xalign 0.5
        yalign 0.2
        xsize 500
        ysize 855
        background "images/phone_background.png"

        frame:
            xalign 0.489
            yalign 0.15
            xsize 410
            ysize 80
            background "#537d90"

            hbox:
                spacing 10
                xalign 0
                yalign 0.5
                image chat_partner["icon"] size (50, 50)

                vbox:
                    text chat_partner["name"] size 22 color "#ffffff" bold True
                    text chat_partner["status"] size 16 color "#90EE90"

        frame:
            xalign 0.489
            yalign 0.7
            xsize 410
            ysize 567
            background "images/message_screen.png"

            viewport:
                draggable True
                mousewheel True
                vbox:
                    spacing 10
                    for message in persistent.messages:
                        hbox:
                            spacing 10
                            if message["sender"] == "player":
                                spacing 10
                                xalign 1.0
                                frame:
                                    background Frame("images/player_bubble.png", 10, 10)
                                    xpadding 10
                                    ypadding 5
                                    text message["content"] size 20 color "#ffffff"
                            else:
                                image "images/sender_icon.png" xalign 0.0 yalign 0.5
                                frame:
                                    background Frame("images/sender_bubble.png", 10, 10)
                                    xpadding 10
                                    ypadding 5
                                    text message["content"] size 20 color "#ffffff"

        imagebutton:
            idle "images/phonebutton.png"
            hover "images/phonebuttonh.png"
            xpos 400
            ypos 130
            action [
                Hide("phone_screen"),  # Hide the phone screen
                Hide("phone_icon_screen"),  # Hide the phone icon screen
                Function(reset_phone_notification)  # Reset the notification
            ]

        imagebutton:
            xpos 350
            ypos 130
            idle "images/video_call_icon.png"
            hover "images/video_call_icon_hover.png"
            action Function(add_player_message,"Video call started!")  # Trigger add_message when clicked

        imagebutton:
            xpos 300
            ypos 130
            idle "images/phone_call_icon.png"
            hover "images/phone_call_icon_hover.png"
            action Function(reset_messages)


