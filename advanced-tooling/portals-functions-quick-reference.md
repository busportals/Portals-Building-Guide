# Portals Functions Quick Reference

A quick reference for all Portals-specific functions. These work in both the Function Effect and the Javascript Function effect.

***

## Reading Game State

| Syntax | Returns | Description |
|--------|---------|-------------|
| `$T{taskName}` | `'NotActive'`, `'Active'`, or `'Completed'` | Read a task's state as text |
| `$TN{taskName}` | `0`, `1`, or `2` | Read a task's state as a number (0 = NotActive, 1 = Active, 2 = Completed) |
| `$N{variableName}` | Number | Read a variable's current value |
| `$N{timerName}` | Number (seconds) | Read a running timer's elapsed time |

***

## Setting Game State

| Function | Syntax | Description |
|----------|--------|-------------|
| `SetTask` | `SetTask('taskName', 'TaskState', delay)` | Set a task to `'NotActive'`, `'Active'`, or `'Completed'`. Delay is in seconds. |
| `SetVariable` | `SetVariable('variableName', value, delay)` | Set a variable to a number. Delay is in seconds. |

***

## Random Selection

| Function | Syntax | Description |
|----------|--------|-------------|
| `SelectRandom` | `SelectRandom(item1, item2, item3, ...)` | Returns one random item from the list. Works with numbers, strings, and expressions. |

***

## Multiplayer Functions

### Player Lists

| Syntax | Description |
|--------|-------------|
| `[Players]` | All players currently in the room |

### Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| `AssignNumbersInOrder` | `AssignNumbersInOrder([Players], 'variableName')` | Give each player a unique number (1, 2, 3...) |
| `SelectRandomPlayers` | `SelectRandomPlayers([Players], count)` | Pick a random set of players |
| `SelectPlayers` | `SelectPlayers([Players], 'paramName', paramValue)` | Filter players by a parameter value |
| `SelectPlayersParameters` | `SelectPlayersParameters([Players], 'paramName')` | Get a parameter value from each player |
| `SetPlayersParameters` | `SetPlayersParameters([Players], 'paramName', value)` | Set a parameter on all players in a list |
| `CountArray` | `CountArray(list)` | Count items in a list |
| `PrintString` | `PrintString(value)` | Debug output to browser console |
| `UpdateMultiplayerNumericVariable` | `UpdateMultiplayerNumericVariable('varName', value, opType, delay)` | Update a multiplayer variable via server |

### UpdateMultiplayerNumericVariable Operation Types

| Type | Operation |
|------|-----------|
| 0.0 | Set (replace) |
| 1.0 | Add |
| 2.0 | Subtract |
| 3.0 | Multiply |
| 4.0 | Divide |

### Built-in Player Properties

| Property | Description |
|----------|-------------|
| `playerName` | Player's username |
| `health` | Player's health (default 100) |

***

## Important Notes

* **Use decimals** — Always write `0.0`, `1.0`, `10.0` instead of `0`, `1`, `10` to avoid number type errors.
* **Delays are in seconds** — `0.0` means immediately, `2.0` means after 2 seconds.
* **Task state strings** — Always use `'NotActive'`, `'Active'`, `'Completed'` (exact spelling, single quotes).
* **Timer must be running** — Reading a timer with `$N{}` returns 0 if the timer hasn't been started.
* **Multiplayer syncs automatically** — `SetPlayersParameters` and `UpdateMultiplayerNumericVariable` sync to all clients.
