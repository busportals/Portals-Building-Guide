---
icon: gun
description: 'Effect: Give a player a gun.'
---

# Equip Gun

## Use Cases

***

* Give players weapons at game start
* Reward players with weapons for completing objectives
* Create weapon pickup zones without collision detection
* Programmatically arm players during events

## Configuration

***

No additional configuration beyond the base configuration parameters. This effect gives the player the gun that the effect is attached to.

> **Note**: The Equip Gun effect must be configured on the gun object itself. When triggered, it equips that specific gun to the player.

## Compatibility

***

| Object Type | Compatibility |
|-------------|:-------------:|
| Gun | ✅ |
