# Overview

### Javascript Function Effect

The Javascript Function effect lets you write JavaScript to control game logic in your Portals space. You can read and write game state — tasks, variables, timers — and use the full power of JavaScript for your logic.

#### What it's great for

* Writing game logic using standard JavaScript syntax
* Complex conditions with `if/else if/else`
* Loops, arrays, and string manipulation
* Multi-step logic that runs in sequence

#### The big idea

1. You write JavaScript code
2. Your code can read game state (tasks, variables, timers)
3. Your code can change game state (set tasks, set variables)
4. Actions can happen immediately or after a delay

***

### Quick examples

#### Set a variable

```javascript
SetVariable('coins', 10.0, 0.0);
```

What it does: sets `coins` to 10 immediately.

#### Set a task state

```javascript
SetTask('alarm', 'Active', 0.0);
```

What it does: sets the `alarm` task to Active immediately.

#### Conditional logic

```javascript
if ($N{coins} >= 10.0) {
  SetTask('shopUnlocked', 'Active', 0.0);
}
```

What it does: checks if coins are 10 or more, then activates the shop task.

#### Multiple actions in sequence

```javascript
SetVariable('coins', 0.0, 0.0);
SetTask('round1', 'Active', 0.0);
SetVariable('health', 100.0, 0.0);
```

What it does: resets coins to 0, activates round1, and sets health to 100.

***

### Key terms

#### Task

A named piece of progress with 3 states:

* `'NotActive'`
* `'Active'`
* `'Completed'`

#### Variable / Value

A named number like coins, score, health, doorUnlocked.

***

### What's next

In the next pages you'll learn:

* The Portals functions available in JavaScript (SetTask, SetVariable, reading game state)
* Multiplayer functions for working with multiple players
