---
icon: message-circle
description: Build NPCs that give quests, track progress, and reward players
---

# Create an NPC Quest Giver

This tutorial shows you how to create an NPC that gives quests to players, tracks their progress, and provides rewards upon completion.

**Difficulty:** Intermediate
**Time:** 25-30 minutes

## What You'll Build

- An NPC that offers a quest when clicked
- Quest tracking visible in the quest log
- Objective completion detection
- NPC dialogue that changes based on quest state
- Reward delivery on quest turn-in

## Prerequisites

- A Portals space in Build Mode
- A rigged GLB avatar for the NPC (or use a preset)
- An objective for players to complete (collectible, location, etc.)

---

## Part 1: Place the NPC

### Step 1: Add NPC Tool

1. Enter **Build Mode**
2. Select **NPC** from the building tools
3. Click to place the NPC in your space

### Step 2: Configure NPC Appearance

1. Select the placed NPC
2. In settings, either:
   - Paste a rigged GLB avatar URL, or
   - Choose from preset avatars
3. Set the NPC name (e.g., "Elder Marcus")
4. Choose a default animation (Idle recommended)

### Step 3: Position the NPC

- Face the NPC toward where players will approach
- Ensure there's space for players to stand in front
- Consider adding a visual marker (glow, sign) to draw attention

---

## Part 2: Create the Quest Task

### Step 1: Create the Task

1. With the NPC selected, open the **Tasks** panel
2. Create a new task named `elderQuest`
3. This task will track the quest state

### Step 2: Configure Quest Visibility

1. Go to **Space Options > Tasks**
2. Find `elderQuest`
3. Enable **Visibility** (makes it appear in quest log)
4. Set a **Quest Group** if you have multiple quests (e.g., "Village")
5. Add a description: "Help Elder Marcus find his lost amulet"

---

## Part 3: Quest Offer Dialogue

When players click the NPC before accepting the quest.

### Step 1: Add Click Trigger

1. Select the NPC
2. Add a **Click** trigger
3. This trigger will show the quest offer

### Step 2: Add Condition

The dialogue should only show if the quest hasn't been accepted:

**Option A: Simple approach**
- Set this trigger to only work when `elderQuest` is NotActive

**Option B: Using Function Effect**
```
if($T{elderQuest} == 'NotActive',
   SetTask('showQuestOffer', 'Active', 0.0),
   0.0
)
```

### Step 3: Add Dialogue Effect

Add **Dialogue Effector Display** effect:
- Text: "Traveler! I've lost my precious amulet in the forest. Will you help me find it?"
- Add accept/decline options if using dialogue trees

### Step 4: Accept Quest

When player accepts:
- **Set Task State**: `elderQuest` → Active
- **Notification Pill**: "Quest accepted: Find the Lost Amulet"
- **Play Sound Once**: quest_accept.mp3

---

## Part 4: Create the Objective

### Example: Find a Collectible

1. Place a **Collectible GLB** (the amulet) in the forest
2. Name it `lostAmulet`
3. Add **Item Collected** trigger
4. Add effects:
   - **Update Value**: `hasAmulet` = 1
   - **Notification Pill**: "Amulet found! Return to Elder Marcus."

### Example: Reach a Location

1. Place a **Trigger Cube** at the destination
2. Add **User Enter Trigger**
3. Condition: `elderQuest` is Active
4. Add effects:
   - **Update Value**: `reachedLocation` = 1
   - **Notification Pill**: "Location discovered!"

### Example: Defeat Enemies

1. Use Combat NPCs as enemies
2. On last enemy's **Player Died** trigger (when enemy dies):
   - **Update Value**: `enemiesDefeated` + 1
3. When count reaches target:
   - **Notification Pill**: "All enemies defeated!"

---

## Part 5: Quest Turn-In

### Step 1: Add Turn-In Trigger

1. Select the NPC
2. Add another **Click** trigger
3. This one activates when quest is ready to turn in

### Step 2: Check Conditions

The player should have the quest active AND completed the objective:

**Using Function Effect:**
```
if($T{elderQuest} == 'Active' && $N{hasAmulet} == 1.0,
   SetTask('showQuestComplete', 'Active', 0.0),
   0.0
)
```

### Step 3: Complete Quest Dialogue

Add **Dialogue Effector Display**:
- Text: "You found my amulet! Thank you, brave traveler. Please accept this reward."

### Step 4: Grant Reward & Complete

Add effects:
- **Set Task State**: `elderQuest` → Completed
- **Update Value**: `gold` + 100 (or your currency)
- **Equip Wearable**: Reward item (if applicable)
- **Notification Pill**: "Quest complete! +100 gold"
- **Play Sound Once**: quest_complete.mp3
- **Update Value**: `hasAmulet` = 0 (consume the item)

---

## Part 6: State-Based Dialogue

The NPC should say different things based on quest state.

### Dialogue States

| Quest State | Objective | NPC Says |
|-------------|-----------|----------|
| NotActive | - | Quest offer |
| Active | Incomplete | Reminder |
| Active | Complete | Turn-in ready |
| Completed | - | Thank you |

### Implementation with Multiple Triggers

Add multiple Click triggers to the NPC, each with conditions:

**Trigger 1: Quest Offer**
- Condition: `elderQuest` is NotActive
- Dialogue: "Will you help me find my amulet?"

**Trigger 2: Reminder**
- Condition: `elderQuest` is Active AND `hasAmulet` == 0
- Dialogue: "Please hurry! The amulet is somewhere in the forest."

**Trigger 3: Turn-In**
- Condition: `elderQuest` is Active AND `hasAmulet` == 1
- Dialogue: "You found it!" + rewards

**Trigger 4: Completed**
- Condition: `elderQuest` is Completed
- Dialogue: "Thank you again, friend!"

### Implementation with Function Effect

Single Click trigger with branching logic:

```
if($T{elderQuest} == 'NotActive',
   SetTask('dialogueOffer', 'Active', 0.0),
   if($T{elderQuest} == 'Active',
      if($N{hasAmulet} == 1.0,
         SetTask('dialogueTurnIn', 'Active', 0.0),
         SetTask('dialogueReminder', 'Active', 0.0)
      ),
      SetTask('dialogueComplete', 'Active', 0.0)
   )
)
```

Each dialogue task shows the appropriate message.

---

## Part 7: NPC Animations

Make the NPC feel alive with animations.

### Turn to Face Player

Add **Turn To Player** effect when NPC is clicked:
- The NPC rotates to face the player during conversation

### Change Animation for Dialogue

Add **Change Animation** effect:
- When talking: "Talking" or "Gesture" animation
- Return to "Idle" after dialogue ends

### Celebrate on Quest Complete

Add **Play Emote** or **Change Animation**:
- "Celebrate" or "Happy" animation when quest is turned in

---

## Complete Example: Elder Marcus Quest

**Story:** Elder Marcus lost his amulet in the forest. Find it and return it for a reward.

### Objects

| Object | Type | Name |
|--------|------|------|
| Quest giver | NPC | `elderMarcus` |
| Lost item | Collectible GLB | `lostAmulet` |

### Tasks

| Task | Visibility | Group | Description |
|------|------------|-------|-------------|
| `elderQuest` | On | Village | "Find Elder Marcus's lost amulet" |
| `dialogueOffer` | Off | - | Shows quest offer |
| `dialogueReminder` | Off | - | Shows reminder |
| `dialogueTurnIn` | Off | - | Shows turn-in |
| `dialogueComplete` | Off | - | Shows thanks |

### Variables

| Variable | Purpose |
|----------|---------|
| `hasAmulet` | 1 when amulet collected |
| `gold` | Player's currency |

### Full Setup

**1. NPC Click (Elder Marcus):**

Function Effect:
```
if($T{elderQuest} == 'NotActive',
   SetTask('dialogueOffer', 'Active', 0.0),
   if($T{elderQuest} == 'Active',
      if($N{hasAmulet} == 1.0,
         SetTask('dialogueTurnIn', 'Active', 0.0),
         SetTask('dialogueReminder', 'Active', 0.0)
      ),
      SetTask('dialogueComplete', 'Active', 0.0)
   )
)
```

Additional effects:
- Turn To Player

**2. dialogueOffer task:**
- Dialogue: "Traveler! I've lost my precious amulet..."
- On accept: Set `elderQuest` Active
- Notification: "Quest accepted!"

**3. dialogueReminder task:**
- Dialogue: "Please, the amulet is in the forest to the east..."
- Set dialogueReminder NotActive (auto-close)

**4. Amulet Collection (Item Collected):**
- Update Value: `hasAmulet` = 1
- Notification: "Amulet found!"
- Play Sound: item_pickup.mp3

**5. dialogueTurnIn task:**
- Dialogue: "You found it! Here's your reward."
- Set `elderQuest` Completed
- Update Value: `gold` + 100
- Update Value: `hasAmulet` = 0
- Notification: "Quest complete! +100 gold"
- Play Sound: quest_complete.mp3
- Change Animation: "Celebrate"

**6. dialogueComplete task:**
- Dialogue: "Thank you again, brave traveler!"
- Set dialogueComplete NotActive

---

## Part 8: Quest Chains

Make quests that unlock after completing others.

### Using Dependent Tasks

1. Create second quest task: `elderQuest2`
2. In Space Options > Tasks, set:
   - Depends On: `elderQuest`
3. When `elderQuest` completes, `elderQuest2` automatically becomes Active

### Dialogue for New Quest

Add to the NPC's click logic:
```
if($T{elderQuest} == 'Completed' && $T{elderQuest2} == 'Active',
   SetTask('dialogueQuest2', 'Active', 0.0),
   ...
)
```

---

## Troubleshooting

### NPC doesn't respond to clicks
- Ensure NPC tool is used (not just a Custom GLB)
- Verify Click trigger is attached
- Check that conditions are met

### Wrong dialogue shows
- Review condition logic carefully
- Ensure only one dialogue task is Active at a time
- Check task states in Debug Panel

### Quest doesn't appear in log
- Enable Visibility in Space Options > Tasks
- Quest task must be Active (NotActive quests are hidden)

### Reward not granted
- Verify Update Value uses decimal notation
- Check variable names match
- Ensure turn-in trigger fires (add notification to test)

### NPC animations not working
- NPC must use a rigged GLB avatar
- Animation names must match exactly
- Some animations only work with specific avatar types

---

## Next Steps

- Create a [quest chain](../game-design-patterns/quest-rpg-games.md) with multiple NPCs
- Add [collectible objectives](create-collectible-hunt.md) to quests
- Build branching dialogue with player choices
- Create reputation systems that affect NPC reactions
