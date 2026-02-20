# Portals API

Build and manage interactive 3D rooms programmatically.

**Base URL:** `https://theportal.to`

## Authentication

All endpoints require an access key passed as a request header. Get your key at [theportal.to/api-access](https://theportal.to/api-access).

| Header | Used by |
|--------|---------|
| `x-access-key` | Room endpoints |
| `x-api-key` | Asset upload endpoints |

Both headers accept the same key.

## Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v2/mcp/verify-access-key` | Validate access key and get user ID |

### Rooms

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v2/rooms/create` | Create a room from a template |
| POST | `/api/v2/rooms/duplicate` | Duplicate an existing room |
| POST | `/api/v2/room/update-room-settings` | Update room settings |
| GET | `/api/v2/mcp/download-room-data` | Download room data |
| POST | `/api/v2/mcp/upload-room-data-url` | Upload room data from URL |

### Asset Uploads

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v2/utils/generate-json-upload-url` | Get signed URL for JSON upload |
| POST | `/api/v2/utils/generate-gltf-upload-url` | Get signed URL for GLB/GLTF upload |
| POST | `/api/v2/utils/generate-image-upload-url` | Get signed URL for image upload |

## Room Data

Rooms are represented as JSON with five top-level keys:

```json
{
  "roomItems": {},
  "settings": {},
  "roomTasks": {"Tasks": []},
  "quests": {},
  "logic": {}
}
```

See [Room Data Format](room-data-format.md) for the complete schema.

## Room URL

After creating or updating a room, players can access it at:

```
https://theportal.to/?room={room-id}
```

## Coordinate System

- **Ground plane**: Y = 0
- **Up**: +Y
- **1x1 cube on ground**: center at Y = 0.5
- **Default rotation**: `{"x": 0, "y": 0, "z": 0, "w": 1}` (identity quaternion)
- **GLB models face +Z** in Portals

## Rate Limits

Be mindful of request frequency. Asset uploads involve S3 signed URLs, so each upload is a two-step process (request URL, then PUT data).
