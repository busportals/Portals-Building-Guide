# Portals Specific Functions

This page covers the Portals-specific features added on top of NCalc.

These additions let you:

* Read task states, values, and timer values from Portals
* React when a task or value changes
* Set task states and values (with an optional delay)

All examples use single quotes.

***

### Read values from Portals

#### $T{taskName} (task state as text)

Returns the task’s state as text:

* 'NotActive'
* 'Active'
* 'Completed'

Example:

```
$T{alarm} == 'Active'
```

What it does: checks if the alarm task is currently Active. Returns true or false.

***

#### $TN{taskName} (task state as number)

Returns the task’s state as a number:

* 0 = NotActive
* 1 = Active
* 2 = Completed

Example:

```
$TN{alarm} == 1.0
```

What it does: checks if the alarm task is Active (because 1 means Active). Returns true or false.

***

#### $N{VariableName} (variable/value as number)

Returns the current value of a variable.

Example:

```
$N{coins} >= 10.0
```

What it does: checks if coins is 10 or more. Returns true or false.

***

#### $N{TimerName} (timer value as number)

Returns the current elapsed time of a running timer as a number (in seconds).

Example:

```
$N{RaceTimer} >= 60.0
```

What it does: checks if the timer named RaceTimer has been running for 60 seconds or more. Returns true or false.

You can use timer values in calculations and store the results in variables:

Example:

```
SetVariable('HalfTime', $N{RaceTimer} / 2.0, 0.0)
```

What it does: takes the current timer value, divides it by 2, and stores the result in the HalfTime variable immediately.

Example:

```
SetVariable('BonusTime', $N{RaceTimer} + 30.0, 0.0)
```

What it does: takes the current timer value, adds 30 seconds, and stores the result in the BonusTime variable.

Example:

```
SetVariable('TimeRemaining', 120.0 - $N{CountdownTimer}, 0.0)
```

What it does: calculates how much time is left from a 2-minute limit by subtracting the elapsed time.

Timer variables are useful for:

* Creating time-based scoring (faster = more points)
* Setting up time bonuses or penalties
* Storing checkpoint times
* Calculating elapsed time between events

Note: The timer must be started (using the Start Timer effect) before reading its value. Reading an unstarted timer returns 0.

***

### Change tasks and variables

#### SetTask

Sets a task to a new state. Use state names, not numbers.

Syntax

```
SetTask('taskName', 'TaskState', delaySeconds)
```

Accepted TaskState values:

* 'NotActive'
* 'Active'
* 'Completed'

Example:

```
SetTask('alarm', 'Active', 0.0)
```

What it does: sets the alarm task to Active immediately.

Example:

```
SetTask('puzzle1', 'Completed', 2.0)
```

What it does: waits 2 seconds, then marks puzzle1 as Completed.

Example:

```
SetTask('alarm', 'NotActive', 5.0)
```

What it does: waits 5 seconds, then sets alarm back to NotActive.

***

#### SetVariable

Sets a variable/value to a target number (optionally after a delay).

Syntax

```
SetVariable('variableName', targetValue, delaySeconds)
```

Example:

```
SetVariable('coins', 0.0, 0.0)
```

What it does: sets coins to 0 immediately.

#### Number types (important)

Use 0.0 instead of 0 to avoid number type errors.

Rule of thumb:

* Use 0.0 / 1.0 / 10.0 in comparisons, SetVariable, and if(...) branches.
* Use decimal values for delays (0.0, 2.0).
* When using SelectRandom for SetVariable, prefer decimal lists (1.0, 2.0, ...) so the result is a Double.

Before (causes cast error):

```
if($N{Player_Team} == 0,
   SetVariable('Player_Team', 1, 0.0),
   0
)
```

After (works):

```
if($N{Player_Team} == 0.0,
   SetVariable('Player_Team', 1.0, 0.0),
   0.0
)
```

Example:

```
SetVariable('coins', $N{coins} + 10.0, 0.0)
```

What it does: reads the current coins, adds 10, then writes the new number back immediately.

Example:

```
SetVariable('health', $N{health} - 1.0, 0.0)
```

What it does: subtracts 1 from health immediately.

Tip: write delays as 0.0, 1.5, 2.0 (not 0, 2) to avoid number type issues.

***

### Random selection

#### SelectRandom

SelectRandom picks one item at random from the list you provide.

Syntax

```
SelectRandom(item1, item2, item3, ...)
```

What it does: returns one of the provided items at random.

Example: add a random number (1–10) to coins

```
SetVariable('coins', $N{coins} + SelectRandom(1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0), 0.0)
```

What it does: picks a random number from 1 to 10, adds it to coins, then saves the result.

Example: random 50/50 (true or false)

```
SelectRandom(true, false)
```

What it does: returns true about half the time and false the other half.

Example: random reward amount

```
SetVariable('reward', SelectRandom(5.0, 10.0, 25.0, 50.0), 0.0)
```

What it does: sets reward to one of the provided numbers at random.

Example: random task state

```
SetTask('alarm', SelectRandom('NotActive', 'Active', 'Completed'), 0.0)
```

What it does: sets the alarm task to a random state.

Note: SelectRandom can include numbers, strings, variables, and full expressions. Make sure the result type matches what you’re doing (numbers for SetVariable, task state strings for SetTask).

***

### Trigger on Tasks Change

When you enable the **Trigger on Tasks Change** toggle, the function will automatically evaluate whenever any variable or task mentioned in your expression changes value or state.

This replaces the need for manually wrapping expressions in OnChange checks. The system automatically detects which tasks and variables your function references and re-evaluates when any of them change.

Example:

```
if($T{puzzle1} == 'Completed',
   SetVariable('doorUnlocked', 1.0, 0.0),
   0.0
)
```

With **Trigger on Tasks Change** enabled:

* The function automatically runs whenever `puzzle1` changes state
* When `puzzle1` becomes Completed, it sets doorUnlocked to 1
* No need to wrap in OnChange — the toggle handles it

***

### Activate on Start

When you enable the **Activate on Start** toggle, the function will evaluate once when the player logs into the space. This is equivalent to having **Trigger on Tasks Change** checked on player login.

Common uses:

* Initialize player variables on join
* Assign player to a team or role
* Set up starting game state
* Trigger welcome effects or spawn logic

***

### Common patterns (explained)

#### 1) When a task completes, set a variable

With **Trigger on Tasks Change** enabled:

```
if($T{puzzle1} == 'Completed',
   SetVariable('doorUnlocked', 1.0, 0.0),
   0.0
)
```

What it does:

* The function runs automatically when puzzle1 changes state
* If puzzle1 is Completed, it sets doorUnlocked to 1 immediately
* Otherwise it does nothing (returns 0)

***

#### 2) When coins reach 10+, complete a task

With **Trigger on Tasks Change** enabled:

```
if($N{coins} >= 10.0,
   SetTask('buyDoor', 'Completed', 0.0),
   0.0
)
```

What it does:

* The function runs automatically when coins changes value
* If coins is 10 or more, it completes the buyDoor task immediately
* Otherwise it does nothing

***

#### 3) React when both conditions are satisfied

With **Trigger on Tasks Change** enabled:

```
if($T{task1} == 'Active' && $T{task2} == 'Completed',
   SetTask('reward', 'Active', 0.0),
   0.0
)
```

What it does:

* The function runs whenever task1 or task2 changes
* If both conditions are true (task1 is Active AND task2 is Completed), it activates the reward task
* This pattern is useful for "unlock when multiple conditions are met" scenarios

***

#### 4) Pick a result based on current state

With **Trigger on Tasks Change** enabled:

```
ifs(
  $T{questStep} == 'NotActive', SetVariable('hintText', 0.0, 0.0),
  $T{questStep} == 'Active',    SetVariable('hintText', 1.0, 0.0),
                                SetVariable('hintText', 2.0, 0.0)
)
```

What it does:

* The function runs whenever questStep changes state
* Sets hintText based on the current state:
  * NotActive → hintText = 0
  * Active → hintText = 1
  * Completed → hintText = 2
