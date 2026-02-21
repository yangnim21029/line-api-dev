# Messaging API Reference

## Webhook Event Object

Every webhook request contains a JSON body with a `destination` (bot's user ID) and an array of `events`.

### Common Event Structure
```json
{
  "type": "message",
  "message": {
    "type": "text",
    "id": "...",
    "text": "Hello, world!"
  },
  "timestamp": 1625061600000,
  "source": {
    "type": "user",
    "userId": "U..."
  },
  "replyToken": "nH7wFpWujUuCq9S...",
  "mode": "active",
  "webhookEventId": "...",
  "deliveryContext": {
    "isRedelivery": false
  }
}
```

### Event Types
- `message`: User sent a message (text, image, video, audio, location, sticker).
- `unsend`: User unsent a message.
- `follow`: User added the bot as a friend.
- `unfollow`: User blocked the bot.
- `join`: Bot joined a group/room.
- `leave`: Bot left a group/room.
- `memberJoined`: User joined a group/room where the bot is.
- `memberLeft`: User left a group/room where the bot is.
- `postback`: User triggered a postback action (e.g., from a button).
- `videoViewingComplete`: User finished watching a video message.
- `beacon`: User entered/left a beacon range.
- `accountLink`: User linked their account.

### Source Types
- `user`: `userId`
- `group`: `groupId`, `userId` (optional)
- `room`: `roomId`, `userId` (optional)

## Sending Messages

### Endpoints
- **Reply**: `POST https://api.line.me/v2/bot/message/reply`
- **Push**: `POST https://api.line.me/v2/bot/message/push`
- **Multicast**: `POST https://api.line.me/v2/bot/message/multicast`
- **Broadcast**: `POST https://api.line.me/v2/bot/message/broadcast`

### Message Objects

#### Text Message
```json
{
  "type": "text",
  "text": "Hello, world!"
}
```

#### Sticker Message
```json
{
  "type": "sticker",
  "packageId": "446",
  "stickerId": "1988"
}
```

#### Image Message
```json
{
  "type": "image",
  "originalContentUrl": "https://example.com/original.jpg",
  "previewImageUrl": "https://example.com/preview.jpg"
}
```

#### Flex Message
```json
{
  "type": "flex",
  "altText": "This is a Flex Message",
  "contents": {
    "type": "bubble",
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "Hello, Flex!"
        }
      ]
    }
  }
}
```

## User Profile API
`GET https://api.line.me/v2/bot/profile/{userId}`

Returns:
```json
{
  "displayName": "LINE Botto",
  "userId": "U...",
  "pictureUrl": "https://...",
  "statusMessage": "Hello world!"
}
```
