# Portals Specific Functions

This page covers the Portals-specific features added on top of NCalc.

These additions let you:

* Read task states and values from Portals
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
$TN{alarm} == 1
```

What it does: checks if the alarm task is Active (because 1 means Active). Returns true or false.

***

#### $N{VariableName} (variable/value as number)

Returns the current value of a variable.

Example:

```
$N{coins} >= 10
```

What it does: checks if coins is 10 or more. Returns true or false.

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
SetVariable('coins', 0, 0.0)
```

What it does: sets coins to 0 immediately.

Example:

```
SetVariable('coins', $N{coins} + 10, 0.0)
```

What it does: reads the current coins, adds 10, then writes the new number back immediately.

Example:

```
SetVariable('health', $N{health} - 1, 0.0)
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
SetVariable('coins', $N{coins} + SelectRandom(1,2,3,4,5,6,7,8,9,10), 0.0)
```

What it does: picks a random number from 1 to 10, adds it to coins, then saves the result.

Example: random 50/50 (true or false)

```
SelectRandom(true, false)
```

What it does: returns true about half the time and false the other half.

Example: random reward amount

```
SetVariable('reward', SelectRandom(5, 10, 25, 50), 0.0)
```

What it does: sets reward to one of the provided numbers at random.

Example: random task state

```
SetTask('alarm', SelectRandom('NotActive', 'Active', 'Completed'), 0.0)
```

What it does: sets the alarm task to a random state.

Note: SelectRandom can include numbers, strings, variables, and full expressions. Make sure the result type matches what you’re doing (numbers for SetVariable, task state strings for SetTask).

***

### OnChange trigger

OnChange is used to react when something changes:

* A task changes state, or
* A variable changes value

Important:

* Use task names without the 1\_ prefix.

***

#### OnChange for tasks

**OnChange('taskName', 'TaskState')**

&#x20;**(only when it hits a specific state)**

Example:

```
OnChange('puzzle1', 'Completed')
```

What it does: becomes true at the moment puzzle1 changes into the Completed state. (It won’t be true forever — it’s a “just happened” trigger.)

**OnChange('taskName')**

&#x20;**(any state change)**

Example:

```
OnChange('questStep')
```

What it does: becomes true whenever questStep changes state (NotActive → Active, Active → Completed, etc).

***

#### OnChange for variables

**OnChange('variableName', logicalExpression)**

Example:

```
OnChange('coins', >= 10)
```

What it does: triggers when coins changes and meets the condition “10 or more”.

Example:

```
OnChange('health', == 0)
```

What it does: triggers when health changes and becomes exactly 0.

Example:

```
OnChange('speed', < 3)
```

What it does: triggers when speed changes and becomes less than 3.

***

### Common patterns (explained)

#### 1) When a task completes, set a variable

```
if(OnChange('puzzle1', 'Completed'),
   SetVariable('doorUnlocked', 1, 0.0),
   0
)
```

What it does:

* When puzzle1 becomes Completed, it sets doorUnlocked to 1 immediately.
* Otherwise it does nothing (returns 0).

***

#### 2) When coins reach 10+, complete a task

```
if(OnChange('coins', >= 10),
   SetTask('buyDoor', 'Completed', 0.0),
   0
)
```

What it does:

* When coins changes and is now 10 or more, it completes the buyDoor task immediately.
* Otherwise it does nothing.

***

#### 3) Trigger when either change happens, but only when both states are true

```
(OnChange('task1', 'Active') || OnChange('task2', 'Completed'))
&& $T{task1} == 'Active'
&& $T{task2} == 'Completed'
```

What it does:

* It triggers when either:
  * task1 becomes Active, or
  * task2 becomes Completed
* But it only returns true if _right now_ both are true:
  * task1 is Active
  * task2 is Completed



This is useful when you want “as soon as both conditions are satisfied, react”.

***

#### 4) React to any state change and pick a result based on the current state

```
if(OnChange('questStep'),
   ifs(
     $T{questStep} == 'NotActive', SetVariable('hintText', 0, 0.0),
     $T{questStep} == 'Active',    SetVariable('hintText', 1, 0.0),
                                   SetVariable('hintText', 2, 0.0)
   ),
   0
)
```

What it does:

* Whenever questStep changes state:
  * If it’s NotActive → set hintText to 0
  * If it’s Active → set hintText to 1
  * Otherwise (Completed) → set hintText to 2
* If questStep didn’t change, nothing happens.
