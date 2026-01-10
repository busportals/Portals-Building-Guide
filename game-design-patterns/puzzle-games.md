---
icon: puzzle
description: Design escape rooms, logic challenges, and hidden object games
---

# Puzzle Games

Puzzle games challenge players to solve problems using logic, observation, and experimentation. They're satisfying to complete and encourage exploration.

## Core Loop

```
Discover Puzzle → Experiment → Solve → Unlock Progress → Next Puzzle
```

## Game Variations

| Variation | Description | Example |
|-----------|-------------|---------|
| **Escape Room** | Solve puzzles to escape | "Find clues and unlock the exit door" |
| **Hidden Object** | Find concealed items | "Locate 5 hidden switches in the room" |
| **Sequence Puzzle** | Activate in correct order | "Press buttons in the right sequence" |
| **Lock & Key** | Find items to unlock paths | "Find the red key to open the red door" |
| **Environmental** | Manipulate the world | "Redirect light beams to activate the portal" |

---

## Core Concepts

### State-Based Puzzles

Most puzzles track states:
- **Unsolved** (NotActive) - Player hasn't started
- **In Progress** (Active) - Player is working on it
- **Solved** (Completed) - Puzzle completed

Use Tasks to track each puzzle state.

### Lock & Key Pattern

The fundamental puzzle mechanic:

```
Player has key? → YES → Door opens
                → NO  → Door stays locked
```

In Portals:
- **Key** = Variable set to 1 when collected
- **Lock check** = Condition in Function Effect or Value Updated trigger
- **Door open** = Show/Hide effects or task state change

### Sequential Dependencies

Puzzles that must be solved in order:

```
Puzzle 1 Completed → Puzzle 2 becomes available → Puzzle 3...
```

Use **Dependent Tasks** to enforce order.

---

## Components Needed

### Basic Setup

| Component | Portals Tool/Feature | Purpose |
|-----------|---------------------|---------|
| Puzzle objects | Custom GLB, Trigger Cube | Interactive elements |
| Puzzle state | Tasks | Track solved/unsolved |
| Player inventory | Variables | Track collected keys/items |
| Locked doors | Show/Hide effects | Gate progression |
| Clues/hints | NPCs, World Text | Guide the player |

### Optional Enhancements

| Component | Portals Tool/Feature | Purpose |
|-----------|---------------------|---------|
| Sound feedback | Play Sound Once | Correct/incorrect audio |
| Visual hints | Show Outline, Change Bloom | Highlight interactables |
| Reset mechanism | Reset tasks/variables | Let players retry |
| Hint system | NPC dialogue | Progressive hints |
| Timer | Timer trigger | Timed escape rooms |

---

## Pattern 1: Lock & Key

### Design
Player finds a key item, then uses it to unlock a door.

### Setup

**Variables:**
| Variable | Purpose |
|----------|---------|
| `hasRedKey` | 1 if player has red key, 0 if not |

**Tasks:**
| Task | Purpose |
|------|---------|
| `redDoorClosed` | Door is locked (Active when locked) |
| `redDoorOpen` | Door is unlocked |

**Implementation:**

1. **Key Collection:**
   - Collectible GLB for the key
   - Item Collected trigger:
     - Update Value: `hasRedKey` = 1
     - Notification: "Red key acquired!"
     - Play Sound: key_pickup.mp3

2. **Door Interaction:**
   - Click trigger on the door
   - Function Effect:
   ```
   if($N{hasRedKey} == 1.0,
      SetTask('redDoorClosed', 'NotActive', 0.0) +
      SetTask('redDoorOpen', 'Active', 0.0) +
      SetVariable('hasRedKey', 0.0, 0.0),
      0.0
   )
   ```

   Or use a Value Updated trigger on the door click task that checks `hasRedKey`.

3. **Door Visuals:**
   - `redDoorClosed` Active → Show closed door model
   - `redDoorOpen` Active → Show open door model, Hide closed door

---

## Pattern 2: Sequence Puzzle

### Design
Player must activate objects in the correct order (e.g., press buttons 1-2-3).

### Setup

**Variables:**
| Variable | Purpose |
|----------|---------|
| `sequenceStep` | Current position in sequence (0-3) |
| `puzzleSolved` | 1 when complete |

**Correct sequence:** Button A → Button B → Button C

**Implementation:**

1. **Initialize on room entry:**
   ```
   SetVariable('sequenceStep', 0.0, 0.0)
   SetVariable('puzzleSolved', 0.0, 0.0)
   ```

2. **Button A Click:**
   ```
   if($N{puzzleSolved} == 0.0,
      if($N{sequenceStep} == 0.0,
         SetVariable('sequenceStep', 1.0, 0.0),
         SetVariable('sequenceStep', 0.0, 0.0)
      ),
      0.0
   )
   ```
   - If at step 0, advance to step 1
   - Otherwise, reset (wrong order)

3. **Button B Click:**
   ```
   if($N{puzzleSolved} == 0.0,
      if($N{sequenceStep} == 1.0,
         SetVariable('sequenceStep', 2.0, 0.0),
         SetVariable('sequenceStep', 0.0, 0.0)
      ),
      0.0
   )
   ```

4. **Button C Click:**
   ```
   if($N{puzzleSolved} == 0.0,
      if($N{sequenceStep} == 2.0,
         SetVariable('puzzleSolved', 1.0, 0.0) +
         SetTask('vaultOpen', 'Active', 0.0),
         SetVariable('sequenceStep', 0.0, 0.0)
      ),
      0.0
   )
   ```

5. **Feedback:**
   - Correct button: Green flash, positive sound
   - Wrong button: Red flash, error sound, reset

---

## Pattern 3: Hidden Object

### Design
Player must find and interact with hidden switches/objects.

### Setup

**Variables:**
| Variable | Purpose |
|----------|---------|
| `switchesFound` | Counter for found switches |

**Tasks:**
| Task | Purpose |
|------|---------|
| `switch1`, `switch2`, etc. | Track each switch (Completed when found) |
| `allSwitchesFound` | Triggers when all are found |

**Implementation:**

1. **Each Hidden Switch:**
   - Place subtle Trigger Cube or clickable object
   - Click trigger:
     - Only if this switch's task is NotActive:
       - Set switch task to Completed
       - Update Value: `switchesFound` + 1
       - Show visual confirmation (outline, glow)
       - Play discovery sound

2. **Completion Check:**
   - Value Updated trigger on `switchesFound`:
     - Condition: `>= 5` (or however many switches)
     - Set `allSwitchesFound` Active
     - Trigger reward/door opening

3. **Function Effect Version:**
   ```
   if(OnChange('switch1', 'Completed'),
      SetVariable('switchesFound', $N{switchesFound} + 1.0, 0.0) +
      if($N{switchesFound} >= 5.0,
         SetTask('secretDoor', 'Active', 0.0),
         0.0
      ),
      0.0
   )
   ```

---

## Pattern 4: Environmental Puzzle

### Design
Player manipulates objects to solve (e.g., move blocks, rotate mirrors).

### Setup

This pattern uses **Move Item** and **task states** to track object positions.

**Example: Pressure Plate Puzzle**
- Two pressure plates
- Both must have blocks on them simultaneously
- Door opens when both are pressed

**Variables:**
| Variable | Purpose |
|----------|---------|
| `plate1Active` | 1 if plate 1 is pressed |
| `plate2Active` | 1 if plate 2 is pressed |

**Implementation:**

1. **Plate 1 Entry:**
   - User Enter Trigger:
     - Set `plate1Active` = 1
     - Visual: plate sinks, light turns green

2. **Plate 1 Exit:**
   - User Exit Trigger:
     - Set `plate1Active` = 0
     - Visual: plate rises, light turns red

3. **Check Both Plates:**
   ```
   if($N{plate1Active} == 1.0 && $N{plate2Active} == 1.0,
      SetTask('puzzleDoor', 'Active', 0.0),
      SetTask('puzzleDoor', 'NotActive', 0.0)
   )
   ```

**Multiplayer consideration:** If both plates need to be pressed simultaneously, use **Multiplayer variables** so player positions are shared.

---

## Complete Example: Mini Escape Room

**Design:**
- Room with locked exit
- 3 puzzles that each give a code digit
- Enter code on keypad to escape

**Puzzles:**
1. Hidden object: Find the note with first digit
2. Sequence: Press paintings in order for second digit
3. Lock & key: Find key, open box for third digit

**Tasks:**
| Task | Purpose |
|------|---------|
| `puzzle1` | Note found |
| `puzzle2` | Painting sequence solved |
| `puzzle3` | Box opened |
| `escaped` | Player won |

**Variables:**
| Variable | Purpose |
|----------|---------|
| `digit1`, `digit2`, `digit3` | Revealed digits |
| `codeEntered` | Player's keypad input |

**Flow:**
1. Player enters room → All puzzles NotActive
2. Solve puzzle 1 → Show digit 1 (e.g., "3")
3. Solve puzzle 2 → Show digit 2 (e.g., "7")
4. Solve puzzle 3 → Show digit 3 (e.g., "1")
5. Enter "371" on keypad → Door opens, `escaped` Active

---

## Hint Systems

Help stuck players without giving away solutions.

### Progressive Hints

1. Create an NPC "hint giver"
2. Track `hintLevel` variable (0, 1, 2, 3)
3. Each NPC click increments `hintLevel` and shows next hint:
   - Level 0: "Look around carefully..."
   - Level 1: "Have you checked behind the bookshelf?"
   - Level 2: "The switch is hidden on the left side"
   - Level 3: "Click the red book on the third shelf"

### Timed Hints

Show hints automatically after time passes:
```
SetVariable('showHint1', 1.0, 120.0)  // Show hint after 2 minutes
```

---

## Troubleshooting

### Puzzle state not saving
- Enable **Persistent** in Variable Manager for key variables
- Check if Reset All Tasks is firing unexpectedly

### Sequence keeps resetting
- Verify the reset only happens on wrong input, not every click
- Check for race conditions with multiple triggers

### Door won't open even with key
- Verify variable name matches exactly (case-sensitive)
- Check condition uses `== 1.0` not `== 1`
- Ensure the key sets the variable before door check runs

### Multiplayer puzzle desync
- Use **Multiplayer** variables for shared state
- Use **Multiplayer** tasks for shared progress
- Test with multiple players

## Next Steps

- Combine with [collectibles](collectible-games.md) for hybrid treasure-puzzle games
- Add [NPC quest givers](quest-rpg-games.md) for story context
- Add [time pressure](race-games.md) for escape room tension
