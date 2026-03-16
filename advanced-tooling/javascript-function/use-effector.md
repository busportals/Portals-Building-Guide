# UseEffector

UseEffector lets you call effects directly from JavaScript code. Instead of wiring up effects through the visual UI, you can trigger them with a single line of JS. UseEffector fires immediately — there is no delay parameter.

***

### Syntax

```javascript
// No parameters
UseEffector('760', 'ShowObject');

// With parameters (JSON string)
UseEffector({{Object}}, 'MoveToSpot', '{"transformState":{"position":[1.0,0.0,0.0],"rotation":[0.0,0.0,0.0,1.0],"scale":[0.0,0.0,0.0],"duration":1.0},"relative":true,"fixedUpdate":false}');
```

The first argument is the **target** — the object to apply the effect to. The second argument is the **effect name**. The optional third argument is a **JSON string** containing the effect's parameters.

#### Targets

| Target | What it targets |
|--------|----------------|
| `'760'` | The object with ID 760 (a string literal) |
| `{{Object}}` | The object the JavaScript Function is set up on |
| `{{Parent}}` | The parent of the object the function is set up on |
| `{{Child}}` | The child of the object the function is set up on |

These are the only valid target forms. Note that `{{Object}}`, `{{Parent}}`, and `{{Child}}` are not wrapped in quotes.

```javascript
// Target a specific object by ID
UseEffector('760', 'ShowObject');

// Target the object this function is on
UseEffector({{Object}}, 'ShowObject');

// Target the parent object
UseEffector({{Parent}}, 'ShowObject');

// Target a child object
UseEffector({{Child}}, 'ShowObject');
```

***

### Passing Parameters

For effects that have parameters, pass them as a JSON string in the third argument. The JSON keys match the parameter names listed for each effect.

#### Type Reference

| Type | JSON format | Example |
|------|------------|---------|
| string | `"value"` | `"FFFFFF"` |
| float | number with decimal | `1.0`, `5.0` |
| int | whole number | `5`, `1` |
| long | whole number | `1672531200` |
| bool | `true` / `false` | `true` |
| Vector3 | array of 3 floats | `[1.0, 0.0, 0.0]` |
| Quaternion | array of 4 floats | `[0.0, 0.0, 0.0, 1.0]` |
| TransformState | object | `{"position":[x,y,z],"rotation":[x,y,z,w],"scale":[x,y,z],"duration":float}` |
| List\<T\> | array of T | `[[1.0,0.0,0.0],[0.0,1.0,0.0]]` |

> **Note:** If a parameter name starts with an underscore in the reference (e.g. `_transformState`), strip the underscore in the JSON (use `transformState`).

> **Enum types** (e.g. `HumanBodyBones`, `RepeatEvery`, `CameraFilter.ImageScaleType`) are passed as strings matching the enum name (e.g. `"Head"`, `"RightHand"`).

***

### Quick Examples

#### Show and hide an object

```javascript
UseEffector('760', 'HideObject');
```

What it does: hides the object with ID 760 immediately.

```javascript
UseEffector('760', 'ShowObject');
```

What it does: shows the object with ID 760 immediately.

***

#### Lock and unlock movement

```javascript
UseEffector({{Object}}, 'LockMovement');
```

What it does: locks the player's movement immediately.

```javascript
UseEffector({{Object}}, 'UnlockMovement');
```

What it does: unlocks the player's movement.

***

#### Combining with conditions

```javascript
if ($T{puzzle1} == 'Completed') {
  UseEffector('760', 'ShowObject');
}
```

What it does: shows object 760 only when the puzzle1 task is completed.

***

#### Combining with SetTask

```javascript
UseEffector({{Object}}, 'HideObject');
SetTask('objectHidden', 'Active', 0.0);
```

What it does: hides the object and then marks the objectHidden task as Active.

***

#### Passing parameters with conditions

```javascript
if ($T{puzzle1} == 'Completed') {
  UseEffector('760', 'MoveToSpot', '{"transformState":{"position":[0.0,5.0,0.0],"rotation":[0.0,0.0,0.0,1.0],"scale":[0.0,0.0,0.0],"duration":2.0},"relative":true,"fixedUpdate":false}');
}
```

What it does: when puzzle1 is completed, moves object 760 up 5 units on the Y axis over 2 seconds relative to its current position.

***

#### Change fog color

```javascript
UseEffector({{Object}}, 'ChangeFog', '{"color":"FF0000","distance":50.0}');
```

What it does: changes the fog to red with a distance of 50.

***

### Supported Effects

The effect name string must match exactly (case-sensitive). For details on what each effect does, see the [Effects](../../interactive-studio/effects/README.md) documentation.

***

#### Visibility & Display

##### ChangeText

`'ChangeText'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | string | | New text |

##### DisplayAvatarScreen

`'DisplayAvatarScreen'` — No parameters.

##### DisplayBuySwap

`'DisplayBuySwap'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `id` | string | | Swap ID |
| `prepared` | bool | | Whether swap is prepared |

##### DisplaySellSwap

`'DisplaySellSwap'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `id` | string | | Swap ID |
| `prepared` | bool | | Whether swap is prepared |

##### DisplayValue

`'DisplayValue'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `label` | string | | Value label |
| `color` | string | `"FF9500"` | Hex color without `#` |

##### HideAllPlayers

`'HideAllPlayers'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `show` | bool | `false` | Set to `true` to show all players |

##### HideObject

`'HideObject'` — No parameters.

##### HideOutline

`'HideOutline'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `color` | string | `"FFFFFF"` | Hex color without `#` |

##### HideSellSwap

`'HideSellSwap'` — No parameters.

##### HideValue

`'HideValue'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `label` | string | | Value label |

##### NotificationPill

`'NotificationPill'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `nt` | string | | Notification text |
| `c` | string | | Color (hex) |
| `hideBackground` | bool | `false` | Hide background |

##### ShowObject

`'ShowObject'` — No parameters.

##### ShowOutline

`'ShowOutline'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `color` | string | `"FFFFFF"` | Hex color without `#` |
| `width` | float | `6.0` | Outline width |

***

#### Movement & Player Control

##### AddVelocityToPlayer

`'AddVelocityToPlayer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `vel` | Vector3 | | Velocity vector |
| `accelerationTime` | float | | Time to reach target velocity |
| `local` | bool | `false` | Use local space |
| `randomOffset` | Vector3 | | Random offset to velocity |

##### ChangeMovementProfile

`'ChangeMovementProfile'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `mvmtProfile` | string | | Movement profile name |

##### LockMovement

`'LockMovement'` — No parameters.

##### MoveItemToPlayer

`'MoveItemToPlayer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `offset` | Vector3 | | Position offset from player |
| `playerRotation` | bool | `false` | Follow player rotation |
| `rotationOffset` | Vector3 | | Rotation offset |
| `useForwardDirection` | bool | `false` | Use player's forward direction |
| `multiplayer` | bool | `false` | Enable for multiplayer |

##### MoveToSpot

`'MoveToSpot'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `transformState` | TransformState | | Target transform |
| `relative` | bool | `false` | Use relative positioning |
| `fixedUpdate` | bool | `false` | Use fixed update |

**Example:** Move an object 1 unit on the X axis relative to its current position over 1 second:

```javascript
UseEffector({{Object}}, 'MoveToSpot', '{"transformState":{"position":[1.0,0.0,0.0],"rotation":[0.0,0.0,0.0,1.0],"scale":[0.0,0.0,0.0],"duration":1.0},"relative":true,"fixedUpdate":false}');
```

##### MutePlayer

`'MutePlayer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `mute` | bool | `true` | Mute the player |

##### StartAutoRun

`'StartAutoRun'` — No parameters.

##### StopAutoRun

`'StopAutoRun'` — No parameters.

##### Teleport

`'Teleport'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `id` | string | | Spawn point ID |
| `sn` | string | | Spawn point name |
| `sr` | float | `0` | Spawn radius |

**Example:** Teleport to a specific spawn point:

```javascript
UseEffector({{Object}}, 'Teleport', '{"id":"your-room-id","sn":"test1","sr":0.0}');
```

**Example:** Teleport to a spawn point with a random radius of 3:

```javascript
UseEffector({{Object}}, 'Teleport', '{"id":"your-room-id","sn":"test1","sr":3.0}');
```

##### ToggleLockCursor

`'ToggleLockCursor'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `lockCursor` | bool | `true` | Lock the cursor |

##### UnlockMovement

`'UnlockMovement'` — No parameters.

***

#### Camera & Visual

##### ChangeBloom

`'ChangeBloom'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Intensity` | float | | Bloom intensity |
| `Clamp` | float | | Bloom clamp |
| `Diffusion` | float | | Bloom diffusion |

##### ChangeCameraState

`'ChangeCameraState'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `camState` | string | | Camera state name |
| `smoothTransition` | bool | `true` | Smooth camera transition |
| `transitionSpeed` | float | `6.0` | Speed of transition |

##### ChangeCameraStateToPrevous

`'ChangeCameraStateToPrevous'` — No parameters.

##### ChangeCameraZoom

`'ChangeCameraZoom'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `zoomAmount` | float | `0` | Target zoom amount |
| `lockZoom` | bool | `false` | Lock zoom at this level |

##### ChangeFog

`'ChangeFog'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `color` | string | `"FFFFFF"` | Hex color without `#` |
| `distance` | float | | Fog distance |

##### ChangeTimeOfDay

`'ChangeTimeOfDay'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `toNight` | bool | `true` | Change to night |

##### LockCamera

`'LockCamera'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `allowEffectorOnStart` | bool | | Allow effector on start |
| `timeToUnlock` | float | `5.0` | Seconds until auto-unlock (0 = never) |

##### RotateSkybox

`'RotateSkybox'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `rotation` | float | `180.0` | Target rotation in degrees |
| `duration` | float | `5.0` | Duration of rotation |

##### SetCameraFilter

`'SetCameraFilter'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `url` | string | | Image URL |
| `alpha` | float | `0.8` | Filter opacity |
| `blackBars` | bool | `false` | Show black bars |
| `imageScaleType` | CameraFilter.ImageScaleType | | Scale type for the image |

##### ToggleFreeCam

`'ToggleFreeCam'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `enterFreeCam` | bool | | Enter free camera mode |
| `x` | float | | Camera X position |
| `y` | float | | Camera Y position |
| `z` | float | | Camera Z position |
| `lookAtPlayer` | bool | | Camera looks at player |

##### UnlockCamera

`'UnlockCamera'` — No parameters.

***

#### Audio

##### ChangeAudius

`'ChangeAudius'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ap` | string | | Audius playlist/track URL |

##### PlaySoundInALoop

`'PlaySoundInALoop'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Url` | string | | Sound file URL |
| `Dist` | float | | Max audible distance |
| `Preload` | bool | | Preload the sound |
| `PlayOnStart` | bool | | Play when effect starts |
| `pitchVariance` | float | | Random pitch variation |
| `delay` | float | | Delay before playing |
| `volume` | float | `1.0` | Volume level |
| `fadeIn` | float | `0` | Fade in duration |

##### PlaySoundOnce

`'PlaySoundOnce'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Url` | string | | Sound file URL |
| `Dist` | float | | Max audible distance |
| `Preload` | bool | | Preload the sound |
| `PlayOnStart` | bool | | Play when effect starts |
| `pitchVariance` | float | | Random pitch variation |
| `delay` | float | | Delay before playing |
| `volume` | float | `1.0` | Volume level |
| `spatialise` | bool | `false` | Enable spatial audio |
| `fadeIn` | float | `0` | Fade in duration |
| `playFromPlayerNetworked` | bool | `false` | Play from player in multiplayer |

**Example:** Play a sound at full volume with a max distance of 10:

```javascript
UseEffector({{Object}}, 'PlaySoundOnce', '{"Url":"https://your-sound-url.mp3","Dist":10.0,"Preload":false,"PlayOnStart":false,"pitchVariance":0.0,"delay":0.0,"volume":1.0,"spatialise":false,"fadeIn":0.0,"playFromPlayerNetworked":false}');
```

**Example:** Play with spatial audio, half volume, and a 1 second fade in:

```javascript
UseEffector({{Object}}, 'PlaySoundOnce', '{"Url":"https://your-sound-url.mp3","Dist":20.0,"Preload":false,"PlayOnStart":false,"pitchVariance":0.0,"delay":0.0,"volume":0.5,"spatialise":true,"fadeIn":1.0,"playFromPlayerNetworked":false}');
```

##### StopSound

`'StopSound'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `url` | string | `""` | URL of sound to stop (empty = stop all) |
| `fadeOut` | float | `0` | Fade out duration |

##### TurnSound

`'TurnSound'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Muted` | bool | | Mute the sound |

***

#### Avatar & Wearables

##### AttachItemToPlayer

`'AttachItemToPlayer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `bodyPart` | string | `"Head"` | Body part to attach to (see list below) |
| `localOffset` | TransformState | | Local offset (position, rotation, scale) |
| `multiplayer` | bool | `false` | Enable for multiplayer |

**Available body parts:**

`"PlayerRoot"`, `"Hips"`, `"Spine"`, `"Chest"`, `"UpperChest"`, `"Neck"`, `"Head"`, `"LeftShoulder"`, `"RightShoulder"`, `"LeftUpperArm"`, `"RightUpperArm"`, `"LeftLowerArm"`, `"RightLowerArm"`, `"LeftHand"`, `"RightHand"`, `"LeftUpperLeg"`, `"RightUpperLeg"`, `"LeftLowerLeg"`, `"RightLowerLeg"`, `"LeftFoot"`, `"RightFoot"`

**Example:** Attach an item to the player's head:

```javascript
UseEffector({{Object}}, 'AttachItemToPlayer', '{"bodyPart":"Head","localOffset":{"position":[0.0,0.0,0.0],"rotation":[0.0,0.0,0.0,1.0],"scale":[1.0,1.0,1.0],"duration":0.0},"multiplayer":false}');
```

**Example:** Attach to the player's right hand with a position offset:

```javascript
UseEffector({{Object}}, 'AttachItemToPlayer', '{"bodyPart":"RightHand","localOffset":{"position":[0.0,0.1,0.0],"rotation":[0.0,0.0,0.0,1.0],"scale":[1.0,1.0,1.0],"duration":0.0},"multiplayer":false}');
```

##### ChangeAvatar

`'ChangeAvatar'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Url` | string | | Avatar URL |
| `Persistent` | bool | | Persist across sessions |

##### ChangeAvatarMood

`'ChangeAvatarMood'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `mood` | int | | Mood index |

##### ChangeRoundyWearable

`'ChangeRoundyWearable'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ItemID` | string | | Wearable item ID |
| `Persistent` | bool | | Persist across sessions |

##### ChangeVoiceGroup

`'ChangeVoiceGroup'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `group` | string | `""` | Voice group name |

##### DetachItemFromPlayer

`'DetachItemFromPlayer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `multiplayer` | bool | `false` | Enable for multiplayer |

##### DoEmote

`'DoEmote'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `emoteName` | string | | Emote name |
| `moveStopsEmote` | bool | | Movement cancels the emote |

##### LockAvatarChange

`'LockAvatarChange'` — No parameters.

##### PlayerEmote

`'PlayerEmote'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `animationName` | string | `""` | Emote animation name |
| `moveStopsEmote` | bool | | Movement cancels the emote |

##### UnlockAvatarChange

`'UnlockAvatarChange'` — No parameters.

***

#### Timers, Scores & Leaderboards

##### CancelTimer

`'CancelTimer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `tn` | string | | Timer name |
| `ci` | string | `""` | Custom identifier |

##### ClearLeaderboard

`'ClearLeaderboard'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `label` | string | `"Score"` | Score label |
| `ci` | string | `""` | Custom identifier |
| `locally` | bool | | Clear locally only |

##### DateTimer

`'DateTimer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ToUnixTimeSeconds` | long | | Unix timestamp (seconds) |
| `r` | int | | Number of repetitions |
| `p` | int | | Repeat period (multiplied by `re`) |
| `re` | RepeatEvery | | `Never=0`, `Minute=60`, `Hour=3600`, `Day=86400`, `Week=604800` |
| `f` | bool | `true` | Fire on first player trigger |

##### OpenLeaderboard

`'OpenLeaderboard'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `lb` | string | | Leaderboard label |
| `ci` | string | `""` | Custom identifier |
| `tb` | bool | `true` | Show top board |

##### PostScoreToLeaderboard

`'PostScoreToLeaderboard'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `label` | string | `"Score"` | Score label |
| `ow` | bool | | Overwrite existing score |

##### StartTimer

`'StartTimer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `tn` | string | | Timer name |
| `ci` | string | `""` | Custom identifier |
| `r` | bool | `true` | Reset timer if already running |
| `countdown` | bool | `false` | Count down instead of up |
| `timerDuration` | float | | Duration in seconds (used with countdown) |
| `showTimerUI` | bool | `true` | Show timer in UI |

##### StopTimer

`'StopTimer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `tn` | string | | Timer name |
| `ci` | string | `""` | Custom identifier |
| `sendTimeToChat` | bool | `true` | Send time to chat |

##### UpdateScore

`'UpdateScore'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `label` | string | | Score label |
| `scoreChange` | int | | Amount to change |

##### UpdateScoreEventString

`'UpdateScoreEventString'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `label` | string | | Score label |
| `targetText` | string | | Target text value |

***

#### Animation & Objects

##### AnimateObjectInLoop

`'AnimateObjectInLoop'` — No parameters.

##### DuplicateItem

`'DuplicateItem'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `TS` | TransformState | | Transform for the duplicate |
| `destroyAfterTime` | float | `0` | Seconds until destroyed (0 = never) |

##### PlayAnimationOnce

`'PlayAnimationOnce'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `speed` | float | | Animation speed |

##### PortalsAnimation

`'PortalsAnimation'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `stateEvents` | List\<AnimationStateEvents\> | | Animation state events |
| `transformStates` | List\<TransformState\> | | Transform keyframes |
| `loopAnimation` | bool | `false` | Loop the animation |
| `relative` | bool | `false` | Use relative positioning |
| `fixedUpdate` | bool | `false` | Use fixed update |
| `seamless` | bool | `false` | Seamless looping |

##### PortalsAnimationStop

`'PortalsAnimationStop'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `StopAtCertainTransformStep` | int | | Stop at specific keyframe index |

##### StopAnimation

`'StopAnimation'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `stop` | float | `-1.0` | Normalized time to stop at (-1 = end of clip) |

***

#### Weapons & Combat

##### ChangeEnemyHealth

`'ChangeEnemyHealth'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `op` | int | | Operation (e.g. add/set) |
| `healthChange` | int | | Amount to change |

##### ChangePlayerHealth

`'ChangePlayerHealth'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `op` | int | `1` | Operation (e.g. add/set) |
| `healthChange` | int | | Amount to change |

##### DamageOverTime

`'DamageOverTime'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `damage` | int | `2` | Damage per tick |
| `duration` | float | `5.0` | Duration in seconds |

##### DequipGun

`'DequipGun'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `returnToOriginalSpot` | bool | `true` | Return gun to original position |

##### EquipGun

`'EquipGun'` — No parameters.

##### RespawnDestructible

`'RespawnDestructible'` — No parameters.

##### ResetGun

`'ResetGun'` — No parameters.

##### TakeDamage

`'TakeDamage'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `damage` | int | `5` | Damage amount |

##### TossGun

`'TossGun'` — No parameters.

***

#### NPC

##### AgentSayMessage

`'AgentSayMessage'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | string | | Message text |

##### AttackPlayer

`'AttackPlayer'` — No parameters.

##### ChangeNPCName

`'ChangeNPCName'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `newName` | string | `""` | New NPC name |

##### DuplicateEnemy

`'DuplicateEnemy'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `spawnName` | string | `""` | Spawn point name |
| `count` | int | `1` | Number of duplicates |
| `randomRadius` | float | `2` | Random spawn radius |

##### NpcAnimation

`'NpcAnimation'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `animationName` | string | `""` | Animation name |

##### NpcCopyPlayerPath

`'NpcCopyPlayerPath'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `positions` | List\<Vector3\> | | Path positions |
| `rotations` | List\<Quaternion\> | | Path rotations |
| `animatorParameterDatas` | List\<AnimatorParameterData\> | | Animator parameters |
| `shouldLoop` | bool | | Loop the path |

##### NpcCopyPlayerPathStop

`'NpcCopyPlayerPathStop'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `RP` | bool | | Return to path start |

##### NPCMessage

`'NPCMessage'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `n` | string | | NPC name |
| `m` | string | | Message text |
| `r` | bool | | Reverse (hide message) |

##### ResetEnemy

`'ResetEnemy'` — No parameters.

##### ReviveEnemy

`'ReviveEnemy'` — No parameters.

##### StartSpeaking

`'StartSpeaking'` — No parameters.

##### StopSpeaking

`'StopSpeaking'` — No parameters.

##### TurnBackToDefaultRotation

`'TurnBackToDefaultRotation'` — No parameters.

##### TurnToPlayer

`'TurnToPlayer'` — No parameters.

##### WalkNpcToSpot

`'WalkNpcToSpot'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `walkSpeed` | float | `3` | Walk speed |
| `endPosition` | Vector3 | | Destination position |
| `endRotation` | Quaternion | | Destination rotation |

***

#### Iframes & Web

##### Iframe

`'Iframe'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `url` | string | | Iframe URL |
| `animatedBody` | bool | | Animate body |

##### IframeStop

`'IframeStop'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `closeAll` | bool | `false` | Close all iframes |
| `iframeUrl` | string | `""` | Specific URL to close (empty = close all) |

##### OpenWebsite

`'OpenWebsite'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `url` | string | | Website URL |

##### SendMessageToIframes

`'SendMessageToIframes'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `iframeMsg` | string | | Message (supports `\|username\|` and `\|variable_label\|` placeholders) |

***

#### Video

##### PlayVideo

`'PlayVideo'` — No parameters.

##### StopVideo

`'StopVideo'` — No parameters.

***

#### Vehicle

##### EnterVehicle

`'EnterVehicle'` — No parameters.

##### ExitVehicle

`'ExitVehicle'` — No parameters.

##### VehicleBoost

`'VehicleBoost'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | float | `5.0` | Boost duration |
| `speedOfBoost` | float | `100.0` | Boost speed |
| `rampUpTime` | float | `1.0` | Time to reach full boost |
| `rampDownTime` | float | `2.0` | Time to decelerate |

***

#### Spectating

##### SpectatePlayer

`'SpectatePlayer'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `filterVariable` | string | `""` | Variable name to filter by |
| `filterValue` | string | `""` | Value to match |

##### StopSpectate

`'StopSpectate'` — No parameters.

***

#### Triggers & Tasks

##### ActivateTriggerZone

`'ActivateTriggerZone'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `triggerZoneId` | string | | Trigger zone ID |

##### CompleteQuest

`'CompleteQuest'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `id` | string | | Quest ID |

##### DeactivateTriggerZone

`'DeactivateTriggerZone'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `triggerZoneId` | string | | Trigger zone ID |

##### ResetAllTasks

`'ResetAllTasks'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `h` | bool | | Reset host tasks |
| `m` | bool | | Reset multiplayer tasks |
| `np` | bool | | Reset non-persistent tasks |

##### ResetAllVariables

`'ResetAllVariables'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `h` | bool | | Reset host variables |
| `s` | bool | `true` | Reset server variables |
| `m` | bool | | Reset multiplayer variables |
| `np` | bool | | Reset non-persistent variables |

##### ResetCollectableItems

`'ResetCollectableItems'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `OnStart` | bool | | Reset on start |
| `ItemId` | string | | Item ID to reset |

##### RunTriggerFrom

`'RunTriggerFrom'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `linkedTask` | TaskTriggerSubscription | | Linked task trigger |
| `times` | int | `-1` | Number of times to fire (-1 = unlimited) |

##### RunTriggersFrom

`'RunTriggersFrom'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `linkedTasks` | List\<TaskTriggerSubscription\> | | Linked task triggers |
| `useRandom` | bool | `false` | Fire a random one instead of all |

***

#### Other

##### ChangeToken

`'ChangeToken'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `tokenId` | string | | Token ID |

##### ChangeTokenTimeFrame

`'ChangeTokenTimeFrame'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `time` | int | | Time interval index (options: 1, 15, 60 minutes) |

##### EditInfoBox

`'EditInfoBox'`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | string | `""` | Info box title |
| `elements` | List\<string\> | | List of content elements |

***

### Notes

* UseEffector fires immediately — there is no delay parameter. If you need a delayed effect, use a SetTask delay to trigger a separate interaction chain:

```javascript
// Fires immediately
UseEffector('760', 'ShowObject');

// For a delayed effect, use SetTask with a delay instead
SetTask('showLater', 'Active', 3.0);
// Then set up a separate trigger on showLater to fire the effect
```

* Effect name strings are **case-sensitive** — `'ShowObject'` works, `'showobject'` does not.
* For detailed descriptions of what each effect does and its configuration options, see the [Effects](../../interactive-studio/effects/README.md) section.
