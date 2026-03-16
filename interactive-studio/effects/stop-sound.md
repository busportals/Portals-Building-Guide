---
icon: volume-slash
description: 'Effect: Stops a playing sound.'
---

# Stop Sound

## Use Cases

***

* Stopping background music when a player leaves an area
* Ending a looping sound effect when a game state changes
* Fading out audio during scene transitions

## Configuration

***

| Setting  | Permitted Values    | Description                                                                                            |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------ |
| URL      | URL to an MP3 file  | The URL of the sound to stop. Must match the URL used in Play Sound Once or Play Sound In A Loop.      |
| Fade Out | Numerical value     | Duration in seconds to fade the sound out. Set to 0 for an immediate stop.                             |

{% hint style="info" %}
The URL must exactly match the URL used when the sound was started. If no URL is provided, all currently playing sounds will be stopped.
{% endhint %}

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr></tbody></table>
