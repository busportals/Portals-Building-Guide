---
icon: kaaba
---

# Trigger Cube

### Overview

The Trigger Cube activates events when a player enters or interacts with it. It can trigger actions like opening doors, giving items, playing sounds, or starting animations.

### Placement Settings

#### Trigger Settings Panel

* Press X to Activate – When enabled, players must press X to trigger the event instead of it activating automatically on entry
* Events – Click Add to assign one or more actions to be triggered (e.g., show message, teleport, change state)
* Custom Title – Optional label for organizing or identifying the trigger

### Important Behavior

> **Spawn/Load Limitation**: Trigger cubes only activate when a player **enters** the cube (crosses the boundary from outside). If a player spawns or loads into the game already inside a trigger cube, the trigger will NOT fire. Plan spawn point placement accordingly, or use alternative triggers (like Player Login) for logic that must run immediately when players join.

### Common Use Cases

* Trigger environmental changes or effects
* Activate puzzles, doors, or scripted sequences
* Distribute items or messages when players reach specific locations
