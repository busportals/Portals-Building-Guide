---
icon: gun
---

# Guns

### Overview

Guns are interactive weapons that players can equip to deal damage to other players, Combat NPCs, and destructibles. Guns use hitscan mechanics for instant hit detection.

### Adding a Gun to Your Space

To add a gun to your space:

1. Open the building inventory
2. Navigate to the Guns category
3. Select a gun type (e.g., Shotgun)
4. Click to spawn the gun into your space
5. Position the gun where you want players to find it

Guns spawn with sensible default settings that you can customize in the placement settings panel.

### How Players Acquire Guns

Players can acquire guns in two ways:

* **Collision Pickup** – Walk over the gun to automatically pick it up (if "Can Collect By Collision" is enabled)
* **Equip Gun Effect** – Use a trigger and the Equip Gun effect to give players a gun programmatically

### Gun Behavior

* **Single Weapon** – Players can only hold one gun at a time. Picking up a new gun replaces the current one
* **Single Pickup** – When enabled, the gun disappears from the world after one player picks it up
* **Damage Targets** – Guns can damage other players, Combat NPCs, and destructibles

### Gun-Specific Triggers

Guns have dedicated triggers for building interactive experiences:

| Trigger | Description |
|---------|-------------|
| Gun Equipped | Fires when a player equips the gun |
| Gun Got Kill | Fires when a player kills another player with the gun |
| Gun Shot Hit | Fires when a shot hits a damageable target |
| Gun Started Aiming | Fires when a player starts aiming (right-click / left trigger) |
| Gun Stopped Aiming | Fires when a player stops aiming |
| Gun Tossed | Fires when a player drops or unequips the gun |

### Gun-Specific Effects

| Effect | Description |
|--------|-------------|
| Equip Gun | Gives the player the gun. Must be configured on the gun object itself |
| Toss Gun | Makes the player drop the gun (if Single Pickup) or unequip it |

### Available Gun Types

* [Pistol](pistol.md) – Versatile weapon
* [Rifle](rifle.md) – Weapon for various combat scenarios
* [Shotgun](shotgun.md) – Close-range weapon with spread projectiles
