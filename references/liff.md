# LIFF (LINE Front-end Framework) Reference

## Integration

### CDN (Fixed Version)
```html
<script src="https://static.line-scdn.net/liff/edge/versions/2.22.3/sdk.js"></script>
```

### npm
```bash
npm install @line/liff
```
```javascript
import liff from '@line/liff';
```

## Core Methods

### Initialization
```javascript
liff.init({
  liffId: 'YOUR_LIFF_ID', // e.g., '1234567890-AbcdEfgh'
  withLoginOnExternalBrowser: true, // Optional
})
.then(() => {
  // Start using LIFF SDK
})
.catch((err) => {
  console.error(err);
});
```

### Login & Status
- `liff.isLoggedIn()`: Returns `true` if the user is logged in.
- `liff.login()`: Starts the login process.
- `liff.logout()`: Logs out the user.
- `liff.isInClient()`: Returns `true` if running inside LINE app.

### User Data
- `liff.getProfile()`: Returns display name, user ID, profile image URL, status message.
- `liff.getAccessToken()`: Returns the access token.
- `liff.getIDToken()`: Returns the raw ID token (JWT).
- `liff.getDecodedIDToken()`: Returns decoded profile information (name, email, etc.).

### Context & Environment
- `liff.getContext()`: Returns `type` (utou, group, room, none), `userId`, `groupId`, `roomId`, `viewType` (compact, tall, full).
- `liff.getOS()`: returns 'ios', 'android', or 'web'.
- `liff.getLanguage()`: returns the language setting of the LINE app.

### Interaction
- `liff.sendMessages([{ type: 'text', text: 'Hello' }])`: Sends a message to the current chat (only in-app).
- `liff.shareTargetPicker([{ type: 'text', text: 'Hello' }])`: Opens a picker to select friends/groups to send a message.
- `liff.openWindow({ url: '...', external: true })`: Opens a URL in the browser.
- `liff.scanCodeV2()`: Launches the 2D code reader.
- `liff.closeWindow()`: Closes the LIFF app.

## Best Practices
1. **Initialize on Every Page**: `liff.init()` must be called on every page of the LIFF app.
2. **Handle Redirects**: `liff.init()` should be completed before any URL manipulations.
3. **Check Capabilities**: Use `liff.isApiAvailable()` to check if a feature (like `shareTargetPicker`) is available on the current OS/version.
