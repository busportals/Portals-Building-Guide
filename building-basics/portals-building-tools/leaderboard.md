---
icon: medal
---

# Leaderboard

## Overview

The Leaderboard tool displays player scores or times for a specific game or challenge in your space. It supports both point-based and time-based rankings to encourage competition and replayability.

It is designed for per-player values. Each player sees their name on the board with their current value.

### How it works

* The leaderboard reads a value by its label (the Score Label).
* That value can be created or updated in different ways, such as the Update Value effect or Function Effect (SetVariable).
* For point-based leaderboards, a score appears when you call Post Score to Leaderboard.
* For time-based leaderboards, a score posts automatically when the timer ends (you do not need to call Post Score to Leaderboard).

### Placement Settings

#### Leaderboard Settings Panel

* Score Label – Name of the tracked value label (e.g., "Coins Collected" or "Time")
* Game Name – Identifier for the game or challenge this leaderboard tracks
* Time Based – Toggle to switch between point-based or time-based sorting
* Custom Title – Optional label for organizing or referencing the object

### Related Tools

* [Update Value](../../interactive-studio/effects/update-value.md) (create or change the value)
* [Function Effect: SetVariable](../../advanced-tooling/function-effect/portals-specific-functions.md) (set or adjust values with logic)
* [Post Score to Leaderboard](../../interactive-studio/effects/post-score-to-leaderboard.md) (submit point-based scores)
* [Timer Stopped](../../interactive-studio/triggers/timer-stopped.md) (time-based scores post when the timer ends)

### Common Use Cases

* Track fastest times in obstacle courses
* Display scores for collectible or combat challenges
* Host competitions or events with ranked results
