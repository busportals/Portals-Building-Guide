---
icon: door-open
description: Build doors that open on click, auto-close, and require keys
---

# Create a Door System

This tutorial shows you how to create interactive doors in your Portals space. You'll learn three variations: basic click-to-open, auto-closing doors, and locked doors requiring keys.

**Difficulty:** Beginner
**Time:** 15-20 minutes

## What You'll Build

- A door that opens when clicked
- Auto-close functionality after a delay
- A locked door requiring a key item

## Prerequisites

- A Portals space in Build Mode
- Two door models (open and closed states) OR one animated door GLB
- Basic familiarity with Triggers and Effects

---

## Part 1: Basic Click-to-Open Door

### Step 1: Place Your Door Models

1. Enter **Build Mode** (wrench icon)
2. Place your **closed door** model using Custom GLB
3. Name it `door_closed`
4. Place your **open door** model in the same position
5. Name it `door_open`

### Step 2: Create the Door Task

1. Select the closed door object
2. Open the **Tasks** panel
3. Create a new task named `door1`
4. The task starts as **NotActive** (door closed)

### Step 3: Add Click Trigger

1. With `door_closed` selected, add a **Click** trigger
2. Add these effects:
   - **Set Task State**: `door1` → Active
   - **Hide Object**: `door_closed`
   - **Show Object**: `door_open`
   - **Play Sound Once**: door_open.mp3 (optional)

### Step 4: Test It

1. Exit Build Mode
2. Click the door
3. The closed door should hide and open door should appear

---

## Part 2: Auto-Close Door

Add automatic closing after a delay.

### Step 1: Add Exit Trigger

1. Place a **Trigger Cube** in the doorway (where players walk through)
2. Make it large enough to cover the passage
3. Add a **User Exit Trigger**

### Step 2: Configure Auto-Close

Add these effects to the User Exit Trigger:

- **Delay**: 2 seconds (or your preference)
- **Set Task State**: `door1` → NotActive
- **Show Object**: `door_closed`
- **Hide Object**: `door_open`
- **Play Sound Once**: door_close.mp3 (optional)

### Alternative: Close on Timer

Instead of exit trigger, close after fixed time:

1. On the Click trigger (when opening), add:
   - **Set Task State**: `door1` → NotActive (with 3.0 second delay)
   - **Show Object**: `door_closed` (with 3.0 second delay)
   - **Hide Object**: `door_open` (with 3.0 second delay)

---

## Part 3: Toggle Door (Open/Close on Click)

Make the door toggle between states on each click.

### Using Function Effect

1. On the door click trigger, add a **Function Effect**:

```
if($T{door1} == 'NotActive',
   SetTask('door1', 'Active', 0.0),
   SetTask('door1', 'NotActive', 0.0)
)
```

2. Add visual effects that respond to task state:
   - When `door1` becomes Active → Hide closed, Show open
   - When `door1` becomes NotActive → Show closed, Hide open

### Using Separate Triggers

Alternatively, add click triggers to both door models:

**On `door_closed` Click:**
- Set `door1` Active
- Hide `door_closed`
- Show `door_open`

**On `door_open` Click:**
- Set `door1` NotActive
- Show `door_closed`
- Hide `door_open`

---

## Part 4: Locked Door with Key

Create a door that only opens if the player has collected a key.

### Step 1: Create the Key

1. Place a **Collectible GLB** for your key model
2. Name it `redKey`

### Step 2: Track Key Collection

1. On the key's **Item Collected** trigger, add:
   - **Update Value**: Variable `hasRedKey`, Set to `1`
   - **Notification Pill**: "Red key acquired!"
   - **Play Sound Once**: key_pickup.mp3

### Step 3: Configure Locked Door

Replace the simple click trigger with a conditional one.

**Option A: Using Function Effect**

On door click, add Function Effect:

```
if($N{hasRedKey} == 1.0,
   SetTask('door1', 'Active', 0.0) +
   SetVariable('hasRedKey', 0.0, 0.0),
   0.0
)
```

This opens the door and consumes the key.

**Option B: Using Value Updated Trigger**

1. Create a task `tryOpenDoor`
2. On door click → Set `tryOpenDoor` Active
3. Add **Value Updated** trigger watching `tryOpenDoor`:
   - Condition: When `hasRedKey` >= 1
   - Effects: Open the door, set `hasRedKey` = 0

### Step 4: Feedback for Locked Door

Add feedback when player clicks without the key:

```
if($N{hasRedKey} == 1.0,
   SetTask('door1', 'Active', 0.0) +
   SetVariable('hasRedKey', 0.0, 0.0),
   SetTask('lockedFeedback', 'Active', 0.0)
)
```

On `lockedFeedback` task:
- **Notification Pill**: "This door is locked. Find the red key!"
- **Play Sound Once**: door_locked.mp3
- Set `lockedFeedback` back to NotActive after 0.5s

---

## Part 5: Animated Door (Single GLB)

If your door GLB has open/close animations built in:

### Step 1: Use Portals Animation Effect

1. On click trigger, add **Portals Animation** effect
2. Select the door object
3. Choose the "open" animation
4. Set animation to play once

### Step 2: Close Animation

1. On exit trigger (or timer), add **Portals Animation** effect
2. Select the door object
3. Choose the "close" animation

---

## Complete Example: Dungeon Door

**Scenario:** A locked door in a dungeon that requires a key, plays sounds, and auto-closes.

### Objects

| Object | Type | Name |
|--------|------|------|
| Closed door model | Custom GLB | `dungeonDoor_closed` |
| Open door model | Custom GLB | `dungeonDoor_open` |
| Key collectible | Collectible GLB | `dungeonKey` |
| Doorway zone | Trigger Cube | `doorwayZone` |

### Tasks

| Task | Purpose |
|------|---------|
| `dungeonDoor` | Door state (NotActive=closed, Active=open) |

### Variables

| Variable | Purpose |
|----------|---------|
| `hasKey` | 1 if player has the key |

### Setup

**1. Key Collection (`dungeonKey` Item Collected):**
- Update Value: `hasKey` = 1
- Notification Pill: "Dungeon key found!"
- Play Sound Once: key_collect.mp3

**2. Door Click (`dungeonDoor_closed` Click):**

Function Effect:
```
if($N{hasKey} == 1.0,
   SetTask('dungeonDoor', 'Active', 0.0) +
   SetVariable('hasKey', 0.0, 0.0),
   SetTask('doorLocked', 'Active', 0.0)
)
```

Additional effects when door opens (use OnChange or separate trigger):
- Hide Object: `dungeonDoor_closed`
- Show Object: `dungeonDoor_open`
- Play Sound Once: door_creak_open.mp3

**3. Locked Feedback (`doorLocked` task becomes Active):**
- Notification Pill: "The door is locked..."
- Play Sound Once: door_rattle.mp3
- Set `doorLocked` NotActive (0.5s delay)

**4. Auto-Close (`doorwayZone` User Exit):**
- Delay: 2 seconds
- Set `dungeonDoor` NotActive
- Show Object: `dungeonDoor_closed`
- Hide Object: `dungeonDoor_open`
- Play Sound Once: door_close.mp3

---

## Troubleshooting

### Door doesn't respond to clicks
- Verify the closed door has a Click trigger attached
- Check that the door object is set as clickable
- Ensure you're clicking the correct object (not a trigger cube)

### Door opens but visuals don't change
- Verify Show/Hide effects target the correct objects
- Check object names match exactly (case-sensitive)
- Ensure both door models exist and are named properly

### Key doesn't unlock door
- Verify variable name matches: `hasKey` vs `haskey`
- Check you're using `== 1.0` not `== 1` (decimal notation)
- Confirm the key's Item Collected trigger sets the variable

### Door closes immediately
- Check for conflicting triggers
- Verify delay values are set correctly
- Ensure User Exit trigger is on the doorway, not the door itself

---

## Next Steps

- Add multiple locked doors with different colored keys
- Create doors that require multiple keys
- Build pressure-plate activated doors (see [Puzzle Games](../game-design-patterns/puzzle-games.md))
- Add visual indicators showing which key is needed
