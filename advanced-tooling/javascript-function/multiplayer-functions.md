# Multiplayer Functions

These functions let you work with players in multiplayer spaces. They're essential for games like team battles, role assignment (impostors, hunters), and any logic that needs to affect multiple players at once.

***

## Quick Reference

### Player List & Properties

| Syntax | What It Does | Example |
|--------|--------------|---------|
| `[Players]` | All players currently in the room | `SetPlayersParameters([Players], 'health', 100)` |
| `$N{variableName}` | Read current player's variable | `$N{team}` returns player's team value |
| `playerName` | Built-in: player's username | Use with `SelectPlayersParameters` |
| `health` | Built-in: player's health (default 100) | Use with `SelectPlayersParameters` |

### Functions

| Function | What It Does |
|----------|--------------|
| `AssignNumbersInOrder` | Give each player a unique number (1, 2, 3...) |
| `SelectRandomPlayers` | Pick random players from a list |
| `SelectPlayers` | Filter players by a parameter value |
| `SelectPlayersParameters` | Get a parameter value from each player |
| `SetPlayersParameters` | Set a parameter on all players in a list |
| `CountArray` | Count items in a list |
| `PrintString` | Debug output to console |
| `UpdateMultiplayerNumericVariable` | Update a multiplayer variable via server |

### Common Patterns

| Pattern | Example |
|---------|---------|
| Assign roles to random players | `SetPlayersParameters(SelectRandomPlayers([Players], 2), 'impostor', 'true');` |
| Count players with a role | `CountArray(SelectPlayers([Players], 'impostor', 'true'))` |
| Set default then override | Set all to blue, then pick some for red (see examples below) |

***

## Detailed Reference

***

### AssignNumbersInOrder([Players], 'variableName')

Assigns sequential numbers (1, 2, 3, etc.) to each player in the room.

```javascript
AssignNumbersInOrder([Players], 'playernumber');
```

What it does:

* Gives each player a unique number starting from 1
* First player gets 1, second gets 2, third gets 3, etc.
* Stores the number in the specified variable for each player

Common use: assigning spawn points, player slots, turn order, or team positions.

Then use the player number for spawn logic:

```javascript
if ($N{playernumber} == 1.0) {
  SetTask('spawn1', 'Active', 0.0);
} else if ($N{playernumber} == 2.0) {
  SetTask('spawn2', 'Active', 0.0);
} else if ($N{playernumber} == 3.0) {
  SetTask('spawn3', 'Active', 0.0);
}
```

***

### SelectRandomPlayers([Players], count)

Picks a random selection of players from a list.

```javascript
SelectRandomPlayers([Players], 2);
```

What it does:

* Picks 2 random players from all players in the room
* Returns a list of player IDs

**Important:** This selection is:
- **Deterministic** — all clients get the same result
- **Persistent** — the same players stay selected even after reconnects

Common use: picking teams, assigning roles, choosing a "seeker" in hide and seek.

***

### SelectPlayersParameters([Players], 'parameterName')

Gets a parameter value from each player in a list.

```javascript
// Get all player health values
SelectPlayersParameters([Players], 'health');
// Example result: [100, 85, 100, 50]
```

```javascript
// Get names of 3 random players
SelectPlayersParameters(SelectRandomPlayers([Players], 3), 'playerName');
```

***

### SetPlayersParameters([Players], 'parameterName', value)

Sets a parameter on all players in a list. Changes sync to all clients automatically.

```javascript
// Set canMove to true for everyone
SetPlayersParameters([Players], 'canMove', true);
```

```javascript
// Set everyone's health to 50
SetPlayersParameters([Players], 'health', 50);
```

Common use: applying effects to all players, resetting values, setting up game state.

***

### SelectPlayers([Players], 'parameterName', parameterValue)

Filters a list of players to only those matching a specific parameter value.

```javascript
// Get all players on the red team
SelectPlayers([Players], 'team', 'red');
```

```javascript
// Get all impostors
SelectPlayers([Players], 'impostor', 'true');
```

What it does:

* Returns a list of players whose parameter equals the specified value
* Only includes players that match exactly

***

### CountArray(list)

Counts the number of items in a list.

```javascript
// Count how many impostors are left
var impostorCount = CountArray(SelectPlayers([Players], 'impostor', 'true'));

if (impostorCount == 0.0) {
  SetTask('CrewmatesWin', 'Active', 0.0);
}
```

What it does:

* `SelectPlayers` gets all players where impostor is `'true'`
* `CountArray` counts how many players are in that list
* Returns a number (e.g., 2 if there are 2 impostors)

Common use: checking how many players have a specific role, counting team sizes, win condition logic.

***

### PrintString(value)

Prints a value to the console for debugging. Only visible in browser developer tools.

```javascript
PrintString(SelectPlayersParameters([Players], 'playerName'));
```

Common use: testing and debugging your code before going live.

***

### UpdateMultiplayerNumericVariable('variableName', value, operationType, delay)

Updates a multiplayer variable via the server, ensuring proper synchronization and tracking across all clients.

**Parameters:**
- `variableName` — Name of the multiplayer variable to update
- `value` — The number to use in the operation
- `operationType` — The type of operation (see table below)
- `delay` — Delay in seconds before the update (use decimals like `0.0`)

**Operation Types:**

| Type | Operation | Description |
|------|-----------|-------------|
| 0.0 | Set | Replace the current value |
| 1.0 | Add | Add to the current value |
| 2.0 | Subtract | Subtract from the current value |
| 3.0 | Multiply | Multiply the current value |
| 4.0 | Divide | Divide the current value |

**Important:** Use decimals (`0.0`, `1.0`, etc.) for all numeric values to avoid cast errors.

```javascript
// Set red team score to 10
UpdateMultiplayerNumericVariable('red', 10.0, 0.0, 0.0);
```

```javascript
// Add 5 to red team score
UpdateMultiplayerNumericVariable('red', 5.0, 1.0, 0.0);
```

```javascript
// Subtract 2 from red team score
UpdateMultiplayerNumericVariable('red', 2.0, 2.0, 0.0);
```

```javascript
// Multiply red team score by 2
UpdateMultiplayerNumericVariable('red', 2.0, 3.0, 0.0);
```

```javascript
// Divide red team score by 2
UpdateMultiplayerNumericVariable('red', 2.0, 4.0, 0.0);
```

#### When to use

Use `UpdateMultiplayerNumericVariable` instead of `SetVariable` for multiplayer variables when you need:
- Server-side validation and tracking
- Atomic operations (add/subtract/multiply/divide) that avoid race conditions
- Proper synchronization across all clients

Common use: team scores, shared resource pools, game state counters, any multiplayer variable that multiple players might update simultaneously.

***

## Multiplayer Examples

### Example 1: Impostor Assignment (Among Us style)

```javascript
// Make everyone a crewmate first
SetPlayersParameters([Players], 'impostor', false);

// Pick 2 random impostors
SetPlayersParameters(SelectRandomPlayers([Players], 2), 'impostor', true);
```

What it does:

1. Sets ALL players' `impostor` variable to false
2. Picks 2 random players
3. Sets their `impostor` to true

The result syncs to everyone. Use this on a game start trigger.

***

### Example 2: Team Assignment (Red vs Blue)

First, track how many players are ready to play using a multiplayer variable:

**Setup:**
- Create a multiplayer variable `PlayerCount` (initial value: 0)
- When a player enters the "ready" zone, increment: `SetVariable('PlayerCount', $N{PlayerCount} + 1.0, 0.0);`

**Then assign teams on game start:**

```javascript
// Everyone starts on blue
SetPlayersParameters([Players], 'team', 'blue');

// Half the players go to red
var halfCount = Math.floor($N{PlayerCount} / 2.0);
SetPlayersParameters(SelectRandomPlayers([Players], halfCount), 'team', 'red');
```

What it does:

1. Sets ALL players to blue team first
2. Calculates half the player count (rounded down)
3. Selects that many random players and switches them to red

This approach guarantees:
* Every player is on a team (no one left unassigned)
* Teams are balanced (or off by 1 if odd number of players)
* Works with any number of players

***

### Example 3: One Hunter, Everyone Else Hides

```javascript
SetPlayersParameters([Players], 'role', 'hider');
SetPlayersParameters(SelectRandomPlayers([Players], 1), 'role', 'hunter');
```

What it does:

1. Makes everyone a hider
2. Picks one random player to be the hunter

***

### Example 4: Conditional Role Assignment

```javascript
if ($N{ready} == 1.0) {
  SetPlayersParameters([Players], 'imposter', 'false');

  var numImposters = $N{impostersNeeded};
  SetPlayersParameters(SelectRandomPlayers([Players], numImposters), 'imposter', 'true');
}
```

What it does:

1. Checks if the triggering player's `ready` variable is 1
2. If ready, sets all players' `imposter` to false
3. Then picks a number of random players (based on `impostersNeeded` variable) and sets their `imposter` to true

Common use: only starting game logic when players have confirmed they're ready.

***

### Example 5: Win Condition Check

```javascript
var impostorsLeft = CountArray(SelectPlayers([Players], 'impostor', 'true'));
var crewLeft = CountArray(SelectPlayers([Players], 'alive', 'true'));

if (impostorsLeft == 0.0) {
  SetTask('CrewmatesWin', 'Active', 0.0);
} else if (impostorsLeft >= crewLeft) {
  SetTask('ImpostorsWin', 'Active', 0.0);
}
```

What it does:

1. Counts remaining impostors and living crew members
2. If no impostors left, crewmates win
3. If impostors outnumber or equal crew, impostors win

***

### Example 6: Print All Player Names (Debug)

```javascript
PrintString(SelectPlayersParameters([Players], 'playerName'));
```

What it does: outputs all player usernames to the console. Useful for testing before building your actual logic.

***

## Notes

* **One trigger, all clients:** When one player triggers a multiplayer function, the result propagates to everyone.
* **Order matters:** Later `SetPlayersParameters` calls can override earlier ones (see Team Assignment example).
* **Custom parameters:** You can use any variable name you've set up in the Variable system, not just built-in ones.
* **Nesting works:** You can use the output of one function as input to another (e.g., `SelectPlayersParameters(SelectRandomPlayers([Players], 3), 'playerName')`).
