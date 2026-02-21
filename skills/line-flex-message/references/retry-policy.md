# Reliability & Retry Policy

To ensure message delivery without duplicates, use the `X-Line-Retry-Key` header and appropriate retry logic.

## 1. X-Line-Retry-Key
- **What**: A hexadecimal UUID generated for each unique request.
- **Usage**: Include in headers for Push, Multicast, Narrowcast, and Broadcast messages.
- **Persistence**: Valid for 24 hours. Subsequent requests with the same key are blocked with `409 Conflict`.

## 2. Retry Logic by Status Code
| Status Code | Description | Action |
|-------------|-------------|--------|
| **2xx** | Success | Do not retry. |
| **409** | Conflict (Key already used) | Do not retry. The request was already accepted. |
| **5xx** / **Timeout** | Server/Network Error | **Retry**. Use exponential backoff. |
| **4xx** (except 409) | Client Error | Do not retry. Fix the request payload/auth. |

## 3. Exponential Backoff Strategy
When retrying after a 5xx or Timeout:
1. Start with a small interval (e.g., 1 second).
2. Increase the interval exponentially for each attempt (e.g., 2^n seconds).
3. Add "jitter" (random noise) to avoid thundering herd problems.

## 4. Rate Limits
A retry with a retry key counts as one API request. Monitor rate limits to avoid being throttled.
