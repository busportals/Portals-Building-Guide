# Operators

Operators are the symbols that let you do math and logic in Function Effect expressions.

You’ll mostly use these for:

* Doing math with values (coins, score, health)
* Comparing values (greater than, equal to)
* Combining conditions (and/or)

***

### Math operators

These return a number.

#### Add and subtract

```
$N{coins} + 10.0
$N{health} - 1.0
```

What they do:

* Adds 10 to the current coins value
* Subtracts 1 from the current health value

#### Multiply and divide

```
$N{score} * 2.0
$N{timeLeft} / 2.0
```

What they do:

* Doubles score
* Halves timeLeft

#### Remainder (mod)

```
$N{coins} % 2.0
```

What it does:

* Returns the remainder after dividing by 2
* Useful for checking “even or odd”
  * If result is 0.0, it’s even
  * If result is 1.0, it’s odd

#### Exponent (power)

```
2.0 ** 3.0
```

What it does:

* 2 to the power of 3 = 8

***

### Comparison operators

Comparison operators return true or false.

#### Equal / not equal

```
$N{coins} == 10.0
$T{questStep} != 'NotActive'
```

What they do:

* Checks if coins is exactly 10
* Checks if questStep is anything except NotActive

Tip: For text checks, use single quotes:

```
$T{alarm} == 'Active'
```

#### Greater / less than

```
$N{coins} > 10.0
$N{health} < 5.0
```

What they do:

* Checks if coins is more than 10
* Checks if health is less than 5

#### Greater/less than or equal

```
$N{coins} >= 10.0
$N{health} <= 0.0
```

What they do:

* Checks if coins is 10 or more
* Checks if health is 0 or less

***

### Logic operators (AND / OR / NOT)

These combine true/false checks.

#### AND (&&)

Both sides must be true.

```
$T{task1} == 'Active' && $T{task2} == 'Completed'
```

What it does:

* True only when task1 is Active AND task2 is Completed

#### OR (||)

Either side can be true.

```
$T{task1} == 'Completed' || $T{task2} == 'Completed'
```

What it does:

* True when task1 is completed OR task2 is completed

#### NOT (!)

Flips true/false.

```
!($T{alarm} == 'Active')
```

What it does:

* True when alarm is NOT Active

***

### Parentheses (highly recommended)



Parentheses make your logic clear and avoid surprises.

Example:

```
($N{coins} >= 10.0 && $T{doorTask} == 'Active') || $T{adminOverride} == 'Completed'
```

What it does:

* True if:
  * coins >= 10.0 AND doorTask is Active
  * OR adminOverride is Completed

***

### Common “game logic” examples

#### Example: can the player buy an item?

```
$N{coins} >= 50.0 && $T{shopOpen} == 'Active'
```

What it does:

* Player has at least 50 coins
* Shop is open (Active)
* Returns true when buying should be allowed

#### Example: low health warning

```
$N{health} <= 3.0
```

What it does:

* Returns true when health is 3 or lower

#### Example: only allow once (simple check)

```
$T{rewardClaimed} != 'Completed'
```

What it does:

* Returns true if the reward has NOT been claimed yet

(Then you’d usually set rewardClaimed to Completed using SetTask from the [Portals Specific Functions page](portals-specific-functions.md).)
