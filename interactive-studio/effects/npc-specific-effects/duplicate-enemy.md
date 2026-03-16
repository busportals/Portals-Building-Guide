---
icon: clone
description: 'Effect: Spawns copies of an enemy NPC at a spawn point.'
---

# Duplicate Enemy

## Use Cases

***

* Spawning waves of enemies at designated spawn points
* Creating multiple enemy copies for a horde mode
* Dynamically increasing enemy count based on player progress

## Configuration

***

| Setting       | Permitted Values | Description                                                                |
| ------------- | ---------------- | -------------------------------------------------------------------------- |
| Spawn Name    | String           | The name of the SpawnPoint where copies will appear.                       |
| Count         | Integer          | The number of enemy copies to spawn.                                       |
| Random Radius | Float            | The radius around the spawn point within which copies are randomly placed. |

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Enemy NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>
