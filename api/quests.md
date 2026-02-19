# Quests

Quests are the state management system in Portals. They drive persistent animations, game logic, and interactive experiences by providing a 3-state machine that items can subscribe to.

**Key concepts:**

- **3-state system** -- Not Active (0), Active (1), Completed (2)
- **Persistent** -- state survives page reloads (unless configured otherwise)
- **Effect orchestration** -- items react to quest state changes via subscriptions
- **Per-player or shared** -- single-player, non-persistent, or multiplayer modes

Quests live in the `quests` top-level key of the [room data format](room-data-format.md). Items subscribe to quest state changes via `TaskEffectorSubscription` entries in their [logic](room-data-format.md#logic) data. Triggers advance quest states via `TaskTriggerSubscription` entries.

---

## Quest States

Every quest has three states:

| State | Numeric Value | Description |
|-------|---------------|-------------|
| **Not Active** | 0 | Default state. Quest has not started. |
| **Active** | 1 | Quest is in progress. |
| **Completed** | 2 | Quest is finished. |

State transitions trigger effects on all items subscribed to the quest. A quest always starts in Not Active (0) and must be explicitly transitioned to Active or Completed via a trigger.

---

## Quest Pair Structure

Quests are stored in the `quests` top-level key as a **flat dictionary** keyed by quest ID.

Each logical quest requires **two entries**: one with `"Status": "inProgress"` and one with `"Status": "completed"`. Both entries share the same `EntryId` (a UUID) but have **different** `id` values.

```json
{
  "quests": {
    "mlhab7cd3efg12": {
      "EntryId": "07b29300-f6df-47e4-8f55-5aa697303896",
      "Name": "0_collect",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": false,
      "ExtraText": "",
      "id": "mlhab7cd3efg12"
    },
    "mlhxy9zw2abc34": {
      "EntryId": "07b29300-f6df-47e4-8f55-5aa697303896",
      "Name": "0_collect",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Rewards": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": false,
      "ExtraText": "",
      "SuccessMsg": "",
      "id": "mlhxy9zw2abc34"
    }
  }
}
```

Both entries are identical except for:
- `Status` -- `"inProgress"` vs `"completed"`
- `id` -- each entry has a unique quest ID
- `Rewards` -- only present on the completed entry
- `SuccessMsg` -- only present on the completed entry

---

## Field Reference

### All Fields

| Field | Type | Description |
|-------|------|-------------|
| `EntryId` | string (UUID) | Shared identifier between the inProgress and completed entries of a quest pair. Generate with UUID v4. |
| `id` | string | Unique quest ID. Format: `mlh` + 11-14 lowercase alphanumeric characters. Must match the dictionary key. Each entry in a pair has a **different** `id`. |
| `Name` | string | Quest name. **Must** use numbered format: `"0_name"`, `"1_name"`, `"2_name"`, etc. The numbered prefix is required. |
| `Description` | string | Must always be `"created in unity"`. This is a required fixed value. |
| `Status` | string | `"inProgress"` or `"completed"`. Determines which half of the pair this entry represents. |
| `Group` | string | Controls scope and persistence. `""` = single-player persistent, `"nonPersistent"` = resets on leave, `"multiplayer"` = shared across all players. See [Quest Groups](#quest-groups). |
| `DisplayGroup` | string | Category label in the quest log UI. `""` = no group. Set the same value on multiple quests to group them together. |
| `Enabled` | boolean | Must be `true` for the quest to function. |
| `RepeatableLimit` | integer | `0` = infinite repeats, `1` = one-shot (can only complete once), `N` = max N completions. |
| `FinishTime` | number | `0` = no time limit. Positive value = seconds before the quest auto-expires back to Not Active. |
| `AutoStart` | boolean | Must be `false`. This field does **not** auto-activate the quest. You must always use a trigger to transition a quest to Active. |
| `TriggeredByInventory` | boolean | `false` unless the quest is triggered by an inventory item activation. |
| `Requirements` | array | Quest dependencies. `[]` for no dependencies. See [Requirements](#requirements). |
| `Creator` | string | Firebase UID of the room owner. Obtain this from the [Verify Access Key](authentication.md#verify-access-key) response `data.uid` field. |
| `TemplateName` | string | Always `""`. |
| `Tracked` | boolean | `true` = quest appears in the player's quest log. |
| `Visible` | boolean | `false` for animation-only quests (invisible to the player). `true` to show the quest in the quest log UI. |
| `ExtraText` | string | `""` for standard quests. JSON string for dialogue trees (used with `DialogEffectorDisplay`). |
| `Rewards` | array | **Completed entry only.** `[]` for no rewards. Can contain reward objects for wearable/collectible grants. |
| `SuccessMsg` | string | **Completed entry only.** `""` or a message displayed to the player when the quest completes. |

### Completed-Entry-Only Fields

The `Rewards` and `SuccessMsg` fields only appear on the completed entry (the entry with `"Status": "completed"`). They must be omitted from the inProgress entry.

---

## Quest ID Format

Quest IDs follow a specific pattern:

```
mlh + 11-14 random lowercase alphanumeric characters
```

**Valid examples:**

- `"mlhab7cd3efg12"`
- `"mlh9kkyxvll8ql"`
- `"mlhxy9zw2abc34"`
- `"mlhjstsdgsfy4d7"`

**Invalid examples:**

- `"07b29300-f6df-47e4-8f55-5aa697303896"` -- this is a UUID format, only used for `EntryId`
- `"quest_0"` -- does not follow the `mlh` prefix pattern

The `id` field must match its dictionary key in the `quests` object.

---

## Quest Names

Quest names **must** follow the numbered format with an underscore separator:

```
{number}_{descriptive_name}
```

**Valid:**
- `"0_collect"` -- quest index 0, named "collect"
- `"1_activate"` -- quest index 1, named "activate"
- `"2_open_door"` -- quest index 2, named "open_door"
- `"15_final_boss"` -- quest index 15, named "final_boss"

**Invalid:**
- `"collect"` -- missing numbered prefix
- `"quest1"` -- no underscore separator
- `"myQuest"` -- no numbered prefix

Both entries in a quest pair use the **same** `Name`.

> **FunctionEffector note:** When referencing quest names in NCalc expressions (`SetTask()`, `$T{}`, `OnChange()`), use only the name **without** the numbered prefix. A quest named `"0_collect"` is referenced as `'collect'` in NCalc. See [Function Effects & NCalc](function-effects.md) for details.

---

## Quest Groups

The `Group` field controls both scope (who sees the quest state) and persistence (whether state survives reloads):

| Type | `Group` Value | Scope | Persistence | Use Case |
|------|---------------|-------|-------------|----------|
| **Single Player** | `""` (empty string) | Per-player | Saved between sessions | Personal progress, achievements, tutorials |
| **Non-Persistent** | `"nonPersistent"` | Per-player | Resets on leave/reload | Game rounds, temporary state, arcade-style games |
| **Multiplayer** | `"multiplayer"` | Shared (all players see the same state) | Saved between sessions | Cooperative objectives, room-wide events, boss fights |

### Single Player (Persistent)

```json
{
  "Group": "",
  "Name": "0_tutorial"
}
```

Each player has their own independent quest state. If Player A completes the quest, Player B's state is unaffected. State persists across sessions -- if a player leaves and returns, their progress is preserved.

### Non-Persistent

```json
{
  "Group": "nonPersistent",
  "Name": "0_game_round"
}
```

Per-player state that resets when the player leaves the room or reloads the page. Use this for game logic that should start fresh each session (active rounds, temporary roles, arcade mechanics).

### Multiplayer (Shared)

```json
{
  "Group": "multiplayer",
  "Name": "0_boss_defeated"
}
```

When any player changes this quest's state, all players see the change. If one player defeats the boss, all players see the boss-defeat effects. State persists across sessions.

### Room-Level Reset

Setting `"tasksRefresh": true` in the room's top-level `settings` object resets **all** quest states to Not Active on page reload, regardless of their `Group` setting. This is a room-wide override useful for testing or arcade-style rooms.

```json
{
  "settings": {
    "tasksRefresh": true
  }
}
```

---

## Requirements (Dependencies)

Quests can depend on other quests via the `Requirements` array. A quest with requirements will not be activatable until all required quests have been completed the specified number of times.

### Requirement Object

```json
{
  "Requirements": [
    {
      "delete": false,
      "amount": 1,
      "type": "quest",
      "id": "mlhab7cd3efg12"
    }
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `delete` | boolean | `false`. |
| `amount` | integer | How many times the required quest must be completed. Usually `1`. |
| `type` | string | `"quest"`. |
| `id` | string | The quest ID of the required quest. Use the **inProgress** entry's `id`. |

### Example -- Sequential Dependency

Quest 1 ("open_door") requires quest 0 ("find_key") to be completed first:

```json
{
  "quests": {
    "mlh0000findkey1": {
      "EntryId": "aaa11111-1111-1111-1111-111111111111",
      "Name": "0_find_key",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "id": "mlh0000findkey1"
    },
    "mlh0000findkey2": {
      "EntryId": "aaa11111-1111-1111-1111-111111111111",
      "Name": "0_find_key",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Rewards": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "SuccessMsg": "",
      "id": "mlh0000findkey2"
    },
    "mlh0000opendor1": {
      "EntryId": "bbb22222-2222-2222-2222-222222222222",
      "Name": "1_open_door",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [
        {
          "delete": false,
          "amount": 1,
          "type": "quest",
          "id": "mlh0000findkey1"
        }
      ],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "id": "mlh0000opendor1"
    },
    "mlh0000opendor2": {
      "EntryId": "bbb22222-2222-2222-2222-222222222222",
      "Name": "1_open_door",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [
        {
          "delete": false,
          "amount": 1,
          "type": "quest",
          "id": "mlh0000findkey1"
        }
      ],
      "Rewards": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "SuccessMsg": "The door is open!",
      "id": "mlh0000opendor2"
    }
  }
}
```

The requirement references `"mlh0000findkey1"` -- the **inProgress** entry's `id` of quest 0. Quest 1 cannot be activated until quest 0 has been completed at least once.

---

## Linking Effects to Quests

Items subscribe to quest state changes via `TaskEffectorSubscription` entries in their `Tasks` array (inside the item's [logic](room-data-format.md#logic) entry). When a quest transitions to a specific state, all subscribed items fire their effects.

### TaskEffectorSubscription Format

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": { "$type": "EffectType", ... },
  "Id": "unique-uuid-v4",
  "TargetState": 2,
  "Name": "0_collect",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `$type` | string | Always `"TaskEffectorSubscription"`. |
| `Effector` | object | The effect to fire. Any valid effect object (see [Interactions](interactions.md)). |
| `Id` | string (UUID) | Unique identifier for this subscription. Generate with UUID v4. |
| `TargetState` | integer | Which quest state triggers this effect. `1` = Active, `2` = Completed. **Omit entirely for state 0** (Not Active). |
| `Name` | string | Must match the quest's `Name` field exactly (e.g., `"0_collect"`). |
| `TaskTriggerId` | string | Must be the **inProgress** entry's `id` from the quest pair. |

### The 3-State Pattern

An item can have up to three `TaskEffectorSubscription` entries for a single quest -- one for each state. All three share the same `TaskTriggerId` and `Name`.

**State 0 -- Not Active (default position):**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "MoveToSpot",
    "_transformState": {
      "position": [0, 0.5, 0],
      "rotation": [0, 0, 0, 1],
      "scale": [1, 1, 1],
      "duration": 0.0
    }
  },
  "Id": "aaaaaaaa-1111-1111-1111-111111111111",
  "Name": "0_collect",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

> State 0 has **no** `TargetState` field. Do not include `"TargetState": 0` -- omit the field entirely.

**State 1 -- Active (item rises):**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "MoveToSpot",
    "_transformState": {
      "position": [0, 5, 0],
      "rotation": [0, 0, 0, 1],
      "scale": [1, 1, 1],
      "duration": 2.0
    }
  },
  "Id": "bbbbbbbb-2222-2222-2222-222222222222",
  "TargetState": 1,
  "Name": "0_collect",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

**State 2 -- Completed (item returns):**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "MoveToSpot",
    "_transformState": {
      "position": [0, 0.5, 0],
      "rotation": [0, 0, 0, 1],
      "scale": [1, 1, 1],
      "duration": 1.0
    }
  },
  "Id": "cccccccc-3333-3333-3333-333333333333",
  "TargetState": 2,
  "Name": "0_collect",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

### Hide/Show on Quest State

A common pattern is hiding or revealing items based on quest progress:

**Hide an item when quest completes:**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": { "$type": "HideObjectEvent" },
  "Id": "dddddddd-4444-4444-4444-444444444444",
  "TargetState": 2,
  "Name": "0_collect",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

**Show an item when quest becomes active:**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": { "$type": "ShowObjectEvent" },
  "Id": "eeeeeeee-5555-5555-5555-555555555555",
  "TargetState": 1,
  "Name": "0_collect",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

---

## Triggering Quest State Changes

Quests start in Not Active (state 0) and stay there until something triggers a state change. There are two primary mechanisms.

### Via TaskTriggerSubscription (Direct Trigger)

A `TaskTriggerSubscription` on an item can directly change a quest's state when a trigger fires. This links the trigger event to the quest using encoded `TargetState` values.

**Example -- Click an item to activate a quest:**

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": { "$type": "OnClickEvent" },
  "Id": "ffffffff-6666-6666-6666-666666666666",
  "TargetState": 111,
  "Name": "0_collect",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `$type` | string | `"TaskTriggerSubscription"` |
| `Trigger` | object | The trigger event. Any valid trigger (see [Interactions](interactions.md)). |
| `Id` | string (UUID) | Unique identifier. |
| `TargetState` | integer | Encoded state transition value. See [TargetState Values](#targetstate-values). |
| `Name` | string | Quest name. Must match the quest's `Name` field. |
| `TaskTriggerId` | string | The **inProgress** entry's `id` from the quest pair. |

> Note: This form of `TaskTriggerSubscription` has **no** `DirectEffector` field -- it changes the quest state directly. This is different from the basic interaction form (which has `DirectEffector` and no `TaskTriggerId`). See [Interactions](interactions.md) for the basic interaction format.

**Example -- Player enters a zone to activate a quest:**

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": { "$type": "OnEnterEvent" },
  "Id": "11111111-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
  "TargetState": 111,
  "Name": "0_collect",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

`OnEnterEvent` only works on Trigger items (`"prefabName": "Trigger"`).

### Via RunTriggersFromEffector (Quest Chaining)

When one quest reaches a specific state, it can trigger state changes on other quests using `RunTriggersFromEffector`. This is an effect that fires as a `TaskEffectorSubscription` and contains `linkedTasks` that target other quests.

**Example -- When quest 0 completes, activate quest 1:**

```json
{
  "$type": "TaskEffectorSubscription",
  "Effector": {
    "$type": "RunTriggersFromEffector",
    "linkedTasks": [
      {
        "Trigger": {},
        "Id": "22222222-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
        "TargetState": 111,
        "Name": "1_activate",
        "TaskTriggerId": "mlh0000quest1id"
      }
    ]
  },
  "Id": "33333333-cccc-cccc-cccc-cccccccccccc",
  "TargetState": 2,
  "Name": "0_collect",
  "TaskTriggerId": "mlhab7cd3efg12"
}
```

The **outer** `TaskEffectorSubscription` watches quest 0 (`"0_collect"`) for state 2 (Completed). When it fires, the **inner** `linkedTasks` entry triggers quest 1 (`"1_activate"`) to transition via TargetState 111 (Not Active to Active).

#### linkedTasks Entry Fields

| Field | Type | Description |
|-------|------|-------------|
| `Trigger` | object | `{}` for immediate execution. `{"Delay": 1.0}` to delay the trigger by 1 second. |
| `Id` | string (UUID) | Unique identifier. |
| `TargetState` | integer | Encoded state transition value. See [TargetState Values](#targetstate-values). |
| `Name` | string | Target quest's `Name` field. |
| `TaskTriggerId` | string | Target quest's inProgress entry `id`. |

`linkedTasks` is an array -- you can trigger **multiple** quest state changes from a single event, each targeting a different quest or the same quest with a different transition.

#### useRandom

Set `"useRandom": true` on the `RunTriggersFromEffector` effector (sibling to `linkedTasks`) to randomly pick **one** of the linked tasks to fire instead of firing all of them.

```json
{
  "$type": "RunTriggersFromEffector",
  "useRandom": true,
  "linkedTasks": [
    { "Trigger": {}, "Id": "...", "TargetState": 111, "Name": "0_path_a", "TaskTriggerId": "mlh..." },
    { "Trigger": {}, "Id": "...", "TargetState": 111, "Name": "0_path_b", "TaskTriggerId": "mlh..." }
  ]
}
```

---

## TargetState Values

When triggering quest state changes (via `TaskTriggerSubscription` or `RunTriggersFromEffector.linkedTasks`), the `TargetState` field uses encoded values that specify the exact transition:

| Value | From | To | Description |
|-------|------|----|-------------|
| `101` | Any | Not Active | Reset to Not Active regardless of current state |
| `111` | Not Active | Active | Standard activation. Only fires if quest is currently Not Active. |
| `121` | Active | Completed | Standard completion. Only fires if quest is currently Active. |
| `131` | Completed | Active | Re-activate a completed quest. Only fires if currently Completed. |
| `141` | Any | Completed | Force complete regardless of current state. |
| `151` | Any | Active | Force activate regardless of current state. |
| `161` | Active | Not Active | Deactivate. Only fires if currently Active. |
| `171` | Completed | Not Active | Reset completed quest. Only fires if currently Completed. |
| `181` | Not Active | Completed | Skip Active, go directly to Completed. Only fires if currently Not Active. |

The "Any" variants (`101`, `141`, `151`) fire regardless of the quest's current state. The constrained variants (e.g., `121`) only fire when the quest is in the specified "from" state, acting as a guard.

> These encoded values are only used in `TaskTriggerSubscription` (quest-advancing triggers) and `RunTriggersFromEffector.linkedTasks`. They are **not** used in `TaskEffectorSubscription.TargetState`, which uses plain values `1` and `2` (or is omitted for state 0).

---

## Common Patterns

### 1. Sequential Quests

Quest 0 completes, then quest 1 automatically activates, then quest 1 completes and quest 2 activates.

**Quests:**

```json
{
  "quests": {
    "mlhseq0progress": {
      "EntryId": "aaa00000-0000-0000-0000-000000000001",
      "Name": "0_step_one",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "id": "mlhseq0progress"
    },
    "mlhseq0complete": {
      "EntryId": "aaa00000-0000-0000-0000-000000000001",
      "Name": "0_step_one",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Rewards": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "SuccessMsg": "",
      "id": "mlhseq0complete"
    },
    "mlhseq1progress": {
      "EntryId": "bbb00000-0000-0000-0000-000000000002",
      "Name": "1_step_two",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "id": "mlhseq1progress"
    },
    "mlhseq1complete": {
      "EntryId": "bbb00000-0000-0000-0000-000000000002",
      "Name": "1_step_two",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Rewards": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "SuccessMsg": "",
      "id": "mlhseq1complete"
    }
  }
}
```

**Chaining logic (in an item's logic entry):**

Place this `RunTriggersFromEffector` in the `Tasks` array of any item's logic. When quest 0 completes, it activates quest 1:

```json
{
  "Tasks": [
    {
      "$type": "TaskEffectorSubscription",
      "Effector": {
        "$type": "RunTriggersFromEffector",
        "linkedTasks": [
          {
            "Trigger": {},
            "Id": "44444444-dddd-dddd-dddd-dddddddddddd",
            "TargetState": 111,
            "Name": "1_step_two",
            "TaskTriggerId": "mlhseq1progress"
          }
        ]
      },
      "Id": "55555555-eeee-eeee-eeee-eeeeeeeeeeee",
      "TargetState": 2,
      "Name": "0_step_one",
      "TaskTriggerId": "mlhseq0progress"
    }
  ]
}
```

### 2. Auto-Reset Loop

A quest that automatically resets itself after completing, so it can be triggered again. Useful for repeatable interactions like buttons, switches, or collectibles.

Place this in any item's `Tasks` array. When quest 0 completes (state 2), it resets back to Not Active (101) after a 2-second delay:

```json
{
  "Tasks": [
    {
      "$type": "TaskEffectorSubscription",
      "Effector": {
        "$type": "RunTriggersFromEffector",
        "linkedTasks": [
          {
            "Trigger": { "Delay": 2.0 },
            "Id": "66666666-ffff-ffff-ffff-ffffffffffff",
            "TargetState": 101,
            "Name": "0_toggle",
            "TaskTriggerId": "mlhtoggle00001"
          }
        ]
      },
      "Id": "77777777-1111-2222-3333-444444444444",
      "TargetState": 2,
      "Name": "0_toggle",
      "TaskTriggerId": "mlhtoggle00001"
    }
  ]
}
```

The delay gives subscribed effects time to play their state 2 animations before the quest resets. Without the delay (`"Trigger": {}`), the reset would be instantaneous.

### 3. Multiplayer Cooperative Quest

A quest shared across all players. When any player triggers it, all players see the state change and all subscribed effects fire for everyone.

**Quest pair** -- note `"Group": "multiplayer"` on both entries:

```json
{
  "quests": {
    "mlhcoop0progres": {
      "EntryId": "ccc00000-0000-0000-0000-000000000003",
      "Name": "0_team_goal",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "multiplayer",
      "DisplayGroup": "Team Objectives",
      "Enabled": true,
      "RepeatableLimit": 1,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "id": "mlhcoop0progres"
    },
    "mlhcoop0complet": {
      "EntryId": "ccc00000-0000-0000-0000-000000000003",
      "Name": "0_team_goal",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "multiplayer",
      "DisplayGroup": "Team Objectives",
      "Enabled": true,
      "RepeatableLimit": 1,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Rewards": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "SuccessMsg": "Team objective complete!",
      "id": "mlhcoop0complet"
    }
  }
}
```

Key differences from single-player quests:
- `"Group": "multiplayer"` -- state is shared across all players
- `"RepeatableLimit": 1` -- one-shot, so once any player completes it, it stays completed for everyone
- `"Visible": true` and `"DisplayGroup": "Team Objectives"` -- shows in the quest log under a group header

### 4. Timed Quest

A quest with a time limit. If the player does not complete it within the specified time, it expires back to Not Active.

**Quest pair** -- note `"FinishTime": 30` for a 30-second timer:

```json
{
  "quests": {
    "mlhtimed0progre": {
      "EntryId": "ddd00000-0000-0000-0000-000000000004",
      "Name": "0_speed_run",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "nonPersistent",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 30,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "id": "mlhtimed0progre"
    },
    "mlhtimed0comple": {
      "EntryId": "ddd00000-0000-0000-0000-000000000004",
      "Name": "0_speed_run",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "nonPersistent",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 30,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Rewards": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": true,
      "ExtraText": "",
      "SuccessMsg": "Speed run complete!",
      "id": "mlhtimed0comple"
    }
  }
}
```

When the quest is activated (transitions to Active), a 30-second countdown begins. If the quest is not completed within 30 seconds, it auto-expires back to Not Active. Combined with `"Group": "nonPersistent"`, this creates a repeatable timed challenge.

---

## Complete Working Example

A minimal room with a clickable button that activates a quest, which moves a platform upward. Demonstrates the full quest lifecycle: quest definition, trigger, and effect subscription.

### Room Data

```json
{
  "roomItems": {
    "2": {
      "prefabName": "SpawnPoint",
      "pos": {"x": 0, "y": 0, "z": 0},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 1, "y": 1, "z": 1},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "parentItemID": 0,
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    },
    "3": {
      "prefabName": "ResizableCube",
      "pos": {"x": 0, "y": -0.05, "z": 0},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 20, "y": 0.1, "z": 20},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "parentItemID": 0,
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    },
    "4": {
      "prefabName": "ResizableCube",
      "pos": {"x": 3, "y": 0.5, "z": 3},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 1, "y": 1, "z": 1},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "parentItemID": 0,
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "Click me",
      "hoverBodyContent": "Activates the platform",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    },
    "5": {
      "prefabName": "ResizableCube",
      "pos": {"x": -3, "y": 0.25, "z": 3},
      "rot": {"x": 0, "y": 0, "z": 0, "w": 1},
      "scale": {"x": 3, "y": 0.5, "z": 3},
      "modelsize": {"x": 0, "y": 0, "z": 0},
      "modelCenter": {"x": 0, "y": 0, "z": 0},
      "contentString": "",
      "parentItemID": 0,
      "placed": true,
      "locked": false,
      "superLocked": false,
      "interactivityType": 0,
      "interactivityURL": "",
      "hoverTitle": "",
      "hoverBodyContent": "",
      "ImageInteractivityDetails": {},
      "sessionData": "",
      "instanceId": "",
      "currentEditornetId": 0
    }
  },
  "settings": {
    "roomBase": "BlankScene",
    "isNight": false,
    "chatDisabled": false,
    "tasksRefresh": true,
    "roomSettingsExtraData": "{\"showNameTags\":true}"
  },
  "roomTasks": {
    "Tasks": []
  },
  "quests": {
    "mlhexample0prog": {
      "EntryId": "11111111-2222-3333-4444-555555555555",
      "Name": "0_activate",
      "Description": "created in unity",
      "Status": "inProgress",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": false,
      "ExtraText": "",
      "id": "mlhexample0prog"
    },
    "mlhexample0comp": {
      "EntryId": "11111111-2222-3333-4444-555555555555",
      "Name": "0_activate",
      "Description": "created in unity",
      "Status": "completed",
      "Group": "",
      "DisplayGroup": "",
      "Enabled": true,
      "RepeatableLimit": 0,
      "FinishTime": 0,
      "AutoStart": false,
      "TriggeredByInventory": false,
      "Requirements": [],
      "Rewards": [],
      "Creator": "your-firebase-uid",
      "TemplateName": "",
      "Tracked": true,
      "Visible": false,
      "ExtraText": "",
      "SuccessMsg": "",
      "id": "mlhexample0comp"
    }
  },
  "logic": {
    "3": "{\"Tasks\":[],\"ViewNodes\":[],\"col\":\"444444\",\"e\":0,\"c\":true}",
    "4": "{\"Tasks\":[{\"$type\":\"TaskTriggerSubscription\",\"Trigger\":{\"$type\":\"OnClickEvent\"},\"Id\":\"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\",\"TargetState\":111,\"Name\":\"0_activate\",\"TaskTriggerId\":\"mlhexample0prog\"},{\"$type\":\"TaskTriggerSubscription\",\"Trigger\":{\"$type\":\"OnClickEvent\"},\"Id\":\"ffffffff-1111-2222-3333-444444444444\",\"TargetState\":121,\"Name\":\"0_activate\",\"TaskTriggerId\":\"mlhexample0prog\"}],\"ViewNodes\":[],\"col\":\"00AAFF\",\"e\":0.5,\"c\":true}",
    "5": "{\"Tasks\":[{\"$type\":\"TaskEffectorSubscription\",\"Effector\":{\"$type\":\"MoveToSpot\",\"_transformState\":{\"position\":[-3,0.25,3],\"rotation\":[0,0,0,1],\"scale\":[3,0.5,3],\"duration\":0.0}},\"Id\":\"11111111-aaaa-bbbb-cccc-dddddddddddd\",\"Name\":\"0_activate\",\"TaskTriggerId\":\"mlhexample0prog\"},{\"$type\":\"TaskEffectorSubscription\",\"Effector\":{\"$type\":\"MoveToSpot\",\"_transformState\":{\"position\":[-3,5,3],\"rotation\":[0,0,0,1],\"scale\":[3,0.5,3],\"duration\":2.0}},\"Id\":\"22222222-aaaa-bbbb-cccc-dddddddddddd\",\"TargetState\":1,\"Name\":\"0_activate\",\"TaskTriggerId\":\"mlhexample0prog\"},{\"$type\":\"TaskEffectorSubscription\",\"Effector\":{\"$type\":\"MoveToSpot\",\"_transformState\":{\"position\":[-3,0.25,3],\"rotation\":[0,0,0,1],\"scale\":[3,0.5,3],\"duration\":1.0}},\"Id\":\"33333333-aaaa-bbbb-cccc-dddddddddddd\",\"TargetState\":2,\"Name\":\"0_activate\",\"TaskTriggerId\":\"mlhexample0prog\"}],\"ViewNodes\":[],\"col\":\"00FF00\",\"e\":0,\"c\":true}"
  }
}
```

### What It Does

| Item | ID | Role |
|------|----|------|
| Spawn Point | `"2"` | Player spawns at origin |
| Floor | `"3"` | Dark grey floor, 20x20 units |
| Button | `"4"` | Blue glowing cube. First click activates quest (111). Second click completes it (121). |
| Platform | `"5"` | Green platform. Rises to Y=5 when quest is Active. Returns to Y=0.25 when Completed or Not Active. |

### Logic Breakdown

**Item "4" (button) -- parsed Tasks:**

```json
[
  {
    "$type": "TaskTriggerSubscription",
    "Trigger": {"$type": "OnClickEvent"},
    "Id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "TargetState": 111,
    "Name": "0_activate",
    "TaskTriggerId": "mlhexample0prog"
  },
  {
    "$type": "TaskTriggerSubscription",
    "Trigger": {"$type": "OnClickEvent"},
    "Id": "ffffffff-1111-2222-3333-444444444444",
    "TargetState": 121,
    "Name": "0_activate",
    "TaskTriggerId": "mlhexample0prog"
  }
]
```

Two click handlers on the same item: one transitions Not Active to Active (111), the other transitions Active to Completed (121). Only one fires per click, depending on the quest's current state.

**Item "5" (platform) -- parsed Tasks:**

```json
[
  {
    "$type": "TaskEffectorSubscription",
    "Effector": {
      "$type": "MoveToSpot",
      "_transformState": {
        "position": [-3, 0.25, 3],
        "rotation": [0, 0, 0, 1],
        "scale": [3, 0.5, 3],
        "duration": 0.0
      }
    },
    "Id": "11111111-aaaa-bbbb-cccc-dddddddddddd",
    "Name": "0_activate",
    "TaskTriggerId": "mlhexample0prog"
  },
  {
    "$type": "TaskEffectorSubscription",
    "Effector": {
      "$type": "MoveToSpot",
      "_transformState": {
        "position": [-3, 5, 3],
        "rotation": [0, 0, 0, 1],
        "scale": [3, 0.5, 3],
        "duration": 2.0
      }
    },
    "Id": "22222222-aaaa-bbbb-cccc-dddddddddddd",
    "TargetState": 1,
    "Name": "0_activate",
    "TaskTriggerId": "mlhexample0prog"
  },
  {
    "$type": "TaskEffectorSubscription",
    "Effector": {
      "$type": "MoveToSpot",
      "_transformState": {
        "position": [-3, 0.25, 3],
        "rotation": [0, 0, 0, 1],
        "scale": [3, 0.5, 3],
        "duration": 1.0
      }
    },
    "Id": "33333333-aaaa-bbbb-cccc-dddddddddddd",
    "TargetState": 2,
    "Name": "0_activate",
    "TaskTriggerId": "mlhexample0prog"
  }
]
```

Three effector subscriptions -- one per quest state. State 0 (no `TargetState`) snaps the platform to its resting position instantly. State 1 (`TargetState: 1`) animates it up over 2 seconds. State 2 (`TargetState: 2`) animates it back down over 1 second.

---

## Critical Rules

1. **Every quest needs BOTH entries.** A quest pair must have one `"Status": "inProgress"` entry and one `"Status": "completed"` entry. Missing either entry will cause the quest to malfunction.

2. **Both entries share `EntryId` but have different `id` values.** The `EntryId` is a UUID that links the pair together. The `id` fields are unique quest IDs in `mlh` format.

3. **Names must have a numbered prefix.** Format: `"0_name"`, `"1_name"`, etc. Quests without the numbered prefix will not function.

4. **Description must be `"created in unity"`.** This is a required fixed value. Other values will cause issues.

5. **Creator must be a valid Firebase UID.** Obtain it from the [Verify Access Key](authentication.md#verify-access-key) endpoint. Quests with an invalid Creator will not function.

6. **AutoStart does not activate the quest.** Setting `AutoStart` to `true` does not transition the quest to Active. You must always use a trigger (`TaskTriggerSubscription`) to change quest state.

7. **State 0 effects have no TargetState field.** In `TaskEffectorSubscription`, state 0 entries must omit `TargetState` entirely. Do not set `"TargetState": 0`.

8. **The inProgress entry's `id` is used as `TaskTriggerId`.** When linking effects or triggers to a quest, always reference the `id` from the inProgress entry, not the completed entry.

9. **The `Name` field must match exactly.** The `Name` in a `TaskEffectorSubscription` or `TaskTriggerSubscription` must match the quest's `Name` field character-for-character (e.g., `"0_collect"`).

10. **Logic values are JSON strings.** When writing quest-linked effects into `logic`, remember that each value in the `logic` object is a stringified JSON object, not a raw object. See [Room Data Format](room-data-format.md#logic).

---

## Related Pages

- [Room Data Format](room-data-format.md) -- Top-level structure including quests and logic
- [Interactions](interactions.md) -- Trigger and effect formats for the Tasks array
- [Function Effects & NCalc](function-effects.md) -- Variables, conditionals, and quest state in expressions
- [Authentication](authentication.md) -- Obtaining your Firebase UID for the Creator field
- [Settings](settings.md) -- Room-level settings including `tasksRefresh`
