# LINE Rich Menu API Reference

## 1. Core Object: Rich Menu Object
Every rich menu is defined by a JSON object containing its size, default state, name, and tap areas.

```json
{
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": false,
  "name": "Rich Menu Name",
  "chatBarText": "Tap to Open",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 1250,
        "height": 1686
      },
      "action": {
        "type": "uri",
        "label": "Link A",
        "uri": "https://example.com"
      }
    }
  ]
}
```

## 2. Action Types
These actions can be assigned to `areas`:
- `uri`: Opens a website or deep link.
- `postback`: Sends data to your webhook without user text.
- `message`: Sends a predefined text message as if the user typed it.
- `datetimepicker`: Opens a date/time selection UI.
- `richmenuswitch`: Switches to another rich menu using an **Alias**.

## 3. Image Requirements
- **Format**: JPEG or PNG
- **Max File Size**: 1 MB
- **Width**: 800 to 2500 pixels
- **Height**: 250 pixels or more
- **Standard Sizes**: 
  - Full: 2500 x 1686, 1200 x 810
  - Half: 2500 x 843, 1200 x 405

## 4. Common API Endpoints
All requests require `Authorization: Bearer {channel access token}`.

| Task | Method | Endpoint |
| :--- | :--- | :--- |
| Create Rich Menu | POST | `/v2/bot/richmenu` |
| Upload Image | POST | `/v2/bot/richmenu/{richMenuId}/content` |
| Set Default | POST | `/v2/bot/user/all/richmenu/{richMenuId}` |
| Link to User | POST | `/v2/bot/user/{userId}/richmenu/{richMenuId}` |
| Get List | GET | `/v2/bot/richmenu/list` |
| Delete | DELETE | `/v2/bot/richmenu/{richMenuId}` |

## 5. Tab Switching (Rich Menu Alias)
To enable tab switching:
1. Create Menu A and Menu B.
2. Set an **Alias** for each (e.g., `alias-a`, `alias-b`).
3. In Menu A, add an area with `type: richmenuswitch` targeting `alias-b`.
4. In Menu B, add an area with `type: richmenuswitch` targeting `alias-a`.
