---
icon: map
description: 'Effect: Rebuilds the AI navigation mesh at runtime.'
---

# Rebuild Nav Mesh

## Use Cases

***

* Updating AI pathfinding after dynamically moving or showing/hiding objects
* Recalculating navigation after opening a door or destroying a wall
* Refreshing enemy patrol routes when the environment changes

## Configuration

***

No additional configuration needed. When triggered, the navigation mesh is rebuilt to reflect the current state of the environment.

{% hint style="warning" %}
Only use this effect when objects that affect AI pathfinding have been moved, shown, or hidden at runtime. Unnecessary rebuilds may cause a brief performance impact.
{% endhint %}

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr></tbody></table>
