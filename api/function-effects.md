# Function Effects & NCalc

The `FunctionEffector` is a powerful effect type that evaluates NCalc expressions at runtime. Use it when you need conditional logic, variable manipulation, quest state branching, randomness, timers, or multiplayer coordination.

## Basic Usage

A `FunctionEffector` goes inside a `TaskTriggerSubscription` or `TaskEffectorSubscription` like any other effect:

```json
{
  "$type": "FunctionEffector",
  "V": "if($N{coins} >= 10.0, SetTask('shop', 'Active', 0.0), 0.0)"
}
```

The `V` field contains the NCalc expression string.

---

## Syntax Rules

1. **All numeric values must use decimals**: `0.0` not `0`, `1.0` not `1`. Integers cause cast errors.
2. **Strings use single quotes**: `'Active'` not `"Active"`
3. **Task names omit the numbered prefix**: Quest `Name` fields use `0_redteam`, but NCalc uses just `'redteam'` (no `0_` prefix). This applies to `SetTask()`, `$T{}`, `$TN{}`, and `OnChange()`.

---

## Reading Values

| Syntax | Returns | Example |
|--------|---------|---------|
| `$T{name}` | `'NotActive'` / `'Active'` / `'Completed'` | `$T{door} == 'Active'` |
| `$TN{name}` | `0` / `1` / `2` | `$TN{door} == 1.0` |
| `$N{name}` | Number (variable value) | `$N{coins} >= 10.0` |
| `$N{timerName}` | Number (elapsed seconds) | `$N{RaceTimer} >= 60.0` |

> **Note:** `$T{}` is preferred over `$TN{}` — more readable, same performance.

---

## Operators

**Math:** `+` `-` `*` `/` `%` (mod) `**` (power)

**Compare:** `==` `!=` `>` `<` `>=` `<=`

**Logic:** `&&` (and) `||` (or) `!` (not)

Group with parentheses:
```
($N{coins} >= 10.0) && ($T{quest} == 'Active')
```

---

## Control Flow

### if(condition, whenTrue, whenFalse)

```
if($N{coins} >= 10.0,
   SetTask('shop', 'Active', 0.0),
   0.0
)
```

Nested (else-if):
```
if($T{quest} == 'NotActive',
   SetTask('offer', 'Active', 0.0),
   if($T{quest} == 'Active',
      SetTask('reminder', 'Active', 0.0),
      SetTask('done', 'Active', 0.0)
   )
)
```

### ifs(cond1, val1, cond2, val2, ..., default)

Multi-branch switch:
```
ifs(
  $T{step} == 'NotActive', SetVariable('hint', 0.0, 0.0),
  $T{step} == 'Active',    SetVariable('hint', 1.0, 0.0),
                            SetVariable('hint', 2.0, 0.0)
)
```

The last entry (no condition) is the default.

---

## Portals Functions

### SetTask(taskName, state, delay)

Changes a quest's state. Task names omit the numbered prefix.

```
SetTask('alarm', 'Active', 0.0)
SetTask('alarm', 'NotActive', 5.0)   // reset after 5 seconds
```

States: `'NotActive'`, `'Active'`, `'Completed'`

### SetVariable(varName, value, delay)

Sets a numeric variable's value.

```
SetVariable('coins', 0.0, 0.0)                  // set to 0
SetVariable('coins', $N{coins} + 10.0, 0.0)     // add 10
SetVariable('health', Max($N{health} - 1.0, 0.0), 0.0)  // subtract, floor at 0
```

### SelectRandom(item1, item2, ...)

Picks one value at random.

```
SetVariable('reward', SelectRandom(5.0, 10.0, 25.0, 50.0), 0.0)
SelectRandom(true, false)   // coin flip
```

### OnChange(taskName, targetState)

Returns `true` only at the moment of a state transition, not on every evaluation. Edge-triggered.

```
if(OnChange('puzzle1', 'Completed'),
   SetVariable('doorOpen', 1.0, 0.0),
   0.0
)
```

Combine multiple:
```
(OnChange('task1', 'Active') || OnChange('task2', 'Completed'))
&& $T{task1} == 'Active' && $T{task2} == 'Completed'
```

---

## Math Functions

| Function | Example | Result |
|----------|---------|--------|
| `Min(a, b)` | `Min($N{coins}, 999.0)` | Cap at 999 |
| `Max(a, b)` | `Max($N{health}, 0.0)` | Floor at 0 |
| `Round(n)` | `Round(3.6)` | 4 |
| `Floor(n)` | `Floor(3.9)` | 3 |
| `Ceiling(n)` | `Ceiling(3.1)` | 4 |
| `Abs(n)` | `Abs(-5.0)` | 5 |
| `Sqrt(n)` | `Sqrt(9.0)` | 3 |

**Clamp pattern:** `Min(Max($N{health}, 0.0), 100.0)`

---

## Multiplayer Functions

### Player Lists

- `[Players]` — all players in room (literal syntax, brackets required)
- Chain operations with `+`: later operations override earlier ones

### Functions

```
AssignNumbersInOrder([Players], 'playerNum')        // sequential 1,2,3...
SelectRandomPlayers([Players], 2)                    // pick 2 random
SelectPlayers([Players], 'team', 'red')              // filter by param
SelectPlayersParameters([Players], 'health')         // get param from all
SetPlayersParameters([Players], 'canMove', true)     // set param on all
CountArray(SelectPlayers([Players], 'alive', 'true'))  // count matching
PrintString(value)                                   // debug to console
```

### UpdateMultiplayerNumericVariable(varName, value, opType, delay)

| opType | Operation |
|--------|-----------|
| `0.0` | Set |
| `1.0` | Add |
| `2.0` | Subtract |
| `3.0` | Multiply |
| `4.0` | Divide |

```
UpdateMultiplayerNumericVariable('score', 10.0, 1.0, 0.0)  // add 10
```

---

## Common Multiplayer Patterns

### Team Split

```
SetPlayersParameters([Players], 'team', 'blue')
+ SetPlayersParameters(
    SelectRandomPlayers([Players], Floor($N{PlayerCount} / 2.0)),
    'team', 'red'
  )
```

### Impostor Assignment

```
SetPlayersParameters([Players], 'impostor', false)
+ SetPlayersParameters(SelectRandomPlayers([Players], 2), 'impostor', true)
```

---

## Displaying Variables in Text

Use pipe syntax `|variableName|` to show a variable's live value inline. The value updates automatically.

**Works in:**
- `WorldText` `text` field: `"Score: |coins|"`
- `NotificationPillEvent` `nt` field: `"You earned |reward| points!"`

---

## FunctionEffector Flags

When attached to an item as a `TaskTriggerSubscription`, the FunctionEffector supports two behavioral flags in the Portals editor:

| Flag | Effect |
|------|--------|
| **Trigger on Tasks Change** | Auto-evaluates when any referenced task/variable changes |
| **Activate on Start** | Evaluates once on player login |

---

## Complete Examples

### Gate Progress Behind Variable

When a player has 10+ coins, activate the shop quest:

```json
{
  "$type": "TaskTriggerSubscription",
  "Trigger": {"$type": "ScoreTrigger"},
  "DirectEffector": {
    "Effector": {
      "$type": "FunctionEffector",
      "V": "if($N{coins} >= 10.0, SetTask('shop', 'Active', 0.0), 0.0)"
    },
    "Id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "TargetState": 2,
    "Name": ""
  },
  "Id": "f1e2d3c4-b5a6-7890-abcd-ef1234567890",
  "TargetState": 2,
  "Name": ""
}
```

### Random Reward on Collect

```json
{
  "$type": "FunctionEffector",
  "V": "SetVariable('reward', SelectRandom(1.0, 5.0, 10.0, 50.0), 0.0)"
}
```

### Timed Bonus Check

```json
{
  "$type": "FunctionEffector",
  "V": "if($N{RaceTimer} < 30.0, SetVariable('bonus', 100.0, 0.0), SetVariable('bonus', 0.0, 0.0))"
}
```

### Multi-Condition Quest Advance

```json
{
  "$type": "FunctionEffector",
  "V": "if(($T{key} == 'Completed') && ($T{map} == 'Completed'), SetTask('door', 'Active', 0.0), 0.0)"
}
```

---

## Critical Rules

1. **Always use decimals** — `0.0` not `0`, `1.0` not `1`
2. **Single quotes for strings** — `'Active'` not `"Active"`
3. **Task names omit numbered prefix** — quest `Name` is `0_redteam`, NCalc uses `'redteam'`
4. **Unstarted timers return 0** — start the timer effect first
5. **`OnChange` is edge-triggered** — fires once at the transition, not continuously
6. **`+` chains multiplayer operations** — order matters, later overrides earlier

---

## Related Pages

- [Interactions](interactions.md) — trigger and effect wrappers
- [Quests](quests.md) — quest state system
- [Settings](settings.md) — numeric parameter (variable) declarations
- [Item Types](item-types.md) — WorldText pipe syntax for variable display
