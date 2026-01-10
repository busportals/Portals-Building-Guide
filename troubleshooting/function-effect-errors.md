---
icon: code
description: Debug Function Effect expressions that aren't working
---

# Function Effect Errors

Function Effects use the NCalc expression language. Most issues come from syntax errors or type mismatches.

## Quick Checklist

Before diving into specific errors, verify these common requirements:

- [ ] **Decimal notation** - Use `0.0`, `1.0`, `50.0` (not `0`, `1`, `50`)
- [ ] **"Trigger on Task Change" checkbox** - Must be enabled for the Function Effect to run
- [ ] **Task/variable names** - Case-sensitive, must match exactly
- [ ] **Single quotes for strings** - Use `'Active'` not `"Active"`

---

## Error: Expression Not Executing

**Symptom:** Nothing happens when the trigger fires.

**Diagnostic Steps:**

1. **Is the trigger firing?**
   - Open Task Debug Panel (Space Options > Tasks Debug)
   - Trigger the action and watch for activity
   - If no activity, the issue is with your trigger, not the Function Effect

2. **Is "Trigger on Task Change" enabled?**
   - Edit the task containing the Function Effect
   - Scroll to the Function Effect settings
   - Ensure the checkbox is checked

3. **Check for syntax errors**
   - Look for mismatched parentheses
   - Verify all function calls have proper arguments
   - Check that operators are correct (`==` not `=` for comparison)

---

## Error: Type Cast / Cannot Convert

**Symptom:** Effect silently fails or produces unexpected results.

**Cause:** Mixing integers and decimals, or comparing wrong types.

**Fix:** Always use decimal notation for numbers.

```
// Wrong - causes type issues
SetVariable('coins', $N{coins} + 10, 0)
if($N{score} > 100, ...)

// Correct - use decimals
SetVariable('coins', $N{coins} + 10.0, 0.0)
if($N{score} > 100.0, ...)
```

---

## Error: Task Name Not Found

**Symptom:** `$T{taskName}` returns unexpected value or effect doesn't trigger.

**Cause:** Task name doesn't match exactly (spaces, capitalization).

**Fix:**
1. Open Space Options > Tasks
2. Copy the exact task name
3. Paste directly into your expression
4. Check for leading/trailing spaces

```
// If your task is named "Door Open"
$T{Door Open}     // Correct
$T{door open}     // Wrong - case matters
$T{DoorOpen}      // Wrong - space matters
```

---

## Error: Variable Not Updating

**Symptom:** `SetVariable` runs but value doesn't change.

**Diagnostic Steps:**

1. **Check Variable Manager**
   - Go to Space Options > Variable Manager
   - Find your variable
   - Verify current value

2. **Check persistence settings**
   - Is the variable set to Persistent when it shouldn't be?
   - Is it Multiplayer when you're testing solo?

3. **Verify the expression evaluates correctly**
   ```
   // Debug by setting a known value first
   SetVariable('testVar', 999.0, 0.0)
   ```

---

## Error: Condition Always True/False

**Symptom:** `if()` statement always takes the same branch.

**Common Causes:**

1. **Using assignment instead of comparison**
   ```
   // Wrong - this assigns, not compares
   if($N{coins} = 10.0, ...)

   // Correct - double equals for comparison
   if($N{coins} == 10.0, ...)
   ```

2. **Comparing wrong types**
   ```
   // Wrong - comparing number to string
   if($N{coins} == '10', ...)

   // Correct - compare number to number
   if($N{coins} == 10.0, ...)
   ```

3. **Checking task state with wrong syntax**
   ```
   // Wrong - $T returns string, can't use > or <
   if($T{quest} > 1, ...)

   // Correct - use $TN for numeric comparison
   if($TN{quest} > 1.0, ...)

   // Or compare strings properly
   if($T{quest} == 'Completed', ...)
   ```

---

## Error: OnChange Not Firing

**Symptom:** `OnChange()` trigger never activates.

**Diagnostic Steps:**

1. **Verify the value actually changes**
   - OnChange only fires when value transitions
   - Setting a value to its current value won't trigger

2. **Check the condition syntax**
   ```
   // Trigger on specific state
   OnChange('quest1', 'Completed')

   // Trigger on any state change
   OnChange('quest1')

   // Trigger on variable condition
   OnChange('coins', '>= 10')
   ```

3. **Ensure the Function Effect is on a task that's Active**
   - Function Effects only run when their parent task is Active

---

## Error: ifs() Not Working as Expected

**Symptom:** Wrong branch executes in `ifs()` statement.

**Known Issue:** `ifs()` has bugs in some cases. Use nested `if()` instead.

```
// Problematic - ifs() may not evaluate correctly
ifs(
  $N{health} <= 0.0, SetVariable('status', 3.0, 0.0),
  $N{health} <= 30.0, SetVariable('status', 2.0, 0.0),
                      SetVariable('status', 1.0, 0.0)
)

// Recommended - nested if()
if($N{health} <= 0.0,
   SetVariable('status', 3.0, 0.0),
   if($N{health} <= 30.0,
      SetVariable('status', 2.0, 0.0),
      SetVariable('status', 1.0, 0.0)
   )
)
```

---

## Debugging Tips

### Test in Isolation
Create a simple test case that only does one thing:
```
SetVariable('debug', 1.0, 0.0)
```
If this works, gradually add complexity.

### Use Display Value for Debugging
Add a Display Value effect to show variable values on screen while testing.

### Check the Order of Operations
Remember that expressions evaluate left-to-right. Use parentheses to control order:
```
// May not work as expected
$N{a} + $N{b} * $N{c}

// Clear order of operations
$N{a} + ($N{b} * $N{c})
```

### Common Operator Reference

| Operator | Purpose | Example |
|----------|---------|---------|
| `==` | Equals | `$N{coins} == 10.0` |
| `!=` | Not equals | `$T{door} != 'Active'` |
| `&&` | AND | `$N{a} > 0.0 && $N{b} > 0.0` |
| `\|\|` | OR | `$T{a} == 'Active' \|\| $T{b} == 'Active'` |
| `!` | NOT | `!($N{locked} == 1.0)` |
