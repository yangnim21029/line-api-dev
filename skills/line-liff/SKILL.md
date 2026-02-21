---
name: line-liff
description: "Expert guide for developing LINE Front-end Framework (LIFF) applications. Covers SDK integration (CDN/npm), initialization, authentication (LINE Login), user profile retrieval, sending messages, and using advanced features like Share Target Picker and 2D code reader. Use when a user needs to: (1) Build a web app that runs inside LINE, (2) Get user profiles from a web page, (3) Send messages to LINE chats from a website, (4) Implement deep linking with LIFF URLs."
---

# LINE LIFF (Front-end Framework) Skill

This skill provides specialized knowledge and workflows for building applications using the LINE Front-end Framework (LIFF).

## Core Capabilities

1. **SDK Integration & Initialization**: Using CDN edge/fixed paths or `@line/liff` npm package. Proper use of `liff.init()` and `liff.ready`.
2. **Authentication & User Data**: Managing login state with `liff.login()`/`liff.logout()`, retrieving user profiles, email addresses (with `openid` scope), and friendship status.
3. **In-App Interaction**: Sending messages to the current chat room (`liff.sendMessages`) or to friends/groups via the **Share Target Picker** (`liff.shareTargetPicker`).
4. **Device Features**: Utilizing the 2D code (QR) reader (`liff.scanCodeV2`) and opening URLs in external browsers.
5. **Context & Linking**: Retrieving app context (user ID, chat type) and creating permanent links for LIFF pages.

## Common Workflows

### 1. Setting Up a LIFF App
1. Create a **LINE Login channel** in the [LINE Developers Console](https://developers.line.biz/console/).
2. Add a **LIFF app** to the channel and specify the **Endpoint URL**.
3. Integrate the SDK and call `liff.init({ liffId: "YOUR_LIFF_ID" })`.
4. Use the `liff-starter.html` template in `assets/` to begin.

### 2. Handling Authentication
1. Check login status: `if (!liff.isLoggedIn()) { liff.login(); }`.
2. Get profile: `liff.getProfile().then(profile => { ... })`.
3. For server-side verification, use `liff.getIDToken()` to get a JWT.

### 3. Sending Messages via Share Target Picker
1. Verify availability: `liff.isApiAvailable('shareTargetPicker')`.
2. Execute: `liff.shareTargetPicker([{ type: 'text', text: 'Hello!' }])`.
3. Note: Requires the "Share Target Picker" to be enabled in the Console.

## Resources

- **[LIFF API Reference](references/api.md)**: Detailed method signatures and usage examples.
- **[Development Guidelines](references/guidelines.md)**: Best practices for URLs, redirect flows, and OGP tags.
- **[LIFF Starter Template](assets/liff-starter.html)**: Minimal boilerplate for quick prototyping.

## Important Note on Security
- **Confidentiality**: Treat `access_token` and `ID token` as sensitive. Never leak them to external logging tools.
- **Endpoint Constraints**: `liff.init()` only works on URLs at or below the configured Endpoint URL.
- **Universal Links**: Use `https://liff.line.me/{liffId}` as the primary entry point for best compatibility.
