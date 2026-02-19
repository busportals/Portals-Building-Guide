# Interactions

The interaction system is how you make items in a Portals room respond to player actions. Every clickable button, walk-through trigger zone, animated door, and quest-driven cutscene is built with interactions.

Interactions live inside the `logic` object of your [room data](room-data-format.md). Each key in `logic` is an item ID, and its value is a **JSON string** containing a `Tasks` array. Each entry in `Tasks` is one interaction.

```json
{
  "roomItems": {
    "item-1": { "prefabName": "ResizableCube", "pos": {"x": 0, "y": 0.5, "z": 0} }
  },
  "logic": {
    "item-1": "{\"Tasks\":[{\"$type\":\"TaskTriggerSubscription\",\"Trigger\":{\"$type\":\"OnClickEvent\"},\"DirectEffector\":{\"Effector\":{\"$type\":\"NotificationPillEvent\",\"nt\":\"Hello!\",\"c\":\"00FF00\"},\"Id\":\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\",\"TargetState\":2,\"Name\":\"\"},\"Id\":\"f0e1d2c3-b4a5-6789-0abc-def123456789\",\"TargetState\":2,\"Name\":\"\"}]}"
  }
}
```

> **Important:** The `logic` value must be a JSON **string**, not a raw object. When constructing room data, build your Tasks array as a normal object, then `JSON.stringify()` the entire `{"Tasks": [...]}` object before inserting it into the `logic` map.

---

## Two Interaction Systems

Portals has two types of interactions, and both are entries in the same `Tasks` array:

| System | `$type` | Persistence | Quest required? | Use case |
|--------|---------|-------------|-----------------|----------|
| **Basic Interactions** | `TaskTriggerSubscription` | Not persistent | No | Direct cause-and-effect. Click a button, show a notification. |
| **Quest-Driven Effects** | `TaskEffectorSubscription` | Persistent (survives reload) | Yes | State-based behavior. Door opens when quest activates, stays open after reload. |

You can mix both types in the same `Tasks` array on the same item.

---

## Basic Interactions (TaskTriggerSubscription)

A basic interaction fires an effect immediately when a trigger occurs. No quest needed. The effect is not persistent -- if the player reloads the page, any changes made by the effect are lost.

### Structure

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": {
    "$type": "OnClickEvent"
  },
  "DirectEffector": {
    "Effector": {
      "$type": "NotificationPillEvent",
      "nt": "You clicked me!",
      "c": "00FF00"
    },
    "Id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "TargetState": 2,
    "Name": ""
  },
  "Id": "f0e1d2c3-b4a5-6789-0abc-def123456789",
  "TargetState": 2,
  "Name": ""
}
```

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `$type` | string | Yes | Always `"TaskTriggerSubscription"` |
| `Trigger` | object | Yes | The event that fires this interaction. See [Triggers](#triggers). |
| `DirectEffector` | object | Yes | Wrapper for the effect to execute |
| `DirectEffector.Effector` | object | Yes | The actual effect. See [Effects](#effects). |
| `DirectEffector.Id` | string (UUID) | Yes | Unique identifier for the effector |
| `DirectEffector.TargetState` | number | Yes | Always `2` for basic interactions |
| `DirectEffector.Name` | string | Yes | Always `""` for basic interactions |
| `Id` | string (UUID) | Yes | Unique identifier for the interaction |
| `TargetState` | number | Yes | Always `2` for basic interactions |
| `Name` | string | Yes | Always `""` for basic interactions |

### Examples

**Click to show a notification:**

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": {"$type": "OnClickEvent"},
  "DirectEffector": {
    "Effector": {
      "$type": "NotificationPillEvent",
      "nt": "Welcome to the game!",
      "c": "FFD700"
    },
    "Id": "d4a5b6c7-e8f9-0123-4567-89abcdef0123",
    "TargetState": 2,
    "Name": ""
  },
  "Id": "1a2b3c4d-5e6f-7890-1234-567890abcdef",
  "TargetState": 2,
  "Name": ""
}
```

**Walk into a trigger zone to play a sound:**

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": {"$type": "OnEnterEvent"},
  "DirectEffector": {
    "Effector": {
      "$type": "PlaySoundOnce",
      "Url": "https://example.com/doorbell.mp3",
      "Dist": 20.0
    },
    "Id": "e5f6a7b8-c9d0-1234-5678-9abcdef01234",
    "TargetState": 2,
    "Name": ""
  },
  "Id": "2b3c4d5e-6f70-8901-2345-678901abcdef",
  "TargetState": 2,
  "Name": ""
}
```

> **Note:** `OnEnterEvent` and `OnExitEvent` only work on items with `prefabName: "Trigger"`. See [Trigger Zone Triggers](#trigger-zone-only).

**Collide with an item to apply velocity (jump pad):**

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": {"$type": "OnCollideEvent"},
  "DirectEffector": {
    "Effector": {
      "$type": "AddVelocityToPlayer",
      "vel": [0, 15, 0],
      "local": false
    },
    "Id": "f6a7b8c9-d0e1-2345-6789-abcdef012345",
    "TargetState": 2,
    "Name": ""
  },
  "Id": "3c4d5e6f-7081-9012-3456-789012abcdef",
  "TargetState": 2,
  "Name": ""
}
```

**Player login triggers an effect:**

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": {"$type": "OnPlayerLoggedIn"},
  "DirectEffector": {
    "Effector": {
      "$type": "PlaySoundInALoop",
      "Url": "https://example.com/ambient.mp3",
      "Dist": -1,
      "Preload": true
    },
    "Id": "a7b8c9d0-e1f2-3456-7890-abcdef012345",
    "TargetState": 2,
    "Name": ""
  },
  "Id": "4d5e6f70-8192-0123-4567-890123abcdef",
  "TargetState": 2,
  "Name": ""
}
```

### Click-to-Advance-Quest

A special variant of `TaskTriggerSubscription` that changes a quest state directly on click, without a `DirectEffector`. This links a player click to a quest state transition.

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": {"$type": "OnClickEvent"},
  "Id": "5e6f7081-9203-1234-5678-901234abcdef",
  "TargetState": 111,
  "Name": "0_open_door",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `TargetState` | number | Encoded state transition value. See [TargetState Encoding](#targetstate-encoding). |
| `Name` | string | Quest name (e.g., `"0_open_door"`) |
| `TaskTriggerId` | string | Quest ID -- the `id` of the quest's `inProgress` entry |

This variant has **no** `DirectEffector` field. The trigger changes the quest state directly. Combine with `TaskEffectorSubscription` effects on other items to make clicking one item animate, show, or hide other items.

---

## Quest-Driven Effects (TaskEffectorSubscription)

Effects that fire when a quest changes state. These are persistent -- the state survives page reloads, and items will re-apply their effects based on the current quest state when the room loads.

Quest-driven effects require a [quest](quests.md) to be set up first.

### Structure

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "HideObjectEvent"
  },
  "Id": "6f708192-0314-2345-6789-012345abcdef",
  "TargetState": 2,
  "Name": "0_puzzle_solved",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `$type` | string | Yes | Always `"TaskEffectorSubscription"` |
| `Effector` | object | Yes | The effect to fire. See [Effects](#effects). |
| `Id` | string (UUID) | Yes | Unique identifier for this effect |
| `TargetState` | number | Conditional | Which quest state triggers this effect. **Omit entirely for state 0.** See below. |
| `Name` | string | Yes | Quest name (e.g., `"0_puzzle_solved"`) |
| `TaskTriggerId` | string | Yes | Quest ID -- the `id` of the quest's `inProgress` entry |

### TargetState Values

| Quest State | `TargetState` value | Rule |
|-------------|---------------------|------|
| **Not Active** (state 0) | *omit the field entirely* | Do NOT include `TargetState` at all |
| **Active** (state 1) | `1` | Include `"TargetState": 1` |
| **Completed** (state 2) | `2` | Include `"TargetState": 2` |

> **Critical:** State 0 must have NO `TargetState` field. Including `"TargetState": 0` will produce incorrect behavior. Omit the field entirely.

### 3-State Pattern

Items commonly have effects for all three quest states. All three entries share the same `TaskTriggerId` and `Name` but use different `TargetState` values and different `Id` values.

**Example: A platform that rises when a quest activates and returns when it completes.**

State 0 -- Not Active (platform at ground level):

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "MoveToSpot",
    "_transformState": {
      "position": [0, 1, 0],
      "rotation": [0, 0, 0, 1],
      "scale": [3, 0.2, 3],
      "duration": 0.0
    }
  },
  "Id": "aaaa1111-bbbb-2222-cccc-333344445555",
  "Name": "0_elevator",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

State 1 -- Active (platform rises):

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "MoveToSpot",
    "_transformState": {
      "position": [0, 10, 0],
      "rotation": [0, 0, 0, 1],
      "scale": [3, 0.2, 3],
      "duration": 3.0
    }
  },
  "Id": "bbbb2222-cccc-3333-dddd-444455556666",
  "TargetState": 1,
  "Name": "0_elevator",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

State 2 -- Completed (platform returns):

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "MoveToSpot",
    "_transformState": {
      "position": [0, 1, 0],
      "rotation": [0, 0, 0, 1],
      "scale": [3, 0.2, 3],
      "duration": 1.5
    }
  },
  "Id": "cccc3333-dddd-4444-eeee-555566667777",
  "TargetState": 2,
  "Name": "0_elevator",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

All three entries go in the same item's `Tasks` array alongside any other interactions on that item.

---

## Triggers

Triggers define what event fires an interaction. They go inside the `Trigger` field of a `TaskTriggerSubscription`.

### General Triggers

These work on any visible item type. Most take no extra parameters -- just `{"$type": "TriggerName"}`.

| Trigger | `$type` | Description |
|---------|---------|-------------|
| Click | `OnClickEvent` | Player clicks the item |
| Collide | `OnCollideEvent` | Player collides with the item |
| Collision Stopped | `OnCollisionStoppedEvent` | Player stops colliding |
| Hover Start | `OnHoverStartEvent` | Cursor enters the item |
| Hover End | `OnHoverEndEvent` | Cursor leaves the item |
| Player Logged In | `OnPlayerLoggedIn` | Player joins the room |
| Key Pressed | `OnKeyPressedEvent` | Player presses a key |
| Key Released | `OnKeyReleasedEvent` | Player releases a key |
| Player Died | `OnPlayerDied` | Player health reaches zero |
| Player Revived | `OnPlayerRevived` | Player revives after death |
| Player Move | `OnPlayerMove` | Player starts moving |
| Player Stopped Moving | `OnPlayerStoppedMoving` | Player stops moving |
| Mic Unmuted | `OnMicrophoneUnmuted` | Player unmutes microphone |
| Timer Stopped | `OnTimerStopped` | A timer finishes |
| Countdown Finished | `OnCountdownTimerFinished` | A countdown timer reaches zero |
| Value Updated | `ScoreTrigger` | A variable value changes |
| Animation Stopped | `OnAnimationStoppedEvent` | A PortalsAnimation finishes playing |
| Item Collected | `OnItemCollectedEvent` | A collectible item is picked up |
| Backpack Item Activated | `OnItemClickEvent` | Player activates an inventory item |
| Player Leave | `PlayerLeave` | Player leaves the room |
| Swap Volume | `SwapVolume` | Swap volume event fires |
| Item Destroyed | `OnDestroyedEvent` | A Destructible item is destroyed |

> **Visibility requirement:** `OnClickEvent`, `OnHoverStartEvent`, and `OnHoverEndEvent` require the item to be **visible** to players. Never attach these triggers to Trigger cubes (they are invisible during play). Use a `ResizableCube`, `GLB`, or other visible item type instead.

**Example -- general trigger:**

```json
{
  "Trigger": {"$type": "OnClickEvent"}
}
```

### Trigger Zone Only

These triggers **only** work on items with `prefabName: "Trigger"`. They do not work on cubes, GLBs, or any other item type.

| Trigger | `$type` | Description |
|---------|---------|-------------|
| Enter Zone | `OnEnterEvent` | Player enters the trigger zone |
| Exit Zone | `OnExitEvent` | Player exits the trigger zone |

**Example -- trigger zone enter:**

```json
{
  "Trigger": {"$type": "OnEnterEvent"}
}
```

> **Note:** Trigger cubes are invisible during play. This means click and hover triggers will not work on them, but collision-based triggers (`OnEnterEvent`, `OnExitEvent`) work by design since they detect the player walking through the zone volume.

### Gun Triggers

These triggers **only** work on items with `prefabName: "Gun"` or `"Shotgun"`.

| Trigger | `$type` | Extra Parameters |
|---------|---------|------------------|
| Gun Equipped | `OnGunEquippedTrigger` | Optional `"Delay"` (float, seconds) |
| Shot Hit | `ShotHitTrigger` | None |
| Got Kill | `GotKillTrigger` | None |
| Started Aiming | `StartedAimingTrigger` | None |
| Stopped Aiming | `StoppedAimingTrigger` | None |
| Gun Tossed | `OnGunTossedTrigger` | None |

**Example -- gun equipped with delay:**

```json
{
  "Trigger": {
    "$type": "OnGunEquippedTrigger",
    "Delay": 0.5
  }
}
```

---

## Effects

Effects define what happens when a trigger fires or a quest changes state. They go inside `DirectEffector.Effector` (for basic interactions) or directly in `Effector` (for quest-driven effects).

### No-Parameter Effects

These effects take no parameters -- the `Effector` object contains only the `$type` field.

| Effect | `$type` | Description |
|--------|---------|-------------|
| Show Object | `ShowObjectEvent` | Makes a hidden item visible |
| Hide Object | `HideObjectEvent` | Makes an item invisible |
| Show Outline | `ShowOutline` | Adds a highlight outline to the item |
| Hide Outline | `HideOutline` | Removes the highlight outline |
| Damage Over Time | `DamageOverTime` | Applies continuous damage to the player |
| Lock Movement | `LockMovement` | Freezes the player in place |
| Unlock Movement | `UnlockMovement` | Unfreezes the player |
| Start Auto Run | `StartAutoRun` | Starts automatic forward movement |
| Stop Auto Run | `StopAutoRun` | Stops automatic forward movement |
| Lock Avatar Change | `LockAvatarChange` | Prevents the player from changing avatar |
| Unlock Avatar Change | `UnlockAvatarChange` | Allows avatar changes again |
| Lock Camera | `LockCamera` | Locks the camera in its current position |
| Unlock Camera | `UnlockCamera` | Unlocks the camera |
| Toggle Free Cam | `ToggleFreeCam` | Toggles free camera mode |
| Mute Player | `MutePlayer` | Mutes the player's microphone |
| Hide All Players | `HideAllPlayersEvent` | Hides all other player avatars |
| Display Avatar Screen | `DisplayAvatarScreen` | Opens the avatar selection screen |
| Move Item to Player | `MoveItemToPlayer` | Moves this item to the player's position |
| Reset All Tasks | `ResetAllTasks` | Resets all quests to Not Active |
| Post Score to Leaderboard | `PostScoreToLeaderboard` | Posts the player's score to the leaderboard |
| Refresh Inventory | `RefreshUserInventory` | Refreshes the player's inventory |
| Change Time of Day | `ChangeTimeOfDay` | Cycles the time of day |
| Hide Token Swap | `HideSellSwap` | Hides the token swap UI |
| Equip Gun | `EquipGunEffect` | Auto-equips the gun (Gun items only) |
| Toss Gun | `TossGunEffect` | Forces the player to drop the gun (Gun items only) |
| Reset Gun | `ResetGunEffect` | Resets gun state (Gun items only) |
| Respawn Destructible | `RespawnDestructible` | Respawns a destroyed item (Destructible items only) |
| Activate Trigger Zone | `ActivateTriggerZoneEffect` | Enables a trigger zone (Trigger items only) |
| Deactivate Trigger Zone | `DeactivateTriggerZoneEffect` | Disables a trigger zone (Trigger items only) |

**Example -- hide an object when a quest completes:**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {"$type": "HideObjectEvent"},
  "Id": "7081920a-1425-3637-4849-5a6b7c8d9e0f",
  "TargetState": 2,
  "Name": "0_wall_removed",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

**Example -- equip gun on player login:**

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": {"$type": "OnPlayerLoggedIn"},
  "DirectEffector": {
    "Effector": {"$type": "EquipGunEffect"},
    "Id": "8192a0b1-c2d3-e4f5-6071-8293a4b5c6d7",
    "TargetState": 2,
    "Name": ""
  },
  "Id": "920ab1c2-d3e4-f506-7182-93a4b5c6d7e8",
  "TargetState": 2,
  "Name": ""
}
```

### Parameterized Effects

#### AddVelocityToPlayer

Applies a velocity impulse to the player.

```json
{
  "$type": "AddVelocityToPlayer",
  "vel": [0, 15, 5],
  "local": false
}
```

| Field | Type | Description |
|-------|------|-------------|
| `vel` | number[3] | Velocity vector `[x, y, z]`. Y is up. |
| `local` | boolean | `true` = relative to player facing direction, `false` = world space |

#### MoveToSpot

Animates an item's position, rotation, and scale over a duration.

```json
{
  "$type": "MoveToSpot",
  "_transformState": {
    "position": [0, 5, 0],
    "rotation": [0, 0, 0, 1],
    "scale": [1, 1, 1],
    "duration": 2.0
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `_transformState.position` | number[3] | Target position `[x, y, z]` |
| `_transformState.rotation` | number[4] | Target rotation as quaternion `[qx, qy, qz, qw]` |
| `_transformState.scale` | number[3] | Target scale `[x, y, z]` |
| `_transformState.duration` | number | Animation time in seconds. `0.0` = instant. |

#### NotificationPillEvent

Displays a toast notification on the player's screen.

```json
{
  "$type": "NotificationPillEvent",
  "nt": "You found a secret!",
  "c": "FFD700",
  "hideBackground": false
}
```

| Field | Type | Description |
|-------|------|-------------|
| `nt` | string | Notification text. Supports pipe syntax for inline variable display (see below). |
| `c` | string | Hex color code (6 characters, no `#` prefix) |
| `hideBackground` | boolean | `true` = transparent background, `false` = default background |

**Variable display in notifications:**

Use `|variableName|` to show a variable's live value inline:

```json
{
  "$type": "NotificationPillEvent",
  "nt": "You have |coins| coins!",
  "c": "00FF00"
}
```

#### TeleportEvent

Teleports the player to a spawn point, optionally in a different room.

```json
{
  "$type": "TeleportEvent",
  "id": "8d4cbf13-625f-4b90-9050-6884cd514e6a",
  "sn": "level-2-start",
  "sr": 0.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Target room ID. Use current room ID to teleport within the same room. |
| `sn` | string | Target spawn point name |
| `sr` | number | Spawn rotation offset (degrees) |

#### ChangePlayerHealth

Heals or damages the player.

**Heal:**

```json
{
  "$type": "ChangePlayerHealth",
  "healthChange": 25
}
```

**Damage:**

```json
{
  "$type": "ChangePlayerHealth",
  "op": 2,
  "healthChange": 10
}
```

| Field | Type | Description |
|-------|------|-------------|
| `healthChange` | number | Amount of health to add or remove |
| `op` | number | Operation type. Omit for heal. `2` = damage. |

#### DisplayValueEvent

Displays a variable value on the player's HUD.

```json
{
  "$type": "DisplayValueEvent",
  "label": "coins",
  "color": "FFD700"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `label` | string | Variable name to display |
| `color` | string | Hex color code (6 characters, no `#` prefix) |

#### HideValueEvent

Hides a previously displayed variable from the HUD.

```json
{
  "$type": "HideValueEvent",
  "label": "coins"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `label` | string | Variable name to hide |

#### UpdateScoreEvent

Modifies a numeric variable value.

```json
{
  "$type": "UpdateScoreEvent",
  "op": 1,
  "scoreChange": 10.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `op` | number | Operation: `1` = add, `2` = subtract, `3` = set, `4` = multiply |
| `scoreChange` | number | Value to apply with the operation |

#### UpdateScoreEventString

Sets a string variable value.

```json
{
  "$type": "UpdateScoreEventString",
  "targetText": "active",
  "label": "gameState"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `targetText` | string | The string value to set |
| `label` | string | Variable name to update |

#### FunctionEffector

Executes an NCalc expression for complex logic. See [Function Effects & NCalc](function-effects.md) for the full expression language.

```json
{
  "$type": "FunctionEffector",
  "V": "if($N{coins} >= 10.0, SetTask('shop', 'Active', 0.0), 0.0)"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `V` | string | NCalc expression to evaluate |

> **Important:** Task names in NCalc expressions omit the numbered prefix. A quest with `Name: "0_shop"` is referenced as `'shop'` (not `'0_shop'`) in `SetTask()`, `$T{}`, `$TN{}`, and `OnChange()`.

#### PlayerEmote

Makes the player perform an emote animation.

```json
{
  "$type": "PlayerEmote",
  "animationName": "wave"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `animationName` | string | Name of the emote animation |

#### SetCameraFilter

Applies an image overlay to the camera.

```json
{
  "$type": "SetCameraFilter",
  "url": "https://example.com/vignette.png",
  "alpha": 0.5
}
```

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | URL of the filter image |
| `alpha` | number | Opacity (0.0 = transparent, 1.0 = fully opaque) |

#### ChangeCameraZoom

Changes the camera zoom level.

```json
{
  "$type": "ChangeCameraZoom",
  "zoomAmount": 2.0,
  "lockZoom": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| `zoomAmount` | number | Zoom multiplier |
| `lockZoom` | boolean | `true` = prevent player from changing zoom |

#### ToggleLockCursor

Locks or unlocks the mouse cursor.

```json
{
  "$type": "ToggleLockCursor",
  "lockCursor": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| `lockCursor` | boolean | `true` = lock cursor to center, `false` = free cursor |

#### ChangeFog

Changes the fog color and distance.

```json
{
  "$type": "ChangeFog",
  "color": "1a1a2e",
  "distance": 50.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `color` | string | Hex color code (6 characters, no `#` prefix) |
| `distance` | number | Fog distance (lower = denser fog) |

#### SendMessageToIframes

Sends a text message to all iframes in the room.

```json
{
  "$type": "SendMessageToIframes",
  "iframeMsg": "game-started"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `iframeMsg` | string | Message text to send |

#### ClearLeaderboard

Clears all entries from a leaderboard.

```json
{
  "$type": "ClearLeaderboard",
  "label": "race-times"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `label` | string | Leaderboard name to clear |

#### OpenLeaderboardEffect

Opens a leaderboard UI for the player.

```json
{
  "$type": "OpenLeaderboardEffect",
  "lb": "race-times"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `lb` | string | Leaderboard name to open |

#### StartTimerEffect

Starts a named timer. Counts up by default.

```json
{
  "$type": "StartTimerEffect",
  "tn": "RaceTimer",
  "ci": "",
  "showTimerUI": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| `tn` | string | Timer name (used to reference in `StopTimerEffect`, `$N{timerName}`, etc.) |
| `ci` | string | Counter ID. Use `""`. |
| `showTimerUI` | boolean | `true` = show a visible timer on screen, `false` = silent timer |

#### StopTimerEffect

Stops a running timer. Fires the `OnTimerStopped` trigger.

```json
{
  "$type": "StopTimerEffect",
  "tn": "RaceTimer",
  "ci": ""
}
```

| Field | Type | Description |
|-------|------|-------------|
| `tn` | string | Timer name to stop |
| `ci` | string | Counter ID. Use `""`. |

#### CancelTimerEffect

Cancels a timer without firing `OnTimerStopped`.

```json
{
  "$type": "CancelTimerEffect",
  "tn": "RaceTimer"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `tn` | string | Timer name to cancel |

#### ChangeVoiceGroup

Assigns the player to a voice chat group.

```json
{
  "$type": "ChangeVoiceGroup",
  "group": "team-red"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `group` | string | Voice group name. Players in the same group can hear each other. |

#### DuplicateItem

Clones the item at a specified position with an optional auto-destroy timer.

```json
{
  "$type": "DuplicateItem",
  "TS": {
    "position": [5, 0, 0],
    "rotation": [0, 0, 0, 1],
    "scale": [1, 1, 1]
  },
  "destroyAfterTime": 5.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `TS` | object | Transform state for the clone. **Note:** Uses `TS`, not `_transformState`. |
| `TS.position` | number[3] | Clone position `[x, y, z]` |
| `TS.rotation` | number[4] | Clone rotation `[qx, qy, qz, qw]` |
| `TS.scale` | number[3] | Clone scale `[x, y, z]` |
| `destroyAfterTime` | number | Seconds before the clone is destroyed. `0` = permanent. |

> **Syntax quirk:** `DuplicateItem` uses `"TS"` for its transform, not `"_transformState"` like `MoveToSpot`.

#### PlaySoundOnce

Plays an audio file once.

```json
{
  "$type": "PlaySoundOnce",
  "Url": "https://example.com/explosion.mp3",
  "Dist": 30.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `Url` | string | URL to an MP3 file. **Note:** Capital `U`. |
| `Dist` | number | Audible distance in meters. **Note:** Capital `D`. |

> **Syntax quirk:** `PlaySoundOnce` uses capital `"Url"` and `"Dist"`, unlike most other fields.

#### PlaySoundInALoop

Plays an audio file on repeat.

```json
{
  "$type": "PlaySoundInALoop",
  "Url": "https://example.com/ambient-rain.mp3",
  "Dist": -1,
  "Preload": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| `Url` | string | URL to an MP3 file. **Note:** Capital `U`. |
| `Dist` | number | Audible distance in meters. `-1` = global (heard everywhere). **Note:** Capital `D`. |
| `Preload` | boolean | `true` = preload the audio file on room load |

#### StopSound

Stops a currently playing sound.

```json
{
  "$type": "StopSound",
  "url": "https://example.com/ambient-rain.mp3",
  "fadeOut": 2.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | URL of the sound to stop. **Note:** Lowercase `u`, unlike `PlaySoundOnce`/`PlaySoundInALoop`. |
| `fadeOut` | number | Fade-out duration in seconds |

> **Syntax quirk:** `StopSound` uses lowercase `"url"`, while `PlaySoundOnce` and `PlaySoundInALoop` use uppercase `"Url"`.

#### ChangeAudiusEffect

Changes the Audius playlist.

```json
{
  "$type": "ChangeAudiusEffect",
  "ap": "chill-vibes"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `ap` | string | Audius playlist name |

#### ChangeBloom

Changes the post-processing bloom settings.

```json
{
  "$type": "ChangeBloom",
  "Intensity": 2.0,
  "Clamp": 1.0,
  "Diffusion": 5.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `Intensity` | number | Bloom intensity |
| `Clamp` | number | Bloom brightness clamp |
| `Diffusion` | number | Bloom spread |

#### RotateSkybox

Rotates the skybox over a duration.

```json
{
  "$type": "RotateSkybox",
  "rotation": 180.0,
  "duration": 10.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `rotation` | number | Target rotation in degrees |
| `duration` | number | Animation time in seconds |

#### ChangeAvatarEffector

Changes the player's avatar.

```json
{
  "$type": "ChangeAvatarEffector",
  "Url": "https://example.com/robot-avatar.glb",
  "Persistent": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| `Url` | string | URL to a GLB avatar model |
| `Persistent` | boolean | `true` = avatar persists across sessions |

#### ChangeMovementProfile

Changes the player's movement settings.

```json
{
  "$type": "ChangeMovementProfile",
  "mvmtProfile": "swimming"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `mvmtProfile` | string | Movement profile name |

#### ChangeCamState

Changes the camera behavior.

```json
{
  "$type": "ChangeCamState",
  "camState": "first-person",
  "transitionSpeed": 1.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `camState` | string | Camera state name |
| `transitionSpeed` | number | Speed of the camera transition |

#### ChangeRoundyWearableEffector

Equips a wearable item on the player.

```json
{
  "$type": "ChangeRoundyWearableEffector",
  "ItemID": "hat-001"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `ItemID` | string | Wearable item ID |

#### PlayAnimationOnce

Plays a GLB model's embedded animation once.

```json
{
  "$type": "PlayAnimationOnce",
  "speed": 1.0
}
```

| Field | Type | Description |
|-------|------|-------------|
| `speed` | number | Playback speed. `1.0` = normal. Negative values play in reverse. |

#### IframeEvent

Opens an iframe overlay.

```json
{
  "$type": "IframeEvent",
  "url": "https://example.com/minigame"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | URL to display in the iframe |

#### IframeStopEvent

Closes an open iframe.

```json
{
  "$type": "IframeStopEvent",
  "iframeUrl": "https://example.com/minigame"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `iframeUrl` | string | URL of the iframe to close (must match the URL used in `IframeEvent`) |

#### NPCMessageEvent

Displays a message from an NPC.

```json
{
  "$type": "NPCMessageEvent",
  "n": "Guard",
  "m": "Halt! Who goes there?",
  "r": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| `n` | string | NPC name displayed in the message |
| `m` | string | Message text |
| `r` | boolean | `true` = message can be repeated |

#### DisplaySellSwap

Shows a token swap interface.

```json
{
  "$type": "DisplaySellSwap",
  "id": "swap-config-001",
  "typ": 1
}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Swap configuration ID |
| `typ` | number | Swap type |

---

## Complex Effects

### PortalsAnimation

Multi-keyframe animation that moves an item through a sequence of transform states. More powerful than `MoveToSpot` which only supports a single target position.

```json
{
  "$type": "PortalsAnimation",
  "stateEvents": [],
  "_transformStates": [
    {
      "position": [0, 0, 0],
      "rotation": [0, 0, 0, 1],
      "scale": [1, 1, 1]
    },
    {
      "position": [0, 5, 0],
      "rotation": [0, 0.707, 0, 0.707],
      "scale": [1, 1, 1]
    },
    {
      "position": [5, 5, 0],
      "rotation": [0, 1, 0, 0],
      "scale": [1, 1, 1]
    }
  ],
  "states": [
    {"x": 0, "y": 0, "z": 0, "rx": 0.0, "sx": 1.0, "sy": 1.0, "sz": 1.0, "duration": 0.0},
    {"x": 0, "y": 5, "z": 0, "rx": 90.0, "sx": 1.0, "sy": 1.0, "sz": 1.0, "duration": 2.0},
    {"x": 5, "y": 5, "z": 0, "rx": 180.0, "sx": 1.0, "sy": 1.0, "sz": 1.0, "duration": 2.0}
  ],
  "loopAnimation": false,
  "seamless": false,
  "fixedUpdate": false
}
```

The effect uses **two parallel arrays** that describe the same keyframes in different formats:

| Array | Format | Notes |
|-------|--------|-------|
| `_transformStates` | `position` [x,y,z], `rotation` [qx,qy,qz,qw], `scale` [x,y,z] | Quaternion-based. No duration field. |
| `states` | `x,y,z` (position), `rx` (rotation degrees), `sx,sy,sz` (scale), `duration` (seconds) | Euler-based. Each keyframe has its own duration. |

Both arrays **must** have the same number of entries and describe the same positions. The `states` array controls the `duration` of each step.

**Fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `stateEvents` | array | `[]` | Events triggered at specific keyframes. Use `[]` for basic animations. |
| `_transformStates` | array | Required | Keyframes in quaternion format |
| `states` | array | Required | Keyframes in Euler format with durations |
| `loopAnimation` | boolean | `false` | Loop the animation continuously |
| `seamless` | boolean | `false` | Smooth the loop transition (only useful when `loopAnimation` is `true`) |
| `fixedUpdate` | boolean | `false` | Use physics tick for updates. Enable only if the animated item has collision triggers. |

**Full example -- looping patrol animation on a quest-driven item:**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "PortalsAnimation",
    "stateEvents": [],
    "_transformStates": [
      {"position": [-5, 1, 0], "rotation": [0, 0, 0, 1], "scale": [1, 1, 1]},
      {"position": [5, 1, 0], "rotation": [0, 0, 0, 1], "scale": [1, 1, 1]},
      {"position": [5, 1, 10], "rotation": [0, 0, 0, 1], "scale": [1, 1, 1]},
      {"position": [-5, 1, 10], "rotation": [0, 0, 0, 1], "scale": [1, 1, 1]}
    ],
    "states": [
      {"x": -5, "y": 1, "z": 0, "rx": 0.0, "sx": 1.0, "sy": 1.0, "sz": 1.0, "duration": 0.0},
      {"x": 5, "y": 1, "z": 0, "rx": 0.0, "sx": 1.0, "sy": 1.0, "sz": 1.0, "duration": 3.0},
      {"x": 5, "y": 1, "z": 10, "rx": 0.0, "sx": 1.0, "sy": 1.0, "sz": 1.0, "duration": 3.0},
      {"x": -5, "y": 1, "z": 10, "rx": 0.0, "sx": 1.0, "sy": 1.0, "sz": 1.0, "duration": 3.0}
    ],
    "loopAnimation": true,
    "seamless": true,
    "fixedUpdate": false
  },
  "Id": "a0b1c2d3-e4f5-6789-0abc-def012345678",
  "TargetState": 1,
  "Name": "0_patrol",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

---

### RunTriggersFromEffector

Triggers quest state changes from within an effect. This is the primary mechanism for chaining quests together -- when one quest reaches a state, it can activate, complete, or reset other quests.

```json
{
  "$type": "RunTriggersFromEffector",
  "linkedTasks": [
    {
      "Trigger": {},
      "Id": "b1c2d3e4-f506-7890-1abc-def234567890",
      "TargetState": 111,
      "Name": "1_next_quest",
      "TaskTriggerId": "mlhcd9ef0ghij1"
    }
  ],
  "useRandom": false
}
```

**linkedTasks entry fields:**

| Field | Type | Description |
|-------|------|-------------|
| `Trigger` | object | `{}` = fire immediately. `{"Delay": 2.0}` = delay in seconds before firing. |
| `Id` | string (UUID) | Unique identifier |
| `TargetState` | number | Encoded state transition. See [TargetState Encoding](#targetstate-encoding). |
| `Name` | string | Target quest name (e.g., `"1_next_quest"`) |
| `TaskTriggerId` | string | Target quest ID (the `id` of the quest's `inProgress` entry) |

**useRandom:**

| Value | Behavior |
|-------|----------|
| `false` | Fire ALL linked tasks |
| `true` | Randomly pick ONE linked task to fire |

**Full example -- when quest 0 completes, activate quest 1 and play a sound:**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "RunTriggersFromEffector",
    "linkedTasks": [
      {
        "Trigger": {},
        "Id": "c2d3e4f5-0617-8901-2bcd-ef3456789012",
        "TargetState": 111,
        "Name": "1_second_phase",
        "TaskTriggerId": "mlhef2gh3ijkl4"
      }
    ],
    "useRandom": false
  },
  "Id": "d3e4f506-1728-9012-3cde-f45678901234",
  "TargetState": 2,
  "Name": "0_first_phase",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

**Example -- auto-reset loop (quest resets itself after completing):**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "RunTriggersFromEffector",
    "linkedTasks": [
      {
        "Trigger": {"Delay": 3.0},
        "Id": "e4f50617-2839-0123-4def-567890123456",
        "TargetState": 101,
        "Name": "0_door_toggle",
        "TaskTriggerId": "mlhab7cd3efg12"
      }
    ],
    "useRandom": false
  },
  "Id": "f5061728-3940-1234-5ef0-678901234567",
  "TargetState": 2,
  "Name": "0_door_toggle",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

This fires when quest `0_door_toggle` reaches Completed, then resets it to Not Active after a 3-second delay, creating a repeatable cycle.

**Example -- random outcome:**

```json
{
  "$type": "RunTriggersFromEffector",
  "linkedTasks": [
    {
      "Trigger": {},
      "Id": "06172839-4051-2345-6f01-789012345678",
      "TargetState": 111,
      "Name": "1_reward_gold",
      "TaskTriggerId": "mlhgh5ij6klmn7"
    },
    {
      "Trigger": {},
      "Id": "17283940-5162-3456-7012-890123456789",
      "TargetState": 111,
      "Name": "2_reward_silver",
      "TaskTriggerId": "mlhop8qr9stuv0"
    },
    {
      "Trigger": {},
      "Id": "28394051-6273-4567-8123-901234567890",
      "TargetState": 111,
      "Name": "3_reward_bronze",
      "TaskTriggerId": "mlhwx1yz2abcd3"
    }
  ],
  "useRandom": true
}
```

When `useRandom` is `true`, only one of the three reward quests will activate at random.

#### TargetState Encoding

The `TargetState` values used in `RunTriggersFromEffector.linkedTasks` and the click-to-advance-quest variant of `TaskTriggerSubscription` encode specific state transitions:

| Value | From State | To State | Description |
|-------|-----------|----------|-------------|
| `101` | Any | Not Active | Reset quest to initial state |
| `111` | Not Active | Active | Start the quest |
| `121` | Active | Completed | Complete the quest |
| `131` | Completed | Active | Reactivate a completed quest |
| `141` | Any | Completed | Force-complete regardless of current state |
| `151` | Any | Active | Force-activate regardless of current state |
| `161` | Active | Not Active | Cancel an active quest |
| `171` | Completed | Not Active | Reset a completed quest |
| `181` | Not Active | Completed | Skip directly to completed |

The "Any" variants (`101`, `141`, `151`) trigger regardless of current state. The constrained variants (e.g., `121`) only fire when the quest is currently in the specified "from" state, acting as a guard.

---

### DialogEffectorDisplay

Creates an interactive dialogue tree with branching choices. This is the most complex effect type -- it embeds inline quest entries for each dialogue node.

```json
{
  "$type": "DialogEffectorDisplay",
  "tasksN": [
    {"N": "-0_greeting"},
    {"N": "-1_accept_quest"},
    {"N": "-2_decline_quest"}
  ],
  "GN": "Village Elder",
  "S": "_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "Audio": false,
  "HF": true,
  "R": true,
  "DV": "",
  "GB": "leave",
  "Story": "_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "tasksSorM": {
    "-0_greeting": {
      "completed": {
        "id": "mlhcomp000greet",
        "EntryId": "11111111-aaaa-bbbb-cccc-dddddddddddd",
        "Name": "-0_greeting",
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
        "Creator": "your-firebase-uid",
        "TemplateName": "",
        "Tracked": true,
        "Visible": false,
        "ExtraText": "{\"ExtraTaskDTODataDialog\":{\"QT\":\"Welcome, traveler. Our village needs your help.\",\"AT\":[{\"Task\":\"-1_accept_quest\",\"Txt\":\"I'll help!\",\"Name\":\"accept\"},{\"Task\":\"-2_decline_quest\",\"Txt\":\"Not interested.\",\"Name\":\"decline\"}]}}",
        "SuccessMsg": ""
      },
      "inProgress": {
        "id": "mlhprog000greet",
        "EntryId": "11111111-aaaa-bbbb-cccc-dddddddddddd",
        "Name": "-0_greeting",
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
        "Creator": "your-firebase-uid",
        "TemplateName": "",
        "Tracked": true,
        "Visible": false,
        "ExtraText": "{\"ExtraTaskDTODataDialog\":{\"QT\":\"Welcome, traveler. Our village needs your help.\",\"AT\":[{\"Task\":\"-1_accept_quest\",\"Txt\":\"I'll help!\",\"Name\":\"accept\"},{\"Task\":\"-2_decline_quest\",\"Txt\":\"Not interested.\",\"Name\":\"decline\"}]}}"
      }
    },
    "-1_accept_quest": {
      "completed": {
        "id": "mlhcomp001accpt",
        "EntryId": "22222222-aaaa-bbbb-cccc-dddddddddddd",
        "Name": "-1_accept_quest",
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
        "Creator": "your-firebase-uid",
        "TemplateName": "",
        "Tracked": true,
        "Visible": false,
        "ExtraText": "{\"ExtraTaskDTODataDialog\":{\"QT\":\"Thank you! Head to the cave north of here.\",\"AT\":[]}}",
        "SuccessMsg": ""
      },
      "inProgress": {
        "id": "mlhprog001accpt",
        "EntryId": "22222222-aaaa-bbbb-cccc-dddddddddddd",
        "Name": "-1_accept_quest",
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
        "Creator": "your-firebase-uid",
        "TemplateName": "",
        "Tracked": true,
        "Visible": false,
        "ExtraText": "{\"ExtraTaskDTODataDialog\":{\"QT\":\"Thank you! Head to the cave north of here.\",\"AT\":[]}}"
      }
    },
    "-2_decline_quest": {
      "completed": {
        "id": "mlhcomp002decln",
        "EntryId": "33333333-aaaa-bbbb-cccc-dddddddddddd",
        "Name": "-2_decline_quest",
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
        "Creator": "your-firebase-uid",
        "TemplateName": "",
        "Tracked": true,
        "Visible": false,
        "ExtraText": "{\"ExtraTaskDTODataDialog\":{\"QT\":\"Very well. Come back if you change your mind.\",\"AT\":[]}}",
        "SuccessMsg": ""
      },
      "inProgress": {
        "id": "mlhprog002decln",
        "EntryId": "33333333-aaaa-bbbb-cccc-dddddddddddd",
        "Name": "-2_decline_quest",
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
        "Creator": "your-firebase-uid",
        "TemplateName": "",
        "Tracked": true,
        "Visible": false,
        "ExtraText": "{\"ExtraTaskDTODataDialog\":{\"QT\":\"Very well. Come back if you change your mind.\",\"AT\":[]}}"
      }
    }
  }
}
```

**Top-level fields:**

| Field | Type | Description |
|-------|------|-------------|
| `tasksN` | array | Ordered list of task name references. Each entry is `{"N": "-index_name"}`. |
| `GN` | string | Character name displayed in the dialogue UI |
| `S` | string | Story UUID prefixed with `_` (e.g., `"_a1b2c3d4-..."`) |
| `Audio` | boolean | Enable audio playback for dialogue |
| `HF` | boolean | Hide the dialogue UI when the conversation ends |
| `R` | boolean | Allow the dialogue to be repeated |
| `DV` | string | Dialogue voice ID for text-to-speech. `""` = no voice. |
| `GB` | string | Goodbye action. `"leave"` = close dialogue window. |
| `Story` | string | Same value as `S` (story identifier) |
| `tasksSorM` | object | Maps task names to `{completed, inProgress}` quest entry pairs |

**Dialogue data format (inside `ExtraText` JSON string):**

```json
{
  "ExtraTaskDTODataDialog": {
    "QT": "What the NPC says to the player",
    "AT": [
      {
        "Task": "-1_next_node",
        "Txt": "Player's response text (displayed as a button)",
        "Name": "answer-label"
      }
    ]
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `QT` | string | The NPC's dialogue text |
| `AT` | array | Player response options. Empty `[]` = terminal node (end of conversation). |
| `AT[].Task` | string | Task name to branch to when this answer is chosen |
| `AT[].Txt` | string | Text displayed on the answer button |
| `AT[].Name` | string | Answer label/identifier |

**Task naming:** Dialogue task names use the pattern `-{index}_{description}` (e.g., `-0_greeting`, `-1_accept`). Note the leading hyphen.

---

## Complete Examples

### Example 1: Click a button to open a door

This example uses a basic interaction on a button and quest-driven effects on a door. Clicking the button activates a quest, which triggers the door to move.

**Quest setup** (in the `quests` object):

```json
{
  "mlh9kkyxvll8ql": {
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
    "Creator": "your-firebase-uid",
    "TemplateName": "",
    "Tracked": true,
    "Visible": false,
    "ExtraText": "",
    "id": "mlh9kkyxvll8ql"
  },
  "mlhab7cd3efg12": {
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
    "Creator": "your-firebase-uid",
    "TemplateName": "",
    "Tracked": true,
    "Visible": false,
    "ExtraText": "",
    "SuccessMsg": "",
    "id": "mlhab7cd3efg12"
  }
}
```

**Button logic** (click to activate quest):

```json
{
  "Tasks": [
    {
      "$type": "TaskTriggerSubscription",
      "Trigger": {"$type": "OnClickEvent"},
      "Id": "11111111-2222-3333-4444-555555555555",
      "TargetState": 111,
      "Name": "0_open_door",
      "TaskTriggerId": "mlh9kkyxvll8ql"
    }
  ]
}
```

**Door logic** (move when quest activates):

```json
{
  "Tasks": [
    {
      "$type": "TaskEffectorSubscription",
      "Effector": {
        "$type": "MoveToSpot",
        "_transformState": {
          "position": [5, 0.5, 0],
          "rotation": [0, 0, 0, 1],
          "scale": [0.2, 3, 2],
          "duration": 0.0
        }
      },
      "Id": "22222222-3333-4444-5555-666666666666",
      "Name": "0_open_door",
      "TaskTriggerId": "mlh9kkyxvll8ql"
    },
    {
      "$type": "TaskEffectorSubscription",
      "Effector": {
        "$type": "MoveToSpot",
        "_transformState": {
          "position": [5, 3.5, 0],
          "rotation": [0, 0, 0, 1],
          "scale": [0.2, 3, 2],
          "duration": 1.5
        }
      },
      "Id": "33333333-4444-5555-6666-777777777777",
      "TargetState": 1,
      "Name": "0_open_door",
      "TaskTriggerId": "mlh9kkyxvll8ql"
    }
  ]
}
```

> Remember: The logic values must be JSON-stringified before being placed in the `logic` object.

### Example 2: Trigger zone with sound and notification

A trigger zone that plays a sound and shows a notification when the player walks through it.

```json
{
  "Tasks": [
    {
      "$type": "TaskTriggerSubscription",
      "Trigger": {"$type": "OnEnterEvent"},
      "DirectEffector": {
        "Effector": {
          "$type": "PlaySoundOnce",
          "Url": "https://example.com/chime.mp3",
          "Dist": 15.0
        },
        "Id": "aaaa1111-bbbb-2222-cccc-333333333333",
        "TargetState": 2,
        "Name": ""
      },
      "Id": "dddd4444-eeee-5555-ffff-666666666666",
      "TargetState": 2,
      "Name": ""
    },
    {
      "$type": "TaskTriggerSubscription",
      "Trigger": {"$type": "OnEnterEvent"},
      "DirectEffector": {
        "Effector": {
          "$type": "NotificationPillEvent",
          "nt": "You discovered a hidden area!",
          "c": "FFD700"
        },
        "Id": "bbbb2222-cccc-3333-dddd-444444444444",
        "TargetState": 2,
        "Name": ""
      },
      "Id": "eeee5555-ffff-6666-aaaa-777777777777",
      "TargetState": 2,
      "Name": ""
    }
  ]
}
```

This item must have `prefabName: "Trigger"` for the `OnEnterEvent` triggers to work.

### Example 3: Sequential quest chain

Three quests that fire in sequence: collect items, then activate a portal, then complete the level.

**RunTriggersFromEffector on a coordinator item -- when quest 0 completes, activate quest 1; when quest 1 completes, activate quest 2:**

```json
{
  "Tasks": [
    {
      "$type": "TaskEffectorSubscription",
      "Effector": {
        "$type": "RunTriggersFromEffector",
        "linkedTasks": [
          {
            "Trigger": {},
            "Id": "chain-1111-2222-3333-444444444444",
            "TargetState": 111,
            "Name": "1_activate_portal",
            "TaskTriggerId": "mlhportalquest1"
          }
        ],
        "useRandom": false
      },
      "Id": "chain-5555-6666-7777-888888888888",
      "TargetState": 2,
      "Name": "0_collect_items",
      "TaskTriggerId": "mlhcollectquest"
    },
    {
      "$type": "TaskEffectorSubscription",
      "Effector": {
        "$type": "RunTriggersFromEffector",
        "linkedTasks": [
          {
            "Trigger": {"Delay": 2.0},
            "Id": "chain-9999-aaaa-bbbb-cccccccccccc",
            "TargetState": 111,
            "Name": "2_level_complete",
            "TaskTriggerId": "mlhlevelcomplt2"
          }
        ],
        "useRandom": false
      },
      "Id": "chain-dddd-eeee-ffff-000000000000",
      "TargetState": 2,
      "Name": "1_activate_portal",
      "TaskTriggerId": "mlhportalquest1"
    }
  ]
}
```

---

## Syntax Quirks Reference

A quick reference for the most common sources of bugs when constructing interactions:

| Issue | Correct | Incorrect |
|-------|---------|-----------|
| DuplicateItem transform field | `"TS"` | `"_transformState"` |
| PlaySoundOnce URL field | `"Url"` (capital U) | `"url"` |
| PlaySoundInALoop URL field | `"Url"` (capital U) | `"url"` |
| StopSound URL field | `"url"` (lowercase u) | `"Url"` |
| PlaySoundOnce distance field | `"Dist"` (capital D) | `"dist"` |
| State 0 TargetState | *omit the field entirely* | `"TargetState": 0` |
| FunctionEffector task names | `'shop'` (no prefix) | `'0_shop'` (with prefix) |
| Logic values in room data | JSON string | Raw object |
| Notification variable syntax | `\|coins\|` (pipe chars) | `{coins}` or `$coins` |

---

## Item-Specific Effect Restrictions

Some effects are designed to work only on specific item types:

| Effect | Required `prefabName` |
|--------|-----------------------|
| `EquipGunEffect` | `Gun` or `Shotgun` |
| `TossGunEffect` | `Gun` or `Shotgun` |
| `ResetGunEffect` | `Gun` or `Shotgun` |
| `RespawnDestructible` | `Destructible` |
| `ActivateTriggerZoneEffect` | `Trigger` |
| `DeactivateTriggerZoneEffect` | `Trigger` |
| `PlayAnimationOnce` | `GLB` (must have embedded animation) |

Similarly, some triggers only work on specific item types:

| Trigger | Required `prefabName` |
|---------|-----------------------|
| `OnEnterEvent` | `Trigger` |
| `OnExitEvent` | `Trigger` |
| `OnGunEquippedTrigger` | `Gun` or `Shotgun` |
| `ShotHitTrigger` | `Gun` or `Shotgun` |
| `GotKillTrigger` | `Gun` or `Shotgun` |
| `StartedAimingTrigger` | `Gun` or `Shotgun` |
| `StoppedAimingTrigger` | `Gun` or `Shotgun` |
| `OnGunTossedTrigger` | `Gun` or `Shotgun` |
