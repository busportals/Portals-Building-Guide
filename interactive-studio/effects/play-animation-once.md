---
icon: play
description: 'Effect: Plays an embedded GLB animation one time.'
---

# Play Animation Once

## Use Cases

***

* Playing a door opening animation when a player triggers it
* Triggering a one-shot explosion or destruction animation
* Playing a custom GLB animation in response to a game event

## Configuration

***

| Setting | Permitted Values | Description                                                                           |
| ------- | ---------------- | ------------------------------------------------------------------------------------- |
| Speed   | Float            | Playback speed of the animation. Use a negative value to play in reverse.             |

{% hint style="info" %}
This effect plays the animation embedded in the GLB model file. To freeze an animation at a specific frame, use [Stop Playing Animation](stop-playing-animation.md).
{% endhint %}

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr></tbody></table>
