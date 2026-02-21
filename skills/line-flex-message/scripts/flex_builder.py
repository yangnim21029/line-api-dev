import json
import uuid

def create_basic_bubble(title, body_text):
    """Creates a basic Flex Message bubble."""
    return {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [{"type": "text", "text": title, "weight": "bold", "size": "xl"}]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [{"type": "text", "text": body_text, "wrap": True}]
        }
    }

def create_carousel(bubbles):
    """Creates a carousel of bubbles."""
    return {
        "type": "carousel",
        "contents": bubbles
    }

def create_video_bubble(video_url, preview_url, title, alt_image_url):
    """Creates a Flex Message bubble with a video hero block."""
    return {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "video",
        "url": video_url,
        "previewUrl": preview_url,
        "altContent": {
          "type": "image",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "url": alt_image_url
        },
        "aspectRatio": "20:13"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [{"type": "text", "text": title, "weight": "bold", "size": "xl"}]
      }
    }

def create_product_list(products):
    """
    Creates a product list bubble using nested boxes.
    products: list of dicts with {'name': str, 'price': str, 'image': str}
    """
    contents = []
    for p in products:
        contents.append({
            "type": "box",
            "layout": "horizontal",
            "margin": "md",
            "contents": [
                {"type": "image", "url": p['image'], "size": "xs", "aspectMode": "cover", "flex": 1},
                {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 4,
                    "contents": [
                        {"type": "text", "text": p['name'], "size": "sm", "weight": "bold"},
                        {"type": "text", "text": p['price'], "size": "xs", "color": "#888888"}
                    ]
                }
            ]
        })
    
    return {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {"type": "text", "text": "Shopping List", "weight": "bold", "size": "lg"},
                {"type": "separator", "margin": "md"},
                *contents
            ]
        }
    }

def generate_retry_headers(retry_key=None):
    """Generates X-Line-Retry-Key header."""
    key = retry_key or str(uuid.uuid4())
    return {"X-Line-Retry-Key": key}

if __name__ == "__main__":
    # Example usage
    products = [
        {"name": "Brown Mug", "price": "$15.00", "image": "https://example.com/mug.png"},
        {"name": "Cony Notebook", "price": "$10.00", "image": "https://example.com/notebook.png"}
    ]
    print(json.dumps(create_product_list(products), indent=2))
