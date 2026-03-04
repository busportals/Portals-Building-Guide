# Portals Functions

This page covers the Portals functions available in the Javascript Function effect.

These let you:

* Read task states, variables, and timer values
* Set task states and variables (with an optional delay)
* Pick random values

All examples use single quotes for strings and end statements with `;`.

***

### About Task States

Before working with task conditions, remember:

* All tasks start as **NotActive** for new players
* **Tasks persist by default** — once changed, they stay in that state across sessions
* Tasks do NOT automatically reset to NotActive on their own
* To make a task reset on reload, enable "Non-Persistent" in task settings

This means checking `$T{myTask} == 'NotActive'` is how you detect "hasn't started yet" for both new and returning players (unless the task is non-persistent).

***

### Trigger on Tasks Change

When you enable the **Trigger on Tasks Change** toggle, the function will automatically run whenever any variable or task mentioned in your code changes value or state.

The system automatically detects which tasks and variables your function references and re-evaluates when any of them change.

```javascript
if ($T{puzzle1} == 'Completed') {
  SetVariable('doorUnlocked', 1.0, 0.0);
}
```

With **Trigger on Tasks Change** enabled:

* The function automatically runs whenever `puzzle1` changes state
* When `puzzle1` becomes Completed, it sets doorUnlocked to 1
* No need to manually trigger the function — the toggle handles it

***

### Activate on Start

When you enable the **Activate on Start** toggle, the function will run once when the player logs into the space.

Common uses:

* Initialize player variables on join
* Assign player to a team or role
* Set up starting game state
* Trigger welcome effects or spawn logic

***

### Read values from Portals

#### $T{taskName} (task state as text)

Returns the task's state as text:

* `'NotActive'`
* `'Active'`
* `'Completed'`

```javascript
// Check if a task is active
if ($T{alarm} == 'Active') {
  SetTask('response', 'Active', 0.0);
}
```

What it does: reads the alarm task's state and checks if it equals `'Active'`.

***

#### $TN{taskName} (task state as number)

Returns the task's state as a number:

* 0 = NotActive
* 1 = Active
* 2 = Completed

```javascript
if ($TN{alarm} == 1.0) {
  SetTask('response', 'Active', 0.0);
}
```

What it does: checks if the alarm task is Active (because 1 means Active).

***

#### $N{variableName} (variable/value as number)

Returns the current value of a variable.

```javascript
// Check if the player has enough coins
if ($N{coins} >= 10.0) {
  SetVariable('doorUnlocked', 1.0, 0.0);
}
```

What it does: reads the current coins value and checks if it's 10 or more.

***

#### Reading timer values

Timer values can be read using `$N{timerName}`. The timer must be started (using the Start Timer effect) before reading its value. Reading an unstarted timer returns 0.

```javascript
// Check if a timer has been running for 60 seconds
if ($N{RaceTimer} >= 60.0) {
  SetTask('timeUp', 'Active', 0.0);
}
```

```javascript
// Store half the timer value
SetVariable('HalfTime', $N{RaceTimer} / 2.0, 0.0);
```

```javascript
// Calculate remaining time from a 2-minute limit
SetVariable('TimeRemaining', 120.0 - $N{CountdownTimer}, 0.0);
```

Timer variables are useful for:

* Creating time-based scoring (faster = more points)
* Setting up time bonuses or penalties
* Storing checkpoint times
* Calculating elapsed time between events

***

### Change tasks and variables

#### SetTask('taskName', 'TaskState', delay)

Sets a task to a new state. Use state names, not numbers.

Accepted TaskState values: `'NotActive'`, `'Active'`, `'Completed'`

```javascript
// Set a task immediately
SetTask('alarm', 'Active', 0.0);
```

```javascript
// Set a task after a 2 second delay
SetTask('puzzle1', 'Completed', 2.0);
```

```javascript
// Reset a task after 5 seconds
SetTask('alarm', 'NotActive', 5.0);
```

***

#### SetVariable('variableName', value, delay)

Sets a variable to a target number, optionally after a delay.

```javascript
// Set coins to 0 immediately
SetVariable('coins', 0.0, 0.0);
```

```javascript
// Add 10 to coins
SetVariable('coins', $N{coins} + 10.0, 0.0);
```

```javascript
// Subtract 1 health
SetVariable('health', $N{health} - 1.0, 0.0);
```

#### Number types (important)

Use `0.0` instead of `0` to avoid number type errors.

Rule of thumb:

* Use `0.0` / `1.0` / `10.0` in SetVariable values and delays
* Use decimal values for delays (`0.0`, `2.0`)

```javascript
// Good
SetVariable('Player_Team', 1.0, 0.0);

// Avoid — can cause cast errors
SetVariable('Player_Team', 1, 0.0);
```

***

### Random selection

#### SelectRandom(item1, item2, item3, ...)

Picks one item at random from the list you provide.

```javascript
// Add a random number (1–10) to coins
SetVariable('coins', $N{coins} + SelectRandom(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0), 0.0);
```

```javascript
// Random reward amount
SetVariable('reward', SelectRandom(5.0, 10.0, 25.0, 50.0), 0.0);
```

```javascript
// Random task state
SetTask('alarm', SelectRandom('NotActive', 'Active', 'Completed'), 0.0);
```

SelectRandom can include numbers, strings, variables, and expressions. Make sure the result type matches what you're doing (numbers for SetVariable, task state strings for SetTask).

***

### Common patterns

#### 1) When a task completes, set a variable

```javascript
if ($T{puzzle1} == 'Completed') {
  SetVariable('doorUnlocked', 1.0, 0.0);
}
```

#### 2) When coins reach 10+, complete a task

```javascript
if ($N{coins} >= 10.0) {
  SetTask('buyDoor', 'Completed', 0.0);
}
```

#### 3) React when both conditions are met

```javascript
if ($T{task1} == 'Active' && $T{task2} == 'Completed') {
  SetTask('reward', 'Active', 0.0);
}
```

#### 4) Multiple choices based on state

```javascript
if ($T{questStep} == 'NotActive') {
  SetVariable('hintText', 0.0, 0.0);
} else if ($T{questStep} == 'Active') {
  SetVariable('hintText', 1.0, 0.0);
} else {
  SetVariable('hintText', 2.0, 0.0);
}
```

#### 5) Warning level based on health

```javascript
if ($N{health} <= 0.0) {
  SetVariable('warningLevel', 3.0, 0.0);
} else if ($N{health} <= 3.0) {
  SetVariable('warningLevel', 2.0, 0.0);
} else if ($N{health} <= 6.0) {
  SetVariable('warningLevel', 1.0, 0.0);
} else {
  SetVariable('warningLevel', 0.0, 0.0);
}
```

#### 6) NPC dialogue based on quest state

```javascript
if ($T{elderQuest} == 'NotActive') {
  SetTask('dialogueOffer', 'Active', 0.0);
} else if ($T{elderQuest} == 'Active') {
  if ($N{hasAmulet} == 1.0) {
    SetTask('dialogueTurnIn', 'Active', 0.0);
  } else {
    SetTask('dialogueReminder', 'Active', 0.0);
  }
} else {
  SetTask('dialogueComplete', 'Active', 0.0);
}
```

What it does:

* If quest not started — show offer dialogue
* If quest is active and player has item — show turn-in dialogue
* If quest is active but no item — show reminder dialogue
* If quest completed — show thank you dialogue

#### 7) Cooldown pattern (do something now, undo it later)

```javascript
SetTask('alarm', 'Active', 0.0);
SetTask('alarm', 'NotActive', 5.0);
```

What it does: activates the alarm immediately, then deactivates it after 5 seconds. Useful for timers and cooldowns.

#### 8) Cap and clamp values

```javascript
// Prevent health from going below 0
var newHealth = $N{health} - 1.0;
if (newHealth < 0.0) {
  newHealth = 0.0;
}
SetVariable('health', newHealth, 0.0);
```

```javascript
// Cap coins at 999
if ($N{coins} > 999.0) {
  SetVariable('coins', 999.0, 0.0);
}
```

#### 9) Shop / purchase logic

```javascript
var price = 50.0;

if ($N{coins} >= price && $T{shopOpen} == 'Active') {
  SetVariable('coins', $N{coins} - price, 0.0);
  SetTask('itemPurchased', 'Completed', 0.0);
}
```

What it does:

* Checks the player has enough coins AND the shop is open
* Deducts the price from coins
* Marks the purchase as completed

#### 10) Game over when health hits 0

With **Trigger on Tasks Change** enabled:

```javascript
if ($N{health} <= 0.0 && $T{gameOver} == 'NotActive') {
  SetTask('gameOver', 'Active', 0.0);
  SetVariable('finalScore', $N{score}, 0.0);
}
```

What it does:

* Runs automatically when health changes
* If health is 0 or below and game over hasn't already triggered, activates game over
* Saves the player's current score as their final score

#### 11) Round management with reset

```javascript
// Start a new round
SetVariable('roundKills', 0.0, 0.0);
SetVariable('health', 100.0, 0.0);
SetTask('roundActive', 'Active', 0.0);

// End the round after 60 seconds
SetTask('roundActive', 'NotActive', 60.0);
```

What it does: resets kills and health, activates the round, then automatically ends it after 60 seconds.

#### 12) Score multiplier based on streak

```javascript
var streak = $N{streak};
var basePoints = 10.0;
var multiplier = 1.0;

if (streak >= 10.0) {
  multiplier = 3.0;
} else if (streak >= 5.0) {
  multiplier = 2.0;
} else if (streak >= 3.0) {
  multiplier = 1.5;
}

SetVariable('score', $N{score} + (basePoints * multiplier), 0.0);
```

What it does: awards more points for longer streaks — 1.5x at 3 streak, 2x at 5, 3x at 10.

#### 13) Initialize player on join

With **Activate on Start** enabled:

```javascript
SetVariable('health', 100.0, 0.0);
SetVariable('coins', 0.0, 0.0);
SetVariable('score', 0.0, 0.0);
SetTask('welcomeMessage', 'Active', 0.0);
SetTask('welcomeMessage', 'NotActive', 5.0);
```

What it does: sets up starting values when a player joins and shows a welcome message for 5 seconds.

#### 14) Time-based scoring

```javascript
// Award points based on how fast the player finished
var timeLimit = 120.0;
var elapsed = $N{RaceTimer};
var timeBonus = timeLimit - elapsed;

if (timeBonus < 0.0) {
  timeBonus = 0.0;
}

SetVariable('score', $N{score} + timeBonus, 0.0);
```

What it does: gives more points for finishing faster. If the player took longer than 2 minutes, no bonus.
