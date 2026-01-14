---
icon: gun
---

# Shotgun

### Overview

The Shotgun is a close-range weapon that fires multiple projectiles in a spread pattern. It uses hitscan mechanics for instant hit detection. Despite firing multiple projectiles, all pellets from a single shot count as one damage instance.

### Damage Settings

#### Damage Falloff

The shotgun's damage varies based on distance from the target:

```
Damage
  ▲
  │ ┌─────────┐
  │ │ MAX DMG │  Linear     ┌─────────┐
  │ │ (const) │  Falloff    │ MIN DMG │
  │ └─────────┴─────────────┴─────────┴──── 0 damage
  │           │             │         │
  └───────────┴─────────────┴─────────┴────► Distance
  0      Min Dmg      Max Dmg       Max
         Distance     Distance     Range
```

* **0 to Min Damage Distance** – Deals Max Damage (constant)
* **Min Damage Distance to Max Damage Distance** – Damage falls off linearly from Max to Min
* **Max Damage Distance to Max Range** – Deals Min Damage (constant)
* **Beyond Max Range** – Deals 0 damage

#### Shotgun Settings Panel

* Max Damage – The maximum damage dealt at close range (within min damage distance)
* Min Damage – The minimum damage dealt at long range (beyond max damage distance)
* Min Damage Distance – Distance where max damage starts falling off (0-100)
* Max Damage Distance – Distance where damage reaches minimum (0-100)
* Fire Rate – Time between each shot in seconds (0.01-2)
* Projectiles Per Shot – Number of projectiles fired per shot (1-20). All projectiles count as a single hit
* Dispersion – Spread angle in degrees (0-90). Higher values create wider spread patterns

### Ammo Settings

* Infinite Ammo – Unlimited ammo, no reloading required
* Infinite Reserve Ammo – Unlimited reserve ammo pool
* Starting Reserve Ammo – Amount of reserve ammo the player starts with (0-500). Only available if Infinite Reserve Ammo is off
* Clip Size – Magazine capacity (1-100). Only available if Infinite Ammo is off
* Start Loaded – Gun spawns with a full clip. Only available if Infinite Ammo is off
* Reload Time – Time to reload in seconds (0.1-5). Only available if Infinite Ammo is off
* Auto Reload – Automatically reloads when the clip is empty. Only available if Infinite Ammo is off
* Combine Ammo – Collected ammo goes directly into the clip instead of reserve. Eliminates the need to reload
* Reload One By One – When enabled, loads shells individually (can interrupt to fire). When disabled, reloads the full clip at once

### Weapon Behaviour

* Max Range – Maximum distance projectiles can travel (0-200). Beyond this distance, shots deal no damage

### Recoil & Camera

* Camera Stability – How steady the camera remains when firing (0-1). 0 is unstable, 1 is fully stable
* Recoil Right – Horizontal camera kick to the right (-5 to 5)
* Recoil Left – Horizontal camera kick to the left (-5 to 5)
* Recoil Up – Vertical camera kick upward (-5 to 5)

### UI Settings

* Show Crosshair – Display the aiming crosshair
* Shot Hitmarkers – Show visual feedback when shots connect
* Display Ammo Count – Show current ammo count in the UI
* Reserve Ammo Label – Variable name for reserve ammo. This name can be used with the Variable Manager and Function Effect for custom logic

### Gun Collection Settings

* Can Collect By Collision – Players can pick up the gun by walking over it
* Single Pickup – Only one player can pick up this gun. The gun disappears from the world after pickup

### Common Use Cases

* Arena shooter games with weapon pickups
* Survival games requiring ammo management
* Tower defense with player-controlled weapons
* PvP combat zones
* Boss fights against Combat NPCs
