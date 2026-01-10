---
icon: gem
description: Build a treasure hunt with collectibles, progress tracking, and rewards
---

# Create a Collectible Hunt

Build a complete treasure hunt game where players find hidden items, track their progress, and unlock rewards.

**Difficulty:** Beginner
**Time:** 20-25 minutes

## What You'll Build

- Multiple collectible items scattered in your space
- Score counter showing items found
- Progress toward completion
- Reward when all items are collected

---

## Part 1: Place Collectibles

### Step 1: Add Collectible Items

1. Enter **Build Mode**
2. Select **Collectible GLB** from tools
3. Paste your 3D model URL (coin, gem, star, etc.)
4. Place 10 collectibles around your space
5. Name them: `gem1`, `gem2`, `gem3`, etc.

### Step 2: Hide Them Well

Good hiding spots:
- Behind objects
- On high ledges
- In corners
- Inside buildings
- Partially obscured by foliage

---

## Part 2: Initialize Tracking

### On Player Entry

1. Place a **Trigger Cube** at spawn
2. Add **Player Login** trigger
3. Add effects:
   - **Update Value**: `gemsFound` = 0
   - **Update Value**: `totalGems` = 10
   - **Display Value**: Show `gemsFound` with label "Gems: "

---

## Part 3: Collection Logic

### For Each Collectible

Add to every gem's **Item Collected** trigger:

1. **Update Value**: `gemsFound` + 1
2. **Play Sound Once**: gem_collect.mp3
3. **Notification Pill**: "+1 Gem!"

### Check for Completion

Add **Value Updated** trigger watching `gemsFound`:
- Condition: `>= 10`
- Effects:
  - Set `huntComplete` Active
  - **Notification Pill**: "All gems found!"
  - Show hidden reward area

---

## Part 4: Reward

When `huntComplete` becomes Active:
- **Show Object**: Reveal treasure chest or door
- **Play Sound Once**: fanfare.mp3
- Optional: **Post Score to Leaderboard**

---

## Complete Example

### Variables
| Variable | Value |
|----------|-------|
| `gemsFound` | 0 (start) |
| `totalGems` | 10 |

### Tasks
| Task | Purpose |
|------|---------|
| `huntComplete` | Triggered when all collected |

### Setup Flow
1. Player Login → Initialize to 0, display counter
2. Each gem collected → Add 1, play sound
3. When gemsFound >= 10 → Complete, show reward

---

## Troubleshooting

- **Score not incrementing**: Check variable name matches exactly
- **Completion not triggering**: Verify >= condition and threshold value
- **Display not showing**: Ensure Display Value is on Active task
