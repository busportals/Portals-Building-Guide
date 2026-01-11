---
name: portals-building-guide
description: Complete guide for building interactive 3D spaces in Portals. Use when creating spaces, configuring triggers/effects, writing function expressions, setting up NPCs, quests, token trading, iframes, or any Portals development task. Covers Interactive Studio, Function Effects, building tools, and all game mechanics.
---

# Portals Building Guide - Complete Reference

## Overview

Portals is a platform for creating interactive 3D virtual spaces. This guide covers all building tools, the Interactive Studio (no-code gamification), and advanced scripting with Function Effects.

---

# BUILDING BASICS

## Creating a Space

1. Sign in to Portals
2. Click profile icon → My Spaces
3. Click "Create New"
4. Choose a template
5. Name your space
6. Click "Create New Space"
7. You'll automatically load into your space

## Build Mode

1. Click the **wrench icon** to enter build mode
2. Select an item from inventory
3. Click in your space to place the item

---

# BUILDING TOOLS (20 Total)

| Tool | Description |
|------|-------------|
| **AI Item Generator** | Automated 3D object creation |
| **Image** | Place 2D images in 3D space |
| **Video** | Embed video players |
| **Build Block** | Basic structural elements |
| **Screenshare** | Display sharing |
| **Portal** | Teleportation between spaces/locations |
| **Custom GLB** | Import custom 3D models |
| **Light Source** | Static lighting |
| **Blink Light** | Animated/flashing lights |
| **Spotlight** | Directional lighting |
| **Spawn Point** | Player entry locations |
| **NPC** | Non-player characters with dialogue/AI |
| **Billboard** | Text/image display surfaces |
| **Jump Pad** | Launch players into air |
| **Trigger Cube** | Invisible interaction zones |
| **Collectible GLB** | Gatherable 3D objects |
| **Leaderboard** | Score tracking display |
| **Elemental** | Environmental effects |
| **Chart** | Live data visualization (crypto) |
| **World Text** | 3D text in space |

## Portal Tool

Creates teleportation between spaces or spawn points.

**Configuration:**
- **Destination**: Full space URL
- **Spawn Name**: Target spawn point (case-sensitive, leave blank for default)
- **Auto Teleport**: On = instant, Off = press X to activate
- **Custom Message**: Action prompt text (e.g., "teleport" shows "Press X to teleport")

## Trigger Cube

Invisible zone that activates events when players enter.

**Settings:**
- **Press X to Activate**: Toggle between auto-trigger or manual activation
- **Events**: Add actions (open doors, play sounds, teleport, etc.)
- **Custom Title**: Label for organization

## NPC (Non-Player Character)

Interactive characters with dialogue trees and AI.

**Setup:**
- Paste GLB avatar URL or choose preset
- Configure: Name, Auto Popup, Default Animation, AI Settings

**NPC-Specific Effects:**
- Turn To Player
- Walk to Position
- Record NPC Path
- Change Animation
- Change Avatar Mood
- Show/Hide NPC

**Requirement:** Must use rigged GLB avatars for animations.

---

# INTERACTIVE STUDIO

The no-code system for gamifying spaces. Three core components:

## Tasks

Tasks are progress trackers with **three states**:
- **NotActive** (default starting state)
- **Active**
- **Completed**

Tasks can transition between states in any order via triggers.

**Task Types:**
- Single Player Tasks
- Multiplayer Tasks
- Dependent Tasks (chains)
- Non-Persistent Tasks (reset on reload)
- Quests (visible in quest log)

## Task Debug Panel

Access via **Space Options > Task Debug Panel**

**Important:** Task system must be turned on BEFORE opening debug panel.

**State Indicators:**
- Red circle = NotActive
- Yellow circle = Active
- Green circle = Completed

**Features:**
- Change state of any task (single or multiplayer)
- View complete history log of all state changes
- Essential for testing effects and triggers

## Node View

Visual graph interface for analyzing game logic.

**Access:** Space Options > Tasks > Click 'Graph' button

**Node Colors:**
- Grey = Objects
- Green = Triggers
- Purple = Tasks
- Yellow = Effects

**Features:**
- View task dependencies (arrows show relationships)
- Create Tasks, Triggers, Effects directly in the graph
- Click any node to edit its configuration
- See which triggers fire which tasks

## Triggers (17 Types)

| Trigger | Description |
|---------|-------------|
| **Backpack Item Activated** | Player uses backpack item |
| **Click** | Object is clicked |
| **Collision** | Physical collision with trigger volume |
| **Item Collected** | Collectible gathered |
| **Key Pressed** | Keyboard input detected |
| **Key Released** | Keyboard key is released |
| **Player Died** | Health reaches zero |
| **Player Login** | Player enters space |
| **Player Started Moving** | Player begins movement |
| **Player Stopped Moving** | Player stops moving |
| **Swap Volume** | Audio changes |
| **Timer Stopped** | Countdown completes |
| **User Enter Trigger** | Player enters zone |
| **User Exit Trigger** | Player leaves zone |
| **Value Updated** | Variable changes |
| **Wearable Off** | Item unequipped |
| **Wearable On** | Item equipped |

## Effects (60+ Types)

**Movement/Camera:**
- Apply Velocity To Player
- Change Camera Filter/State/Zoom
- Lock/Unlock Camera
- Lock/Unlock Movement
- Teleport
- Toggle Free Camera
- Toggle Cursor Lock
- Start/Stop Auto Run

**Visual/Environment:**
- Change Bloom
- Change Fog
- Change Time of Day
- Hide/Show Object
- Hide/Show Outline

**Player:**
- Change Avatar
- Lock/Unlock Avatar Change
- Change Player Health
- Change Movement Profile
- Play Emote
- Equip Wearable
- Avatar Screen

**Audio:**
- Play Sound Once
- Play Sound In Loop
- Toggle Mute
- Change Audius Playlist
- Change Voice Group

**UI/Display:**
- Notification Pill
- Display Value
- Hide Value
- Dialogue Effector Display
- Show/Hide Token Swap
- Iframe
- Close Iframe
- Send Message to Iframes

**Game Logic:**
- Update Value
- Post Score to Leaderboard
- Reset Leaderboard
- Reset All Tasks
- Run Trigger From Effector
- Cancel Timer

**Objects:**
- Move Item
- Duplicate Item
- Portals Animation

**NPC Effects:**
- Turn To Player
- Walk to Position
- Record NPC Path
- Change Animation
- Change Mood
- Show/Hide NPC
- Message to NPC

---

# QUESTS

Turn any task into a trackable quest:

1. Go to **Space Options > Tasks**
2. Select the task
3. Toggle **Visibility On**

**Quest States:**
- NotActive → Not visible in log
- Active → Visible, incomplete
- Completed → Visible, marked complete

**Quest Groups:** Assign same group name to organize tasks together.

**Rewards:** Add wearables/collectibles granted on completion (requires Portals team assistance for item setup).

---

# VARIABLE MANAGER

Manage all variables created with Update Value effect.

**Location:** Space Options → Variable Manager

**Settings:**
- **Persistent**: Value saved across sessions (survives refresh/logout)
- **Multiplayer**: All players share the same value

**Defaults:** Non-persistent, single-player

---

# ADVANCED TOOLING: FUNCTION EFFECT

Scripting system based on NCalc expression language.

## Reading Values

| Syntax | Returns | Example |
|--------|---------|---------|
| `$T{taskName}` | Task state as text | `$T{door}` → 'Active' |
| `$TN{taskName}` | Task state as number | `$TN{door}` → 1 |
| `$N{variableName}` | Variable value | `$N{coins}` → 50 |

**Task State Numbers:** 0=NotActive, 1=Active, 2=Completed

## Setting Values

```
SetTask(taskName, 'TaskState', delaySeconds)
SetVariable(variableName, value, delaySeconds)
```

**Examples:**
```
SetTask('door', 'Active', 0.0)           // Immediate
SetTask('alarm', 'NotActive', 5.0)       // 5-second delay
SetVariable('coins', $N{coins} + 10, 0.0)
```

## Math Operators

| Operator | Example |
|----------|---------|
| `+` | `$N{coins} + 10` |
| `-` | `$N{health} - 1` |
| `*` | `$N{score} * 2` |
| `/` | `$N{time} / 2` |
| `%` | `$N{coins} % 2` (remainder) |
| `**` | `2 ** 3` (exponent = 8) |

## Comparison Operators

| Operator | Example |
|----------|---------|
| `==` | `$N{coins} == 10` |
| `!=` | `$T{quest} != 'NotActive'` |
| `>` | `$N{coins} > 10` |
| `<` | `$N{health} < 5` |
| `>=` | `$N{coins} >= 10` |
| `<=` | `$N{health} <= 0` |

## Logic Operators

| Operator | Name | Example |
|----------|------|---------|
| `&&` | AND | `$T{task1} == 'Active' && $T{task2} == 'Completed'` |
| `\|\|` | OR | `$T{task1} == 'Completed' \|\| $T{task2} == 'Completed'` |
| `!` | NOT | `!($T{alarm} == 'Active')` |

## Conditions

**if() - Single condition:**
```
if(condition, whenTrue, whenFalse)

if($N{coins} >= 10,
   SetVariable('doorUnlocked', 1, 0.0),
   0
)
```

**ifs() - Multiple conditions (first match wins):**
```
ifs(
  $N{health} <= 0, SetVariable('warning', 3, 0.0),
  $N{health} <= 3, SetVariable('warning', 2, 0.0),
  $N{health} <= 6, SetVariable('warning', 1, 0.0),
                   SetVariable('warning', 0, 0.0)
)
```

## OnChange Triggers

```
OnChange('taskName', 'TaskState')     // Specific state
OnChange('taskName')                   // Any state change
OnChange('variableName', '>= 10')     // Variable condition
```

**Task completion triggers variable:**
```
if(OnChange('puzzle1', 'Completed'),
   SetVariable('doorUnlocked', 1.0, 0.0),
   0.0)
```

**Variable threshold completes task:**
```
if(OnChange('coins', >= 10.0),
   SetTask('buyDoor', 'Completed', 0.0),
   0.0)
```

**Multiple conditions with current state check:**
```
(OnChange('task1', 'Active') || OnChange('task2', 'Completed'))
&& $T{task1} == 'Active'
&& $T{task2} == 'Completed'
```

**State change with conditional actions:**
```
if(OnChange('questStep'),
   ifs($T{questStep} == 'NotActive', SetVariable('hintText', 0.0, 0.0),
       $T{questStep} == 'Active', SetVariable('hintText', 1.0, 0.0),
       SetVariable('hintText', 2.0, 0.0)),
   0.0)
```

## SelectRandom

```
SelectRandom(item1, item2, item3, ...)
```

**Random number reward:**
```
SetVariable('coins', $N{coins} + SelectRandom(1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0), 0.0)
```

**50/50 chance:**
```
SelectRandom(true, false)
```

**Random task state:**
```
SetTask('alarm', SelectRandom('NotActive', 'Active', 'Completed'), 0.0)
```

## Math Functions

| Function | Description | Example |
|----------|-------------|---------|
| `Min(a, b)` | Returns smaller of two numbers | `Min($N{coins}, 100.0)` → cap at 100 |
| `Max(a, b)` | Returns larger of two numbers | `Max($N{health}, 0.0)` → prevent negative |
| `Round(number)` | Rounds to nearest whole | `Round(3.6)` → 4 |
| `Abs(number)` | Absolute value | `Abs(-5)` → 5 |
| `Floor(number)` | Rounds down | `Floor(3.9)` → 3 |
| `Ceiling(number)` | Rounds up | `Ceiling(3.1)` → 4 |
| `Sqrt(number)` | Square root | `Sqrt(9.0)` → 3 |

**Nesting functions:**
```
Min(Max($N{health}, 0.0), 100.0)   // Clamp health between 0-100
```

## Important Notes

- **Always use decimal notation:** `0.0`, `1.0`, `50.0` (not `0`, `1`, `50`) to avoid type errors
- **Use nested if(), NOT ifs()** - ifs() may have bugs in some cases
- **Tasks don't auto-reset** - always add reset function effects
- **Enable "Trigger on Task Change"** checkbox for Function Effects

---

# MULTIPLAYER CONSIDERATIONS

## Single Player vs Multiplayer Tasks

| Task Type | Behavior |
|-----------|----------|
| **Single Player** | Effects run only for the player who triggered it |
| **Multiplayer** | When task state changes, effects run for ALL players |

**Critical:** For looping tasks (timers, game loops), use **Single Player** tasks. Multiplayer tasks will cause all players to run the loop, causing acceleration/duplication bugs.

## Multiplayer Variable Sync Delay

Multiplayer variables take **2-3 seconds** to sync across all players. This causes race conditions when:
- Checking if another player already set a value
- Preventing duplicate actions (like multiple hosts)

**Solution:** Add delays before checking multiplayer variables:
```
// On Player Login, delay 3 seconds before checking
SetTask('CheckHostStatus', 'Active', 3.0)
```

## Host System Pattern

When only ONE player should control shared state (timers, game loops), use a host system:

**Variables needed:**
| Variable | Multiplayer? | Purpose |
|----------|--------------|---------|
| `Host_Exists` | Yes | Tracks if any player is host |
| `I_Am_Host` | No | Each player knows if they're host |

**BecomeHost Task (Single Player):**
```
// Effect 1: Claim host if none exists
if($N{Host_Exists} == 0.0,
   SetVariable('I_Am_Host', 1.0, 0.0),
   0.0
)

// Effect 2: Set global flag if we're host
if($N{I_Am_Host} == 1.0,
   SetVariable('Host_Exists', 1.0, 0.0),
   0.0
)

// Effect 3: Start game loop if host
if($N{I_Am_Host} == 1.0,
   SetTask('GameLoop', 'Active', 0.5),
   0.0
)
```

**Trigger:** Player Login → 3-second delay → BecomeHost

## Self-Looping Task Pattern

For timers or continuous updates:

```
// GameTimer task (Single Player, on Active):

// Effect 1: Increment (host only)
if($N{I_Am_Host} == 1.0,
   SetVariable('Elapsed', $N{Elapsed} + 1.0, 0.0),
   0.0
)

// Effect 2: Send to iframe
time_|Elapsed|

// Effect 3: Reset for next loop
SetTask('GameTimer', 'NotActive', 0.9)

// Effect 4: Loop
SetTask('GameTimer', 'Active', 1.0)
```

---

# LEADERBOARDS

## Post Score to Leaderboard

| Setting | Description |
|---------|-------------|
| **Value Label** | Must match the Leaderboard Score Label (e.g., "score", "coins") |

**Compatibility:**
- Works with: Trigger Cube, Building Cube, Nine Cube, Custom Import
- Does NOT work with: NPC

**Note:** For time-based leaderboards, the timer auto-posts when it ends.

---

# USING IFRAMES

Embed external web pages with bidirectional communication.

## Important: Iframe is an Effect, Not a Tool

Iframe is an **effect**, not a building tool. To display an iframe:
1. Create a task with a trigger (e.g., Player Login)
2. Add the Iframe effect to that task
3. The iframe appears when the task activates

## Iframe Effect Settings

| Setting | Description |
|---------|-------------|
| **Iframe URL** | URL to the web page |
| **Layer Order** | Z-index for stacking (higher = on top) |
| **Left Position (px)** | Distance from left edge |
| **Right Position (px)** | Distance from right edge |
| **Top Position (px)** | Distance from top edge |
| **Bottom Position (px)** | Distance from bottom edge |
| **Width (px)** | Iframe width in pixels |
| **Height (px)** | Iframe height in pixels |
| **NPC will animate** | Toggle mouth animation for NPC dialogues |

## Positioning Tips

**Important:** Only fill in position/size values you want to change. **Leave other fields blank** - don't enter zeros for fields you don't need.

**For top-centered HUD:**
- Set **only** `Top Position: 0`
- Leave Left, Right, Width, Height **blank**
- The iframe content will auto-center if CSS uses `justify-content: center`

**For bottom-right popup:**
- Set only `Bottom Position` and `Right Position`
- Leave other fields blank

**For fixed-size centered iframe:**
- Calculate Left: `(screen width - iframe width) / 2`
- Example: 1920px screen, 400px iframe → Left Position = 760
- Note: Fixed positioning doesn't adapt to different screen sizes

## Creating Transparent HUD Iframes

For HUD overlays where only the content should be visible (no background):

```css
body {
  background: transparent;
}

/* Wrap content in a container with the visible background */
.hud-container {
  display: flex;
  background: rgba(0,0,0,0.9);
  border-radius: 8px;
}
```

**Key principle:** Keep body/html transparent, apply backgrounds only to content containers. Size the iframe to match content exactly.

## SDK Setup

Add to your HTML:
```html
<script src="https://portals-labs.github.io/portals-sdk/portals-sdk.js?v=10005456"></script>
```

## Sending Messages to Unity (Iframe → Portals)

```javascript
// MUST stringify the JSON object
PortalsSdk.sendMessageToUnity(JSON.stringify({
  TaskName: "level1_intro",
  TaskTargetState: "SetNotActiveToActive"
}));
```

**Valid TaskTargetState values:**
- `ToNotActive`
- `SetNotActiveToActive`
- `SetActiveToCompleted`
- `SetCompletedToActive`
- `SetAnyToCompleted`
- `SetAnyToActive`
- `SetActiveToNotActive`
- `SetCompletedToNotActive`
- `SetNotActiveToCompleted`

## Receiving Messages from Unity (Portals → Iframe)

Use the SDK's message listener to receive commands from Portals:

```javascript
// Register the listener
PortalsSdk.setMessageListener(function(message) {
  console.log('Received:', message);

  let data = message;

  // Parse if string - but DON'T return on failure (might be underscore format)
  if (typeof message === 'string') {
    try {
      data = JSON.parse(message);
    } catch (e) {
      // Not JSON - keep as string for underscore format parsing
      data = message;
    }
  }

  const msg = typeof data === 'string' ? data : JSON.stringify(data);

  // Handle underscore format (recommended)
  if (msg.startsWith('score_')) {
    const score = parseFloat(msg.substring(6));
    if (!isNaN(score)) updateScore(score);
  } else if (msg.startsWith('time_')) {
    const elapsed = parseFloat(msg.substring(5));
    if (!isNaN(elapsed)) updateTimer(elapsed);
  }
});
```

**Sending from Portals:**

**CRITICAL:** JSON with colons (`:`) breaks Portals' NCalc parser. Use underscore format instead:

| Data | Message Format | Effect Setting |
|------|----------------|----------------|
| Score | `score_25` | `score_\|Score\|` |
| Time | `time_120` | `time_\|Elapsed_Seconds\|` |
| Team scores | `sync_120_25_30` | `sync_\|Time\|_\|Red\|_\|Blue\|` |

**Note:** In "Send Message To Iframes" effect, use `|variableName|` (pipe syntax), NOT `$N{variableName}`.

**Tip:** Use `Value Updated` trigger on variables to automatically send iframe updates when values change.

## Close Iframe

```javascript
// Must be inside user event handler (onclick)
PortalsSdk.closeIframe();
```

## URL Parameters

| Parameter | Effect |
|-----------|--------|
| `?noCloseBtn=true` | Hide close button |
| `?hideMaximizeButton=true` | Hide maximize |
| `?hideRefreshButton=true` | Hide refresh |
| `?maximized=true` | Open fullscreen |
| `?forceClose=true` | X closes instead of minimize |

**Example:**
```
https://example.com/page.html?noCloseBtn=true&maximized=true
```

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| "[object Object] is not supported" | Sending raw object | Use `JSON.stringify()` |
| "Failed to launch uniwebview" | Testing in browser | Test in Unity WebView |
| "User gesture required" | closeIframe outside click | Wrap in onclick handler |
| Iframe not receiving messages | JSON with colons | Use underscore format: `score_\|Score\|` |
| Timer not updating display | Early return in JS | Don't `return` after JSON.parse failure |
| Timer accelerates with 2+ players | All players incrementing | Use host system, Single Player task |
| Variables not syncing | Race condition | Add 3-second delay before checking |
| Multiple players claim host | Sync delay | Increase delay in DelayedHostCheck |

---

# HOW TO: TOKEN TRADING SPACE

## Part 1: Buy/Sell Zones

**Buy Zone Setup:**
1. Place Trigger Cube
2. Add User Enter Trigger → Show Token Swap effect
3. Configure: Buy=On, Sell=Off, Token Address, Wallet Address
4. Add User Exit Trigger → Hide Token Swap effect

**Sell Zone:** Same setup with Buy=Off, Sell=On

## Part 2: 3D Candlestick Chart

1. Copy token contract address
2. Open inventory → Select Chart item
3. Paste contract address
4. Click "Spawn Chart"
5. Position in space

---

# QUICK REFERENCE

## Task State Transitions

```
NotActive → Active → Completed
     ↑         ↓         ↓
     ←─────────←─────────←
```
(Any state can transition to any other)

## Common Patterns

**Door that opens on click, closes after exit:**
- Click Trigger → Set task Active (plays open animation)
- Exit Trigger with delay → Set task NotActive (plays close animation)

**Collectible counter:**
- Item Collected Trigger → Update Value effect (+1)
- Display Value effect to show count

**Multi-step quest:**
- Create dependent tasks
- Each task completion triggers next task to Active
- Toggle visibility for quest log tracking

---

# GAME DESIGN PATTERNS

## Core Loop
All games follow: **Player Action → Feedback → Reward → Repeat**

Spend 10-15 minutes designing before building to prevent confusion and edge cases.

## Pattern Types

| Pattern | Best For | Complexity |
|---------|----------|------------|
| **Collectible** | Treasure hunts, coin collection, exploration | Beginner |
| **Puzzle** | Escape rooms, logic challenges, hidden objects | Intermediate |
| **Quest/RPG** | Story-driven, NPC interactions, progression | Intermediate |
| **Racing** | Time trials, obstacle courses, leaderboards | Beginner |

---

# COMMON GOTCHAS

## Function Effects
- **Decimal notation required:** Use `10.0` not `10`
- **Case-sensitive task names:** `$T{Open Door}` works, `$T{open door}` doesn't
- **Single quotes for strings:** Use `'Active'` not `"Active"`
- **Enable "Trigger on Task Change":** Effects won't execute without this checkbox
- **Avoid ifs():** Use nested `if()` instead due to known bugs

## Tasks
- **No auto-reset:** Manually reset completed tasks if you want repeatable actions
- **Non-persistent tasks reset:** Check Space Options if progress vanishes after refresh
- **Multiplayer tasks are shared:** All players see same state; use single-player for individual progress
- **Dependent tasks:** Parent must reach "Completed" state, not just "Active"

## Triggers
- **Collision vs User Enter:** Collision handles physics; use "User Enter Trigger" for zone entry
- **Trigger cubes invisible during play:** Use build mode to verify placement
- **Key triggers need focus:** Won't work if Portals window loses focus

## NPCs
- **Rigged GLB avatars required:** Standard 3D models won't animate
- **NPC-specific effects:** "Turn To Player" and "Walk to Position" only work on NPC objects
- **Case-sensitive animations:** Names must match exactly what's in the GLB file

## Leaderboards
- **Value Label must match:** Effect label must correspond to Leaderboard label
- **Timer auto-posts:** Racing timer leaderboards post automatically when stopped
- **NPCs can't post scores:** Use Trigger Cubes instead

## Variables
- **Created on first use:** No pre-declaration needed
- **Check persistence settings:** Verify persistent and multiplayer settings in Variable Manager
- **Unset variables are undefined:** Initialize variables when players enter

## Portals/Teleportation
- **Spawn Name is case-sensitive:** Leave blank for default spawn
- **Auto Teleport:** ON = immediate on contact; OFF = requires X key
- **Cross-space teleports reset data:** Non-persistent tasks and variables reset when switching spaces

## Quick Debug Checklist
1. Open Task Debug Panel to verify triggers fire
2. Check exact names (case and space-sensitive)
3. Verify effect configuration settings
4. Use decimal notation (0.0, not 0)
5. Enable required checkboxes
6. Test simple cases first
7. Review Variable Manager values
8. Check browser console for iframe errors

---

# RESOURCES

- **Official Docs:** https://prtls.gitbook.io/portals-building-guide
- **Video Tutorials:** Available in Building Basics section
- **Portals SDK:** https://portals-labs.github.io/portals-sdk/portals-sdk.js
- **Discord:** Community help and discussions
