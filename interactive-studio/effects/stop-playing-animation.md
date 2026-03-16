---
icon: pause
description: 'Effect: Freezes a GLB animation at a specific frame.'
---

# Stop Playing Animation

## Use Cases

***

* Freezing an animation at its starting frame on room load so it can be played later on demand
* Pausing an animation mid-way through for a dramatic effect
* Stopping an animation at its end frame to hold a final pose

## Configuration

***

| Setting    | Permitted Values | Description                                                                                      |
| ---------- | ---------------- | ------------------------------------------------------------------------------------------------ |
| Stop At    | Float (0.0–1.0)  | The normalized time to freeze the animation at. 0.0 is the start, 1.0 is the end of the clip.   |

{% hint style="info" %}
A common pattern is to use this effect on player login (OnPlayerLoggedIn) with `stop: 0.0` to freeze the animation at its first frame, then trigger [Play Animation Once](play-animation-once.md) when needed.
{% endhint %}

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr></tbody></table>
