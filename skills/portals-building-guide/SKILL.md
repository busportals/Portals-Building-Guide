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

## Triggers (14 Types)

| Trigger | Description |
|---------|-------------|
| **Backpack Item Activated** | Player uses backpack item |
| **Click** | Object is clicked |
| **Collision** | Physical collision with trigger volume |
| **Item Collected** | Collectible gathered |
| **Key Pressed** | Keyboard input detected |
| **Player Died** | Health reaches zero |
| **Player Login** | Player enters space |
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
- Start/Stop Auto Run

**Visual/Environment:**
- Change Bloom
- Change Fog
- Change Time of Day
- Hide/Show Object
- Hide/Show Outline

**Player:**
- Change Avatar
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

**UI/Display:**
- Notification Pill
- Display Value
- Dialogue Effector Display
- Show/Hide Token Swap
- Iframe
- Close Iframe

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

**Example:**
```
if(OnChange('puzzle1', 'Completed'),
   SetVariable('doorUnlocked', 1, 0.0),
   0)
```

## SelectRandom

```
SelectRandom(item1, item2, item3, ...)
SelectRandom(1, 2, 3, 4, 5)
SelectRandom('red', 'blue', 'green')
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

# DEBUGGING GUIDE

## When Function Effects Don't Work

1. **Check decimal notation** - Use `0.0` not `0`
2. **Verify task/variable names** - Case-sensitive, must match exactly
3. **Enable "Trigger on Task Change"** - Checkbox must be checked
4. **Use Task Debug Panel** - Space Options > Tasks Debug to see if triggers fire
5. **Check parentheses** - Mismatched parentheses cause silent failures

## When Tasks Don't Change State

1. **Verify trigger is firing** - Check Task Debug Panel
2. **Check dependent task requirements** - Parent must be Completed
3. **Look for conflicting effects** - Multiple effects on same task
4. **Check multiplayer vs single-player** - Different state per player type

## When Iframes Don't Work

1. **Remember: Iframe is an Effect** - Not a building tool
2. **Use JSON.stringify()** - `PortalsSdk.sendMessageToUnity(JSON.stringify({...}))`
3. **Test in Portals, not browser** - SDK only works in-game
4. **User gesture required for close** - Wrap in onclick handler
5. **Check positioning values** - May be off-screen

## Common Error Messages

| Error | Cause | Fix |
|-------|-------|-----|
| "[object Object] is not supported" | Missing JSON.stringify | Use `JSON.stringify()` |
| "Failed to launch uniwebview" | Testing in browser | Test in Portals app |
| Type cast error | Integer instead of decimal | Use `10.0` not `10` |
| Task not found | Name mismatch | Check exact spelling/case |

---

# GAME DESIGN TEMPLATES

## Collectible Game

**Objective:** Collect items, track score, post to leaderboard.

**Components:**
- Tasks: `gameStart`, `gameActive`, `gameComplete`
- Variables: `score` (persistent), `itemsCollected`
- Triggers: Item Collected, Timer Stopped (optional)
- Effects: Update Value, Display Value, Post Score

**Setup Pattern:**
1. Player Login → Set `gameActive` to Active, initialize `score` to 0
2. Item Collected → Update Value: `score + 1`
3. All items collected OR timer ends → Set `gameComplete`, Post Score
4. Display Value effect to show score on screen

**Function Effect Example:**
```
if(OnChange('collectItem'),
   SetVariable('score', $N{score} + 1.0, 0.0) +
   if($N{score} >= 10.0,
      SetTask('gameComplete', 'Active', 0.0),
      0.0
   ),
   0.0
)
```

## Quest/RPG Game

**Objective:** Multi-stage story with NPC interactions.

**Components:**
- Dependent Tasks: `quest1`, `quest2`, `quest3` (chained)
- NPCs with dialogue trees
- Quest visibility enabled for quest log
- Reward items on completion

**Setup Pattern:**
1. NPC Click → Set `quest1` Active, show dialogue
2. Player completes objective → Set `quest1` Completed
3. `quest1` Completed triggers `quest2` Active (dependency)
4. Final quest completion → Grant reward, show completion

**Quest Configuration:**
- Space Options > Tasks > Select quest task
- Enable Visibility for quest log
- Set Quest Group for organization
- Configure rewards (requires Portals team for items)

## Racing/Timed Challenge

**Objective:** Complete course in fastest time, leaderboard ranking.

**Components:**
- Tasks: `raceReady`, `raceActive`, `raceComplete`
- Timer trigger and effects
- Checkpoint trigger cubes
- Leaderboard with time-based scoring

**Setup Pattern:**
1. Player enters start zone → Teleport to start, reset timer
2. Press key or collision → Set `raceActive`, Start Timer (auto-displays on screen)
3. Cross checkpoints → Validate path (optional)
4. Finish line collision → Stop timer, auto-post score

## Puzzle/Escape Room

**Objective:** Solve puzzles in sequence to progress.

**Components:**
- Tasks for each puzzle: `puzzle1`, `puzzle2`, etc.
- Hidden objects (Show/Hide effects)
- Lock/key mechanics using variables
- Sequential dependencies

**Setup Pattern:**
```
Puzzle 1 Completed → Show key object
Key Collected → Set 'hasKey' = 1
Door Click + hasKey = 1 → Open door, activate Puzzle 2
```

**Key Pattern:**
```
if($N{hasKey} == 1.0 && OnChange('doorClick'),
   SetTask('door', 'Active', 0.0) +
   SetTask('puzzle2', 'Active', 0.0),
   0.0
)
```

---

# COMMON EXPRESSION PATTERNS

## Safe Math Operations

```
// Add with upper bound (cap at 100)
Min($N{health} + 10.0, 100.0)

// Subtract with lower bound (floor at 0)
Max($N{health} - 5.0, 0.0)

// Clamp between min and max
Min(Max($N{value}, 0.0), 100.0)
```

## State Machine

```
// Multiple states based on a single variable
if($N{gameState} == 0.0,
   SetTask('intro', 'Active', 0.0),
   if($N{gameState} == 1.0,
      SetTask('playing', 'Active', 0.0),
      if($N{gameState} == 2.0,
         SetTask('gameOver', 'Active', 0.0),
         0.0
      )
   )
)
```

## Cooldown/Debounce

```
// Allow action only if canFire is 1, then disable for 2 seconds
if($N{canFire} == 1.0,
   SetVariable('canFire', 0.0, 0.0) +
   SetVariable('canFire', 1.0, 2.0) +
   SetTask('fireWeapon', 'Active', 0.0),
   0.0
)
```

## Toggle Pattern

```
// Toggle a door open/closed
if($T{door} == 'NotActive',
   SetTask('door', 'Active', 0.0),
   SetTask('door', 'NotActive', 0.0)
)
```

## Counter with Threshold

```
// Increment counter and trigger at threshold
SetVariable('count', $N{count} + 1.0, 0.0) +
if($N{count} >= 5.0,
   SetTask('unlock', 'Active', 0.0) +
   SetVariable('count', 0.0, 0.0),
   0.0
)
```

## Random Selection

```
// Random outcome (1-4)
SetVariable('outcome', SelectRandom(1.0, 2.0, 3.0, 4.0), 0.0)

// Random with action
if(SelectRandom(1.0, 2.0) == 1.0,
   SetTask('pathA', 'Active', 0.0),
   SetTask('pathB', 'Active', 0.0)
)
```

## Chained Delays

```
// Sequence of actions with delays
SetTask('step1', 'Active', 0.0) +
SetTask('step2', 'Active', 1.0) +
SetTask('step3', 'Active', 2.0) +
SetTask('step1', 'NotActive', 3.0)
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

**Centering an iframe horizontally:**
- Calculate: `Left Position = (screen width - iframe width) / 2`
- Example: 1920px screen, 400px iframe → Left Position = 760

**For HUD elements (scores, timers):**
- Size iframe to exactly match content (no extra space)
- Use `Top: 0` for top-of-screen HUDs
- Typical HUD bar: Width ~400px, Height ~50px

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

  // Parse if string
  let data = message;
  if (typeof message === 'string') {
    try {
      data = JSON.parse(message);
    } catch (e) {
      return; // Not JSON
    }
  }

  // Handle actions
  if (data.action === 'updateScore') {
    updateScore(data.score);
  }
});
```

**Sending from Portals:**
Use the "Send Message To Iframes" effect with JSON:
```json
{"action":"updateScore","score":$N{Score}}
```

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

- **"[object Object] is not supported"** → Use `JSON.stringify()`
- **"Failed to launch uniwebview"** → Test in Unity WebView, not browser
- **"User gesture required"** → Wrap in onclick handler

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

# RESOURCES

- **Official Docs:** https://prtls.gitbook.io/portals-building-guide
- **Video Tutorials:** Available in Building Basics section
- **Portals SDK:** https://portals-labs.github.io/portals-sdk/portals-sdk.js
