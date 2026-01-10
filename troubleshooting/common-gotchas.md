---
icon: lightbulb
description: Quick answers to frequently encountered problems
---

# Common Gotchas

Quick fixes for the most common issues builders encounter.

---

## Function Effects

### Numbers must use decimal notation

```
// Wrong - causes type errors
SetVariable('coins', 10, 0)

// Correct
SetVariable('coins', 10.0, 0.0)
```

### Task names are case-sensitive

```
// If task is named "Open Door"
$T{Open Door}    // Correct
$T{open door}    // Wrong
$T{OpenDoor}     // Wrong
```

### Single quotes for strings, not double quotes

```
// Wrong
if($T{quest} == "Active", ...)

// Correct
if($T{quest} == 'Active', ...)
```

### Enable "Trigger on Task Change"

Function Effects won't run unless this checkbox is enabled in the effect settings.

### Use nested if() instead of ifs()

The `ifs()` function has known bugs. Use nested `if()` for reliability:

```
// Instead of ifs()
if(condition1,
   result1,
   if(condition2,
      result2,
      defaultResult
   )
)
```

---

## Tasks

### Tasks don't auto-reset

If a player completes a task and you want them to do it again, you must manually reset it with an effect or Function Effect.

### Non-persistent tasks reset on reload

If your task progress disappears after page refresh, check if the task is marked as "Non-Persistent" in Space Options > Tasks.

### Multiplayer tasks are shared

All players see the same state for multiplayer tasks. Use single-player tasks for individual progress.

### Dependent tasks need parent to be Completed

A dependent task only activates when its parent reaches the **Completed** state, not just Active.

---

## Triggers

### Collision vs Click

| Trigger Type | When It Fires |
|--------------|---------------|
| Collision | Player touches the trigger volume |
| Click | Player clicks the object |
| User Enter Trigger | Player enters the trigger volume |
| User Exit Trigger | Player leaves the trigger volume |

**Collision** is for physics collisions. For zone entry, use **User Enter Trigger**.

### Trigger cubes are invisible in play mode

You can't see trigger cubes when playing. Use the gizmo in build mode to verify placement.

### Key triggers need focus

Key Pressed and Key Released triggers only work when the Portals window has focus. Clicking outside the game window disables them.

---

## Iframes

### Iframe is an Effect, not a Tool

You don't place iframes from the building tools menu. Add an Iframe effect to a task trigger.

### Always JSON.stringify messages

```javascript
// Wrong
PortalsSdk.sendMessageToUnity({TaskName: "x", TaskTargetState: "y"});

// Correct
PortalsSdk.sendMessageToUnity(JSON.stringify({TaskName: "x", TaskTargetState: "y"}));
```

### SDK only works in Portals

Testing in a regular browser won't work. Deploy and test in the actual Portals environment.

### Close requires user gesture

```javascript
// Wrong - won't work
PortalsSdk.closeIframe();

// Correct - inside click handler
button.onclick = () => PortalsSdk.closeIframe();
```

---

## NPCs

### NPCs need rigged GLB avatars

Standard 3D models won't animate. Use a GLB with proper rigging (skeleton/armature).

### NPC effects only work on NPCs

Effects like "Turn To Player" and "Walk to Position" only work when attached to NPC objects, not regular Custom GLBs.

### Animation names are case-sensitive

When using Change Animation effect, the animation name must match exactly what's in the GLB file.

---

## Leaderboards

### Value Label must match

The "Value Label" in Post Score effect must exactly match the score label configured on your Leaderboard object.

### Timer leaderboards auto-post

If using a timer for racing, the score posts automatically when the timer stops. You don't need a separate Post Score effect.

### NPCs can't post scores

Post Score to Leaderboard doesn't work from NPC triggers. Use a Trigger Cube instead.

---

## Variables

### Variables are created on first use

You don't need to pre-declare variables. The first `Update Value` or `SetVariable` creates them.

### Check persistence settings

In Space Options > Variable Manager:
- **Persistent**: Value saved across sessions
- **Multiplayer**: All players share the value

Default is non-persistent, single-player.

### Variables don't exist until set

Referencing a variable that hasn't been set returns undefined/0. Always initialize variables when players enter.

---

## Portals / Teleportation

### Spawn Name is case-sensitive

```
Spawn Name: "start"    // Only works if spawn point is named exactly "start"
```

Leave blank to use the default spawn point.

### Auto Teleport timing

With Auto Teleport ON, players teleport immediately on contact. With it OFF, they must press X.

### Cross-space teleports reset non-persistent data

Teleporting to a different space reloads everything. Non-persistent tasks and variables reset.

---

## Quick Debug Checklist

When something doesn't work:

1. **Open Task Debug Panel** - Is the trigger firing?
2. **Check exact names** - Case-sensitive, space-sensitive
3. **Verify effect configuration** - Correct target, correct settings
4. **Use decimals** - `0.0` not `0`
5. **Enable checkboxes** - "Trigger on Task Change" etc.
6. **Test simple first** - Isolate the problem
7. **Check Variable Manager** - Are values what you expect?
8. **Browser console** - For iframe JavaScript errors
