---
name: line-rich-menu
description: "Expert guide for creating and managing LINE Rich Menus. This skill covers the Messaging API for creating, uploading, and linking rich menus to users or setting them as default. Use when a user needs to: (1) Create a new rich menu for a LINE bot, (2) Implement tab switching (pagination) on rich menus, (3) Link a specific rich menu to a user, (4) Manage rich menu aliases and images."
license: MIT
---

# LINE Rich Menu Skill

This skill provides specialized knowledge and workflows for creating interactive and professional Rich Menus on the LINE Platform.

## Core Capabilities

### 1. Rich Menu Management
- **Creation**: Defining the `Rich Menu Object` with tap areas and actions.
- **Image Upload**: Attaching PNG/JPG assets (up to 1MB) to a menu ID.
- **Assignment**: Setting a default menu for all users or linking specific menus to individual user IDs.
- **Aliases**: Creating and updating aliases for seamless tab switching.

### 2. Interaction & Actions
- **Actions**: URI, Postback, Message, Datetimepicker, and Rich Menu Switch.
- **Tab Switching**: Using the `richmenuswitch` action with aliases to simulate multi-page menus.

See [references/rich-menus.md](references/rich-menus.md) for detailed JSON schemas, API endpoints, and image specifications.

## Common Workflows

### Creating a Basic Rich Menu
1. **Prepare Image**: Create a 2500x1686 or 2500x843 image.
2. **Define JSON**: Create the rich menu object with bounds (x, y, width, height) for each button.
3. **Run API**: Call `POST /v2/bot/richmenu` and save the `richMenuId`.
4. **Upload Image**: Call `POST /v2/bot/richmenu/{richMenuId}/content` with the image binary.
5. **Set Default**: Call `POST /v2/bot/user/all/richmenu/{richMenuId}`.

### Implementing Tab Switching (Pagination)
1. **Create Multiple Menus**: Build Menu A and Menu B with images representing tabs.
2. **Register Aliases**: Create `alias-a` for Menu A and `alias-b` for Menu B via `POST /v2/bot/richmenu/alias`.
3. **Add Switch Action**: 
   - In Menu A's tap area: Use `type: "richmenuswitch"` with `richMenuAliasId: "alias-b"`.
   - In Menu B's tap area: Use `type: "richmenuswitch"` with `richMenuAliasId: "alias-a"`.
4. **Deploy**: Set the initial menu (e.g., Menu A) as default.

## Best Practices
- **Coordinate Calculation**: Always use the top-left corner (0,0) as the origin.
- **Display Priority**: Remember that **Per-user** settings always override the **Default** setting.
- **Security**: Never expose Channel Access Tokens in client-side code. Use server-side calls only.
