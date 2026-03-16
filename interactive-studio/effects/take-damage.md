---
icon: explosion
description: 'Effect: Deals damage to a destructible object.'
---

# Take Damage

## Use Cases

***

* Damaging a destructible object when a player interacts with it
* Instantly destroying a destructible by setting damage equal to its max health
* Applying damage to destructibles from scripted events or traps

## Configuration

***

| Setting | Permitted Values | Description                                                                               |
| ------- | ---------------- | ----------------------------------------------------------------------------------------- |
| Damage  | Integer          | The amount of damage to deal. Set equal to the object's max health to destroy it instantly.|

## Compatibility

***

| Object Type   | Compatibility |
|---------------|:-------------:|
| Destructible  | ✅ |
