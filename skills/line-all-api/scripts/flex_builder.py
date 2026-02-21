import json

def create_basic_bubble(title, body_text):
    """
    Creates a basic Flex Message bubble.
    """
    bubble = {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": title,
                    "weight": "bold",
                    "size": "xl"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": body_text,
                    "wrap": True
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "uri",
                        "label": "Open",
                        "uri": "https://line.me"
                    }
                }
            ]
        }
    }
    return bubble

if __name__ == "__main__":
    bubble = create_basic_bubble("Hello LINE", "This is a basic Flex Message bubble created by a skill script.")
    print(json.dumps(bubble, indent=2))
