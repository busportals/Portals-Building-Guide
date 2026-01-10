# Overview

### Function Effect

Function Effector lets you write a short expression that can:

* Read task states (like Not Active / Active / Completed)
* Read values/variables (like coins, score, health)
* Do math and logic (like +, >, and, or)
* Make decisions with if statements
* Optionally set a task state or variable (immediately or after a delay)

#### What it’s based on

The Function Effect is based on the [NCalc](https://ncalc.github.io/ncalc/articles/index.html) expression language. That means you can write expressions like a tiny calculator, but with extra game-friendly features.

#### The big idea

Think of it like this:

1. You write an expression
2. The expression can check game state (tasks + values)
3. The expression returns a result (true/false, number, or text)
4. Optionally, the expression can also _cause changes_ (set tasks/values)

#### What it’s great for

* Opening a door when two things are done
* Changing a value when a task reaches a certain step
* Setting a cooldown (do something now, undo it a few seconds later)
* Turning complex logic into one reusable “effect”

***

### Quick examples

#### Check if two tasks are in the right states

This only checks current state (no trigger). It returns true or false.

```
$T{task1} == 'Active' && $T{task2} == 'Completed'
```

What it does:

* Reads task1 state and checks if it is 'Active'
* Reads task2 state and checks if it is 'Completed'
* Returns true only if both are correct

This is a pure “check” (it doesn’t change anything).

#### If a task is completed, set a variable

```
if($T{puzzle1} == 'Completed',
   SetVariable('doorUnlocked', 1.0, 0.0),
   0.0
)
```

What it does:

* Checks if puzzle1 is currently 'Completed'
* If yes: sets doorUnlocked to 1 immediately
* If no: does nothing (returns 0)

This is a common pattern: “if something is done, unlock something”.

#### Set a task state

When setting a task, use the state name (not a number).

```
SetTask('alarm', 'Active', 0.0)
```

What it does:

* Sets the task named alarm to 'Active'
* The 0.0 means “no delay” (do it right now)

#### Do something after a delay

```
SetTask('alarm', 'NotActive', 5.0)
```

What it does:

* Waits 5 seconds
* Then sets alarm back to 'NotActive'

This is useful for timers and cooldowns.

***

### Key terms

#### Task

A named piece of progress with 3 states:

* 'NotActive'
* 'Active'
* 'Completed'

#### Variable / Value

A named number like coins, score, health, doorUnlocked.

#### Expression

A short line that can calculate something or check a condition.

***

### What’s next

In the next pages you’ll learn:

* The Portals-only additions (special task/value reads, SetTask, SetVariable, OnChange)
* How to write readable if statements
* The most common operators and functions you’ll use in expressions
