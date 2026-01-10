# Expressions (the basics)

This page explains the basic building blocks you’ll use inside Function Effect expressions.

***

### 1) Numbers

Numbers are used for things like coins, score, health, timers, and calculations.

Examples:

```
10.0
3.5
0.0
```

What they do:

* 10.0 is ten
* 3.5 is three and a half
* 0.0 is zero (we recommend using decimals for delays like 0.0, 1.5, 2.0)

***

### 2) Text (strings)

Text values must be wrapped in single quotes.

Examples:

```
'Active'
'Completed'
'coins'
```

What they do:

* 'Active' is a piece of text (not a task)
* 'coins' is text (not the variable value)

Common use:

```
$T{alarm} == 'Active'
```

What it does: checks if the alarm task state text equals 'Active'.

***

### 3) True / False (booleans)

Some expressions return true or false.

Examples:

```
$N{coins} >= 10.0
$T{task1} == 'Completed'
```

What they do:

* $N{coins} >= 10.0 is true when coins is 10 or more
* $T{task1} == 'Completed' is true when task1 is completed

***

### 4) Parentheses (grouping)

Parentheses control the order things happen in, and make logic easier to read.

Example:

```
($N{coins} >= 10.0) && ($T{questStep} == 'Active')
```

What it does:

* First checks coins >= 10.0
* Also checks questStep is Active
* Returns true only if both are true

***

### 5) Common comparisons

You’ll often compare numbers or text:

#### Number comparisons

```
$N{coins} > 0.0
$N{health} <= 10.0
```

What they do:

* coins is greater than 0
* health is 10 or less

#### Text comparisons

```
$T{alarm} == 'Active'
$T{questStep} != 'NotActive'
```

What they do:

* alarm is Active
* questStep is anything except NotActive

***

### 6) Combining conditions (and/or)

#### AND (both must be true)

```
$T{task1} == 'Active' && $T{task2} == 'Completed'
```

What it does: true only if both states match.

#### OR (either can be true)

```
$T{task1} == 'Completed' || $T{task2} == 'Completed'
```

What it does: true if either task is completed.

***

### 7) Quick Portals-friendly examples

#### Example: check if the player can open a door

```
$N{keys} >= 1.0 && $T{doorTask} == 'Active'
```

What it does:

* Player has at least 1 key
* The door task is Active
* Returns true when the door should be allowed to open

#### Example: basic math using a variable

```
$N{coins} + 5.0
```

What it does:

* Takes current coins
* Adds 5
* Returns the result number

(If you want to actually store it, you’d use SetVariable on the [Portals Specific Functions page](portals-specific-functions.md).)
