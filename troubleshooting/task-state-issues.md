---
icon: list-check
description: Fix tasks that won't change state or behave unexpectedly
---

# Task State Issues

Tasks have three states: **NotActive**, **Active**, and **Completed**. This guide helps when tasks get stuck or don't transition as expected.

## Understanding Task Persistence

**Important:** All tasks in Portals start in the **NotActive** state. This applies to:
- New tasks you create
- All tasks for new players entering your space for the first time

**Tasks persist by default.** Once a task changes state, it stays in that state across sessions unless:
- You explicitly change it with a trigger/effect
- You've enabled "Non-Persistent" in the task settings

This means if a player completes a quest and returns later, the task will still be **Completed**. Tasks do not automatically reset to NotActive on their own.

---

## Quick Checklist

- [ ] **Task exists** - Verify the task name in Space Options > Tasks
- [ ] **Trigger is firing** - Check Task Debug Panel for activity
- [ ] **Effect is configured** - The effect must set the correct target state
- [ ] **No conflicting effects** - Multiple effects on the same task can cause issues

---

## Task Won't Change State

**Symptom:** Trigger fires but task state doesn't change.

### Step 1: Verify the Trigger

1. Open **Task Debug Panel** (Space Options > Tasks Debug)
2. Perform the action that should trigger the change
3. Watch for trigger activity in the panel

**If no activity appears:**
- Check trigger configuration (correct trigger type, correct object)
- For collision triggers, verify the trigger cube is positioned correctly
- For click triggers, ensure the object is clickable

### Step 2: Check the Effect Configuration

1. Edit the task and find the trigger
2. Verify the effect is set to change the task state
3. Check the target state is correct:
   - `SetNotActiveToActive` - Activates from NotActive
   - `SetActiveToCompleted` - Completes from Active
   - `SetAnyToActive` - Activates from any state

### Step 3: Look for Conflicts

Multiple effects targeting the same task can override each other:

```
// Problem: Two triggers fire at once
Trigger A → Set task to Active
Trigger B → Set task to NotActive
// Result: Unpredictable state
```

**Fix:** Add conditions or delays to prevent simultaneous execution.

---

## Dependent Task Not Activating

**Symptom:** A task that depends on another task won't activate even after the parent completes.

### How Dependencies Work

1. Parent task must be **Completed** (not just Active)
2. Dependent task starts in **NotActive**
3. When parent completes, dependent task becomes **Active** automatically

### Diagnostic Steps

1. **Check parent task state**
   - Open Task Debug Panel
   - Verify parent shows "Completed"

2. **Verify dependency configuration**
   - Edit the dependent task
   - Check "Depends On" field
   - Task name must match exactly (case-sensitive)

3. **Check for circular dependencies**
   ```
   // Problem: A depends on B, B depends on A
   Task A: Depends on Task B
   Task B: Depends on Task A
   // Result: Neither can ever activate
   ```

---

## Task Resets Unexpectedly

**Symptom:** Task state reverts to NotActive when it shouldn't.

**Remember:** By default, tasks persist across sessions. If a task is resetting, something is explicitly causing it.

### Common Causes

1. **Non-Persistent Setting Enabled**
   - Check Space Options > Tasks
   - If "Non-Persistent" is enabled, task resets on page reload
   - Disable for tasks that should save progress
   - **Default is persistent** - you must explicitly enable non-persistent behavior

2. **Reset All Tasks Effect**
   - Search for any "Reset All Tasks" effects in your space
   - These reset ALL tasks to NotActive
   - Consider using targeted task state changes instead

3. **Player Login Trigger Resetting Tasks**
   - Check if you have a Player Login trigger that sets tasks to NotActive
   - This would reset returning players' progress
   - If you want one-time initialization, check the task state first:
   ```
   // Only set up if player hasn't started yet
   if($T{gameStarted} == 'NotActive',
      SetTask('tutorial', 'Active', 0.0),
      0.0
   )
   ```

4. **Page Reload Triggered**
   - Teleporting between spaces resets non-persistent tasks
   - Check if any portals are inadvertently reloading the space

---

## Task Shows Wrong State in Debug Panel

**Symptom:** Task Debug Panel shows a different state than expected.

### Single-Player vs Multiplayer Tasks

| Task Type | Behavior |
|-----------|----------|
| **Single Player** | Each player has their own task state |
| **Multiplayer** | All players share the same task state |

**Issue:** You're checking one player's state while another player changed it.

**Fix:**
- For shared progress, use Multiplayer tasks
- For individual progress, use Single Player tasks

### Checking the Correct Task

1. Note the exact task name from Space Options > Tasks
2. In Debug Panel, find that specific task
3. Multiple tasks with similar names can cause confusion

---

## Quest Not Appearing in Quest Log

**Symptom:** Task is Active but doesn't show in the player's quest log.

### Requirements for Quest Visibility

1. **Visibility must be ON**
   - Space Options > Tasks
   - Select the task
   - Enable "Visibility" toggle

2. **Task must be Active or Completed**
   - NotActive tasks don't appear in quest log
   - Activate the task first

3. **Quest group (optional)**
   - Assign a group name to organize related quests
   - All tasks in same group appear together

---

## Task State Transition Reference

Tasks can transition between any states. Use the correct transition value:

| From | To | Value |
|------|-----|-------|
| NotActive | Active | `SetNotActiveToActive` |
| Active | Completed | `SetActiveToCompleted` |
| Completed | Active | `SetCompletedToActive` |
| NotActive | Completed | `SetNotActiveToCompleted` |
| Active | NotActive | `SetActiveToNotActive` |
| Completed | NotActive | `SetCompletedToNotActive` |
| Any | Active | `SetAnyToActive` |
| Any | Completed | `SetAnyToCompleted` |
| Any | NotActive | `ToNotActive` |

### Using with Function Effects

```
// Set task to Active immediately
SetTask('myTask', 'Active', 0.0)

// Set task to Completed after 2 seconds
SetTask('myTask', 'Completed', 2.0)

// Check state before changing
if($T{door} == 'NotActive',
   SetTask('door', 'Active', 0.0),
   0.0
)
```

---

## Debugging Workflow

1. **Open Task Debug Panel**
2. **Identify the task** by name
3. **Note current state** (NotActive/Active/Completed)
4. **Trigger the action** that should change state
5. **Watch for:**
   - Trigger activity (did the trigger fire?)
   - State change (did the task update?)
   - Any other tasks changing (conflicts?)
6. **If state doesn't change**, check effect configuration
7. **If state changes incorrectly**, look for conflicting effects
