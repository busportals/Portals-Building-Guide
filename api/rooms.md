# Rooms

Endpoints for creating, duplicating, configuring, and reading/writing room data.

## Create Room

Creates a new room from a template.

```
POST /api/v2/rooms/create
```

### Headers

```
x-access-key: your-access-key
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `templateName` | string | Yes | Template to create from (see list below) |
| `customTemplateName` | string | No | Custom name for the room |

### Available Templates

`art-gallery`, `blank`, `conference-center`, `conference-stage`, `Cowboy-saloon`, `large-apartment`, `large-art-gallery`, `large-city-district`, `lecture-hall`, `medium-apartment-1`, `medium-city-district`, `small-apartment-1`, `small-city-district`, `spaceship`, `studio-apartment-1`, `studio-apartment-2`, `tropical-paradise`, `volcano-park`

### Response

```json
{
  "roomId": "8d4cbf13-625f-4b90-9050-6884cd514e6a",
  "name": "My Room"
}
```

### Example

```bash
curl -X POST https://theportal.to/api/v2/rooms/create \
  -H "Content-Type: application/json" \
  -H "x-access-key: your-access-key" \
  -d '{"templateName": "blank", "customTemplateName": "My Game"}'
```

---

## Duplicate Room

Duplicates an existing room with all items, settings, tasks, and quests.

```
POST /api/v2/rooms/duplicate
```

### Headers

```
x-access-key: your-access-key
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `roomId` | string | Yes | Room ID to duplicate |

### Response

```json
{
  "newRoomId": "fc77aeca-56cd-4de6-a3dd-33559be0eb07",
  "name": "My Room (Copy)"
}
```

### Example

```bash
curl -X POST https://theportal.to/api/v2/rooms/duplicate \
  -H "Content-Type: application/json" \
  -H "x-access-key: your-access-key" \
  -d '{"roomId": "8d4cbf13-625f-4b90-9050-6884cd514e6a"}'
```

---

## Update Room Settings

Updates display settings for a room. All fields except `RoomID` are optional — only include the fields you want to change.

```
POST /api/v2/room/update-room-settings
```

### Headers

```
x-access-key: your-access-key
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `RoomID` | string | Yes | Room ID to update |
| `Name` | string | No | Room name |
| `Description` | string | No | Room description |
| `Image` | string | No | Cover image URL |
| `room.HideNameOnLoadingScreen` | boolean | No | Hide room name on loading screen |
| `room.LoadingImages` | string[] | No | Array of loading screen image URLs |

> **Note:** These are display/metadata settings only. For room environment settings (physics, lighting, UI, etc.), use [room data upload](room-data-format.md) with the `settings` object.

### Example

```bash
curl -X POST https://theportal.to/api/v2/room/update-room-settings \
  -H "Content-Type: application/json" \
  -H "x-access-key: your-access-key" \
  -d '{
    "RoomID": "8d4cbf13-625f-4b90-9050-6884cd514e6a",
    "Name": "Escape Room",
    "Description": "A puzzle adventure game"
  }'
```

---

## Download Room Data

Downloads the complete room data as a binary JSON buffer.

```
GET /api/v2/mcp/download-room-data
```

### Headers

```
x-room-id: your-room-id
x-access-key: your-access-key
```

### Response

Binary data (JSON buffer). Parse it as JSON to get the room data object.

The response follows the [Room Data Format](room-data-format.md):

```json
{
  "roomItems": { ... },
  "settings": { ... },
  "roomTasks": { "Tasks": [] },
  "quests": { ... },
  "logic": { ... }
}
```

### Example

```bash
curl -X GET https://theportal.to/api/v2/mcp/download-room-data \
  -H "x-room-id: 8d4cbf13-625f-4b90-9050-6884cd514e6a" \
  -H "x-access-key: your-access-key" \
  -o room-data.json
```

---

## Upload Room Data

Uploads room data from a publicly accessible JSON URL. This **replaces** all room data — items, settings, quests, and logic.

```
POST /api/v2/mcp/upload-room-data-url
```

### Headers

```
x-room-id: your-room-id
x-access-key: your-access-key
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `jsonUrl` | string | Yes | Public URL of the room data JSON file |

### Workflow

This is a two-step process:

1. **Upload your JSON file** to get a public URL (use [Generate JSON Upload URL](assets.md#generate-json-upload-url))
2. **Call this endpoint** with that URL to apply the data to your room

### Example

```bash
# Step 1: Get a signed upload URL
UPLOAD_RESPONSE=$(curl -s -X POST https://theportal.to/api/v2/utils/generate-json-upload-url \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-access-key" \
  -d '{"fileName": "room-data.json"}')

SIGNED_URL=$(echo $UPLOAD_RESPONSE | jq -r '.signedUploadURL')
ASSET_URL=$(echo $UPLOAD_RESPONSE | jq -r '.assetURL')

# Step 2: PUT your JSON data to the signed URL
curl -X PUT "$SIGNED_URL" \
  -H "Content-Type: application/json" \
  -d @room-data.json

# Step 3: Apply the uploaded JSON to your room
curl -X POST https://theportal.to/api/v2/mcp/upload-room-data-url \
  -H "Content-Type: application/json" \
  -H "x-room-id: 8d4cbf13-625f-4b90-9050-6884cd514e6a" \
  -H "x-access-key: your-access-key" \
  -d "{\"jsonUrl\": \"$ASSET_URL\"}"
```

> **Important:** Always download existing room data before uploading. Uploads replace the **entire** room — any data not included in your upload will be lost.
