init python:
    def add_next_message():
            global message_index  # Use the global variable to track message progress
            if message_index < len(messages):
                message = messages[message_index]
                if message["sender"] == "player":
                    add_player_message(message["content"])
                    renpy.sound.play("audio/SendText.ogg")

                else:
                    add_other_message(message["content"])
                    renpy.sound.play("audio/ReceiveText.ogg")
                message_index += 1  # Move to the next previous_messages
            else:
                # All messages are sent, set phone_interaction_done to True
                set_phone_interaction_done()
                reset_messages()
                # Hide the phone screen after messages are done
                renpy.hide_screen("phone_screen")  # Hide the phone screen
                renpy.hide_screen("phone_icon_screen")  # Hide the phone icon screen           
    if not hasattr(persistent, "current_messages") or persistent.current_messages is None:
        persistent.current_messages = []  # List to store current displayed messages


    def add_player_message(content):
        """Add a message from the player to the current messages."""
        persistent.current_messages.append({"sender": "player", "content": content})
        
    def add_other_message(content):
        """Add a message from the 'other' to the current messages."""
        persistent.current_messages.append({"sender": "other", "content": content})

    def reset_messages():
        """Move current messages to previous messages and reset current messages."""
        persistent.current_messages = []  # Reset current messages
    def set_phone_interaction_done():
            global phone_interaction_done
            phone_interaction_done = True  # Set phone_interaction_done to True

#managing notification
    phone_notify = False  # Set to True when you want the icon to appear
    chat_partner = {
        "name": "Yuka",
        "status": "Online",
        "icon": "images/chat_partner_icon.png"
    }

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
        imagebutton:
            idle "phone_icon_notifh"  # Image when idle
            hover "phone_icon_notif"  # Image when hovered
            xpos 300
            ypos 980
            action [
                Show("phone_screen"),  # Custom transition with 2-second duration
                Hide("phone_icon_screen"),  # Hide the phone icon screen
                Hide("phone_icon_screen"),  # Hide the phone icon screen
            ]
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
            yalign 0.61           
            xsize 410
            ysize 524
            background "images/message_screen.png"


            viewport:
                draggable True
                mousewheel True
                vbox:
                    spacing 10
                    # Keep track of the last sender to handle consecutive texting
                    $ last_sender = None
                    for message in persistent.current_messages:
                        if message["sender"] == "player":
                            # Player messages aligned to the right
                            hbox:
                                spacing 10
                                null width 130  # Spacer for alignment
                                frame:
                                    xsize 250
                                    background Frame("images/player_bubble.png", 10, 10)
                                    xpadding 10
                                    ypadding 5
                                    text message["content"] size 20 color "#ffffff"
                            $ last_sender = "player"

                        elif message["sender"] == "other":
                            # Other messages aligned to the left
                            hbox:
                                spacing 10
                                if last_sender != "other":
                                    # Show the sender icon only for new message blocks
                                    image "images/sender_icon.png" xalign 0.0 yalign 0.5
                                else:
                                    image "images/sender_icon2.png" xalign 0.0 yalign 0.5
                                frame:
                                    xsize 250
                                    background Frame("images/sender_bubble.png", 10, 10)
                                    xpadding 10
                                    ypadding 5
                                    text message["content"] size 20 color "#ffffff"
                            $ last_sender = "other"        
            
        imagebutton:
            xpos 380
            ypos 130
            idle "images/video_call_icon.png"
            hover "images/video_call_icon_hover.png"
            action Null

        imagebutton:
            xpos 330
            ypos 130
            idle "images/phone_call_icon.png"
            hover "images/phone_call_icon_hover.png"
            action Null

        imagebutton:
            idle "images/arrow_icon.png"
            hover "images/arrow_icon_hover.png"
            xpos 390
            ypos 718
            action Function(add_next_message)  # Add the next message
