---
icon: gun
description: 'Effect: Make a player drop or unequip their gun.'
---

# Toss Gun

## Use Cases

***

* Disarm players when entering safe zones
* Force weapon drops on death or respawn
* Create "drop your weapon" mechanics
* End armed states for cutscenes or events

## Configuration

***

No additional configuration beyond the base configuration parameters.

## Behavior

***

* If the gun has **Single Pickup** enabled, the player drops the gun on the ground where other players can potentially pick it up
* If **Single Pickup** is disabled, the gun is simply unequipped (removed from the player's hands)

## Compatibility

***

| Object Type | Compatibility |
|-------------|:-------------:|
| Gun | ✅ |
