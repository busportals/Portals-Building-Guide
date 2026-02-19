# Asset Uploads

Upload 3D models, images, and JSON files to the Portals CDN. All asset uploads use a **two-step process**:

1. Request a signed upload URL from the API
2. PUT the file data directly to that URL

After uploading, use the returned `assetURL` as the public reference in your room data.

> **Note:** Asset upload endpoints use the `x-api-key` header (same key as `x-access-key`).

---

## Generate JSON Upload URL

Get a signed S3 URL for uploading a JSON file (typically room data).

```
POST /api/v2/utils/generate-json-upload-url
```

### Headers

```
x-api-key: your-access-key
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `fileName` | string | Yes | Name for the JSON file |

### Response

```json
{
  "signedUploadURL": "https://s3.amazonaws.com/...",
  "assetURL": "https://cdn.theportal.to/uploads/.../room-data.json"
}
```

### Upload Flow

```bash
# 1. Get signed URL
RESPONSE=$(curl -s -X POST https://theportal.to/api/v2/utils/generate-json-upload-url \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-access-key" \
  -d '{"fileName": "room-data.json"}')

SIGNED_URL=$(echo $RESPONSE | jq -r '.signedUploadURL')
ASSET_URL=$(echo $RESPONSE | jq -r '.assetURL')

# 2. PUT the JSON data
curl -X PUT "$SIGNED_URL" \
  -H "Content-Type: application/json" \
  -d @room-data.json

# assetURL is now the public reference
echo "Uploaded to: $ASSET_URL"
```

---

## Generate GLB/GLTF Upload URL

Get a signed S3 URL for uploading a 3D model file.

```
POST /api/v2/utils/generate-gltf-upload-url
```

### Headers

```
x-api-key: your-access-key
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `fileName` | string | Yes | Name for the model file |
| `fileType` | string | Yes | `"model/gltf-binary"` |
| `enableDraco` | boolean | No | Enable Draco mesh compression |

### Response

```json
{
  "signedUploadURL": "https://s3.amazonaws.com/...",
  "assetURL": "https://cdn.theportal.to/uploads/.../model.glb",
  "objectKey": "uploads/.../model.glb"
}
```

### Upload Flow

```bash
# 1. Get signed URL
RESPONSE=$(curl -s -X POST https://theportal.to/api/v2/utils/generate-gltf-upload-url \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-access-key" \
  -d '{"fileName": "tree.glb", "fileType": "model/gltf-binary"}')

SIGNED_URL=$(echo $RESPONSE | jq -r '.signedUploadURL')
ASSET_URL=$(echo $RESPONSE | jq -r '.assetURL')

# 2. PUT the raw file data
curl -X PUT "$SIGNED_URL" \
  -H "Content-Type: model/gltf-binary" \
  --data-binary @tree.glb

# Use assetURL as the contentString for GLB items
echo "Model URL: $ASSET_URL"
```

### GLB Requirements

- **Format**: GLB (binary glTF) is strongly recommended over separate .gltf + .bin files
- **Size**: Keep models under ~15,000 triangles and 1-2 MB for good performance
- **Textures must be embedded**: GLB files that reference external texture files (e.g., `images[].uri: "Textures/colormap.png"`) will fail on the CDN. Textures must be embedded in the binary buffer using `images[].bufferView` instead of `images[].uri`.
- **Draco compression**: Optional. Reduces file size but adds client-side decompression time.

---

## Generate Image Upload URL

Get a signed S3 URL for uploading an image file.

```
POST /api/v2/utils/generate-image-upload-url
```

### Headers

```
x-api-key: your-access-key
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `roomId` | string | Yes | Room ID to associate the image with |
| `fileType` | string | Yes | `"image/jpeg"`, `"image/png"`, or `"image/gif"` |

### Response

```json
{
  "signedUploadURL": "https://s3.amazonaws.com/...",
  "assetURL": "https://cdn.theportal.to/uploads/.../image.png",
  "objectKey": "uploads/.../image.png"
}
```

### Upload Flow

```bash
# 1. Get signed URL
RESPONSE=$(curl -s -X POST https://theportal.to/api/v2/utils/generate-image-upload-url \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-access-key" \
  -d '{"roomId": "8d4cbf13-625f-4b90-9050-6884cd514e6a", "fileType": "image/png"}')

SIGNED_URL=$(echo $RESPONSE | jq -r '.signedUploadURL')
ASSET_URL=$(echo $RESPONSE | jq -r '.assetURL')

# 2. PUT the raw image data
curl -X PUT "$SIGNED_URL" \
  -H "Content-Type: image/png" \
  --data-binary @banner.png

# Use assetURL for DefaultPainting contentString, GLBSign, textures, etc.
echo "Image URL: $ASSET_URL"
```

### Supported Formats

| Format | Content-Type | Use Cases |
|--------|-------------|-----------|
| JPEG | `image/jpeg` | Photos, textures, backgrounds |
| PNG | `image/png` | UI elements, signs, textures with transparency |
| GIF | `image/gif` | Animated textures, signs |
