---
icon: calculator
description: Track and display player scores with persistence options
---

# Create a Score Counter

This tutorial shows you how to create a score tracking system that displays on screen, persists across sessions, and posts to leaderboards.

**Difficulty:** Beginner
**Time:** 10-15 minutes

## What You'll Build

- A variable that tracks score
- On-screen display showing current score
- Score that persists when players leave and return
- Leaderboard integration for competition

## Prerequisites

- A Portals space in Build Mode
- Something to collect or interact with (for earning points)

---

## Part 1: Basic Score Variable

### Step 1: Initialize the Score

When players enter your space, initialize their score to zero.

1. Place a **Trigger Cube** at your spawn point
2. Add a **Player Login** trigger
3. Add **Update Value** effect:
   - Variable Name: `score`
   - Operation: `Set`
   - Value: `0`

This creates the `score` variable and sets it to 0 for new players.

### Step 2: Display the Score

1. On the same Player Login trigger, add a **Display Value** effect:
   - Variable: `score`
   - Label: `Score: ` (with trailing space)
   - Position: Top-right corner works well
     - Left: 1600 (for 1920px screen)
     - Top: 20
     - Width: 200
     - Height: 50

### Step 3: Test It

1. Exit Build Mode
2. You should see "Score: 0" in the corner

---

## Part 2: Incrementing the Score

### On Item Collection

1. Select a **Collectible GLB** object
2. Add **Item Collected** trigger
3. Add **Update Value** effect:
   - Variable Name: `score`
   - Operation: `Add`
   - Value: `1`

Each collected item adds 1 point.

### On Click Interaction

1. Select any clickable object
2. Add **Click** trigger
3. Add **Update Value** effect:
   - Variable Name: `score`
   - Operation: `Add`
   - Value: `10`

Clicking the object adds 10 points.

### On Zone Entry

1. Create a **Trigger Cube** in an area
2. Add **User Enter Trigger**
3. Add **Update Value** effect:
   - Variable Name: `score`
   - Operation: `Add`
   - Value: `50`

Entering the zone awards 50 points.

---

## Part 3: Score Feedback

Make scoring feel satisfying with audio and visual feedback.

### Add Sound Effect

On your scoring trigger, add:
- **Play Sound Once**: coin_collect.mp3

### Add Notification

On your scoring trigger, add:
- **Notification Pill**: "+10 points!"

### Dynamic Notification with Function Effect

Show the actual points earned:

```
SetVariable('score', $N{score} + 10.0, 0.0)
```

Note: Notification Pill doesn't support dynamic values directly. For dynamic displays, use an iframe HUD.

---

## Part 4: Persistent Score

By default, variables reset when players leave. To save progress:

### Enable Persistence

1. Go to **Space Options > Variable Manager**
2. Find `score` in the list
3. Enable **Persistent** toggle

Now the score saves across sessions.

### Reset Option

You may want to let players reset their score:

1. Create a "Reset" button or zone
2. Add Click or User Enter trigger
3. Add **Update Value** effect:
   - Variable: `score`
   - Operation: `Set`
   - Value: `0`

---

## Part 5: Multiplayer Score

### Individual Scores (Default)

By default, each player has their own `score` variable. This is ideal for:
- Personal high scores
- Individual progression
- Competitive play

### Shared Score

For cooperative games where everyone contributes to one score:

1. Go to **Space Options > Variable Manager**
2. Find `score`
3. Enable **Multiplayer** toggle

Now all players see and contribute to the same score.

---

## Part 6: Leaderboard Integration

### Place the Leaderboard

1. Enter Build Mode
2. Select **Leaderboard** from tools
3. Place it in your space
4. Configure:
   - Score Label: `score` (must match your variable name)
   - Display options as desired

### Post Score Automatically

When the game ends (all items collected, time runs out, etc.):

1. Add **Post Score to Leaderboard** effect
2. Set Value Label: `score`

The current score is posted to the leaderboard.

### Manual Score Posting

For a "Submit Score" button:

1. Create a clickable object or zone
2. Add Click or User Enter trigger
3. Add **Post Score to Leaderboard** effect
4. Value Label: `score`

---

## Part 7: Advanced - Multiple Score Types

Track different point types (coins, gems, stars):

### Initialize All Scores

On Player Login:
```
SetVariable('coins', 0.0, 0.0)
SetVariable('gems', 0.0, 0.0)
SetVariable('stars', 0.0, 0.0)
```

### Display All Scores

Add multiple **Display Value** effects with different positions:
- Coins: Top-left
- Gems: Top-center
- Stars: Top-right

### Calculate Total

Use Function Effect to compute total:

```
SetVariable('totalScore',
   $N{coins} + ($N{gems} * 5.0) + ($N{stars} * 10.0),
   0.0)
```

This weights gems at 5x and stars at 10x.

---

## Part 8: Score Thresholds

Trigger events when score reaches certain values.

### Using Value Updated Trigger

1. Create a task (e.g., `unlockBonus`)
2. Place a Trigger Cube
3. Add **Value Updated** trigger:
   - Variable: `score`
   - Condition: `>=`
   - Value: `100`
4. Add effects:
   - Set `unlockBonus` Active
   - Show hidden content
   - Play fanfare sound

### Using Function Effect

```
if(OnChange('score') && $N{score} >= 100.0 && $T{bonusUnlocked} == 'NotActive',
   SetTask('bonusUnlocked', 'Active', 0.0),
   0.0
)
```

The extra check prevents re-triggering after already unlocked.

---

## Complete Example: Coin Collector

**Scenario:** Collect coins scattered around, display score, unlock door at 50 coins.

### Objects

| Object | Type | Purpose |
|--------|------|---------|
| 10 coin collectibles | Collectible GLB | Points to collect |
| Score display zone | Trigger Cube | Initialize & display |
| Locked door | Custom GLB | Unlock at 50 points |
| Leaderboard | Leaderboard | High scores |

### Setup

**1. Player Login (spawn point trigger):**
- Update Value: `score` = 0
- Display Value: `score` with label "Coins: "

**2. Each Coin (Item Collected):**
- Update Value: `score` + 10
- Play Sound Once: coin_ding.mp3
- Notification Pill: "+10"

**3. Score Threshold (Value Updated on `score` >= 50):**
- Set `doorUnlocked` Active
- Hide `door_locked`
- Show `door_open`
- Notification Pill: "Door unlocked!"

**4. End Zone (User Enter when all coins collected):**
- Post Score to Leaderboard
- Notification Pill: "Score submitted!"

### Variable Settings

| Variable | Persistent | Multiplayer |
|----------|------------|-------------|
| `score` | Yes | No |

---

## Troubleshooting

### Score doesn't display
- Verify Display Value effect is on an Active task
- Check variable name matches exactly
- Ensure position values place it on screen

### Score doesn't increment
- Check Update Value uses "Add" not "Set"
- Verify variable name is consistent (case-sensitive)
- Confirm the trigger is firing (test with notification)

### Score resets on reload
- Enable Persistent in Variable Manager
- Verify you're not resetting on Player Login
- Check for other triggers that Set score to 0

### Leaderboard doesn't show score
- Verify Score Label matches exactly
- Ensure Post Score effect triggers
- Check leaderboard is configured for correct score type

### Threshold triggers multiple times
- Add a check that it hasn't already triggered
- Use a task state to track "already unlocked"

---

## Next Steps

- Create a [timed challenge](create-timed-challenge.md) with score bonuses
- Build a [collectible hunt](create-collectible-hunt.md) with this system
- Add combo multipliers for consecutive collections
- Create score-based unlockables and achievements
