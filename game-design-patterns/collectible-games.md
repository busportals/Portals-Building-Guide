---
icon: coins
description: Design treasure hunts, coin collection, and exploration rewards
---

# Collectible Games

Collectible games reward players for exploring your space and finding items. They're beginner-friendly to build and create satisfying gameplay loops.

## Core Loop

```
Explore → Find Item → Collect → Score Increases → Unlock Reward
```

## Game Variations

| Variation | Description | Example |
|-----------|-------------|---------|
| **Treasure Hunt** | Find all hidden items | "Find 10 gems scattered across the island" |
| **Timed Collection** | Collect before timer expires | "Grab as many coins as you can in 60 seconds" |
| **Competitive** | Highest score wins | "Most coins collected this week tops the leaderboard" |
| **Unlock Progression** | Items unlock new areas | "Collect 5 keys to open the vault" |

---

## Components Needed

### Basic Setup

| Component | Portals Tool/Feature | Purpose |
|-----------|---------------------|---------|
| Collectible items | Collectible GLB | Items players can pick up |
| Score tracking | Variable (`score`) | Counts collected items |
| Score display | Display Value effect | Shows current score |
| Collection trigger | Item Collected trigger | Detects when item is grabbed |
| Score update | Update Value effect | Increments the score |

### Optional Enhancements

| Component | Portals Tool/Feature | Purpose |
|-----------|---------------------|---------|
| Timer | Start Timer effect (auto-displays) | Time limit for collection |
| Leaderboard | Leaderboard tool + Post Score | Competitive ranking |
| Unlock gate | Tasks + Show/Hide effects | Progression gating |
| Sound feedback | Play Sound Once effect | Audio reward on collect |
| Visual feedback | Notification Pill effect | "Gem collected!" message |

---

## Step-by-Step Setup

### Step 1: Place Collectible Items

1. Open Build Mode
2. Select **Collectible GLB** from tools
3. Paste your 3D model URL (or use a default)
4. Place items throughout your space
5. **Name each collectible** clearly (e.g., `gem1`, `gem2`, etc.)

### Step 2: Create the Score Variable

1. Place a **Trigger Cube** at your spawn point
2. Add **Player Login** trigger
3. Add **Update Value** effect:
   - Variable Name: `score`
   - Operation: `Set`
   - Value: `0`

This initializes the score to 0 when players enter.

### Step 3: Track Collection

For each collectible, add a trigger:

1. Select the collectible object
2. Add **Item Collected** trigger
3. Add **Update Value** effect:
   - Variable Name: `score`
   - Operation: `Add`
   - Value: `1`
4. (Optional) Add **Play Sound Once** effect for feedback
5. (Optional) Add **Notification Pill** effect: "Gem collected!"

### Step 4: Display the Score

1. Create a task (e.g., `showScore`)
2. Add **Player Login** trigger → Set task Active
3. Add **Display Value** effect:
   - Variable: `score`
   - Position on screen (top-right works well)
   - Label: "Gems: "

---

## Advanced: Unlock on Collection Threshold

Unlock a door or area when the player collects enough items.

### Using Update Value Triggers

1. Create a task for the locked area (e.g., `vaultDoor`)
2. Add a **Trigger Cube** near the door
3. Add **Value Updated** trigger:
   - Variable: `score`
   - Condition: `>=`
   - Value: `10`
4. Add effects:
   - Set `vaultDoor` task to Active
   - **Show Object** effect on the open door
   - **Hide Object** effect on the closed door
   - **Notification Pill**: "Vault unlocked!"

### Using Function Effects

```
if(OnChange('score') && $N{score} >= 10.0,
   SetTask('vaultDoor', 'Active', 0.0),
   0.0
)
```

---

## Advanced: Timed Collection

Add a countdown timer for urgency.

### Setup

1. Create tasks: `gameReady`, `gameActive`, `gameOver`
2. On **Player Login** → Set `gameReady` Active, show "Press SPACE to start"
3. On **Key Pressed** (Space) when `gameReady` is Active:
   - Set `gameActive` Active
   - **Start Timer** (60 seconds) - automatically displays countdown on screen
4. On **Timer Stopped**:
   - Set `gameOver` Active
   - **Post Score to Leaderboard**
   - Show final score notification

---

## Advanced: Competitive Leaderboard

### Setup

1. Place a **Leaderboard** object in your space
2. Configure with a score label (e.g., "gems")
3. At game end (all collected OR timer expires):
   - Add **Post Score to Leaderboard** effect
   - Value Label: `gems` (must match leaderboard)

### Score Persistence

In **Space Options > Variable Manager**:
- Find `score` variable
- Enable **Persistent** if you want scores saved across sessions
- Enable **Multiplayer** if all players share the same collectibles

---

## Complete Example: Gem Hunt

**Design:**
- 10 gems hidden across a forest
- Score displayed top-right
- Door unlocks at 5 gems
- Secret room unlocks at 10 gems

**Tasks:**
| Task | Purpose |
|------|---------|
| `gameActive` | Game is running, show score |
| `door1` | First door (unlocks at 5) |
| `secretRoom` | Secret area (unlocks at 10) |

**Variables:**
| Variable | Type | Purpose |
|----------|------|---------|
| `score` | Non-persistent | Current gem count |

**Triggers & Effects:**

1. **Player Login:**
   - Set `score` = 0
   - Set `gameActive` Active
   - Display Value: show `score`

2. **Each Gem (Item Collected):**
   - Update Value: `score` + 1
   - Play Sound Once: collect.mp3
   - Notification Pill: "+1 Gem"

3. **Value Updated (score >= 5):**
   - Set `door1` Active
   - Show open door, hide closed door
   - Notification: "Door unlocked!"

4. **Value Updated (score >= 10):**
   - Set `secretRoom` Active
   - Show secret entrance
   - Notification: "Secret room revealed!"

---

## Troubleshooting

### Items don't increment score
- Verify Item Collected trigger is on the collectible, not a trigger cube
- Check variable name matches exactly (case-sensitive)
- Ensure Update Value uses "Add" not "Set"

### Score resets unexpectedly
- Check for duplicate Player Login triggers resetting score
- Verify variable is Persistent if needed
- Check for Reset All Tasks effects

### Unlock doesn't trigger
- Value Updated trigger needs exact variable name
- Condition must be `>=` not `=` for thresholds
- Verify the door task exists with correct name

## Next Steps

- Add a [timer component](race-games.md) for timed challenges
- Create a [quest wrapper](quest-rpg-games.md) with NPC that gives collection objectives
- Build [puzzle elements](puzzle-games.md) that require specific collectibles
