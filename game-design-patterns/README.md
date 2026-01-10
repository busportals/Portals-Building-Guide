---
icon: gamepad-2
description: Learn game design thinking for Portals
---

# Game Design Patterns

This section helps you think through game design before you start building. Good planning saves time and creates better player experiences.

## Why Design First?

Many builders jump straight into placing triggers and effects. This often leads to:
- Confusing player experiences
- Spaghetti logic that's hard to debug
- Missing edge cases (what if the player does X?)
- Rebuilding from scratch when things don't work

Taking 10-15 minutes to design your game on paper first prevents hours of frustration later.

## The Core Loop

Every game has a **core loop** - the primary action players repeat:

```
Player Action → Feedback → Reward → Repeat
```

**Examples:**
- Collectible game: Find item → Score increases → Unlock area → Find more items
- Quest game: Talk to NPC → Get objective → Complete task → Get reward → Next quest
- Racing: Start race → Navigate course → Beat time → Post score → Race again

Before building, write out your core loop in one sentence.

## Game Design Patterns

Choose a pattern that matches your vision:

| Pattern | Best For | Complexity |
|---------|----------|------------|
| [Collectible Games](collectible-games.md) | Treasure hunts, coin collection, exploration rewards | Beginner |
| [Puzzle Games](puzzle-games.md) | Escape rooms, logic challenges, hidden object games | Intermediate |
| [Quest/RPG Games](quest-rpg-games.md) | Story-driven experiences, NPC interactions, progression | Intermediate |
| [Racing Games](race-games.md) | Time trials, obstacle courses, competitive leaderboards | Beginner |

## Design Document Template

Before building, answer these questions:

### 1. Player Goal
What is the player trying to achieve?
> Example: "Collect all 10 gems to unlock the secret room"

### 2. Core Mechanics
What actions can the player take?
> Example: "Walk, jump, collect items, open doors"

### 3. Progression
How does difficulty or content increase?
> Example: "Each area has more gems but harder platforming"

### 4. Feedback
How does the player know they're making progress?
> Example: "Gem counter on screen, sound effect on collection, door glows when unlocked"

### 5. Win/Lose Conditions
How does the game end?
> Example: "Win: Collect all gems. Lose: None (exploration focused)"

### 6. Edge Cases
What happens if the player...
- Leaves and comes back? (Persistence)
- Does things out of order? (Sequence breaking)
- Gets stuck? (Hints, resets)

## Component Mapping

Once you have your design, map it to Portals components:

| Design Element | Portals Component |
|----------------|-------------------|
| Player action | Trigger (Click, Collision, Key Press) |
| Game state | Task (NotActive, Active, Completed) |
| Score/counter | Variable + Update Value effect |
| Show progress | Display Value effect |
| Unlock content | Show/Hide Object effects |
| Story/dialogue | NPC + Dialogue effects |
| Competition | Leaderboard + Post Score effect |
| Complex logic | Function Effect |

## Quick Start

1. **Pick a pattern** from the list above
2. **Read through the pattern doc** to understand the components
3. **Sketch your specific game** using the template
4. **Map to Portals components** using the table above
5. **Build incrementally** - test each piece before adding the next
