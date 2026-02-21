# LINE Agent Skills

A collection of specialized skills for AI coding agents to integrate with the LINE Platform. These skills provide packaged instructions, API references, and boilerplate assets to extend agent capabilities for LINE development.

Skills follow the [Agent Skills](https://skills.sh) format.

## Available Skills

### line-platform
Comprehensive guide and toolset for integrating with the LINE Platform, covering the Messaging API, LIFF, and LINE Login.

### line-liff
Expert guide for developing LINE Front-end Framework (LIFF) applications, including SDK integration, authentication, and advanced features like Share Target Picker.

**Use when:**
- Building a web app that runs inside LINE
- Getting user profiles or email addresses from a web page
- Sending messages to LINE chats from a website
- Implementing deep linking with LIFF URLs

**Capabilities covered:**
- **Messaging API**: Webhook signature verification, event handling, and complex message types (Flex, Templates).
- **LIFF**: SDK initialization, profile retrieval, and in-app interaction (sending messages, QR scanning).
- **LINE Login**: OAuth 2.1 flow implementation and ID token (JWT) verification for secure user authentication.

## Installation

To add these skills to your local environment, run:

```bash
npx skills add yangnim21029/line-api-dev
```

## Usage

Once installed, the agent will automatically activate these skills when relevant LINE development tasks are detected.

**Examples:**
- "Help me build a LINE bot that replies with a Flex Message."
- "Create a LIFF app that gets the user's profile and email."
- "How do I implement LINE Login for my Next.js website?"
- "Verify the signature of this LINE webhook request."

## Skill Structure

Each skill in this repository is organized following the standard format:

- `SKILL.md`: Core instructions and triggering metadata for the agent.
- `scripts/`: Helper scripts for automation (e.g., Flex Message builders).
- `references/`: Detailed documentation and API schemas.
- `assets/`: Starter templates and boilerplate code (e.g., LIFF starter).
