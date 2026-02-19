# Settings

Complete reference for the `settings` object inside [room data](room-data-format.md). Settings control the room environment, player physics, UI visibility, avatars, camera, visual effects, and more.

---

## Overview

Room settings have **two layers**:

1. **Top-level fields** — basic room configuration (night mode, chat, voice, token gating)
2. **`roomSettingsExtraData`** — a JSON **string** containing a detailed configuration object (movement, fog, bloom, camera states, UI toggles, variables, avatars)

> **Critical:** `roomSettingsExtraData` must be a JSON-encoded **string** (`JSON.stringify(object)`), not a raw object. This is the single most common settings mistake. If you pass a raw object, the settings will not be interpreted correctly.

```json
{
  "settings": {
    "roomBase": "BlankScene",
    "isNight": false,
    "roomSettingsExtraData": "{\"showNameTags\":true,\"movementValues\":{\"runSpeed\":4.0}}"
  }
}
```

> **Uploads replace everything.** When uploading room data, the entire `settings` object is replaced. Always [download](rooms.md#download-room-data) the current room data first, modify the settings, then upload. Any fields you omit will revert to defaults.

---

## Top-Level Fields

These fields sit directly inside the `settings` object.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `roomBase` | string | `"BlankScene"` | Base scene/environment template |
| `isNight` | boolean | `false` | Night mode — switches lighting, skybox, fog, and bloom to their night variants |
| `onlyNftHolders` | boolean | `false` | Restrict entry to NFT holders (requires `tokenAddress`) |
| `wallIndex` | integer | `0` | Wall style index |
| `inTownHallMode` | boolean | `false` | Stage mode — one speaker at a time, others listen |
| `globalSpeaking` | boolean | `false` | Global voice chat (no distance falloff) |
| `chatDisabled` | boolean | `false` | Disable text chat |
| `allCanBuild` | boolean | `false` | Allow all users to place items in the room |
| `audiusPlaylist` | string | `""` | Audius playlist URL for background music |
| `roomPrompt` | string | `""` | System prompt for AI NPCs in the room |
| `bannedUsers` | string | `""` | Banned user list |
| `shareLiveKitCrossInstances` | boolean | `false` | Share voice chat across room instances |
| `tokenImage` | string | `""` | Token gate image URL |
| `tokenName` | string | `""` | Token gate token name |
| `tokenAddress` | string | `""` | Token gate contract address |
| `tasksRefresh` | boolean | `true` | Live-refresh triggers and effects. When `true`, interaction changes take effect immediately without requiring a room reload. |
| `roomNodeExtraData` | string | `""` | Additional room node data |
| `roomSettingsExtraData` | string | *(see below)* | JSON string containing the detailed configuration object. See [roomSettingsExtraData](#roomsettingsextradata). |

### Example

```json
{
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
    "roomSettingsExtraData": "..."
  }
}
```

---

## roomSettingsExtraData

All fields in this section live inside the `roomSettingsExtraData` JSON string. To read these values, parse the string as JSON. To write them, build an object with the fields you need, then `JSON.stringify()` it.

```
// Pseudocode — reading
extraData = JSON.parse(settings.roomSettingsExtraData)
walkSpeed = extraData.movementValues.walkSpeed

// Pseudocode — writing
extraData = { showNameTags: true, movementValues: { runSpeed: 4.0 } }
settings.roomSettingsExtraData = JSON.stringify(extraData)
```

### Welcome & Onboarding

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `welcomeEmbed` | string | `""` | iframe URL shown on room entry |
| `openWelcomeIframeInBackground` | boolean | `false` | Load the welcome iframe in the background |
| `addWelcomeIframeToInfoButton` | boolean | `false` | Add the welcome iframe to the info button |
| `showWelcomeOnEntry` | boolean | `true` | Show the welcome screen when a player enters |
| `onboardingType` | integer | `1` | Onboarding style. `0` = none, `1` = click-to-drag (default), `2` = toggle cursor lock |
| `requireUsername` | boolean | `false` | Force username entry before joining |
| `allowedUsers` | integer | `0` | Access restriction. `0` = anyone, `1` = logged-in users only, `2` = crypto wallet required |

### Skybox

Custom skybox textures for day and night modes. Both day and night skyboxes can be set independently.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `skyBoxDayTextureUrl` | string | `""` | Custom day skybox texture URL |
| `skyBoxNightTextureUrl` | string | `""` | Custom night skybox texture URL |
| `skyBoxDayRotation` | float | `0` | Day skybox rotation (degrees) |
| `skyBoxNightRotation` | float | `0` | Night skybox rotation (degrees) |
| `skyBoxDayExposure` | float | `1.0` | Day skybox brightness multiplier |
| `skyBoxNightExposure` | float | `1.0` | Night skybox brightness multiplier |

### Movement — `movementValues`

The `movementValues` object defines the default player physics. This same field structure is also used in custom movement states (see [Custom Movement States](#custom-movement-states-movementstates)).

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `movementStateName` | string | `""` | State name. Empty for the default state. |
| `walkByDefault` | boolean | `false` | Start in walk mode instead of run |
| `walkSpeed` | float | `2.0` | Walk speed |
| `runSpeed` | float | `4.0` | Run speed |
| `sprintSpeed` | float | `6.8` | Sprint speed |
| `strafing` | boolean | `false` | Enable strafing (side movement without turning) |
| `jumpTimer` | float | `0.3` | Cooldown between jumps (seconds) |
| `jumpHeight` | float | `4.0` | Jump height |
| `airSpeed` | float | `5.0` | Movement speed while airborne |
| `gravity` | float | `-10.0` | Gravity strength (negative = down) |
| `rotationSpeed` | float | `16.0` | Player turn speed |
| `ledgeGrab` | boolean | `false` | Enable ledge grabbing |
| `forceFirstPerson` | boolean | `false` | Lock to first-person view |
| `stopVerticalInput` | boolean | `false` | Disable vertical movement input |
| `stopJumps` | boolean | `false` | Disable jumping entirely |

#### Example

```json
{
  "movementValues": {
    "movementStateName": "",
    "walkByDefault": false,
    "walkSpeed": 2.0,
    "runSpeed": 4.0,
    "sprintSpeed": 6.8,
    "strafing": false,
    "jumpTimer": 0.3,
    "jumpHeight": 4.0,
    "airSpeed": 5.0,
    "gravity": -10.0,
    "rotationSpeed": 16.0,
    "ledgeGrab": false,
    "forceFirstPerson": false,
    "stopVerticalInput": false,
    "stopJumps": false
  }
}
```

### Custom Movement States — `movementStates`

The `movementStates` array defines named movement presets that can be switched to at runtime using the `ChangeMovementProfile` effect. Each entry has the same fields as `movementValues`, but with a required non-empty `movementStateName`.

Use `defaultMovementState` (integer, default `-1`) to set which state is active on room entry. `-1` means use the default `movementValues`. Any other value is an index into the `movementStates` array.

```json
{
  "movementStates": [
    {
      "movementStateName": "swimming",
      "walkByDefault": true,
      "walkSpeed": 1.5,
      "runSpeed": 3.0,
      "sprintSpeed": 4.0,
      "strafing": true,
      "jumpTimer": 0.3,
      "jumpHeight": 2.0,
      "airSpeed": 3.0,
      "gravity": -5.0,
      "rotationSpeed": 12.0,
      "ledgeGrab": false,
      "forceFirstPerson": false,
      "stopVerticalInput": false,
      "stopJumps": false
    },
    {
      "movementStateName": "flying",
      "walkByDefault": false,
      "walkSpeed": 5.0,
      "runSpeed": 10.0,
      "sprintSpeed": 15.0,
      "strafing": true,
      "jumpTimer": 0.1,
      "jumpHeight": 8.0,
      "airSpeed": 12.0,
      "gravity": -2.0,
      "rotationSpeed": 20.0,
      "ledgeGrab": false,
      "forceFirstPerson": false,
      "stopVerticalInput": false,
      "stopJumps": false
    }
  ],
  "defaultMovementState": -1
}
```

To switch a player to the "swimming" state at runtime, fire a `ChangeMovementProfile` effect with the state name `"swimming"`. See [Interactions](interactions.md) for effect syntax.

### Numeric Parameters / Variables — `numericParameters`

The `numericParameters` array defines room-level variables used by triggers and effects (`UpdateScoreEvent`, `ScoreTrigger`, `FunctionEffector`, `DisplayValueEvent`, etc.). Variables must be declared here before they can be referenced in interactions.

| Field | Type | Description |
|-------|------|-------------|
| `N` | string | Variable name. Used to reference this variable in triggers and effects. |
| `VT` | integer | Value type. `0` = numeric, `1` = string. |
| `M` | boolean | Multiplayer synced. When `true`, this variable is shared across all players in the room. When `false`, each player has their own independent value. |
| `P` | boolean | Persistent. When `true`, the value is saved across sessions (the player sees the same value when they return). When `false`, the value resets when the player leaves. |

#### Example

```json
{
  "numericParameters": [
    {"N": "score", "VT": 0, "M": false, "P": false},
    {"N": "team_score", "VT": 0, "M": true, "P": false},
    {"N": "high_score", "VT": 0, "M": false, "P": true},
    {"N": "player_name", "VT": 1, "M": false, "P": true}
  ]
}
```

| Variable | Type | Synced | Persistent | Behavior |
|----------|------|--------|------------|----------|
| `score` | numeric | No | No | Per-player, resets on leave |
| `team_score` | numeric | Yes | No | Shared across all players, resets when room empties |
| `high_score` | numeric | No | Yes | Per-player, saved across sessions |
| `player_name` | string | No | Yes | Per-player, saved across sessions |

### UI Toggles

Control the visibility of interface elements.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `showNameTags` | boolean | `true` | Show player name labels above avatars |
| `showBackpack` | boolean | `true` | Show inventory/backpack button |
| `showQuestLog` | boolean | `false` | Show quest log button |
| `showPlayerCount` | boolean | `true` | Show player count |
| `showMic` | boolean | `true` | Show microphone button |
| `showMusic` | boolean | `true` | Show music controls |
| `showEmotes` | boolean | `true` | Show emote wheel |
| `showSpaceInfo` | boolean | `true` | Show space info button |
| `showCombatUI` | boolean | `false` | Show combat controls (attack/block buttons) |
| `requestMicPopup` | boolean | `false` | Show mic permission popup on room entry |

### Player Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `playerCollisions` | boolean | `true` | Players collide with each other |
| `disableHToSpawn` | boolean | `false` | Disable the H key shortcut that teleports to spawn |
| `playJoinSound` | boolean | `true` | Play a sound when a player joins the room |
| `jumpSounds` | boolean | `false` | Play a sound when a player jumps |

### Avatar Types

Multiple avatar types can be enabled simultaneously. Players choose from the enabled types when entering the room.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `guardianAvatars` | boolean | `true` | Default Portals avatars |
| `blockyAvatars` | boolean | `false` | Block-style avatars |
| `roundyAvatars` | boolean | `false` | Round-style avatars |
| `rpmAvatars` | boolean | `false` | Ready Player Me avatars |
| `collectibleAvatars` | boolean | `false` | Collectible avatars |
| `customAvatars` | boolean | `false` | Custom uploaded avatars (requires `enableCustomAvatars`) |
| `enableCustomAvatars` | boolean | `false` | Master toggle for custom avatars |

### Custom Space Avatars — `customSpaceAvatars`

The `customSpaceAvatars` array defines room-specific avatar options. Both `enableCustomAvatars` and `customAvatars` must be set to `true` for these to appear.

| Field | Type | Description |
|-------|------|-------------|
| `avatarName` | string | Display name for the avatar |
| `glbUrl` | string | URL to the avatar GLB model |
| `imgUrl` | string | URL to the avatar thumbnail image |

```json
{
  "enableCustomAvatars": true,
  "customAvatars": true,
  "customSpaceAvatars": [
    {
      "avatarName": "Robot Guard",
      "glbUrl": "https://cdn.theportal.to/uploads/.../robot.glb",
      "imgUrl": "https://cdn.theportal.to/uploads/.../robot-thumb.png"
    },
    {
      "avatarName": "Space Marine",
      "glbUrl": "https://cdn.theportal.to/uploads/.../marine.glb",
      "imgUrl": "https://cdn.theportal.to/uploads/.../marine-thumb.png"
    }
  ]
}
```

### Custom Camera States — `customCameraStates`

The `customCameraStates` array defines named camera presets that can be switched to at runtime using the `ChangeCamState` effect.

Use `defaultCameraState` (integer, default `-1`) to set which camera state is active on room entry. `-1` means the default third-person camera. Any other value is an index into the `customCameraStates` array.

| Field | Type | Description |
|-------|------|-------------|
| `stateName` | string | Name of the camera state (used by `ChangeCamState` effect) |
| `cameraMode` | integer | `1` = follows player (fixed angle, orbits around player), `2` = fixed world position |
| `distance` | float | Camera distance from the player |
| `height` | float | Camera height offset |
| `fov` | float | Field of view in degrees |
| `right` | float | Horizontal offset (positive = right of player) |
| `angleX` | float | Vertical angle (degrees) |
| `angleY` | float | Horizontal angle (degrees) |
| `pos` | object | World position `{"x": 0, "y": 0, "z": 0}` — used by camera mode `2` only |
| `rot` | object | World rotation in Euler degrees `{"x": 0, "y": 0, "z": 0}` — used by camera mode `2` only |
| `lookAtPlayer` | boolean | Camera always faces the player — used by camera mode `2` only |

#### Camera Mode 1 — Follow Player

The camera orbits around the player at a fixed distance, height, and angle. Good for top-down, isometric, or over-the-shoulder views.

```json
{
  "stateName": "top_down",
  "cameraMode": 1,
  "distance": 15.0,
  "height": 12.0,
  "fov": 60.0,
  "right": 0.0,
  "angleX": 80.0,
  "angleY": 0.0,
  "pos": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0},
  "lookAtPlayer": false
}
```

#### Camera Mode 2 — Fixed World Position

The camera is placed at a specific world position and rotation. Good for security cameras, cutscene angles, or fixed viewpoints.

```json
{
  "stateName": "security_cam",
  "cameraMode": 2,
  "distance": 1.5,
  "height": 0.0,
  "fov": 60.0,
  "right": 0.0,
  "angleX": 0.0,
  "angleY": 0.0,
  "pos": {"x": -7.0, "y": 3.2, "z": 1.0},
  "rot": {"x": 22.0, "y": 91.5, "z": 0.0},
  "lookAtPlayer": true
}
```

### Visual Effects

#### Fog — `fog`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `DayFogMax` | float | `0.0` | Day fog density (`0` = no fog) |
| `NightFogMax` | float | `0.0` | Night fog density |
| `DayFogColor` | string | `""` | Day fog color (6-character hex, no `#` prefix) |
| `NightFogColor` | string | `""` | Night fog color (6-character hex, no `#` prefix) |

```json
{
  "fog": {
    "DayFogMax": 0.03,
    "NightFogMax": 0.06,
    "DayFogColor": "B0C4DE",
    "NightFogColor": "1A1A2E"
  }
}
```

#### Post-Processing — `postprocess`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `BloomDayIntensity` | float | `0.0` | Day bloom strength |
| `BloomNightIntensity` | float | `0.0` | Night bloom strength |
| `BloomDayClamp` | float | `0.0` | Day bloom clamp |
| `BloomNightClamp` | float | `0.0` | Night bloom clamp |
| `BloomDayDiffusion` | float | `0.0` | Day bloom spread/diffusion |
| `BloomNightDiffusion` | float | `0.0` | Night bloom spread/diffusion |
| `CameraMaxDistanceDay` | float | `0.0` | Maximum camera render distance (day) |
| `CameraMaxDistanceNight` | float | `0.0` | Maximum camera render distance (night) |

```json
{
  "postprocess": {
    "BloomDayIntensity": 0.5,
    "BloomNightIntensity": 1.2,
    "BloomDayClamp": 1.0,
    "BloomNightClamp": 1.0,
    "BloomDayDiffusion": 3.0,
    "BloomNightDiffusion": 5.0,
    "CameraMaxDistanceDay": 0.0,
    "CameraMaxDistanceNight": 0.0
  }
}
```

#### Lighting — `lightValues`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `NightShadows` | integer | `0` | Night shadow mode |

#### Retro Rendering

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `psx` | boolean | `false` | PSX-style retro rendering (vertex jitter, low resolution) |
| `pixelation` | float | `0.24` | Pixelation amount. Lower values = more pixelated. Only applies when `psx` is `true`. |

### Performance

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `preloadRoom` | boolean | `false` | Load all GLB assets before the player enters the room. Recommended for games — prevents players from seeing hidden items appear during load. |
| `fastDownload` | boolean | `false` | Faster asset loading. May cause errors in very large rooms. |
| `uncompressedGLB` | boolean | `false` | Use uncompressed GLB files instead of Draco-compressed versions |

### Voice Chat

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `voiceChatRange` | float | `14.0` | Voice chat audible range in meters. Players beyond this distance cannot hear each other. |
| `globalChat` | boolean | `false` | Global text chat (no distance limit on text messages) |

### Vehicles — `carSettings`

Vehicle physics settings. These apply when vehicle items are present in the room.

| Field | Type | Description |
|-------|------|-------------|
| `acceleration` | float | Vehicle acceleration |
| `drag` | float | Vehicle drag/friction |
| `maxSpeed` | float | Top speed |
| `steering` | float | Steering responsiveness |
| `mass` | float | Vehicle mass |
| `gravity` | float | Vehicle gravity |
| `timeToMaxSteer` | float | Time to reach full steering angle (seconds) |

### Ignored Fields

These fields exist in the data but are for internal use. Leave them at their defaults.

| Field | Default | Notes |
|-------|---------|-------|
| `EventData` | `"{\"itemNames\":[],\"itemEvents\":[]}"` | Leave empty |
| `RoomItemsData` | `[]` | Leave empty |
| `weaponDatas` | `[]` | Weapon system (not documented) |
| `defaultWeapon` | `-1` | Leave at `-1` |
| `releasedRoom` | `""` | Internal use |

---

## Complete Example

Below is a complete `settings` object demonstrating both layers. The example configures:
- Day mode (night off)
- Custom movement with slower walk speed
- A `score` numeric variable
- Quest log visible
- Fog enabled
- Preload on

### The `roomSettingsExtraData` Object (Before Stringifying)

This is the object you build before converting it to a JSON string:

```json
{
  "showNameTags": true,
  "showBackpack": true,
  "showQuestLog": true,
  "showPlayerCount": true,
  "showMic": true,
  "showMusic": true,
  "showEmotes": true,
  "showSpaceInfo": true,
  "showCombatUI": false,
  "requestMicPopup": false,
  "playerCollisions": true,
  "disableHToSpawn": false,
  "playJoinSound": true,
  "jumpSounds": false,
  "preloadRoom": true,
  "fastDownload": false,
  "uncompressedGLB": false,
  "voiceChatRange": 14.0,
  "globalChat": false,
  "guardianAvatars": true,
  "blockyAvatars": false,
  "roundyAvatars": false,
  "rpmAvatars": false,
  "collectibleAvatars": false,
  "customAvatars": false,
  "enableCustomAvatars": false,
  "psx": false,
  "onboardingType": 1,
  "requireUsername": false,
  "allowedUsers": 0,
  "showWelcomeOnEntry": true,
  "movementValues": {
    "movementStateName": "",
    "walkByDefault": true,
    "walkSpeed": 1.5,
    "runSpeed": 4.0,
    "sprintSpeed": 6.8,
    "strafing": false,
    "jumpTimer": 0.3,
    "jumpHeight": 4.0,
    "airSpeed": 5.0,
    "gravity": -10.0,
    "rotationSpeed": 16.0,
    "ledgeGrab": false,
    "forceFirstPerson": false,
    "stopVerticalInput": false,
    "stopJumps": false
  },
  "movementStates": [],
  "defaultMovementState": -1,
  "numericParameters": [
    {"N": "score", "VT": 0, "M": false, "P": false}
  ],
  "customCameraStates": [],
  "defaultCameraState": -1,
  "customSpaceAvatars": [],
  "fog": {
    "DayFogMax": 0.03,
    "NightFogMax": 0.0,
    "DayFogColor": "C8D6E5",
    "NightFogColor": ""
  },
  "postprocess": {
    "BloomDayIntensity": 0.0,
    "BloomNightIntensity": 0.0,
    "BloomDayClamp": 0.0,
    "BloomNightClamp": 0.0,
    "BloomDayDiffusion": 0.0,
    "BloomNightDiffusion": 0.0,
    "CameraMaxDistanceDay": 0.0,
    "CameraMaxDistanceNight": 0.0
  }
}
```

### The Complete `settings` Object (Ready to Upload)

After stringifying `roomSettingsExtraData`, the final `settings` object looks like this:

```json
{
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
    "roomSettingsExtraData": "{\"showNameTags\":true,\"showBackpack\":true,\"showQuestLog\":true,\"showPlayerCount\":true,\"showMic\":true,\"showMusic\":true,\"showEmotes\":true,\"showSpaceInfo\":true,\"showCombatUI\":false,\"requestMicPopup\":false,\"playerCollisions\":true,\"disableHToSpawn\":false,\"playJoinSound\":true,\"jumpSounds\":false,\"preloadRoom\":true,\"fastDownload\":false,\"uncompressedGLB\":false,\"voiceChatRange\":14.0,\"globalChat\":false,\"guardianAvatars\":true,\"blockyAvatars\":false,\"roundyAvatars\":false,\"rpmAvatars\":false,\"collectibleAvatars\":false,\"customAvatars\":false,\"enableCustomAvatars\":false,\"psx\":false,\"onboardingType\":1,\"requireUsername\":false,\"allowedUsers\":0,\"showWelcomeOnEntry\":true,\"movementValues\":{\"movementStateName\":\"\",\"walkByDefault\":true,\"walkSpeed\":1.5,\"runSpeed\":4.0,\"sprintSpeed\":6.8,\"strafing\":false,\"jumpTimer\":0.3,\"jumpHeight\":4.0,\"airSpeed\":5.0,\"gravity\":-10.0,\"rotationSpeed\":16.0,\"ledgeGrab\":false,\"forceFirstPerson\":false,\"stopVerticalInput\":false,\"stopJumps\":false},\"movementStates\":[],\"defaultMovementState\":-1,\"numericParameters\":[{\"N\":\"score\",\"VT\":0,\"M\":false,\"P\":false}],\"customCameraStates\":[],\"defaultCameraState\":-1,\"customSpaceAvatars\":[],\"fog\":{\"DayFogMax\":0.03,\"NightFogMax\":0.0,\"DayFogColor\":\"C8D6E5\",\"NightFogColor\":\"\"},\"postprocess\":{\"BloomDayIntensity\":0.0,\"BloomNightIntensity\":0.0,\"BloomDayClamp\":0.0,\"BloomNightClamp\":0.0,\"BloomDayDiffusion\":0.0,\"BloomNightDiffusion\":0.0,\"CameraMaxDistanceDay\":0.0,\"CameraMaxDistanceNight\":0.0}}"
  }
}
```

> Notice that the entire `roomSettingsExtraData` value is a single JSON string with escaped quotes. This is the format the API expects.

---

## Working with Settings

### Reading Settings

```javascript
// After downloading room data
const roomData = await downloadRoomData(roomId);
const settings = roomData.settings;

// Top-level fields are directly accessible
const isNight = settings.isNight;

// Extra data must be parsed
const extraData = JSON.parse(settings.roomSettingsExtraData);
const runSpeed = extraData.movementValues.runSpeed;
const showQuestLog = extraData.showQuestLog;
```

### Modifying Settings

```javascript
// 1. Download current room data
const roomData = await downloadRoomData(roomId);

// 2. Modify top-level settings
roomData.settings.isNight = true;

// 3. Parse, modify, and re-stringify extra data
const extraData = JSON.parse(roomData.settings.roomSettingsExtraData);
extraData.movementValues.runSpeed = 6.0;
extraData.showQuestLog = true;
extraData.numericParameters.push({"N": "coins", "VT": 0, "M": false, "P": false});
roomData.settings.roomSettingsExtraData = JSON.stringify(extraData);

// 4. Upload the modified room data
await uploadRoomData(roomId, roomData);
```

### Common Mistakes

```json
// WRONG — roomSettingsExtraData as a raw object
{
  "roomSettingsExtraData": {
    "showNameTags": true
  }
}

// CORRECT — roomSettingsExtraData as a JSON string
{
  "roomSettingsExtraData": "{\"showNameTags\":true}"
}
```

```json
// WRONG — forgetting to include roomSettingsExtraData when uploading
{
  "settings": {
    "roomBase": "BlankScene",
    "isNight": true
  }
}
// Result: all extra data settings (movement, UI, variables, etc.) revert to defaults

// CORRECT — always include the full settings object
{
  "settings": {
    "roomBase": "BlankScene",
    "isNight": true,
    "roomSettingsExtraData": "{...existing extra data...}"
  }
}
```

---

## Related Pages

- [Room Data Format](room-data-format.md) — Complete room data structure
- [Rooms](rooms.md) — API endpoints for downloading and uploading room data
- [Interactions](interactions.md) — Triggers and effects that reference variables and movement states
- [Function Effects & NCalc](function-effects.md) — Scripted logic using numeric parameters
- [Quests](quests.md) — Quest system (used with `showQuestLog`)
