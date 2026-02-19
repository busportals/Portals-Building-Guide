# Room Data Format

Complete reference for the JSON structure used when uploading and downloading room data via the Portals API.

This is the format returned by [Download Room Data](rooms.md#download-room-data) and expected by [Upload Room Data](rooms.md#upload-room-data).

---

## Top-Level Structure

Room data is a JSON object with five required top-level keys:

```json
{
  "roomItems": {},
  "settings": {},
  "roomTasks": { "Tasks": [] },
  "quests": {},
  "logic": {}
}
```

| Key | Type | Description |
|-----|------|-------------|
| `roomItems` | object | All items in the room, keyed by string ID. See [Room Items](#room-items). |
| `settings` | object | Room configuration (environment, physics, UI, avatars). See [Settings](settings.md). |
| `roomTasks` | object | Must be `{"Tasks": []}`. See [roomTasks](#roomtasks). |
| `quests` | object | Quest definitions, keyed by quest ID. See [Quests](quests.md). |
| `logic` | object | Per-item interaction and configuration data. Values are **JSON strings**. See [Logic](#logic). |

> **Uploads replace everything.** The upload endpoint replaces the entire room. Always download existing data first, modify it, then upload. Any data not included in your upload will be lost.

---

## Room Items

The `roomItems` object contains every item in the room. Each key is a string ID, and each value is an item object.

### Item IDs

- Keys are string integers: `"2"`, `"3"`, `"4"`, etc.
- **ID `"1"` is reserved** by the system. User-created items start at `"2"`.
- IDs must be unique within the room. When adding items, use IDs that do not conflict with existing ones.

### Base Fields

Every item shares these fields regardless of type:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `prefabName` | string | Yes | Item type identifier. See [contentString by Item Type](#contentstring-by-item-type) for all values. |
| `pos` | object | Yes | Position in world space (or local space if parented). Format: `{"x": 0, "y": 0.5, "z": 0}` |
| `rot` | object | Yes | Rotation as a quaternion. Format: `{"x": 0, "y": 0, "z": 0, "w": 1}` |
| `scale` | object | Yes | Scale multiplier. Format: `{"x": 1, "y": 1, "z": 1}` |
| `modelsize` | object | Yes | Bounding box dimensions. Always `{"x": 0, "y": 0, "z": 0}` for non-mesh items. |
| `modelCenter` | object | Yes | Bounding box center offset. Always `{"x": 0, "y": 0, "z": 0}` for non-mesh items. |
| `contentString` | string | Yes | Content URL or identifier. Varies by item type. See [contentString by Item Type](#contentstring-by-item-type). |
| `parentItemID` | integer | Yes | `0` = no parent (world space). Otherwise, the item key of the parent item. See [Parent-Child Relationships](#parent-child-relationships). |
| `placed` | boolean | Yes | Must be `true` for the item to appear in the room. |
| `locked` | boolean | Yes | Locks the item in the editor (prevents accidental moves). |
| `superLocked` | boolean | Yes | Prevents all editing of the item. |
| `interactivityType` | integer | Yes | Click behavior. `0` = none, `3` = view image. |
| `interactivityURL` | string | Yes | URL opened on click (when `interactivityType` is set). |
| `hoverTitle` | string | Yes | Tooltip title shown on hover. |
| `hoverBodyContent` | string | Yes | Tooltip body text shown on hover. |
| `ImageInteractivityDetails` | object | Yes | Image button config. Format: `{"buttonText": "", "buttonURL": ""}` or `{}`. |
| `sessionData` | string | Yes | Runtime session data. Set to `""`. |
| `instanceId` | string | Yes | Instance identifier. Set to `""`. |
| `currentEditornetId` | integer | Yes | Internal editor state. Set to `0`. |

### Example Item

```json
{
  "2": {
    "prefabName": "ResizableCube",
    "pos": {"x": 0, "y": 0.5, "z": 0},
    "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
    "scale": {"x": 2, "y": 1, "z": 2},
    "modelsize": {"x": 0, "y": 0, "z": 0},
    "modelCenter": {"x": 0, "y": 0, "z": 0},
    "contentString": "",
    "parentItemID": 0,
    "placed": true,
    "locked": false,
    "superLocked": false,
    "interactivityType": 0,
    "interactivityURL": "",
    "hoverTitle": "",
    "hoverBodyContent": "",
    "ImageInteractivityDetails": {},
    "sessionData": "",
    "instanceId": "",
    "currentEditornetId": 0
  }
}
```

---

## contentString by Item Type

The `contentString` field carries different content depending on the item's `prefabName`:

| `prefabName` | `contentString` contains | Example |
|--------------|--------------------------|---------|
| `ResizableCube` | Texture URL (optional, empty for solid color) | `""` or `"https://cdn.theportal.to/uploads/.../wood.png"` |
| `GLB` | GLB model URL | `"https://cdn.theportal.to/uploads/.../tree.glb"` |
| `GlbCollectable` | GLB URL with `?dynamic=true` query parameter | `"https://cdn.theportal.to/uploads/.../coin.glb?dynamic=true"` |
| `Destructible` | GLB model URL | `"https://cdn.theportal.to/uploads/.../crate.glb"` |
| `Portal` | Destination room UUID | `"fc77aeca-56cd-4de6-a3dd-33559be0eb07"` |
| `DefaultPainting` | Image URL | `"https://cdn.theportal.to/uploads/.../art.png"` |
| `DefaultVideo` | Video URL | `"https://example.com/video.mp4"` |
| `GLBNPC` | Avatar GLB URL | `"https://cdn.theportal.to/uploads/.../npc.glb"` |
| `9Cube` | Element type string | `"lava"`, `"hotlava"`, `"water"` |
| `Addressable` | VFX addressable path | `"FurnitureAddressables/Fire2"` |
| `Leaderboard` | Leaderboard model URL | (from fixed set of leaderboard GLBs) |
| `Chart` | Solana token address | `"PRTL..."` |
| `GLBSign` | Billboard image URL | `"https://cdn.theportal.to/uploads/.../sign.png"` |
| `SpawnPoint` | Empty | `""` |
| `WorldText` | Empty (text content is in logic) | `""` |
| `Trigger` | Empty | `""` |
| `Light` | Empty | `""` |
| `SpotLight` | Empty | `""` |
| `BlinkLight` | Empty | `""` |
| `JumpPad` | Empty | `""` |
| `Gun` | Empty | `""` |
| `Shotgun` | Empty | `""` |
| `PlaceableTV` | Empty | `""` |
| `CameraObject` | Empty | `""` |

> For item types where `contentString` is empty, all configuration lives in the [logic](#logic) entry for that item.

---

## Logic

The `logic` object holds all per-item interaction data and type-specific configuration. This data is **not** embedded inside items in `roomItems` — it lives in a separate top-level key.

### Structure

Each key in `logic` is an item ID (matching a key in `roomItems`). Each value is a **JSON string** — not a raw object.

```json
{
  "logic": {
    "2": "{\"Tasks\":[],\"ViewNodes\":[],\"col\":\"FF0000\",\"e\":0.5}",
    "3": "{\"Tasks\":[],\"ViewNodes\":[],\"text\":\"Hello World\",\"fs\":2}"
  }
}
```

When you parse a logic value, you get an object like this:

```json
{
  "Tasks": [],
  "ViewNodes": [],
  "col": "FF0000",
  "e": 0.5
}
```

### Logic Object Fields

| Field | Type | Description |
|-------|------|-------------|
| `Tasks` | array | Interaction subscriptions (triggers and effects). See [Interactions](interactions.md). |
| `ViewNodes` | array | Always `[]`. Reserved for internal use. |
| *(type-specific)* | varies | Configuration fields that depend on the item's `prefabName`. See [Item Types](item-types.md). |

### Key Rules

- Logic values **must be JSON strings**, not raw objects. The value for each key is a string produced by `JSON.stringify()` (or equivalent).
- The `Tasks` array holds all trigger/effect subscriptions for the item. See [Interactions](interactions.md) for the full task format.
- `ViewNodes` should always be an empty array `[]`.
- Type-specific fields (like `col` for cube color, `text` for WorldText, `c` for light color) also live inside the logic entry.
- Items that have no logic data can be omitted from the `logic` object entirely.

### Common Type-Specific Logic Fields

These are the most commonly used fields found inside logic entries. For complete per-type schemas, see [Item Types](item-types.md).

**ResizableCube:**
```json
{"Tasks": [], "ViewNodes": [], "col": "FF0000", "e": 0.5, "c": true}
```
- `col` — color as 6-character hex (no `#` prefix). Example: `"FF0000"` for red.
- `e` — emission intensity. `0` = no glow, `0.5` = moderate glow, `1.0` = full glow.
- `c` — collider enabled. `true` = solid (default), `false` = passthrough.

**WorldText:**
```json
{"Tasks": [], "ViewNodes": [], "text": "<b>Title</b>", "fs": 3, "fc": "FFFFFF", "bb": true}
```
- `text` — text content. Supports basic HTML tags like `<b>`, `<i>`, `<color>`, `<size>`.
- `fs` — font size.
- `fc` — font color as 6-character hex.
- `bb` — billboard mode. `true` = text always faces camera.

**Light / SpotLight / BlinkLight:**
```json
{"Tasks": [], "ViewNodes": [], "c": "FFAA00", "i": 2.0, "r": 10}
```
- `c` — light color as 6-character hex. Note: this is `"c"` (not `"col"` like cubes).
- `i` — intensity.
- `r` — range.

**Trigger:**
```json
{"Tasks": [], "ViewNodes": []}
```
- Trigger zones are invisible. All behavior comes from the `Tasks` array.

**JumpPad:**
```json
{"Tasks": [], "ViewNodes": [], "f": 15}
```
- `f` — launch force.

---

## roomTasks

The `roomTasks` field must always be present with the following structure:

```json
{
  "roomTasks": {
    "Tasks": []
  }
}
```

> **This is critical.** Setting `roomTasks` to `{}` (empty object) will break room loading. Even if the room has no room-level tasks, the `Tasks` key with an empty array is required.

---

## Settings

The `settings` object controls the room environment, physics, UI, avatars, and camera. It has two layers:

1. **Top-level fields** — basic room config (`roomBase`, `isNight`, `chatDisabled`, etc.)
2. **`roomSettingsExtraData`** — a JSON **string** containing a nested configuration object with movement, fog, bloom, camera states, UI toggles, and more.

```json
{
  "settings": {
    "roomBase": "BlankScene",
    "isNight": false,
    "chatDisabled": false,
    "roomSettingsExtraData": "{\"showNameTags\":true,\"movementValues\":{\"runSpeed\":4.0}}"
  }
}
```

Note that `roomSettingsExtraData` is itself a JSON string, not a raw object. You must parse it to read its contents and stringify it before uploading.

For the complete settings schema, see [Settings](settings.md).

---

## Quests

The `quests` object defines interactive state machines that drive animations, visibility changes, and game logic. Quests are stored as a flat dictionary keyed by quest ID.

Each logical quest consists of **two entries** — one with `"Status": "inProgress"` and one with `"Status": "completed"` — sharing the same `EntryId` but with different `id` values.

```json
{
  "quests": {
    "mlhab7cd3efg12": {
      "EntryId": "07b29300-f6df-47e4-8f55-5aa697303896",
      "Name": "0_open_door",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "",
      "Creator": "your-firebase-uid",
      "id": "mlhab7cd3efg12"
    },
    "mlhxy9z2klmn45": {
      "EntryId": "07b29300-f6df-47e4-8f55-5aa697303896",
      "Name": "0_open_door",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "",
      "Creator": "your-firebase-uid",
      "id": "mlhxy9z2klmn45"
    }
  }
}
```

Key facts:
- Quest IDs follow the pattern `mlh` + 11-14 lowercase alphanumeric characters.
- Quest names **must** use the numbered format: `"0_name"`, `"1_name"`, `"2_name"`, etc.
- The `Description` field must always be `"created in unity"` (required fixed value).
- The `Creator` field must be the authenticated user's Firebase UID (returned by [Verify Access Key](authentication.md#verify-access-key)).
- The inProgress entry's `id` is used as `TaskTriggerId` when linking effects to the quest.

For the complete quest schema and all fields, see [Quests](quests.md).

---

## Parent-Child Relationships

Items can be parented to other items using the `parentItemID` field:

- `0` — no parent. The item's `pos` and `rot` are in world space.
- Any other integer — the **item key** of the parent. The item's `pos` and `rot` become **local coordinates** relative to the parent's transform.

When a parent item moves (via animation, editor drag, or MoveToSpot effect), all children move with it.

### Example

```json
{
  "roomItems": {
    "10": {
      "prefabName": "ResizableCube",
      "parentItemID": 0,
      "pos": {"x": 5, "y": 3, "z": 0},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 10, "y": 7, "z": 0.2},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    },
    "11": {
      "prefabName": "WorldText",
      "parentItemID": 10,
      "pos": {"x": 0.2, "y": 2.9, "z": 0.1},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 1, "y": 1, "z": 1},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    }
  }
}
```

Item `"11"` is a child of item `"10"`. Its position `(0.2, 2.9, 0.1)` is relative to item `"10"`'s center, not the world origin. Moving item `"10"` moves item `"11"` along with it.

---

## Complete Minimal Example

A valid room with a spawn point, a red floor, a text label, and a trigger zone that shows a notification when the player enters.

```json
{
  "roomItems": {
    "2": {
      "prefabName": "SpawnPoint",
      "pos": {"x": 0, "y": 0, "z": 0},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 1, "y": 1, "z": 1},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "parentItemID": 0,
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    },
    "3": {
      "prefabName": "ResizableCube",
      "pos": {"x": 0, "y": -0.05, "z": 0},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 20, "y": 0.1, "z": 20},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "parentItemID": 0,
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    },
    "4": {
      "prefabName": "WorldText",
      "pos": {"x": 0, "y": 2, "z": 3},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 1, "y": 1, "z": 1},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "parentItemID": 0,
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    },
    "5": {
      "prefabName": "Trigger",
      "pos": {"x": 0, "y": 1, "z": 5},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 4, "y": 2, "z": 4},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "parentItemID": 0,
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    }
  },
  "settings": {
    "roomBase": "BlankScene",
    "isNight": false,
    "onlyNftHolders": false,
    "wallIndex": 0,
    "inTownHallMode": false,
    "globalSpeaking": false,
    "chatDisabled": false,
    "allCanBuild": false,
    "audiusPlaylist": "",
    "roomPrompt": "",
    "bannedUsers": "",
    "shareLiveKitCrossInstances": false,
    "tokenImage": "",
    "tokenName": "",
    "tokenAddress": "",
    "tasksRefresh": true,
    "roomNodeExtraData": "",
    "roomSettingsExtraData": "{\"showNameTags\":true,\"showBackpack\":true,\"showQuestLog\":false,\"showPlayerCount\":true,\"showMic\":true,\"showMusic\":true,\"showEmotes\":true,\"showSpaceInfo\":true,\"showCombatUI\":false,\"playerCollisions\":true,\"movementValues\":{\"walkSpeed\":2.0,\"runSpeed\":4.0,\"sprintSpeed\":6.8,\"jumpHeight\":4.0,\"gravity\":-10.0,\"airSpeed\":5.0}}"
  },
  "roomTasks": {
    "Tasks": []
  },
  "quests": {},
  "logic": {
    "3": "{\"Tasks\":[],\"ViewNodes\":[],\"col\":\"CC0000\",\"e\":0,\"c\":true}",
    "4": "{\"Tasks\":[],\"ViewNodes\":[],\"text\":\"<b>Welcome</b>\\nWalk into the zone ahead.\",\"fs\":3,\"fc\":\"FFFFFF\",\"bb\":true}",
    "5": "{\"Tasks\":[{\"$type\":\"TaskTriggerSubscription\",\"Trigger\":{\"$type\":\"OnEnterEvent\"},\"DirectEffector\":{\"Effector\":{\"$type\":\"NotificationPillEvent\",\"nt\":\"You entered the zone!\",\"c\":\"00FF00\",\"hideBackground\":false},\"Id\":\"b1a2c3d4-e5f6-7890-abcd-ef1234567890\",\"TargetState\":2,\"Name\":\"\"},\"Id\":\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\",\"TargetState\":2,\"Name\":\"\"}],\"ViewNodes\":[]}"
  }
}
```

### What Each Item Does

| ID | Type | Purpose |
|----|------|---------|
| `"2"` | `SpawnPoint` | Player spawn location at the origin. |
| `"3"` | `ResizableCube` | Red floor tile (20x20 units, 0.1 thick). Color and collider configured in logic. |
| `"4"` | `WorldText` | Billboard text label floating at Y=2, reading "Welcome" with instructions below. |
| `"5"` | `Trigger` | Invisible trigger zone at Z=5. When a player enters, it fires a green notification pill saying "You entered the zone!" |

### Logic Breakdown

**Item `"3"` (floor cube) — parsed logic:**
```json
{
  "Tasks": [],
  "ViewNodes": [],
  "col": "CC0000",
  "e": 0,
  "c": true
}
```
- `col`: dark red color
- `e`: no emission glow
- `c`: collider enabled (solid surface)

**Item `"4"` (text label) — parsed logic:**
```json
{
  "Tasks": [],
  "ViewNodes": [],
  "text": "<b>Welcome</b>\nWalk into the zone ahead.",
  "fs": 3,
  "fc": "FFFFFF",
  "bb": true
}
```
- `text`: bold title with line break and body text
- `fs`: font size 3
- `fc`: white text color
- `bb`: billboard mode (always faces camera)

**Item `"5"` (trigger zone) — parsed logic:**
```json
{
  "Tasks": [
    {
      "$type": "TaskTriggerSubscription",
      "Trigger": {"$type": "OnEnterEvent"},
      "DirectEffector": {
        "Effector": {
          "$type": "NotificationPillEvent",
          "nt": "You entered the zone!",
          "c": "00FF00",
          "hideBackground": false
        },
        "Id": "b1a2c3d4-e5f6-7890-abcd-ef1234567890",
        "TargetState": 2,
        "Name": ""
      },
      "Id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "TargetState": 2,
      "Name": ""
    }
  ],
  "ViewNodes": []
}
```
This is a basic interaction (not quest-driven). When a player enters the trigger zone (`OnEnterEvent`), it fires a `NotificationPillEvent` displaying green text. Each interaction task and its direct effector require unique UUID `Id` fields.

---

## Coordinate System

- **Ground plane**: Y = 0
- **Up**: +Y
- **A 1x1 cube sitting on the ground**: center at `pos.y = 0.5`
- **Default rotation**: `{"x": 0, "y": 0, "z": 0, "w": 1}` (identity quaternion, no rotation)
- **GLB models face +Z** in Portals

### Rotation

Rotations use quaternion format `{"x": qx, "y": qy, "z": qz, "w": qw}`.

Common Y-axis rotations (for rotating items to face a direction):

| Direction | Quaternion |
|-----------|-----------|
| Face +Z (default) | `{"x": 0, "y": 0, "z": 0, "w": 1}` |
| Face +X (90 degrees) | `{"x": 0, "y": 0.7071, "z": 0, "w": 0.7071}` |
| Face -Z (180 degrees) | `{"x": 0, "y": 1, "z": 0, "w": 0}` |
| Face -X (270 degrees) | `{"x": 0, "y": -0.7071, "z": 0, "w": 0.7071}` |

General formula for Y-axis rotation by angle `a` (in radians):
```
y = sin(a / 2)
w = cos(a / 2)
```

---

## Common Pitfalls

### 1. roomTasks must contain a Tasks array

```json
// WRONG - breaks room loading
"roomTasks": {}

// CORRECT
"roomTasks": {"Tasks": []}
```

An empty `roomTasks` object (without the `Tasks` key) will cause the room to fail to load. Always include `"Tasks": []` even if there are no room-level tasks.

### 2. Logic values must be JSON strings

```json
// WRONG - raw object
"logic": {
  "2": {"Tasks": [], "ViewNodes": [], "col": "FF0000"}
}

// CORRECT - JSON string
"logic": {
  "2": "{\"Tasks\":[],\"ViewNodes\":[],\"col\":\"FF0000\"}"
}
```

Each value in the `logic` object must be a serialized JSON string. If you pass raw objects, the data will not be interpreted correctly.

### 3. Item IDs start at "2"

ID `"1"` is reserved by the system. Always start your item IDs at `"2"` or higher. Using `"1"` may cause conflicts or data loss.

### 4. placed must be true

```json
// Item will NOT appear in the room
"placed": false

// Item will appear in the room
"placed": true
```

Items with `"placed": false` exist in the data but are invisible and non-functional. Unless you are intentionally hiding an item, always set `"placed": true`.

### 5. Parented items use local coordinates

When an item has a `parentItemID` other than `0`, its `pos` and `rot` fields are relative to the parent's transform — not the world origin.

```json
// This item is at world position (5, 3, 0)
{"parentItemID": 0, "pos": {"x": 5, "y": 3, "z": 0}}

// This item is 1 unit to the right of its parent's center
{"parentItemID": 10, "pos": {"x": 1, "y": 0, "z": 0}}
```

If you move an item from world space into a parent, you need to recalculate its position relative to the new parent.

### 6. Uploads replace the entire room

The upload endpoint does not merge — it replaces everything. If you upload data that only contains 3 items, every other item previously in the room will be deleted.

**Always follow this workflow:**
1. Download the current room data
2. Modify the downloaded data
3. Upload the modified data

### 7. roomSettingsExtraData is a JSON string

The `roomSettingsExtraData` field inside `settings` is a **JSON string**, not a nested object. You must stringify it before including it in the settings object, and parse it to read its contents.

```json
// WRONG - raw object
"roomSettingsExtraData": {"showNameTags": true}

// CORRECT - JSON string
"roomSettingsExtraData": "{\"showNameTags\":true}"
```

### 8. Color fields vary by item type

Different item types use different field names for color in their logic entries:

| Item Type | Color Field | Collider Field |
|-----------|-------------|---------------|
| `ResizableCube` | `"col"` | `"c"` |
| `Light` / `SpotLight` / `BlinkLight` | `"c"` | n/a |

On cubes, `"c"` is the collider toggle (boolean), not the color. On lights, `"c"` is the color (hex string). Mixing these up is a common source of bugs.

### 9. Quest names require numbered prefixes

Quest `Name` fields must start with a number and underscore:

```json
// WRONG
"Name": "collect_coins"
"Name": "quest1"

// CORRECT
"Name": "0_collect_coins"
"Name": "1_open_door"
```

Quests without the numbered prefix will not function.

---

## Related Pages

- [Rooms](rooms.md) — API endpoints for creating, downloading, and uploading rooms
- [Asset Uploads](assets.md) — Uploading GLBs, images, and JSON to the CDN
- [Item Types](item-types.md) — Complete per-type field schemas for logic entries
- [Interactions](interactions.md) — Trigger and effect formats for the Tasks array
- [Quests](quests.md) — Quest system, state management, and quest pair format
- [Settings](settings.md) — Room environment, physics, UI, and camera settings
- [Function Effects & NCalc](function-effects.md) — Variables, conditionals, and scripted logic
