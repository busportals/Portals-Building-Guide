# Authentication

All API endpoints require authentication via your access key. Get your key at [theportal.to/api](https://theportal.to/api).

## Verify Access Key

Validates an access key and returns the associated user ID.

```
POST /api/v2/mcp/verify-access-key
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `accessKey` | string | Yes | Your access key |

### Response

```json
{
  "data": {
    "uid": "your-firebase-uid"
  }
}
```

### Example

```bash
curl -X POST https://theportal.to/api/v2/mcp/verify-access-key \
  -H "Content-Type: application/json" \
  -d '{"accessKey": "your-access-key"}'
```

## Using Your Access Key

After verification, include your key in request headers for all subsequent API calls:

- **Room endpoints** use `x-access-key`:
  ```
  x-access-key: your-access-key
  ```

- **Asset upload endpoints** use `x-api-key`:
  ```
  x-api-key: your-access-key
  ```

Both headers accept the same key value.

## User ID

The `uid` returned from verification is your Firebase user ID. You will need this value when creating [quests](quests.md) — every quest requires a `Creator` field set to your UID.
