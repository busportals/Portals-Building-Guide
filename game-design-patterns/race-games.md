---
icon: timer
description: Design time trials, obstacle courses, and competitive leaderboards
---

# Racing Games

Racing games challenge players to complete courses as fast as possible. They're highly replayable and create natural competition through leaderboards.

## Core Loop

```
Start Race → Navigate Course → Cross Finish → Post Time → Try to Beat Score
```

## Game Variations

| Variation | Description | Example |
|-----------|-------------|---------|
| **Time Trial** | Beat your own best time | "Complete the parkour course in under 60 seconds" |
| **Checkpoint Race** | Hit markers in order | "Race through all 5 checkpoints" |
| **Obstacle Course** | Avoid hazards while racing | "Navigate the laser maze without getting hit" |
| **Competitive** | Beat other players' times | "Top 10 fastest times on the leaderboard" |
| **Ghost Racing** | Race against recorded runs | "Beat the developer's ghost time" |

---

## Core Concepts

### Timer System

Portals has built-in timer functionality:
- **Start Timer:** Use Display Value with a timer variable
- **Stop Timer:** Timer Stopped trigger fires when it reaches zero
- **For counting UP:** Track elapsed time with periodic variable updates

### Checkpoint Validation

Ensure players complete the full course:
- Track which checkpoints are hit
- Only allow finish if all checkpoints were reached
- Prevents shortcut cheating

### Leaderboard Integration

Time-based leaderboards auto-post when timer stops:
1. Configure Leaderboard with time-based scoring
2. Timer automatically posts when it ends
3. Lower times = better ranking

---

## Components Needed

### Basic Setup

| Component | Portals Tool/Feature | Purpose |
|-----------|---------------------|---------|
| Start zone | Trigger Cube | Begin the race |
| Finish zone | Trigger Cube | End the race |
| Timer display | Display Value effect | Show elapsed/remaining time |
| Leaderboard | Leaderboard tool | Rank player times |
| Course markers | Visual objects | Guide the path |

### Optional Enhancements

| Component | Portals Tool/Feature | Purpose |
|-----------|---------------------|---------|
| Checkpoints | Trigger Cubes + Variables | Validate full course |
| Reset zones | Trigger Cubes | Respawn on fall |
| Moving obstacles | Move Item effect | Dynamic challenges |
| Speed boosts | Apply Velocity effect | Add variety |
| Countdown | Timed task sequence | "3, 2, 1, GO!" |

---

## Pattern 1: Simple Time Trial

### Design
Player races from start to finish. Timer runs until they cross the line.

### Setup

**Tasks:**
| Task | Purpose |
|------|---------|
| `raceReady` | Waiting to start |
| `raceActive` | Race in progress |
| `raceComplete` | Finished |

**Variables:**
| Variable | Purpose |
|----------|---------|
| `raceTime` | Elapsed time (if counting up) |

**Implementation:**

1. **Start Zone:**
   - Trigger Cube at starting line
   - User Enter Trigger:
     - Lock Movement (brief, for countdown)
     - Teleport to exact start position
     - Set `raceReady` Active
     - Display: "Press SPACE to start!"

2. **Race Start:**
   - Key Pressed trigger (Space) when `raceReady` is Active:
     - Set `raceActive` Active
     - Set `raceReady` NotActive
     - Unlock Movement
     - Start timer display

3. **Finish Zone:**
   - Trigger Cube at finish line
   - User Enter Trigger when `raceActive` is Active:
     - Set `raceComplete` Active
     - Set `raceActive` NotActive
     - Stop/display final time
     - Post Score to Leaderboard
     - Notification: "Race complete! Time: X.XX"

---

## Pattern 2: Checkpoint Race

### Design
Player must hit all checkpoints in order before finish counts.

### Setup

**Tasks:**
| Task | Purpose |
|------|---------|
| `raceActive` | Race in progress |
| `checkpoint1`, `checkpoint2`, `checkpoint3` | Checkpoint states |

**Variables:**
| Variable | Purpose |
|----------|---------|
| `checkpointsHit` | Counter |
| `totalCheckpoints` | Total required (e.g., 3) |

**Implementation:**

1. **Race Start:**
   - Set all checkpoint tasks to NotActive
   - Set `checkpointsHit` = 0
   - Set `totalCheckpoints` = 3
   - Start timer

2. **Each Checkpoint (in order):**

   **Checkpoint 1:**
   ```
   if($TN{checkpoint1} == 0.0,
      SetTask('checkpoint1', 'Completed', 0.0) +
      SetVariable('checkpointsHit', 1.0, 0.0) +
      // Visual/audio feedback
      0.0,
      0.0
   )
   ```

   **Checkpoint 2:**
   ```
   if($TN{checkpoint1} == 2.0 && $TN{checkpoint2} == 0.0,
      SetTask('checkpoint2', 'Completed', 0.0) +
      SetVariable('checkpointsHit', 2.0, 0.0),
      0.0
   )
   ```

   (Only triggers if checkpoint 1 was already hit)

3. **Finish Line:**
   ```
   if($N{checkpointsHit} >= $N{totalCheckpoints},
      SetTask('raceComplete', 'Active', 0.0) +
      // Post score, stop timer
      0.0,
      // Not all checkpoints hit
      SetTask('missedCheckpoint', 'Active', 0.0)
   )
   ```

4. **Checkpoint Markers:**
   - Show Outline effect on current target checkpoint
   - Hide Outline when passed
   - Color coding: Green = hit, Red = missed, Yellow = current

---

## Pattern 3: Countdown Start

### Design
"3, 2, 1, GO!" sequence before race begins.

### Setup

**Tasks:**
| Task | Purpose |
|------|---------|
| `countdown3` | Shows "3" |
| `countdown2` | Shows "2" |
| `countdown1` | Shows "1" |
| `countdownGo` | Shows "GO!" |

**Implementation:**

When player triggers race start:

```
SetTask('countdown3', 'Active', 0.0) +
SetTask('countdown3', 'NotActive', 1.0) +
SetTask('countdown2', 'Active', 1.0) +
SetTask('countdown2', 'NotActive', 2.0) +
SetTask('countdown1', 'Active', 2.0) +
SetTask('countdown1', 'NotActive', 3.0) +
SetTask('countdownGo', 'Active', 3.0) +
SetTask('countdownGo', 'NotActive', 3.5) +
SetTask('raceActive', 'Active', 3.0)
```

**Each countdown task:**
- Shows a Billboard or World Text with the number
- Plays a beep sound
- Movement locked until "GO!"

---

## Pattern 4: Obstacle Avoidance

### Design
Player must avoid hazards while racing. Getting hit adds time penalty or resets.

### Setup

**Variables:**
| Variable | Purpose |
|----------|---------|
| `penalties` | Time penalties accumulated |
| `lives` | Lives remaining (optional) |

**Implementation:**

1. **Hazard Zones:**
   - Trigger Cubes on dangerous areas
   - User Enter Trigger:
     - Either: Add time penalty
       ```
       SetVariable('penalties', $N{penalties} + 5.0, 0.0)
       ```
     - Or: Reset to last checkpoint
       ```
       SetTask('resetToCheckpoint', 'Active', 0.0)
       // Teleport effect to checkpoint position
       ```
     - Play damage sound
     - Flash screen red (Change Camera Filter)

2. **Moving Obstacles:**
   - Use Move Item effects with looping patterns
   - Trigger on race start, stop on race end

3. **Final Score:**
   - Base time + penalties = final score
   - Or: Only post if no penalties (perfect run)

---

## Pattern 5: Reset/Respawn System

### Design
Let players reset if they fall off or get stuck.

### Setup

**Variables:**
| Variable | Purpose |
|----------|---------|
| `lastCheckpointX`, `lastCheckpointY`, `lastCheckpointZ` | Last safe position |

**Implementation:**

1. **Store Checkpoint Position:**
   When hitting each checkpoint, store its position (or use preset values).

2. **Death Zone:**
   - Trigger Cubes below the course (fall detection)
   - User Enter Trigger:
     - Teleport to last checkpoint position
     - Optional: Add time penalty
     - Play respawn sound

3. **Manual Reset:**
   - Key Pressed trigger (R key):
     - Confirm with dialogue (optional)
     - Teleport to start
     - Reset timer
     - Reset all checkpoints

---

## Leaderboard Setup

### Basic Configuration

1. Place **Leaderboard** object in your space
2. Set Score Label (e.g., "time")
3. Configure display options

### Auto-Post on Timer

For countdown timers (counting down to zero):
- Timer automatically posts to leaderboard when it stops
- Ensure leaderboard Score Label matches

### Manual Post

For count-up timers or custom scoring:
- Add **Post Score to Leaderboard** effect at finish
- Value Label must match leaderboard

### Time Formatting

Leaderboard displays raw values. For time formatting:
- Store time in seconds (e.g., 65.5 for 1:05.5)
- Leaderboard sorts numerically (lower = better for racing)

---

## Complete Example: Parkour Time Trial

**Design:**
- Vertical parkour course
- 5 checkpoints
- Fall resets to last checkpoint
- Leaderboard for best times

**Layout:**
```
[Start] → [Platform 1] → [CP1] → [Platform 2] → [CP2] →
[Moving platforms] → [CP3] → [Wall jumps] → [CP4] →
[Final climb] → [CP5/Finish]
```

**Tasks:**
| Task | Purpose |
|------|---------|
| `raceReady` | At start |
| `raceActive` | Racing |
| `cp1` through `cp5` | Checkpoints |
| `raceComplete` | Finished |

**Variables:**
| Variable | Type | Purpose |
|----------|------|---------|
| `checkpointsHit` | Non-persistent | Progress |
| `currentCP` | Non-persistent | Which CP to respawn at |

**Flow:**

1. **Enter Start Zone:**
   - Lock movement
   - Display: "Press SPACE to begin!"
   - Set `raceReady` Active

2. **Press Space:**
   - Countdown: "3... 2... 1... GO!"
   - Unlock movement
   - Start timer
   - Set `raceActive` Active

3. **Hit Checkpoint 1:**
   - Set `cp1` Completed
   - Set `currentCP` = 1
   - Flash "Checkpoint!" notification
   - Show Outline on next checkpoint

4. **(Repeat for CP2-4)**

5. **Hit CP5 (Finish):**
   - Stop timer
   - Post Score to Leaderboard
   - Display final time
   - Notification: "Course Complete!"
   - Fireworks effect (optional)

6. **Fall Off:**
   - Teleport to checkpoint `currentCP`
   - Brief invincibility
   - Continue timer (no reset)

---

## Performance Tips

### Smooth Course Flow
- Test run your course many times
- Ensure platform spacing matches jump distance
- Add visual guides for tricky jumps

### Fair Competition
- Disable speed modifications during race
- Lock movement profile
- Consistent starting position

### Replay Value
- Multiple routes (different risk/reward)
- Daily/weekly leaderboard resets (optional)
- Cosmetic rewards for top times

---

## Troubleshooting

### Timer doesn't start
- Verify trigger condition (correct task state)
- Check Key Pressed trigger key binding
- Ensure countdown completes before timer starts

### Checkpoints don't register
- Verify trigger cube placement (tall enough for jumps)
- Check checkpoint order logic
- Ensure task names match exactly

### Leaderboard not posting
- Verify Score Label matches exactly
- Check timer is configured for leaderboard
- Ensure race completes properly (raceComplete Active)

### Falls don't reset properly
- Check fall zone trigger cube coverage
- Verify teleport coordinates
- Test respawn positions are safe landing spots

## Next Steps

- Add [collectible shortcuts](collectible-games.md) that shave time
- Create [puzzle doors](puzzle-games.md) as obstacles
- Build [NPC racers](quest-rpg-games.md) for story context
