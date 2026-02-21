# LIFF v2 API Reference

This reference documents the most commonly used methods of the LINE Front-end Framework (LIFF) v2 SDK.

## 1. Initialization & Environment

### `liff.init(config)`
Initializes the LIFF app. Must be called before any other LIFF API.
- **Parameters**: `config` object with `liffId` (required) and `withLoginOnExternalBrowser` (optional).
- **Return**: `Promise<void>`.
- **Usage**:
  ```javascript
  liff.init({ liffId: '1234567890-AbcdEfgh' })
    .then(() => { /* Start using API */ })
    .catch(err => console.error(err));
  ```

### `liff.ready`
A `Promise` that resolves when `liff.init()` has completed for the first time.
- **Usage**:
  ```javascript
  liff.ready.then(() => { /* Initialization complete */ });
  ```

### Environment Checks
- `liff.isInClient()`: `true` if running in LINE app.
- `liff.getOS()`: Returns `'ios'`, `'android'`, or `'web'`.
- `liff.getAppLanguage()`: Returns the language setting of the LINE app.
- `liff.getVersion()`: Returns the version of the LIFF SDK.

---

## 2. Authentication & User Profile

### `liff.login(loginConfig)`
Performs a login process (only for external browsers or LINE's in-app browser).
- **Parameters**: `loginConfig` object with `redirectUri` (optional).

### `liff.isLoggedIn()`
Checks if the user is logged in.

### `liff.getProfile()`
Gets the user's profile information.
- **Return**: `Promise<Profile>` (`userId`, `displayName`, `pictureUrl`, `statusMessage`).
- **Required Scope**: `profile`.

### `liff.getDecodedIDToken()`
Gets the decoded user's profile information from the ID token (including email).
- **Required Scope**: `openid` (and `email` for email address).
- **Usage**:
  ```javascript
  const idToken = liff.getDecodedIDToken();
  console.log(idToken.email);
  ```

### `liff.getIDToken()`
Gets the raw ID token (JWT) for server-side verification.

---

## 3. Interaction & Messages

### `liff.sendMessages(messages)`
Sends messages on behalf of the user to the current chat room.
- **Parameters**: Array of up to 5 message objects.
- **Return**: `Promise<void>`.
- **Usage**:
  ```javascript
  liff.sendMessages([{ type: 'text', text: 'Hello!' }]);
  ```

### `liff.shareTargetPicker(messages)`
Opens a picker for the user to select friends/groups and sends messages to them.
- **Return**: `Promise<object>` (contains `status`).
- **Usage**:
  ```javascript
  if (liff.isApiAvailable('shareTargetPicker')) {
    liff.shareTargetPicker([{ type: 'text', text: 'Check this out!' }]);
  }
  ```

---

## 4. Navigation & Device

### `liff.openWindow(config)`
Opens a URL in LINE's in-app browser or an external browser.
- **Parameters**: `config` object (`url`, `external`).

### `liff.scanCodeV2()`
Launches a 2D code (QR) reader and returns the result string.
- **Return**: `Promise<object>` (`value`).

### `liff.closeWindow()`
Closes the LIFF app window.

---

## 5. Context & Links

### `liff.getContext()`
Gets the current environment context (chat type, IDs).
- **Return**: `Context` object (`type`, `userId`, `utouId`, `groupId`, `roomId`, `viewType`).

### `liff.permanentLink.createUrlBy(url)`
Creates a permanent link (`https://liff.line.me/{liffId}/...`) for any page in the LIFF app.
