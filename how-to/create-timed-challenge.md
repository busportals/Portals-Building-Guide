---
icon: stopwatch
description: Build a timed challenge with countdown, leaderboard, and reset
---

# Create a Timed Challenge

Build a race or time-limited challenge where players compete for the fastest completion time.

**Difficulty:** Beginner-Intermediate
**Time:** 20-25 minutes

## What You'll Build

- Countdown timer displayed on screen
- Start/finish detection
- Automatic leaderboard posting
- Reset functionality for retries

---

## Part 1: Setup Zones

### Start Zone

1. Place **Trigger Cube** at starting line
2. Name it `startZone`
3. Add **User Enter Trigger**

### Finish Zone

1. Place **Trigger Cube** at finish line
2. Name it `finishZone`
3. Add **User Enter Trigger**

---

## Part 2: Timer Logic

### Tasks

| Task | Purpose |
|------|---------|
| `raceReady` | Waiting to start |
| `raceActive` | Timer running |
| `raceComplete` | Finished |

### Start Zone Entry

Effects:
1. Set `raceReady` Active
2. **Lock Movement** (brief pause)
3. **Teleport** to exact start position
4. **Notification Pill**: "Press SPACE to start!"

### Key Press to Start

Add **Key Pressed** trigger (Space) when `raceReady` Active:
1. Set `raceActive` Active
2. Set `raceReady` NotActive
3. **Unlock Movement**
4. **Start Timer** (automatically displays on screen)

### Finish Zone Entry

When `raceActive` is Active:
1. Set `raceComplete` Active
2. Set `raceActive` NotActive
3. **Post Score to Leaderboard**
4. **Notification Pill**: "Finished!"

---

## Part 3: Leaderboard

1. Place **Leaderboard** object in space
2. Set Score Label: `time`
3. Timer auto-posts when it stops

---

## Part 4: Reset

### Manual Reset

Add **Key Pressed** trigger (R key):
1. **Teleport** to start
2. Set all tasks NotActive
3. Reset timer variable

---

## Quick Reference

```
Enter Start → Lock, "Press SPACE"
Press Space → Unlock, Start Timer
Cross Finish → Stop Timer, Post Score
Press R → Reset Everything
```

---

## Troubleshooting

- **Timer not starting**: Check Key Pressed trigger and task conditions
- **Score not posting**: Verify leaderboard Score Label matches
- **Can't restart**: Ensure reset clears all task states
