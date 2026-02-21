# LINE Login Reference (v2.1)

## OAuth 2.1 Authorization Code Flow

### 1. Authorization Request
Redirect the user to the following URL:
`GET https://access.line.me/oauth2/v2.1/authorize`

**Parameters:**
- `response_type`: `code` (Required)
- `client_id`: Channel ID (Required)
- `redirect_uri`: Callback URL (Required, URL-encoded)
- `state`: Random string to prevent CSRF (Required)
- `scope`: `profile openid email` (Required)
- `nonce`: Random string to prevent replay attacks (Optional)
- `bot_prompt`: `normal` or `aggressive` to prompt adding bot as friend (Optional)

**Example:**
```text
https://access.line.me/oauth2/v2.1/authorize?
  response_type=code&
  client_id=1234567890&
  redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&
  state=abcde12345&
  scope=profile%20openid
```

### 2. Authorization Response
The user is redirected back to your `redirect_uri`:
`https://example.com/callback?code=AUTHORIZATION_CODE&state=abcde12345`

### 3. Issue Access Token
Exchange the code for a token:
`POST https://api.line.me/oauth2/v2.1/token`

**Headers:**
- `Content-Type: application/x-www-form-urlencoded`

**Body (Form Data):**
- `grant_type`: `authorization_code`
- `code`: The authorization code received
- `redirect_uri`: Same callback URL used in step 1
- `client_id`: Channel ID
- `client_secret`: Channel Secret

**Response:**
```json
{
  "access_token": "...",
  "expires_in": 2592000,
  "id_token": "...",
  "refresh_token": "...",
  "scope": "profile openid",
  "token_type": "Bearer"
}
```

## ID Token (JWT)
The `id_token` contains:
- `iss`: `https://access.line.me`
- `sub`: User ID
- `aud`: Channel ID
- `exp`: Expiration time
- `iat`: Issued time
- `nonce`: Same as provided in request
- `name`: Display name
- `picture`: Profile image URL
- `email`: User's email address (if scope `email` was granted)

## Token Management
- **Verify Token**: `GET https://api.line.me/oauth2/v2.1/verify?access_token={accessToken}`
- **Refresh Token**: `POST https://api.line.me/oauth2/v2.1/token` with `grant_type=refresh_token`
- **Revoke Token**: `POST https://api.line.me/oauth2/v2.1/revoke`
