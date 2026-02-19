# Examples

Complete working examples showing end-to-end API usage. Each example includes the full room data JSON ready to upload.

---

## Example 1: Simple Room with a Clickable Button

A room with a spawn point, a floor, a red button that shows a notification when clicked, and a light.

### Room Data

```json
{
  "roomItems": {
    "2": {
      "prefabName": "SpawnPoint",
      "pos": {"x": 0, "y": 0.1, "z": -5},
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
      "prefabName": "ResizableCube",
      "pos": {"x": 0, "y": 0.5, "z": 0},
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
      "hoverTitle": "Click me!",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    },
    "5": {
      "prefabName": "Light",
      "pos": {"x": 0, "y": 5, "z": 0},
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
    }
  },
  "settings": {
    "roomBase": "BlankScene",
    "isNight": false,
    "tasksRefresh": true,
    "roomSettingsExtraData": "{\"showNameTags\":true,\"showEmotes\":true,\"preloadRoom\":false}"
  },
  "roomTasks": {"Tasks": []},
  "quests": {},
  "logic": {
    "2": "{\"Tasks\":[],\"ViewNodes\":[],\"n\":\"\",\"r\":0}",
    "3": "{\"Tasks\":[],\"ViewNodes\":[],\"col\":\"333333\"}",
    "4": "{\"Tasks\":[{\"$type\":\"TaskTriggerSubscription\",\"Trigger\":{\"$type\":\"OnClickEvent\"},\"DirectEffector\":{\"Effector\":{\"$type\":\"NotificationPillEvent\",\"nt\":\"Hello! You clicked the button.\",\"c\":\"00FF00\"},\"Id\":\"a1b2c3d4-0001-0001-0001-000000000001\",\"TargetState\":2,\"Name\":\"\"},\"Id\":\"a1b2c3d4-0001-0001-0001-000000000002\",\"TargetState\":2,\"Name\":\"\"}],\"ViewNodes\":[],\"col\":\"FF0000\",\"e\":0.3}",
    "5": "{\"Tasks\":[],\"ViewNodes\":[],\"c\":\"FFFFFF\",\"b\":3.0,\"r\":15.0}"
  }
}
```

### What This Does

| Item | Description |
|------|-------------|
| `"2"` | Spawn point — player appears here |
| `"3"` | Dark grey floor (20x20) |
| `"4"` | Red glowing button — shows green notification on click |
| `"5"` | White overhead light |

---

## Example 2: Coin Collection Game

A room with collectible coins that increment a score variable, a score display, and a trigger zone that congratulates the player.

### Room Data

```json
{
  "roomItems": {
    "2": {
      "prefabName": "SpawnPoint",
      "pos": {"x": 0, "y": 0.1, "z": -8},
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
      "scale": {"x": 30, "y": 0.1, "z": 30},
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
      "prefabName": "GlbCollectable",
      "pos": {"x": -3, "y": 1, "z": 2},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 0.5, "y": 0.5, "z": 0.5},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "https://cdn.theportal.to/uploads/default-coin.glb?dynamic=true",
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
      "prefabName": "GlbCollectable",
      "pos": {"x": 3, "y": 1, "z": 2},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 0.5, "y": 0.5, "z": 0.5},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "https://cdn.theportal.to/uploads/default-coin.glb?dynamic=true",
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
    "6": {
      "prefabName": "GlbCollectable",
      "pos": {"x": 0, "y": 1, "z": 5},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 0.5, "y": 0.5, "z": 0.5},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "https://cdn.theportal.to/uploads/default-coin.glb?dynamic=true",
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
    "7": {
      "prefabName": "WorldText",
      "pos": {"x": 0, "y": 3, "z": 0},
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
    "8": {
      "prefabName": "Trigger",
      "pos": {"x": 0, "y": 1, "z": 8},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 4, "y": 3, "z": 4},
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
    "9": {
      "prefabName": "Light",
      "pos": {"x": 0, "y": 6, "z": 0},
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
    }
  },
  "settings": {
    "roomBase": "BlankScene",
    "isNight": false,
    "tasksRefresh": true,
    "roomSettingsExtraData": "{\"numericParameters\":[{\"N\":\"coins\",\"VT\":0,\"M\":false,\"P\":false}],\"showNameTags\":true,\"showQuestLog\":false,\"preloadRoom\":false}"
  },
  "roomTasks": {"Tasks": []},
  "quests": {},
  "logic": {
    "2": "{\"Tasks\":[],\"ViewNodes\":[],\"n\":\"\",\"r\":0}",
    "3": "{\"Tasks\":[],\"ViewNodes\":[],\"col\":\"2D5A27\"}",
    "4": "{\"Tasks\":[],\"ViewNodes\":[],\"valueLabel\":\"coins\",\"valueChange\":1,\"displayValue\":true,\"a\":true,\"l\":true,\"minRespawnTime\":5.0,\"maxRespawnTime\":10.0}",
    "5": "{\"Tasks\":[],\"ViewNodes\":[],\"valueLabel\":\"coins\",\"valueChange\":1,\"displayValue\":true,\"a\":true,\"l\":true,\"minRespawnTime\":5.0,\"maxRespawnTime\":10.0}",
    "6": "{\"Tasks\":[],\"ViewNodes\":[],\"valueLabel\":\"coins\",\"valueChange\":1,\"displayValue\":true,\"a\":true,\"l\":true,\"minRespawnTime\":5.0,\"maxRespawnTime\":10.0}",
    "7": "{\"Tasks\":[],\"ViewNodes\":[],\"text\":\"<b><color=#FFD700>Coins: |coins|</color></b>\",\"lookAtCamera\":true}",
    "8": "{\"Tasks\":[{\"$type\":\"TaskTriggerSubscription\",\"Trigger\":{\"$type\":\"OnEnterEvent\"},\"DirectEffector\":{\"Effector\":{\"$type\":\"FunctionEffector\",\"V\":\"if($N{coins} >= 3.0, SetVariable('coins', 0.0, 0.0), 0.0)\"},\"Id\":\"b1b2c3d4-0001-0001-0001-000000000001\",\"TargetState\":2,\"Name\":\"\"},\"Id\":\"b1b2c3d4-0001-0001-0001-000000000002\",\"TargetState\":2,\"Name\":\"\"},{\"$type\":\"TaskTriggerSubscription\",\"Trigger\":{\"$type\":\"OnEnterEvent\"},\"DirectEffector\":{\"Effector\":{\"$type\":\"NotificationPillEvent\",\"nt\":\"You collected |coins| coins!\",\"c\":\"FFD700\"},\"Id\":\"b1b2c3d4-0001-0001-0001-000000000003\",\"TargetState\":2,\"Name\":\"\"},\"Id\":\"b1b2c3d4-0001-0001-0001-000000000004\",\"TargetState\":2,\"Name\":\"\"}],\"ViewNodes\":[],\"events\":[],\"opacity\":0.01}",
    "9": "{\"Tasks\":[],\"ViewNodes\":[],\"c\":\"FFD700\",\"b\":4.0,\"r\":20.0}"
  }
}
```

### What This Does

| Item | Description |
|------|-------------|
| `"2"` | Spawn point |
| `"3"` | Green floor |
| `"4"` – `"6"` | Three collectible coins, each adds 1 to `coins` variable, respawns in 5-10 seconds |
| `"7"` | Billboard text showing live coin count using `\|coins\|` pipe syntax |
| `"8"` | Trigger zone — when entered, shows notification with coin count. If 3+ coins, resets to 0. |
| `"9"` | Gold-colored light |

### Key Concepts Demonstrated

- **Variables**: `coins` defined in `numericParameters` in settings
- **Collectibles**: `GlbCollectable` with `valueLabel` and `valueChange`
- **Live text**: WorldText using `|coins|` pipe syntax
- **FunctionEffector**: Conditional logic in trigger zone
- **Multiple interactions**: Two tasks on the same trigger zone

---

## Example 3: Quest-Driven Door

A room with a button that opens a door when clicked, using the quest system for persistent state.

### Room Data

```json
{
  "roomItems": {
    "2": {
      "prefabName": "SpawnPoint",
      "pos": {"x": 0, "y": 0.1, "z": -5},
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
      "prefabName": "ResizableCube",
      "pos": {"x": -2, "y": 0.5, "z": 0},
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
      "hoverTitle": "Open Door",
      "hoverBodyContent": "Click to open",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    },
    "5": {
      "prefabName": "ResizableCube",
      "pos": {"x": 3, "y": 1.5, "z": 0},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 0.2, "y": 3, "z": 2},
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
    "6": {
      "prefabName": "Light",
      "pos": {"x": 0, "y": 5, "z": 0},
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
    }
  },
  "settings": {
    "roomBase": "BlankScene",
    "isNight": false,
    "tasksRefresh": true,
    "roomSettingsExtraData": "{\"preloadRoom\":true}"
  },
  "roomTasks": {"Tasks": []},
  "quests": {
    "mlhab7cd3efg12": {
      "EntryId": "07b29300-f6df-47e4-8f55-5aa697303896",
      "Name": "0_open_door",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Creator": "YOUR_FIREBASE_UID",
      "TemplateName": "",
      "Tracked": true,
      "Visible": false,
      "ExtraText": "",
      "id": "mlhab7cd3efg12"
    },
    "mlhxy9zw2abc34": {
      "EntryId": "07b29300-f6df-47e4-8f55-5aa697303896",
      "Name": "0_open_door",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Rewards": [],
      "Creator": "YOUR_FIREBASE_UID",
      "TemplateName": "",
      "Tracked": true,
      "Visible": false,
      "ExtraText": "",
      "SuccessMsg": "",
      "id": "mlhxy9zw2abc34"
    }
  },
  "logic": {
    "2": "{\"Tasks\":[],\"ViewNodes\":[],\"n\":\"\",\"r\":0}",
    "3": "{\"Tasks\":[],\"ViewNodes\":[],\"col\":\"444444\"}",
    "4": "{\"Tasks\":[{\"$type\":\"TaskTriggerSubscription\",\"Trigger\":{\"$type\":\"OnClickEvent\"},\"Id\":\"c1c2c3c4-0001-0001-0001-000000000001\",\"TargetState\":111,\"Name\":\"0_open_door\",\"TaskTriggerId\":\"mlhab7cd3efg12\"},{\"$type\":\"TaskTriggerSubscription\",\"Trigger\":{\"$type\":\"OnClickEvent\"},\"DirectEffector\":{\"Effector\":{\"$type\":\"NotificationPillEvent\",\"nt\":\"Door opened!\",\"c\":\"00FF00\"},\"Id\":\"c1c2c3c4-0001-0001-0001-000000000002\",\"TargetState\":2,\"Name\":\"\"},\"Id\":\"c1c2c3c4-0001-0001-0001-000000000003\",\"TargetState\":2,\"Name\":\"\"}],\"ViewNodes\":[],\"col\":\"00AA00\",\"e\":0.5}",
    "5": "{\"Tasks\":[{\"$type\":\"TaskEffectorSubscription\",\"Effector\":{\"$type\":\"MoveToSpot\",\"_transformState\":{\"position\":[3,1.5,0],\"rotation\":[0,0,0,1],\"scale\":[0.2,3,2],\"duration\":0.0}},\"Id\":\"d1d2d3d4-0001-0001-0001-000000000001\",\"Name\":\"0_open_door\",\"TaskTriggerId\":\"mlhab7cd3efg12\"},{\"$type\":\"TaskEffectorSubscription\",\"Effector\":{\"$type\":\"MoveToSpot\",\"_transformState\":{\"position\":[3,5,0],\"rotation\":[0,0,0,1],\"scale\":[0.2,3,2],\"duration\":2.0}},\"Id\":\"d1d2d3d4-0001-0001-0001-000000000002\",\"TargetState\":1,\"Name\":\"0_open_door\",\"TaskTriggerId\":\"mlhab7cd3efg12\"}],\"ViewNodes\":[],\"col\":\"8B4513\"}",
    "6": "{\"Tasks\":[],\"ViewNodes\":[],\"c\":\"FFFFFF\",\"b\":3.0,\"r\":15.0}"
  }
}
```

### What This Does

| Item | Description |
|------|-------------|
| `"2"` | Spawn point |
| `"3"` | Grey floor |
| `"4"` | Green glowing button — clicking it advances quest `0_open_door` from Not Active to Active (TargetState 111) and shows a notification |
| `"5"` | Brown door — has two quest states: State 0 (Not Active) keeps it at its starting position; State 1 (Active) animates it upward over 2 seconds |
| `"6"` | White light |

### Key Concepts Demonstrated

- **Quest pair**: Two entries in `quests` sharing `EntryId` with different `id` values
- **Click-to-advance-quest**: `TaskTriggerSubscription` with `TargetState: 111` and `TaskTriggerId`
- **Quest-driven animation**: `TaskEffectorSubscription` with `MoveToSpot` on the door
- **3-state pattern**: State 0 has no `TargetState` field, State 1 has `"TargetState": 1`
- **`Creator` field**: Replace `YOUR_FIREBASE_UID` with your actual Firebase UID from authentication

---

## Upload Workflow

Here's how to upload any of these examples to a room using the API:

```bash
# 1. Verify your access key and get your UID
curl -X POST https://theportal.to/api/v2/mcp/verify-access-key \
  -H "Content-Type: application/json" \
  -d '{"accessKey": "your-access-key"}'
# Response: {"data": {"uid": "your-firebase-uid"}}

# 2. Create a room (or use an existing room ID)
curl -X POST https://theportal.to/api/v2/rooms/create \
  -H "Content-Type: application/json" \
  -H "x-access-key: your-access-key" \
  -d '{"templateName": "blank", "customTemplateName": "My Test Room"}'
# Response: {"roomId": "your-room-id", "name": "My Test Room"}

# 3. Save your room data to a file
# (replace YOUR_FIREBASE_UID in the JSON with the uid from step 1)
cat > room-data.json << 'EOF'
{ ... your room data JSON ... }
EOF

# 4. Get a signed upload URL for the JSON
RESPONSE=$(curl -s -X POST https://theportal.to/api/v2/utils/generate-json-upload-url \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-access-key" \
  -d '{"fileName": "room-data.json"}')

SIGNED_URL=$(echo $RESPONSE | jq -r '.signedUploadURL')
ASSET_URL=$(echo $RESPONSE | jq -r '.assetURL')

# 5. Upload the JSON to S3
curl -X PUT "$SIGNED_URL" \
  -H "Content-Type: application/json" \
  -d @room-data.json

# 6. Apply it to your room
curl -X POST https://theportal.to/api/v2/mcp/upload-room-data-url \
  -H "Content-Type: application/json" \
  -H "x-room-id: your-room-id" \
  -H "x-access-key: your-access-key" \
  -d "{\"jsonUrl\": \"$ASSET_URL\"}"

# 7. Visit your room
echo "https://theportal.to/?room=your-room-id"
```

---

## Related Pages

- [Room Data Format](room-data-format.md) — complete schema reference
- [Item Types](item-types.md) — all item type fields
- [Interactions](interactions.md) — trigger and effect reference
- [Quests](quests.md) — quest system
- [Settings](settings.md) — room settings
- [Function Effects](function-effects.md) — NCalc expressions
- [Rooms](rooms.md) — room CRUD endpoints
- [Assets](assets.md) — asset upload workflow
