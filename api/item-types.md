# Item Types

Complete reference for all Portals item types. Each item lives in `roomItems` (spatial/visual data only) with its interaction data stored separately in `logic` (keyed by the same item ID, as a JSON string).

## Room Data Structure

```json
{
  "roomItems": {
    "2": { "prefabName": "ResizableCube", "pos": {...}, ... },
    "3": { "prefabName": "GLB", "pos": {...}, ... }
  },
  "logic": {
    "2": "{\"col\":\"FF0000\",\"Tasks\":[],\"ViewNodes\":[]}",
    "3": "{\"s\":true,\"c\":true,\"Tasks\":[],\"ViewNodes\":[]}"
  },
  "settings": {},
  "roomTasks": {"Tasks": []},
  "quests": {}
}
```

**Key rules:**
- Items in `roomItems` do NOT contain `extraData`. All interaction/configuration data lives in `logic`.
- Every `logic` value is a **JSON string** (not a raw object). You must `JSON.stringify()` the logic object.
- Every logic entry requires at minimum `{"Tasks": [], "ViewNodes": []}` plus any type-specific fields.
- Item IDs are string numbers. ID `"1"` is reserved. Start at `"2"`.

---

## Common Item Fields

Every item in `roomItems` shares these base fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `prefabName` | string | Yes | Item type identifier (see categories below) |
| `pos` | `{x, y, z}` | Yes | World position. Ground is Y=0. |
| `rot` | `{x, y, z, w}` | Yes | Quaternion rotation. `{x:0, y:0, z:0, w:1}` = no rotation. |
| `scale` | `{x, y, z}` | Yes | Scale multiplier. Meaning varies by type. |
| `contentString` | string | No | Type-specific content (URL, element name, etc.) |
| `parentItemID` | integer | No | Parent item key for hierarchies. `0` = no parent. |
| `placed` | boolean | Yes | Must be `true` for item to appear in room |
| `locked` | boolean | No | `true` = item locked in editor |
| `superLocked` | boolean | No | `true` = item super-locked in editor |
| `interactivityType` | integer | No | Click behavior. `0` = none. |
| `interactivityURL` | string | No | URL for click behavior |
| `hoverTitle` | string | No | Tooltip title on hover |
| `hoverBodyContent` | string | No | Tooltip body on hover |
| `ImageInteractivityDetails` | object | No | `{"buttonText": "", "buttonURL": ""}` |
| `currentEditornetId` | integer | No | Always `0` |
| `modelsize` | `{x, y, z}` | No | Always `{x:0, y:0, z:0}` for non-GLB items |
| `modelCenter` | `{x, y, z}` | No | Always `{x:0, y:0, z:0}` for non-GLB items |
| `sessionData` | string | No | Always `""` |
| `instanceId` | string | No | Always `""` |

---

## Item Categories

| Category | prefabNames |
|----------|------------|
| [Building](#building) | `ResizableCube`, `WorldText`, `Portal`, `SpawnPoint` |
| [Models](#models) | `GLB`, `GlbCollectable`, `Destructible` |
| [Gameplay](#gameplay) | `Trigger`, `JumpPad`, `9Cube`, `Gun`, `Shotgun`, `CameraObject` |
| [Media](#media) | `DefaultPainting`, `DefaultVideo`, `PlaceableTV` |
| [Lighting](#lighting) | `Light`, `BlinkLight`, `SpotLight` |
| [Display](#display) | `Leaderboard`, `Chart`, `GLBSign` |
| [Interactive](#interactive) | `GLBNPC` |
| [Effects](#effects) | `Addressable` |

---

## Field Name Conflicts

Single-letter fields mean **different things** on different item types. This is the most common source of bugs.

| Field | ResizableCube | Light / SpotLight | GLB | 9Cube | Chart | GLBSign |
|-------|--------------|-------------------|-----|-------|-------|---------|
| `c` | collider (bool) | color (hex string) | collider (bool) | required `""` | collision (bool) | border color (hex string) |
| `b` | -- | brightness (float) | -- | -- | -- | -- |
| `r` | -- | range (float) | remove first frame (bool) | -- | curve rotation (float) | -- |
| `s` | shadows (bool) | -- | shadows (bool) | texture scale (float) | -- | -- |
| `e` | emission (float) | -- | -- | emission (float) | -- | emission (float) |
| `t` | tiling (float) | -- | -- | transparency (float) | time interval (int) | -- |
| `o` | opacity (float) | -- | -- | -- | -- | -- |

Also note: `col` is color on ResizableCube (NOT `c`, which is collider on cubes). `c` is color on Lights.

---

## Building

### ResizableCube

Primary building block. Default 1x1x1 cube, freely scalable to any dimensions.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `col` | string | `"888888"` | Color as 6-char hex (no `#` prefix) |
| `e` | float | -- | Emission/glow intensity. Omit for no glow. |
| `o` | float | -- | Opacity (0.0--1.0). Omit for fully opaque. |
| `c` | boolean | `true` | Collider. `false` = players pass through. |
| `s` | boolean | `true` | Shadows. `false` = no shadows. |
| `nav` | boolean | `false` | Nav mesh. `true` = AI-walkable surface. |
| `t` | float | -- | Texture tiling when `contentString` has an image URL. `2.0` = repeats 2x. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** Optional image URL to texture the cube surface.

**Example:**

`roomItems["2"]`:
```json
{
  "prefabName": "ResizableCube",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 0.05, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 20, "y": 0.1, "z": 20},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["2"]`:
```json
"{\"col\":\"4169E1\",\"e\":0.3,\"s\":false,\"Tasks\":[],\"ViewNodes\":[]}"
```

> **Positioning note:** A 1x1x1 cube sitting on the ground (Y=0) has its center at Y=0.5. A platform with `scale.y = 0.1` has its surface at `pos.y + (0.1 / 2)`.

---

### WorldText

3D text label with Unity rich text formatting.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `text` | string | -- | Text content. Supports Unity rich text tags. |
| `lookAtCamera` | boolean | `true` | Billboard mode. `true` = always faces player's camera. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Rich text tags:** `<b>bold</b>`, `<i>italic</i>`, `<u>underline</u>`, `<color=#FF0000>colored</color>` (note: `#` prefix is required inside the color tag).

**Dynamic variables:** Use `|variableName|` to display a variable's current value inline. Example: `"Score: |coins|"` renders as `"Score: 42"`.

**Orientation:** When `lookAtCamera` is `false`, text faces the +Z direction. A player looking toward -Z will see it correctly. Rotate 180 degrees around Y to flip it for players facing +Z.

**Example:**

`roomItems["3"]`:
```json
{
  "prefabName": "WorldText",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 3, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["3"]`:
```json
"{\"text\":\"<b><color=#FFD700>Welcome!</color></b>\\nScore: |coins|\",\"lookAtCamera\":true,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### Portal

Teleportation between rooms or to named spawn points.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `id` | string | -- | Destination room UUID. Must match `contentString`. |
| `sn` | string | `""` | Spawn point name at destination. `""` = default spawn. |
| `auto` | boolean | -- | `true` = instant teleport on contact. Omit for press-to-interact. |
| `cm` | string | -- | Custom message. Displays as "Press X to [message]". |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** Must contain the destination room UUID (same value as `id` in logic).

**Example -- auto-teleport to named spawn:**

`roomItems["4"]`:
```json
{
  "prefabName": "Portal",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 10, "y": 0.5, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 2, "y": 3, "z": 2},
  "contentString": "fc77aeca-56cd-4de6-a3dd-33559be0eb07",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["4"]`:
```json
"{\"id\":\"fc77aeca-56cd-4de6-a3dd-33559be0eb07\",\"sn\":\"RedSpawn1\",\"auto\":true,\"cm\":\"teleport\",\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### SpawnPoint

Defines where players appear when entering or teleporting into a room.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `n` | string | `""` | Spawn name. `""` = default spawn. Any string = named spawn. |
| `r` | float | `0.0` | Facing direction in degrees. `0` = faces +Z. |
| `absPos` | `{x, y, z}` | -- | Absolute world position (optional, set by editor) |
| `absRot` | `{x, y, z, w}` | -- | Absolute world rotation (optional, set by editor) |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |

**Behavior:**
- Default spawn (`n: ""`) -- used when entering a room or through a portal without a spawn name.
- Named spawn -- used when a Portal's `sn` field matches this name.
- Multiple spawns with the same name -- player is randomly assigned to one.

**Example -- named spawn:**

`roomItems["5"]`:
```json
{
  "prefabName": "SpawnPoint",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 5, "y": 0.2, "z": 3},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 0.3, "y": 0.3, "z": 0.3},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["5"]`:
```json
"{\"n\":\"RedSpawn1\",\"r\":90.0,\"Tasks\":[]}"
```

> **Note:** Scale is always `{0.3, 0.3, 0.3}` for spawn points.

---

## Models

### GLB

Static or animated 3D model loaded from a GLB file URL.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `s` | boolean | `true` | Shadows. `false` = no shadows (improves performance). |
| `c` | boolean | `true` | Collider. `false` = no collision. |
| `l` | boolean | `true` | Local animation. `true` = independent per client. `false` = synced. |
| `f` | boolean | -- | Camera fade. `true` = fades instead of camera collision. |
| `r` | boolean | -- | Remove first frame. `true` = removes frame 0 for animations. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** Public URL to the `.glb` model file.

**`scale`:** Proportional multiplier on the model's native size. `{1,1,1}` = original size.

**Example:**

`roomItems["6"]`:
```json
{
  "prefabName": "GLB",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 3, "y": 0, "z": 5},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "https://cdn.theportal.to/uploads/models/chair.glb",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["6"]`:
```json
"{\"s\":true,\"c\":true,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### GlbCollectable

Pickupable 3D model that modifies a variable when collected by a player.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `valueLabel` | string | -- | Variable name to modify (e.g. `"coins"`) |
| `valueChange` | integer | `1` | Amount to add or subtract |
| `op` | integer | -- | Operation. Omit = add. `2` = subtract. |
| `displayValue` | boolean | -- | `true` = show UI with current value on collection |
| `a` | boolean | `true` | Animation. `true` = rotates. `false` = static. |
| `se` | string | -- | Sound effect URL (MP3) played on collection |
| `l` | boolean | `true` | Local animation. `true` = per-client. |
| `minRespawnTime` | float | -- | Minimum seconds before respawn |
| `maxRespawnTime` | float | -- | Maximum seconds before respawn (random between min/max) |
| `minDespawnTime` | float | -- | Minimum seconds before auto-despawn |
| `maxDespawnTime` | float | -- | Maximum seconds before auto-despawn |
| `randomRadius` | float | -- | Respawn radius in meters from original position |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** GLB model URL. **Must** append `?dynamic=true` to the URL.

**Example:**

`roomItems["7"]`:
```json
{
  "prefabName": "GlbCollectable",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 5, "y": 1, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 0.4, "y": 0.4, "z": 0.4},
  "contentString": "https://cdn.theportal.to/uploads/models/coin.glb?dynamic=true",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["7"]`:
```json
"{\"valueLabel\":\"coins\",\"valueChange\":1,\"displayValue\":true,\"a\":true,\"se\":\"https://cdn.theportal.to/uploads/audio/coin-collect.mp3\",\"minRespawnTime\":3.0,\"maxRespawnTime\":5.0,\"Tasks\":[],\"ViewNodes\":[]}"
```

> **Important:** The `?dynamic=true` query parameter on the `contentString` URL is required for collectibles to function.

---

### Destructible

3D model that can be destroyed by players using guns. Plays a particle explosion on destruction and respawns after a delay.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `maxHealth` | integer | `100` | Health points before destruction |
| `respawnTime` | float | -- | Seconds before reappearing after destruction |
| `multiplayer` | boolean | -- | `true` = shared destruction state across all players |
| `showHealthBar` | boolean | `true` | `false` = hide the health bar |
| `destructionEffect` | object | -- | Particle explosion configuration (see below) |
| `particleOrigin` | object | -- | Transform for particle spawn point |
| `healthBarPos` | object | -- | Transform for health bar position |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`destructionEffect` object:**

| Field | Type | Description |
|-------|------|-------------|
| `particleCount` | integer | Number of particles spawned |
| `minParticleSize` | float | Minimum particle size |
| `maxParticleSize` | float | Maximum particle size |
| `minParticleSpeed` | float | Minimum particle speed |
| `maxParticleSpeed` | float | Maximum particle speed |
| `particleLifetime` | float | How long particles last (seconds) |
| `radius` | float | Explosion radius |

**`particleOrigin` object:**

| Field | Type | Description |
|-------|------|-------------|
| `rotation` | `[qx, qy, qz, qw]` | Quaternion as array |
| `scale` | `[x, y, z]` | Scale as array |

**`healthBarPos` object:**

| Field | Type | Description |
|-------|------|-------------|
| `position` | `[x, y, z]` | Offset from item center |
| `rotation` | `[qx, qy, qz, qw]` | Quaternion as array |
| `scale` | `[x, y, z]` | Scale as array |

**`contentString`:** Public URL to the `.glb` model file.

**Example:**

`roomItems["8"]`:
```json
{
  "prefabName": "Destructible",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 1, "z": 5},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "https://cdn.theportal.to/uploads/models/crate.glb",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["8"]`:
```json
"{\"maxHealth\":100,\"respawnTime\":10.0,\"multiplayer\":true,\"showHealthBar\":true,\"destructionEffect\":{\"particleCount\":40,\"minParticleSize\":0.01,\"maxParticleSize\":0.4,\"minParticleSpeed\":1.0,\"maxParticleSpeed\":6.0,\"particleLifetime\":5.0,\"radius\":2.0},\"particleOrigin\":{\"rotation\":[0.0,0.0,0.0,1.0],\"scale\":[1.0,1.0,1.0]},\"healthBarPos\":{\"position\":[0.0,2.0,0.0],\"rotation\":[0.0,0.0,0.0,1.0],\"scale\":[1.0,1.0,1.0]},\"Tasks\":[],\"ViewNodes\":[]}"
```

---

## Gameplay

### Trigger

Invisible zone that activates events when players enter, exit, or press a key while inside.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `events` | array | `[]` | Event array. Usually `[]` when using Tasks. |
| `pressBtn` | boolean | -- | `true` = require key press while inside zone. Omit for auto-trigger. |
| `keyCode` | string | -- | Key to press (e.g. `"X"`, `"H"`, `"E"`). Only used when `pressBtn` is `true`. |
| `cm` | string | `""` | Custom message. Displays as "Press [key] to [message]". |
| `opacity` | float | -- | Editor-only opacity (0.0--1.0). Does not affect gameplay. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Important:** Trigger cubes are **invisible during play**. Never use visibility-dependent triggers (`OnClickEvent`, `OnHoverStartEvent`, `OnHoverEndEvent`) on Trigger items. Use `OnEnterEvent` and `OnExitEvent` triggers only. For click/hover interactions, use visible items like `ResizableCube` or `GLB`.

**Example -- auto-trigger zone:**

`roomItems["9"]`:
```json
{
  "prefabName": "Trigger",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 0.5, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 5, "y": 2, "z": 5},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["9"]`:
```json
"{\"events\":[],\"cm\":\"\",\"Tasks\":[],\"ViewNodes\":[]}"
```

**Example -- press X to activate:**

`logic["9"]` (press-to-interact variant):
```json
"{\"events\":[],\"pressBtn\":true,\"keyCode\":\"X\",\"cm\":\"activate switch\",\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### JumpPad

Launches players into the air when stepped on.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `p` | float | -- | Launch power. Higher = more height/distance. |

> **Power reference:** The editor slider ranges from 1--10. Setting 1 is approximately a normal jump (~1.63m height). Setting 3 gives roughly 6.73m height and 22.5m horizontal distance.

**Example:**

`roomItems["10"]`:
```json
{
  "prefabName": "JumpPad",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 2, "y": 0.5, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1.5, "y": 1.5, "z": 1.5},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["10"]`:
```json
"{\"p\":6.9}"
```

---

### 9Cube (Elemental Cube)

Animated elemental block with rounded corners. Works like a ResizableCube but with an animated texture. The element type is set via `contentString`.

**`contentString` values:**

| Value | Description |
|-------|-------------|
| `lava` | Lava texture |
| `hotlava` | Hot lava texture (alternate lava variant) |
| `water` | Water texture |

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `GLBUrl` | string | (required) | Always `"https://dwh7ute75zx34.cloudfront.net/Models/08_09/9SliceBlock_Rig_Empty.glb"` |
| `c` | string | (required) | Always empty string `""` |
| `s` | float | -- | Texture scale. Higher = larger visual texture. |
| `t` | float | -- | Transparency. `0.0` = fully transparent, `1.0` = fully opaque. |
| `e` | float | -- | Emission/glow intensity |
| `nc` | boolean | -- | No collider. `true` = players pass through. |
| `so` | boolean | -- | Shadow off. `true` = no shadows. |
| `nav` | boolean | -- | Nav mesh. `true` = AI-walkable surface. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Example:**

`roomItems["11"]`:
```json
{
  "prefabName": "9Cube",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 0.5, "z": 8},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 3, "y": 0.5, "z": 3},
  "contentString": "lava",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["11"]`:
```json
"{\"GLBUrl\":\"https://dwh7ute75zx34.cloudfront.net/Models/08_09/9SliceBlock_Rig_Empty.glb\",\"c\":\"\",\"e\":1.0,\"nc\":true,\"so\":true,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### Gun

Pickupable weapon. Deals damage to other players and Destructible items.

**Logic fields -- Weapon Type:**

| Field | Type | Description |
|-------|------|-------------|
| `weaponType` | integer | `1` = Pistol, `2` = Rifle, `3` = Shotgun |

**Logic fields -- Damage:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `maxDamage` | integer | `25` | Maximum damage at close range |
| `minDamage` | integer | `10` | Minimum damage at long range |
| `minDamageDistance` | float | `8` | Distance (meters) where damage falloff starts |
| `maxDamageDistance` | float | `50` | Distance (meters) where damage reaches minimum |

**Logic fields -- Firing:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `firerate` | float | `0.8` | Seconds between shots |
| `projectilesPerShot` | integer | `8` | Pellets/bullets per shot |
| `dispersion` | float | `5.0` | Bullet spread angle (degrees) |
| `automaticWeapon` | boolean | `false` | `true` = fires continuously while holding trigger |
| `maxRange` | float | `30` | Maximum bullet travel distance (meters) |

**Logic fields -- Ammo:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `isInfinityAmmo` | boolean | `false` | `true` = infinite ammo, never needs reloading |
| `infiniteReserveAmmo` | boolean | `false` | `true` = infinite reserve, still reloads clips |
| `clipSize` | integer | `8` | Magazine capacity |
| `startLoaded` | boolean | `true` | `true` = starts with a full magazine |
| `startingReserveAmmo` | integer | `0` | Reserve ammo on pickup |
| `reloadTime` | float | `1.0` | Reload duration (seconds) |
| `autoReload` | boolean | `false` | `true` = auto reload when empty |
| `dontUseReload` | boolean | `false` | `true` = disable reload mechanic entirely |
| `reloadOneByOne` | boolean | `false` | `true` = reload one round at a time (shotgun style) |

**Logic fields -- Recoil:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `cameraStability` | float | `0.5` | Camera stability. Lower = more shake. |
| `recoilUp` | float | `2.0` | Upward recoil per shot |
| `recoilRight` | float | `2.5` | Maximum rightward recoil |
| `recoilLeft` | float | `-2.5` | Maximum leftward recoil |

**Logic fields -- Audio:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `gunShotVolume` | float | `1.0` | Gunshot sound volume |
| `reloadVolume` | float | `1.0` | Reload sound volume |
| `audioMaxVolumeDistance` | float | `10` | Distance (meters) for full volume |
| `audioMinVolumeDistance` | float | `50` | Distance (meters) where sound fades to zero |
| `customGunShotUrl` | string | `""` | URL to custom gunshot sound (MP3) |

**Logic fields -- Display & Behavior:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `multiplayer` | boolean | `false` | `true` = syncs across all players |
| `canCollectByCollision` | boolean | `true` | `true` = pick up by walking over it |
| `showCrosshair` | boolean | `true` | Display crosshair when aiming |
| `showHitmarkers` | boolean | `true` | Show hit feedback markers |
| `displayAmmoCount` | boolean | `true` | Show ammo counter UI |
| `clipAmmoLabel` | string | `"Clip Ammo"` | Label for clip ammo display |
| `reserveAmmoLabel` | string | `"Reserve Ammo"` | Label for reserve ammo display |
| `gunColor` | string | `"000000"` | Gun model color (6-char hex, no `#`) |
| `animateGun` | boolean | `true` | Enable gun animations |

**Logic fields -- Model:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `s` | boolean | `true` | Shadows |
| `l` | boolean | `true` | Local animation |
| `c` | boolean | `true` | Collider |
| `f` | boolean | `false` | Camera fade |
| `r` | boolean | `false` | Remove first frame |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Example -- Pistol:**

`roomItems["12"]`:
```json
{
  "prefabName": "Gun",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 0.5, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["12"]`:
```json
"{\"weaponType\":1,\"maxDamage\":20,\"minDamage\":10,\"minDamageDistance\":10.0,\"maxDamageDistance\":40.0,\"firerate\":0.2,\"projectilesPerShot\":1,\"dispersion\":0.5,\"clipSize\":12,\"startLoaded\":true,\"startingReserveAmmo\":36,\"reloadTime\":1.5,\"autoReload\":true,\"maxRange\":50.0,\"isInfinityAmmo\":false,\"cameraStability\":0.7,\"recoilUp\":1.5,\"recoilRight\":0.5,\"recoilLeft\":-0.5,\"multiplayer\":true,\"showCrosshair\":true,\"showHitmarkers\":true,\"displayAmmoCount\":true,\"gunColor\":\"000000\",\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### Shotgun

Weapon variant with a different visual model. Functionally identical to Gun -- uses all the same logic fields. Setting `weaponType: 3` on a Gun item also produces a shotgun model, so this prefab is an alternative way to create shotgun-type weapons.

**Example:**

`roomItems["13"]`:
```json
{
  "prefabName": "Shotgun",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 3, "y": 0.5, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["13"]`:
```json
"{\"weaponType\":3,\"maxDamage\":25,\"minDamage\":10,\"firerate\":0.8,\"projectilesPerShot\":8,\"dispersion\":5.0,\"clipSize\":8,\"startLoaded\":true,\"startingReserveAmmo\":24,\"reloadTime\":1.0,\"reloadOneByOne\":true,\"autoReload\":false,\"maxRange\":30.0,\"multiplayer\":true,\"Tasks\":[],\"ViewNodes\":[]}"
```

See [Gun](#gun) for the full field reference.

---

### CameraObject

Defines a named camera position/state. Linked to `customCameraStates` in room settings via the `sn` field.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `fov` | float | -- | Field of view in degrees |
| `sn` | string | -- | State name. Must match a `customCameraStates[].stateName` in room settings. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Usage:** Place CameraObject items at desired camera viewpoints. Set `sn` to match a `customCameraStates` entry in settings. Use the `ChangeCamState` effect to switch players to this camera view.

**Example:**

`roomItems["14"]`:
```json
{
  "prefabName": "CameraObject",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 2.238, "y": 0.582, "z": 2.270},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0.075, "y": -0.075, "z": -0.703, "w": 0.703},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["14"]`:
```json
"{\"fov\":86.0,\"sn\":\"crewmate\",\"Tasks\":[],\"ViewNodes\":[]}"
```

---

## Media

### DefaultPainting (Image)

2D image placed in 3D space.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `t` | boolean | -- | Transparency. `true` = PNG alpha channel is respected. |
| `b` | boolean | -- | Borderless. `true` = no frame around the image. |
| `e` | float | -- | Emission/glow intensity. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** Public image URL.

**`scale`:** `x` = width, `y` = height, `z` = thickness (keep thin, e.g. `0.03`). Size is relative to the image's pixel dimensions.

**Orientation:** Images default to lying flat on the ground. You must set a rotation quaternion to orient them upright. Images can also be parented to a ResizableCube via `parentItemID` for wall mounting.

**Example:**

`roomItems["15"]`:
```json
{
  "prefabName": "DefaultPainting",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 2, "z": -5},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": -0.7071068, "y": 0, "z": 0, "w": 0.7071068},
  "scale": {"x": 3.0, "y": 2.0, "z": 0.03},
  "contentString": "https://cdn.theportal.to/uploads/room-id/painting.png",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["15"]`:
```json
"{\"t\":true,\"b\":true,\"e\":0.5,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### DefaultVideo

MP4 video placed in 3D space. Only accepts `.mp4` files.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `b` | boolean | -- | Borderless. `true` = no frame around the video. |
| `e` | float | -- | Emission/glow intensity. |
| `fStart` | float | -- | Sound falloff start distance (meters). Beyond this, audio begins to fade. |
| `sEnd` | float | -- | Sound falloff end distance (meters). At this distance, audio is silent. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** Public `.mp4` video URL.

**`scale`:** `x` = width, `y` = height, `z` = thickness. Size is relative to the video's pixel dimensions.

**Orientation:** Unlike images, videos display upright by default. Identity rotation `{x:0, y:0, z:0, w:1}` produces a correctly oriented video.

**Example:**

`roomItems["16"]`:
```json
{
  "prefabName": "DefaultVideo",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 1.5, "z": -8},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 4.0, "y": 2.25, "z": 0.03},
  "contentString": "https://cdn.theportal.to/uploads/room-id/videos/intro.mp4",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["16"]`:
```json
"{\"b\":true,\"e\":1.0,\"fStart\":5.0,\"sEnd\":20.0,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### PlaceableTV (Screenshare)

Screen sharing display. Players can share their screen in-world.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `useSpatialAudio` | boolean | -- | `true` = audio volume changes based on player distance |
| `fullVolumeRange` | float | -- | Distance (meters) within which audio plays at full volume. Only relevant when `useSpatialAudio` is `true`. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Orientation:** Displays upright by default with identity rotation.

**Example:**

`roomItems["17"]`:
```json
{
  "prefabName": "PlaceableTV",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 5, "y": 1, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 2, "y": 2, "z": 2},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["17"]`:
```json
"{\"useSpatialAudio\":true,\"fullVolumeRange\":5.0,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

## Lighting

### Light

Static point light source. Emits light in all directions from its position.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `c` | string | `"FFFFFF"` | Color as 6-char hex (no `#` prefix) |
| `b` | float | -- | Brightness intensity. Higher = brighter. |
| `r` | float | -- | Range in meters. How far the light reaches. |
| `no` | boolean | -- | Night only. `true` = only active when room is in night mode. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Toggling lights:** Lights are always on by default. Use `HideObjectEvent` to turn off and `ShowObjectEvent` to turn on via triggers.

**Example:**

`roomItems["18"]`:
```json
{
  "prefabName": "Light",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 3, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["18"]`:
```json
"{\"c\":\"FFB200\",\"b\":2.5,\"r\":10.0,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### BlinkLight

Animated flashing light. Inherits all Light fields with additional blink controls.

**Logic fields (in addition to Light fields):**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `c` | string | `"FFFFFF"` | Color as 6-char hex (no `#` prefix) |
| `b` | float | -- | Brightness intensity |
| `r` | float | -- | Range in meters |
| `bd` | float | -- | Blink duration. How long the light stays on (seconds). |
| `bi` | float | -- | Blink interval. Time between blinks (seconds). |
| `no` | boolean | -- | Night only. `true` = only active in night mode. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Example:**

`roomItems["19"]`:
```json
{
  "prefabName": "BlinkLight",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 5, "y": 3, "z": 5},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["19"]`:
```json
"{\"c\":\"FF0000\",\"b\":3.0,\"r\":7.0,\"bd\":1.2,\"bi\":2.6,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### SpotLight

Directional cone light. Points in the direction set by the item's `rot` quaternion.

**Logic fields (in addition to Light base fields):**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `c` | string | `"FFFFFF"` | Color as 6-char hex (no `#` prefix) |
| `b` | float | -- | Brightness intensity |
| `r` | float | -- | Range in meters |
| `ang` | float | -- | Cone angle in degrees. Smaller = narrow beam, larger = wide flood. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Example:**

`roomItems["20"]`:
```json
{
  "prefabName": "SpotLight",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 4, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0.7071068, "y": 0, "z": 0, "w": 0.7071068},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["20"]`:
```json
"{\"c\":\"FFFFFF\",\"b\":2.0,\"r\":8.0,\"ang\":60.0,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

## Display

### Leaderboard

Displays player rankings and scores. The visual style is chosen via `contentString`.

**`contentString` values (leaderboard models):**

| Style | contentString |
|-------|---------------|
| Black / Neon Blue | `~1slpk_Leaderboard_Black_NeonBlue.glb?alt=media&token=8b518415-b51b-4264-ae7e-d49465260757` |
| Gray / Neon Orange | `~5wnot_Leaderboard_Gray_NeonOrange.glb?alt=media&token=5312ebfe-b00b-4f99-ad4b-a72bd518a74a` |
| Screen Only | `https://firebasestorage.googleapis.com/v0/b/portals-1b487.appspot.com/o/GLBs%2F00L_screenLeaderboard.glb?alt=media&token=b1f9eef5-ee70-4d5e-a9ee-3e8e2ef26e59?screenOnly=true` |

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `gn` | string | -- | Game name displayed on the leaderboard |
| `ln` | string | -- | Score label. **Must exactly match** the variable or timer name you want to display. |
| `tb` | boolean | -- | Time-based mode. `true` = timer mode. Omit or `false` = numeric points mode. |
| `ci` | string | `""` | Custom identifier. `""` for standard score tracking. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**Wiring:**

| Tracking | `ln` value | `tb` value |
|----------|-----------|-----------|
| Numeric variable (points, coins, kills) | Exact variable name (e.g. `"coins"`) | `false` / omit |
| Timer | Exact timer name (e.g. `"run_time"`) | `true` |

**Dimensions:** The standing models are approximately 2m wide by 3m tall at scale 1. Place at `y: 0.75` to sit flush on the floor.

**Example:**

`roomItems["21"]`:
```json
{
  "prefabName": "Leaderboard",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 0.75, "z": -10},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "~1slpk_Leaderboard_Black_NeonBlue.glb?alt=media&token=8b518415-b51b-4264-ae7e-d49465260757",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["21"]`:
```json
"{\"gn\":\"Top Traders\",\"ln\":\"coins\",\"ci\":\"\",\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### Chart

3D candlestick chart displaying a Solana token's price. Always displays 25 candles.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `t` | integer | `0` | Time interval per candle. `0` = 1 min, `1` = 15 min, `2` = 60 min. |
| `h` | float | -- | Candle height scale. Higher = taller candles. |
| `r` | float | `0.0` | Curve rotation (degrees). `0.0` = flat. `14.4` = perfect circle (360/25 candles). |
| `c` | boolean | `true` | Collision. `true` = solid. `false` = players pass through. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** Solana token address.

**Dimensions:** At scale 1, the chart is approximately 7m wide by 3m tall.

**Orientation:** Requires a 90-degree Y rotation for proper display: `rot: {x:0, y:0.7071068, z:0, w:0.7071068}`.

**Example:**

`roomItems["22"]`:
```json
{
  "prefabName": "Chart",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 0, "y": 0.5, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0.7071068, "z": 0, "w": 0.7071068},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "PRTLSwfLzpVGSAQiUfXEenJkq1cwTsEcsn1hPL9zwwg",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["22"]`:
```json
"{\"t\":0,\"h\":11.0,\"r\":0.0,\"c\":true,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

### GLBSign (Billboard)

Pre-built hanging sign model with a customizable image display.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `GLBUrl` | string | (required) | Billboard model URL. Must be one of the standard URLs listed below. |
| `c` | string | -- | Border color as 6-char hex (no `#` prefix) |
| `e` | float | -- | Emission/glow intensity |
| `so` | boolean | -- | Shadow off. `true` = no shadows. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** Image URL displayed on the sign face.

**Standard billboard model URLs:**

| Sign Type | GLBUrl |
|-----------|--------|
| 3-Sided A | `https://dwh7ute75zx34.cloudfront.net/Models/08_09/HangingSigns_3Sided_A_Rig.glb` |
| Medium Vertical A | `https://dwh7ute75zx34.cloudfront.net/Models/08_09/HangingSigns_MediumVertical_A_Rig.glb?selectedID=0` |
| Medium Vertical B | `https://dwh7ute75zx34.cloudfront.net/Models/08_09/HangingSigns_MediumVertical_B_Rig.glb?selectedID=0` |
| Large Vertical B | `https://dwh7ute75zx34.cloudfront.net/Models/08_09/HangingSigns_LargeVertical_B_Rig.glb?selectedID=0` |
| Small Square A (with attachments) | `https://dwh7ute75zx34.cloudfront.net/Models/08_09/HangingSigns_SmallSquare_A_Rig.glb` |
| Small Square B (with attachments) | `https://dwh7ute75zx34.cloudfront.net/Models/08_09/HangingSigns_SmallSquare_B_Rig.glb` |
| Small Square A (no attachments) | `https://firebasestorage.googleapis.com/v0/b/portals-1b487.appspot.com/o/GLBs%2FHanging%20Signs%20SmallSquare%20A%20No%20Attachments_HangingSigns_SmallSquare_A_NoAttachments.glb?alt=media&token=22da1096-457e-42f8-878e-da6912b5f4c5` |
| Small Square B (no attachments) | `https://firebasestorage.googleapis.com/v0/b/portals-1b487.appspot.com/o/GLBs%2FHanging%20Signs%20Small%20Square%20B%20No%20Attachments_HangingSigns_SmallSquare_B_NoAttachments.glb?alt=media&token=ab45dddf-50e7-429f-85de-e53b3cc7c0ad` |

**Example:**

`roomItems["23"]`:
```json
{
  "prefabName": "GLBSign",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": -3, "y": 2, "z": 0},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "https://cdn.theportal.to/uploads/room-id/sign-image.png",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["23"]`:
```json
"{\"GLBUrl\":\"https://dwh7ute75zx34.cloudfront.net/Models/08_09/HangingSigns_SmallSquare_A_Rig.glb\",\"c\":\"449C18\",\"e\":1.0,\"so\":true,\"Tasks\":[],\"ViewNodes\":[]}"
```

---

## Interactive

### GLBNPC (NPC)

Interactive non-player character with dialogue, animations, and optional AI chat.

**Logic fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `n` | string | -- | NPC display name |
| `a` | string | `""` | Default animation. `""` = idle. See animation list below. |
| `p` | string | -- | AI personality prompt. When set, the NPC uses this as a system prompt for player conversations. |
| `bq` | boolean | `true` | Enabled. Must be `true`. |
| `swn` | boolean | -- | Show when near. `true` = NPC dialogue appears automatically when player approaches. |
| `events` | array | `[]` | Event array. Usually `[]`. |
| `tags` | array | `[]` | Tag array. Usually `[]`. |
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** GLB avatar model URL. For rigged models (with skeleton/animations), use the URL directly. For non-rigged (static) models, append `?nonrigged=true`.

**Positioning:** NPCs sit on the ground at Y=0 (not Y=0.5 like cubes).

**Available animations:**

| Animation |
|-----------|
| `""` (idle) |
| `Sitting` |
| `Can Can` |
| `Wave` |
| `Salute` |
| `Jive` |
| `Salsa` |
| `Shuffling` |
| `Chicken` |
| `Slide n Jive` |
| `Robot` |

**Example:**

`roomItems["24"]`:
```json
{
  "prefabName": "GLBNPC",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": -5, "y": 0, "z": 3},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "https://cdn.theportal.to/uploads/models/guard.glb",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["24"]`:
```json
"{\"n\":\"Guard\",\"a\":\"Salute\",\"p\":\"You are a palace guard. Be stern but helpful. You know the location of the hidden treasure but will only reveal it if the player says the secret phrase.\",\"bq\":true,\"swn\":true,\"events\":[],\"tags\":[],\"Tasks\":[],\"ViewNodes\":[]}"
```

---

## Effects

### Addressable (VFX)

Pre-built visual effects (particles, fire, explosions, lightning) from the Portals asset library.

**Logic fields:**

No type-specific logic fields. Only the standard `Tasks` and `ViewNodes`.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `Tasks` | array | `[]` | Trigger/effect subscriptions |
| `ViewNodes` | array | `[]` | Always `[]` |

**`contentString`:** Format is `FurnitureAddressables/{EffectName}`. This is NOT a URL -- it references a built-in Unity asset.

**Notes:**
- Effects play continuously by default (looping particle systems).
- Use `ShowObjectEvent` / `HideObjectEvent` effects via triggers to toggle VFX on/off.
- Addressable items have colliders enabled by default. Set `"noCollide": true` in the item data to disable.

**Available effects:**

#### Particles

| contentString | Description |
|---------------|-------------|
| `FurnitureAddressables/DustParticles` | Ambient floating dust motes |
| `FurnitureAddressables/ParticlesExplosion1` | Particle burst variant 1 |
| `FurnitureAddressables/ParticlesExplosion2` | Particle burst variant 2 |
| `FurnitureAddressables/ParticlesExplosion3` | Particle burst variant 3 |
| `FurnitureAddressables/ParticlesExplosion4` | Particle burst variant 4 |
| `FurnitureAddressables/ParticlesExplosion5` | Particle burst variant 5 |

#### Fire

| contentString | Description |
|---------------|-------------|
| `FurnitureAddressables/Fire` | Standard fire |
| `FurnitureAddressables/Fire1` | Fire variant 1 |
| `FurnitureAddressables/Fire2` | Fire variant 2 |
| `FurnitureAddressables/Fire3` | Fire variant 3 |

#### Bomb Explosions

| contentString | Description |
|---------------|-------------|
| `FurnitureAddressables/ExplosionBomb1` | Bomb explosion variant 1 |
| `FurnitureAddressables/ExplosionBomb2` | Bomb explosion variant 2 |
| `FurnitureAddressables/ExplosionBomb3` | Bomb explosion variant 3 |
| `FurnitureAddressables/ExplosionBomb4` | Bomb explosion variant 4 |
| `FurnitureAddressables/ExplosionBomb5` | Bomb explosion variant 5 |
| `FurnitureAddressables/ExplosionBomb6` | Bomb explosion variant 6 |
| `FurnitureAddressables/ExplosionBomb7` | Bomb explosion variant 7 |

#### Ring Explosions

| contentString | Description |
|---------------|-------------|
| `FurnitureAddressables/ExplosionRing1` | Expanding ring explosion |
| `FurnitureAddressables/ExplosionRings2` | Multi-ring variant 2 |
| `FurnitureAddressables/ExplosionRings3` | Multi-ring variant 3 |

> **Note:** `ExplosionRing1` is singular, but `ExplosionRings2` and `ExplosionRings3` are plural. Use exact names.

#### Other Explosions

| contentString | Description |
|---------------|-------------|
| `FurnitureAddressables/MagneticExplosion` | Magnetic field burst |
| `FurnitureAddressables/NuclearExplosion` | Mushroom cloud / nuclear blast |
| `FurnitureAddressables/SmokeExplosion1` | Smoke burst variant 1 |
| `FurnitureAddressables/SmokeExplosion2` | Smoke burst variant 2 |

#### Wave Explosions

| contentString | Description |
|---------------|-------------|
| `FurnitureAddressables/ShockExplosion` | Shockwave burst |
| `FurnitureAddressables/WavesExplosion` | Expanding wave explosion |

#### Lightning

| contentString | Description |
|---------------|-------------|
| `FurnitureAddressables/LightningBall1` | Ball lightning / electric sphere |
| `FurnitureAddressables/LightningExplosion1` | Lightning burst variant 1 |
| `FurnitureAddressables/LightningExplosion2` | Lightning burst variant 2 |
| `FurnitureAddressables/LightningExplosion3` | Lightning burst variant 3 |
| `FurnitureAddressables/LightningParticlesTree` | Branching lightning tree |
| `FurnitureAddressables/LightningShock1` | Electric shock effect |
| `FurnitureAddressables/LightningStrike1` | Lightning bolt strike |
| `FurnitureAddressables/LightningWave3` | Lightning wave variant 3 |
| `FurnitureAddressables/LightningWaves2` | Lightning wave variant 2 |

> **Note:** `LightningWave3` is singular, but `LightningWaves2` is plural. Use exact names.

#### Energy

| contentString | Description |
|---------------|-------------|
| `FurnitureAddressables/AtomBall1` | Atomic energy sphere variant 1 |
| `FurnitureAddressables/AtomBall2` | Atomic energy sphere variant 2 |
| `FurnitureAddressables/FireBall1` | Fireball projectile effect |

#### Other

| contentString | Description |
|---------------|-------------|
| `FurnitureAddressables/LineWaves1` | Undulating line wave pattern |
| `FurnitureAddressables/Portal` | Swirling portal VFX |

**Example:**

`roomItems["25"]`:
```json
{
  "prefabName": "Addressable",
  "parentItemID": 0,
  "currentEditornetId": 0,
  "pos": {"x": 5, "y": 0.5, "z": 10},
  "modelsize": {"x": 0, "y": 0, "z": 0},
  "modelCenter": {"x": 0, "y": 0, "z": 0},
  "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
  "scale": {"x": 1, "y": 1, "z": 1},
  "contentString": "FurnitureAddressables/Fire2",
  "interactivityType": 0,
  "interactivityURL": "",
  "hoverTitle": "",
  "hoverBodyContent": "",
  "ImageInteractivityDetails": {"buttonText": "", "buttonURL": ""},
  "sessionData": "",
  "instanceId": "",
  "placed": true,
  "locked": false,
  "superLocked": false
}
```

`logic["25"]`:
```json
"{\"Tasks\":[],\"ViewNodes\":[]}"
```

---

## Coordinate System Reference

| Concept | Value |
|---------|-------|
| Ground plane | Y = 0 |
| Up direction | +Y |
| Default facing | +Z |
| Identity rotation | `{"x": 0, "y": 0, "z": 0, "w": 1}` |
| 1x1 cube on ground | Center at Y = 0.5 |
| GLB model facing | +Z in Portals |
| Rotation formula | `facing_deg = atan2(target_x, target_z)` |
| 90-degree Y rotation | `{"x": 0, "y": 0.7071068, "z": 0, "w": 0.7071068}` |
| 180-degree Y rotation | `{"x": 0, "y": 1, "z": 0, "w": 0}` |

**Rotation direction mapping:**

| Direction | Y-rotation degrees | Quaternion |
|-----------|--------------------|------------|
| Facing +Z | 0 | `{x:0, y:0, z:0, w:1}` |
| Facing +X | 90 | `{x:0, y:0.7071068, z:0, w:0.7071068}` |
| Facing -Z | 180 | `{x:0, y:1, z:0, w:0}` |
| Facing -X | -90 (or 270) | `{x:0, y:-0.7071068, z:0, w:0.7071068}` |
