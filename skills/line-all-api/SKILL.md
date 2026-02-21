---
name: line-platform
description: "Comprehensive guide for integrating with the LINE Platform. This skill covers the Messaging API (chatbots), LIFF (LINE Front-end Framework), and LINE Login. Use when a user needs to: (1) Create or manage a LINE chatbot, (2) Develop a LIFF app, (3) Implement LINE Login for a website or mobile app, (4) Work with LINE Developers Console configurations."
license: MIT
---

# LINE Platform Skill

This skill provides specialized knowledge and workflows for developing on the LINE Platform.

## Core Capabilities

### 1. Messaging API (Chatbots)
- **Webhook Handling**: Signature verification and event processing (message, follow, join, etc.).
- **Sending Messages**: Reply, Push, Multicast, and Broadcast messages.
- **Message Types**: Text, Sticker, Image, Video, Audio, Location, Flex Messages, and Templates.
- **Rich Menus**: Setting, getting, and switching per-user rich menus.
- **User Profile**: Retrieving display name and status message with user ID.

See [references/messaging-api.md](references/messaging-api.md) for detailed JSON schemas and endpoints.

### 2. LIFF (LINE Front-end Framework)
- **SDK Integration**: Using CDN or npm.
- **Initialization**: `liff.init()` and login state management.
- **Interaction**: Sending messages from LIFF, sharing content, and scanning QR codes.
- **Context**: Accessing user IDs and group IDs from the app's context.

See [references/liff.md](references/liff.md) for core SDK methods.

### 3. LINE Login
- **OAuth 2.1 Flow**: Authorization request, token exchange, and token management.
- **ID Tokens (JWT)**: Securely extracting user profiles (including email).
- **Auto Login**: Best practices for implementing auto login.

See [references/login.md](references/login.md) for the complete auth flow.

## Common Workflows

### Creating a Chatbot
1. Set up a **Provider** and **Messaging API Channel** in the [LINE Developers Console](https://developers.line.biz/console/).
2. Issue a **Channel Access Token**.
3. Register a **Webhook URL** on your server.
4. Implement **Signature Verification** (using your Channel Secret).
5. Handle incoming events (e.g., `type: "message"`) and respond using the **Reply Token**.

### Developing a LIFF App
1. Create a **LINE Login Channel**.
2. Add a **LIFF App** to the channel and get a `LIFF ID`.
3. Use the **LIFF Starter** template from `assets/liff-starter/index.html` to begin development.
4. Call `liff.init({ liffId: '...' })` as the first step in your JavaScript.
5. Use `liff.sendMessages()` to interact with the chat or `liff.getProfile()` to get user info.

## Reusable Resources

### Scripts
- `scripts/flex_builder.py`: Generates a basic Flex Message bubble JSON.

### Assets
- `assets/liff-starter/index.html`: A minimal LIFF app template.

## Important Note on Security
- **Channel Secret**: Never expose your Channel Secret in client-side code (like LIFF). Use it only on your server for signature verification.
- **Channel Access Token**: Store it securely and never commit it to source control. Use Environment Variables.
- **Signature Verification**: Always verify the `x-line-signature` header in webhooks to ensure requests come from LINE.
