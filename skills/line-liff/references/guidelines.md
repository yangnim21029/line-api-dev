# LIFF Development Guidelines & Best Practices

To ensure a high-quality user experience and proper functionality, follow these guidelines when developing LIFF applications.

## 1. URL Constraints & Redirects

### Endpoint URL (Primary Redirect URL)
The **Endpoint URL** is the root of your LIFF app.
- **Rule**: `liff.init()` only works on URLs that are exactly the same as the endpoint URL or at a lower level.
- **Example**: If the endpoint URL is `https://example.com/path1/`:
  - `https://example.com/path1/page1` ✅ (Guaranteed)
  - `https://example.com/path2/` ❌ (Not guaranteed)

### URL Manipulation
- **Important**: Execute any URL changes (using `window.location.replace`, `history.pushState`, etc.) **after** the `liff.init()` Promise is resolved.
- **Why**: The LIFF SDK performs initialization based on query parameters (like `liff.state`) and fragment identifiers. Manipulating the URL before initialization may break the flow.

## 2. Authentication Flow

### In-App vs. External Browser
- **LIFF Browser**: Login is automatically executed with `liff.init()`.
- **External Browser**: Use `liff.login()` to initiate the authentication process.
- **Best Practice**: Use `withLoginOnExternalBrowser: true` in `liff.init()` to automatically trigger the login process when running on an external browser.

### Token Handling
- **Security**: Treat `access_token` and `ID token` as sensitive data.
- **Server Verification**: Never send the decoded ID token (from `liff.getDecodedIDToken()`) to your server. Instead, send the raw ID token (from `liff.getIDToken()`) and verify it on the server using your **Channel Secret**.

## 3. UI/UX Considerations

### Screen Size (viewType)
- **Full**: Covers the entire screen.
- **Tall**: Covers about 75% of the screen.
- **Compact**: Covers about 50% of the screen.
- **Responsive Design**: Ensure your app layout adjusts properly to these view types.

### Title & OGP Tags
- **Header Title**: Specify the `<title>` tag in your HTML.
- **Social Sharing**: Set OGP tags (`og:title`, `og:image`, `og:description`) for the best appearance when sharing the LIFF URL in chats.

## 4. Feature Availability

### API Availability Check
Always check if an API is available in the current environment using `liff.isApiAvailable()`.
- **Example**:
  ```javascript
  if (liff.isApiAvailable('shareTargetPicker')) {
    // Show "Share" button
  }
  ```

### Environment Limitations
- **shareTargetPicker**: Only available on mobile (not on LIFF's desktop browser).
- **scanCodeV2**: Requires the "Scan QR" feature to be enabled in the LINE Developers Console.
- **closeWindow**: May not work in external browsers.

## 5. Deployment & Release

### Universal Links
Always use the format `https://liff.line.me/{liffId}` as the entry point for your LIFF app. This ensures the best compatibility across platforms and automatically triggers the correct app-opening behavior.

### Browser Compatibility
LIFF apps are web applications. However, some browser-specific features (like WebRTC for the 2D code reader) may have different levels of support. Refer to the official documentation for the latest compatibility matrix.
