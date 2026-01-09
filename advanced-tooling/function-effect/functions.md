# Functions

Functions are built-in helpers you can use inside expressions. They save you from doing extra math or complicated logic.

You’ll usually use functions to:

* Clamp values (keep them in a range)
* Round numbers
* Pick the smallest/largest value
* Do simple “math helpers” like absolute value

***

### Min(a, b)

Returns the smaller of two numbers.

Example:

```
Min($N{coins}, 100)
```

What it does:

* If coins is bigger than 100, it returns 100
* If coins is less than 100, it returns coins

Common use: cap a value so it never goes above something.

***

### Max(a, b)

Returns the larger of two numbers.

Example:

```
Max($N{health}, 0)
```

What it does:

* If health goes negative, it returns 0
* Otherwise it returns health

Common use: prevent values from going below 0.

***

### Round(number)

Rounds to the nearest whole number.

Example:

```
Round($N{speed})
```

What it does:

* If speed is 3.6 → becomes 4
* If speed is 3.4 → becomes 3

***

### Abs(number)

Returns the absolute value (distance from 0).

Example:

```
Abs($N{temperature})
```

What it does:

* If temperature is -5 → returns 5
* If temperature is 5 → returns 5

***

### Floor(number)

Rounds down.

Example:

```
Floor(3.9)
```

What it does:

* Returns 3

***

### Ceiling(number)

Rounds up.

Example:

```
Ceiling(3.1)
```

What it does:

* Returns 4

***

### Sqrt(number)

Square root.

Example:

```
Sqrt(9)
```

What it does:

* Returns 3

***

### Using functions with SetVariable (common patterns)

#### 1) Cap coins at 999

```
SetVariable('coins', Min($N{coins}, 999), 0.0)
```

What it does:

* If coins is above 999, it sets coins to 999
* Otherwise it keeps coins the same

#### 2) Prevent health from going below 0

```
SetVariable('health', Max($N{health} - 1, 0), 0.0)
```

What it does:

* Subtracts 1 health
* If that would go below 0, it sets it to 0 instead

#### 3) Round a value before saving it

```
SetVariable('speed', Round($N{speed}), 0.0)
```

What it does:

* Rounds speed to a whole number and saves it

***

### if + functions together

#### Example: if coins are too high, cap them

```
if($N{coins} > 999,
   SetVariable('coins', 999, 0.0),
   0
)
```

What it does:

* If coins are over 999, set them back to 999
* Otherwise do nothing

You can also do this in one line using Min (from above), which is usually cleaner.

***

### Notes

* Functions always use parentheses: Min(1, 2)
* You can nest functions (use a function inside another function) if needed:

```
Min(Max($N{health}, 0), 100)
```

* What it does:
  * First prevents health from going below 0
  * Then prevents it from going above 100
