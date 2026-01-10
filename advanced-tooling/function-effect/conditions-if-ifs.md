# Conditions (if)

Conditions let you make decisions.

They answer questions like:

* "If coins are 10 or more, unlock the door"
* "If a task is completed, start the next task"
* "If health is 0, trigger game over"

The main tool is:

* if(...) for decisions (can be nested for multiple choices)

***

### About Task States

Before working with task conditions, remember:

* All tasks start as **NotActive** for new players
* **Tasks persist by default** - once changed, they stay in that state across sessions
* Tasks do NOT automatically reset to NotActive on their own
* To make a task reset on reload, enable "Non-Persistent" in task settings

This means checking `$T{myTask} == 'NotActive'` is how you detect "hasn't started yet" for both new and returning players (unless the task is non-persistent).

***

### if(condition, whenTrue, whenFalse)

#### Basic idea

if checks a condition.

* If the condition is true → it returns/does the whenTrue part
* If the condition is false → it returns/does the whenFalse part

#### Example: return true/false

```
if($N{coins} >= 10.0, true, false)
```

What it does:

* Returns true if coins are 10 or more
* Otherwise returns false

Most of the time you don’t need this wrapper, because:

```
$N{coins} >= 10.0
```

already returns true/false by itself.

***

### Using if to change something (common Portals pattern)

#### Example: if coins are 10+, unlock a door

```
if($N{coins} >= 10.0,
   SetVariable('doorUnlocked', 1.0, 0.0),
   0.0
)
```

What it does:

* If coins are 10 or more:
  * sets doorUnlocked to 1 immediately
* Otherwise:
  * does nothing

***

#### Example: if a task is completed, activate the next task

```
if($T{puzzle1} == 'Completed',
   SetTask('puzzle2', 'Active', 0.0),
   0.0
)
```

What it does:

* If puzzle1 is completed:
  * sets puzzle2 to Active immediately
* Otherwise:
  * does nothing

***

### Combining conditions inside if

#### Example: two tasks must be ready

```
if($T{task1} == 'Active' && $T{task2} == 'Completed',
   SetTask('alarm', 'Active', 0.0),
   0.0
)
```

What it does:

* Only activates alarm when:
  * task1 is Active
  * AND task2 is Completed

***

### Triggered conditions using OnChange

If you only want something to happen at the moment something changes (instead of checking every time), use OnChange(...) from Portals Specific Functions.

#### Example: when puzzle1 becomes Completed, unlock the door (once)

```
if(OnChange('puzzle1', 'Completed'),
   SetVariable('doorUnlocked', 1.0, 0.0),
   0.0
)
```

What it does:

* Only runs the unlock when puzzle1 changes into Completed (a “just happened” trigger)

***

#### Example: trigger when either change happens, but only when both states are true

```
if(
  (OnChange('task1', 'Active') || OnChange('task2', 'Completed'))
  && $T{task1} == 'Active'
  && $T{task2} == 'Completed',
  true,
  false
)
```

What it does:

* Triggers when task1 becomes Active OR task2 becomes Completed
* Then checks the current state of both tasks
* Returns true only when both are in the correct states

<br>

If you don’t need the if, you can write the clean boolean check:

```
(OnChange('task1', 'Active') || OnChange('task2', 'Completed'))
&& $T{task1} == 'Active'
&& $T{task2} == 'Completed'
```

***

### Nested if for Multiple Choices

#### Basic idea

For multiple conditions (like if/else if/else), nest your `if` statements.

The inner `if` goes in the `whenFalse` position of the outer `if`:

```
if(condition1,
   value1,
   if(condition2,
      value2,
      defaultValue
   )
)
```

It checks each condition in order:

* If condition 1 is true → it uses value 1
* Else if condition 2 is true → it uses value 2
* If none match → it uses the default value

#### Example: set a "warning level" based on health

```
if($N{health} <= 0.0,
   SetVariable('warningLevel', 3.0, 0.0),
   if($N{health} <= 3.0,
      SetVariable('warningLevel', 2.0, 0.0),
      if($N{health} <= 6.0,
         SetVariable('warningLevel', 1.0, 0.0),
         SetVariable('warningLevel', 0.0, 0.0)
      )
   )
)
```

What it does:

* If health is 0 or less → warningLevel = 3 (highest)
* Else if health is 3 or less → warningLevel = 2
* Else if health is 6 or less → warningLevel = 1
* Otherwise → warningLevel = 0

#### Example: NPC dialogue based on quest state

```
if($T{elderQuest} == 'NotActive',
   SetTask('dialogueOffer', 'Active', 0.0),
   if($T{elderQuest} == 'Active',
      if($N{hasAmulet} == 1.0,
         SetTask('dialogueTurnIn', 'Active', 0.0),
         SetTask('dialogueReminder', 'Active', 0.0)
      ),
      SetTask('dialogueComplete', 'Active', 0.0)
   )
)
```

What it does:

* If quest not started → show offer dialogue
* Else if quest is active:
  * If player has item → show turn-in dialogue
  * Otherwise → show reminder dialogue
* Else (quest completed) → show thank you dialogue

***

### Tips for readability (recommended)

#### 1) Put each condition on its own line

It’s easier to read and debug.

#### 2) Prefer $T{} for tasks in docs

It reads more clearly:

```
$T{door} == 'Active'
```

instead of:

```
$TN{door} == 1.0
```

#### 3) Use 0.0 for delays

```
SetTask('alarm', 'Active', 0.0)
SetVariable('coins', 10.0, 0.0)
```

***
