---
icon: scroll
description: Design story-driven experiences with NPC interactions and progression
---

# Quest/RPG Games

Quest games tell stories through NPC interactions, objectives, and rewards. They create memorable experiences by giving players purpose and progression.

## Core Loop

```
Meet NPC → Receive Quest → Complete Objective → Return → Get Reward → Next Quest
```

## Game Variations

| Variation | Description | Example |
|-----------|-------------|---------|
| **Linear Story** | Fixed quest order | "Help the village in order: baker, blacksmith, mayor" |
| **Branching Narrative** | Player choices matter | "Side with the rebels or the king" |
| **Hub & Spoke** | Central NPC, multiple quests | "Guild master offers 5 quests, complete any order" |
| **Open World** | Discover quests by exploring | "Find NPCs throughout the world who need help" |

---

## Core Concepts

### Quest States

Every quest follows a lifecycle:

| State | Player Experience | Task State |
|-------|------------------|------------|
| **Unavailable** | Quest not yet accessible | NotActive |
| **Available** | Can accept quest | Active (or shown via NPC) |
| **In Progress** | Working on objective | Active |
| **Complete** | Objective done, return to NPC | Active (pending turn-in) |
| **Turned In** | Reward received | Completed |

### Quest Chains (Dependencies)

Use **Dependent Tasks** to create quest sequences:

```
Quest 1 Completed → Quest 2 becomes Active → Quest 3...
```

Setup in Space Options > Tasks:
1. Select the dependent quest
2. Set "Depends On" to the prerequisite quest
3. The dependent quest auto-activates when prerequisite completes

### Quest Log Visibility

Make quests trackable by players:
1. Space Options > Tasks
2. Select the quest task
3. Enable **Visibility**
4. (Optional) Set **Quest Group** to organize related quests

---

## Components Needed

### Basic Setup

| Component | Portals Tool/Feature | Purpose |
|-----------|---------------------|---------|
| Quest givers | NPC | Characters who give/receive quests |
| Quest tracking | Tasks (with visibility) | Track quest progress |
| Objectives | Triggers (various) | Detect quest completion |
| Rewards | Variables, Wearables | What player earns |
| Dialogue | Dialogue Effector Display | NPC conversations |

### Optional Enhancements

| Component | Portals Tool/Feature | Purpose |
|-----------|---------------------|---------|
| Quest markers | Show Outline, Billboard | Highlight objectives |
| Reputation | Variables | Track faction standing |
| Inventory | Variables + Display Value | Track quest items |
| Cutscenes | Camera effects, Lock Movement | Dramatic moments |
| Companions | NPC Walk to Position | NPCs that follow |

---

## Pattern 1: Simple Fetch Quest

### Design
NPC asks player to find an item and return.

**"The Baker's Lost Recipe"**
> Baker: "I've lost my grandmother's recipe scroll! It blew away toward the forest. Please find it!"
> Player finds scroll → Returns to baker
> Baker: "Thank you! Here's a fresh pie as thanks."

### Setup

**Tasks:**
| Task | State | Visibility | Purpose |
|------|-------|------------|---------|
| `bakersQuest` | NotActive → Active → Completed | On | Quest tracking |

**Variables:**
| Variable | Purpose |
|----------|---------|
| `hasRecipe` | 1 when scroll collected |

**Implementation:**

1. **NPC Click (Baker) - Quest Available:**
   - Condition: `bakersQuest` is NotActive
   - Effects:
     - Dialogue: "I've lost my grandmother's recipe..."
     - Set `bakersQuest` Active
     - Show Outline on scroll location (optional)

2. **Scroll Collection:**
   - Item Collected trigger on scroll Collectible GLB
   - Effects:
     - Set `hasRecipe` = 1
     - Notification: "Recipe scroll acquired!"
     - Hide Outline on scroll location

3. **NPC Click (Baker) - Turn In:**
   - Condition: `bakersQuest` is Active AND `hasRecipe` == 1
   - Effects:
     - Dialogue: "Thank you! Here's a fresh pie!"
     - Set `bakersQuest` Completed
     - Set `hasRecipe` = 0 (consume item)
     - Grant reward (equip wearable, add currency, etc.)

4. **NPC Click (Baker) - Completed:**
   - Condition: `bakersQuest` is Completed
   - Effects:
     - Dialogue: "Thanks again for finding my recipe!"

---

## Pattern 2: Multi-Objective Quest

### Design
Quest with multiple objectives that can be completed in any order.

**"The Missing Shipment"**
> Merchant: "My shipment was attacked! Recover the 3 crates scattered in the wilderness."

### Setup

**Tasks:**
| Task | Depends On | Purpose |
|------|------------|---------|
| `shipmentQuest` | - | Main quest |
| `crate1` | - | Sub-objective 1 |
| `crate2` | - | Sub-objective 2 |
| `crate3` | - | Sub-objective 3 |

**Variables:**
| Variable | Purpose |
|----------|---------|
| `cratesFound` | Counter (0-3) |

**Implementation:**

1. **Accept Quest:**
   - NPC Click → Set `shipmentQuest`, `crate1`, `crate2`, `crate3` all Active

2. **Each Crate Collection:**
   ```
   if(OnChange('crate1', 'Completed'),
      SetVariable('cratesFound', $N{cratesFound} + 1.0, 0.0),
      0.0
   )
   ```

3. **Check All Found:**
   ```
   if($N{cratesFound} >= 3.0,
      SetTask('shipmentQuest', 'Completed', 0.0),
      0.0
   )
   ```

4. **Quest Log Display:**
   - All sub-objectives visible in quest log
   - Player sees: "Crate 1 ✓, Crate 2 ✓, Crate 3 ○"

---

## Pattern 3: Quest Chain

### Design
Linear sequence of quests that unlock in order.

**"The Blacksmith's Apprentice"**
1. Quest 1: Gather ore
2. Quest 2: Deliver to furnace
3. Quest 3: Retrieve the forged sword

### Setup

**Tasks:**
| Task | Depends On | Quest Group |
|------|------------|-------------|
| `smithQuest1` | - | Blacksmith |
| `smithQuest2` | smithQuest1 | Blacksmith |
| `smithQuest3` | smithQuest2 | Blacksmith |

With dependencies:
- `smithQuest1` starts Active (or activated by NPC)
- `smithQuest2` auto-activates when `smithQuest1` Completes
- `smithQuest3` auto-activates when `smithQuest2` Completes

**Implementation:**

Each quest follows the simple fetch pattern, but:
- Quest 1 turn-in → `smithQuest1` Completed → `smithQuest2` auto-activates
- NPC dialogue changes based on which quest is active

---

## Pattern 4: Branching Choices

### Design
Player choices affect story outcome.

**"The Disputed Land"**
> Two NPCs claim the same land. Player must choose who to help.
> - Help Farmer → Get farming tools, Merchant hostile
> - Help Merchant → Get gold, Farmer hostile

### Setup

**Tasks:**
| Task | Purpose |
|------|---------|
| `landDispute` | Main quest |
| `helpedFarmer` | Branch A outcome |
| `helpedMerchant` | Branch B outcome |

**Variables:**
| Variable | Purpose |
|----------|---------|
| `farmerRep` | Farmer reputation |
| `merchantRep` | Merchant reputation |

**Implementation:**

1. **Accept Quest:**
   - Either NPC click → Set `landDispute` Active
   - Both NPCs now have dialogue offering their side

2. **Make Choice (Farmer):**
   - NPC Click with choice:
     - Set `helpedFarmer` Active
     - Set `farmerRep` = 100
     - Set `merchantRep` = -50
     - Complete the quest for Farmer

3. **Make Choice (Merchant):**
   - NPC Click with choice:
     - Set `helpedMerchant` Active
     - Set `merchantRep` = 100
     - Set `farmerRep` = -50
     - Complete the quest for Merchant

4. **Consequence:**
   - Future NPC dialogue checks reputation
   - Low rep: "I have nothing to say to you!"
   - High rep: Unlock additional quests

---

## NPC Dialogue States

NPCs should say different things based on quest state.

### Using Multiple Click Triggers

Add multiple Click triggers to the NPC, each with conditions:

| Condition | Dialogue |
|-----------|----------|
| Quest NotActive | "Hello traveler!" (offer quest) |
| Quest Active, objective incomplete | "Have you found the scroll yet?" |
| Quest Active, objective complete | "You found it! Thank you!" (turn in) |
| Quest Completed | "Thanks again, friend!" |

### Using Function Effects

```
if($T{bakersQuest} == 'NotActive',
   SetTask('dialogueOffer', 'Active', 0.0),
   if($T{bakersQuest} == 'Active',
      if($N{hasRecipe} == 1.0,
         SetTask('dialogueTurnIn', 'Active', 0.0),
         SetTask('dialogueReminder', 'Active', 0.0)
      ),
      SetTask('dialogueComplete', 'Active', 0.0)
   )
)
```

---

## Rewards

### Currency
```
SetVariable('gold', $N{gold} + 100.0, 0.0)
```

### Items/Wearables
Use **Equip Wearable** effect with the item's contract address.

### Reputation
```
SetVariable('villageRep', $N{villageRep} + 25.0, 0.0)
```

### Unlocking Content
Set a task to Completed that:
- Shows a new area (Show Object)
- Unlocks a door
- Makes a new NPC appear

---

## Complete Example: Village Quest Line

**Story:** New player arrives in village, helps residents, becomes hero.

**Quest Chain:**

| # | Quest | Giver | Objective | Reward |
|---|-------|-------|-----------|--------|
| 1 | Welcome | Elder | Talk to 3 villagers | 50 gold |
| 2 | Baker's Recipe | Baker | Find scroll | Pie wearable |
| 3 | Missing Sheep | Farmer | Find 3 sheep | 100 gold |
| 4 | The Bandit | Guard | Defeat bandit | Sword |
| 5 | Hero's Welcome | Elder | Return to village | Title + Area unlock |

**Tasks:**
```
elderQuest1 (no dependency)
  └→ bakersQuest (depends on elderQuest1)
      └→ farmerQuest (depends on bakersQuest)
          └→ guardQuest (depends on farmerQuest)
              └→ elderQuest2 (depends on guardQuest)
```

**Implementation Tips:**
- All quests in same Quest Group: "Village Story"
- Enable visibility on all for quest log
- Each NPC has dialogue for all states
- Rewards granted on turn-in
- Final quest unlocks "Hero's Hall" area

---

## Quest Design Tips

### 1. Clear Objectives
Players should always know what to do next.
- Use quest log visibility
- Add markers (Show Outline)
- NPC reminders when clicked

### 2. Meaningful Rewards
Rewards should feel earned.
- Currency that can be spent
- Wearables that show achievement
- Access to new areas
- New NPC interactions

### 3. Logical Flow
Quest objectives should make narrative sense.
- "Find 5 mushrooms" → why does NPC need them?
- "Defeat the wolf" → what's the threat?

### 4. Avoid Backtracking
Minimize tedious running back and forth.
- Place turn-in NPCs near objectives when possible
- Or use teleportation rewards

---

## Troubleshooting

### Quest doesn't appear in log
- Check Visibility is enabled in Task settings
- Verify task is Active (NotActive quests don't show)

### Dependent quest won't activate
- Parent quest must be **Completed**, not just Active
- Check exact task name in "Depends On" field

### NPC says wrong dialogue
- Verify condition checks are correct
- Check task state matches expected value
- Ensure only one dialogue task is Active at a time

### Reward not granted
- Verify turn-in effect triggers on correct condition
- Check wearable contract address is correct
- Verify variable update uses decimal notation

## Next Steps

- Add [collectible objectives](collectible-games.md) within quests
- Create [puzzle elements](puzzle-games.md) as quest objectives
- Add [timed challenges](race-games.md) for urgency
