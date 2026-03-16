---
icon: alarm-plus
description: 'Effect: Starts a named timer.'
---

# Start Timer

## Use Cases

***

* Starting a countdown for a timed challenge or race
* Tracking how long a player takes to complete a puzzle
* Beginning a game clock at round start

## Configuration

***

| Setting          | Permitted Values | Description                                                                                  |
| ---------------- | ---------------- | -------------------------------------------------------------------------------------------- |
| Timer Name       | String           | The name of the timer to start. Use the same name with Stop Timer or Cancel Timer.           |
| Custom ID        | String (optional)| An optional custom identifier for the timer instance.                                        |
| Show Timer UI    | Toggle           | When enabled, the timer is displayed on the player's screen.                                 |

{% hint style="info" %}
Use [Stop Timer](stop-timer.md) to stop the timer and fire the OnTimerStopped trigger. Use [Cancel Timer](cancel-timer.md) to cancel the timer silently without firing any trigger.
{% endhint %}

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>
