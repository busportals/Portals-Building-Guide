# Multiplayer Functions

These functions let you work with players in multiplayer spaces. They're essential for games like team battles, role assignment (impostors, hunters), and any logic that needs to affect multiple players at once.

***

## Player Parameters

Before diving into functions, you need to know about player parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `[Players]` | List | All players currently in the room |
| `[Player]` | Single | The player who triggered the effect |

**Built-in player properties:**
- `playerName` - The player's username
- `health` - The player's health (default: 100, no max limit)

You can also use custom variables you've created in the Variable system.

***

### SelectRandomPlayers([Players], count)

Picks a random selection of players from a list.

Example:

```
SelectRandomPlayers([Players], 2)
```

What it does:

* Picks 2 random players from all players in the room
* Returns a list of player IDs

**Important:** This selection is:
- **Deterministic** - all clients get the same result
- **Persistent** - the same players stay selected even after reconnects

Common use: picking teams, assigning roles, choosing a "seeker" in hide and seek.

***

### SelectPlayersParameters([Players], 'parameterName')

Gets a parameter value from each player in a list.

Example:

```
SelectPlayersParameters([Players], 'health')
```

What it does:

* Returns a list of health values for all players
* Example result: [100, 85, 100, 50]

Example with nesting:

```
SelectPlayersParameters(SelectRandomPlayers([Players], 3), 'playerName')
```

What it does:

* Picks 3 random players
* Returns their usernames

***

### SetPlayersParameters([Players], 'parameterName', value)

Sets a parameter on all players in a list. Changes sync to all clients automatically.

Example:

```
SetPlayersParameters([Players], 'canMove', true)
```

What it does:

* Sets `canMove` to true for every player in the room

Common use: applying effects to all players, resetting values, setting up game state.

***

### PrintString(value)

Prints a value to the console for debugging. Only visible in browser developer tools.

Example:

```
PrintString(SelectPlayersParameters([Players], 'playerName'))
```

What it does:

* Prints the list of all player names to the console

Common use: testing and debugging your expressions before going live.

***

## Multiplayer Examples

### Example 1: Impostor Assignment (Among Us style)

```
SetPlayersParameters([Players], 'impostor', false) +
SetPlayersParameters(SelectRandomPlayers([Players], 2), 'impostor', true)
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
- When a player enters the "ready" zone, increment: `SetVariable('PlayerCount', $N{PlayerCount} + 1.0, 0.0)`

**Then assign teams on game start:**

```
SetPlayersParameters([Players], 'team', 'blue') +
SetPlayersParameters(SelectRandomPlayers([Players], Floor($N{PlayerCount} / 2.0)), 'team', 'red')
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

```
SetPlayersParameters([Players], 'role', 'hider') +
SetPlayersParameters(SelectRandomPlayers([Players], 1), 'role', 'hunter')
```

What it does:

1. Makes everyone a hider
2. Picks one random player to be the hunter

***

### Example 4: Damage All Players

```
SetPlayersParameters([Players], 'health', 50)
```

What it does:

* Sets everyone's health to 50

***

### Example 5: Print All Player Names (Debug)

```
PrintString(SelectPlayersParameters([Players], 'playerName'))
```

What it does:

* Outputs all player usernames to the console
* Useful for testing before building your actual logic

***

## Notes

* **One trigger, all clients:** When one player triggers a multiplayer function, the result propagates to everyone.
* **Order matters:** In chained expressions using `+`, later operations can override earlier ones (see Team Assignment example).
* **Custom parameters:** You can use any variable name you've set up in the Variable system, not just built-in ones.
* **Nesting works:** You can use the output of one function as input to another (see SelectPlayersParameters example with SelectRandomPlayers).
