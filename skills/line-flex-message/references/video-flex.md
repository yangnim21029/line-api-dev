# Creating Flex Messages with Video

The `video` component allows you to display a video in the **hero** block of a Flex Message.

## 1. Requirements
To include a video component:
- **Hero Block Only**: The hero block's `type` must be `video`.
- **Bubble Size**: The bubble `size` must be `kilo`, `mega`, or `giga`.
- **No Carousel**: The bubble containing a video **cannot** be a child of a carousel.

## 2. Component Properties
- `url`: HTTPS URL of the video file (mp4, max 200MB).
- `previewUrl`: HTTPS URL of the preview image (jpg/png, max 1MB).
- `altContent`: Content to display on LINE versions that don't support video (e.g., an `image` or `box`). **Required**.
- `aspectRatio`: Aspect ratio of the video (e.g., `20:13`, `1:1`, `16:9`).
- `action`: (Optional) A `uri` action that appears as a button (e.g., "More information") during and after playback.

## 3. Example JSON
```json
{
  "type": "bubble",
  "size": "mega",
  "hero": {
    "type": "video",
    "url": "https://example.com/video.mp4",
    "previewUrl": "https://example.com/video_preview.jpg",
    "altContent": {
      "type": "image",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "url": "https://example.com/image.jpg"
    },
    "action": {
      "type": "uri",
      "label": "More information",
      "uri": "http://example.com/"
    },
    "aspectRatio": "20:13"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Title",
        "weight": "bold",
        "size": "xl"
      }
    ]
  }
}
```

## 4. Best Practices
- **Matching Aspect Ratios**: Ensure the video file, `aspectRatio` property, and `previewUrl` image all have the same aspect ratio to avoid cropping.
- **Alt Content**: Always provide high-quality `altContent` as it's used for older LINE versions and as a fallback.
- **Auto-play**: Playback behavior depends on user settings (Wi-Fi/Mobile).
