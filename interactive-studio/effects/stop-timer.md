---
icon: alarm-exclamation
description: 'Effect: Stops a running timer and fires the OnTimerStopped trigger.'
---

# Stop Timer

## Use Cases

***

* Stopping a race timer when the player crosses the finish line
* Ending a countdown when an objective is completed
* Recording a player's time for leaderboard submission

## Configuration

***

| Setting    | Permitted Values  | Description                                                                                           |
| ---------- | ----------------- | ----------------------------------------------------------------------------------------------------- |
| Timer Name | String            | The name of the timer to stop. Must match the name used in Start Timer.                               |
| Custom ID  | String (optional) | The custom identifier matching the timer instance to stop.                                            |

{% hint style="warning" %}
Stop Timer fires the **OnTimerStopped** trigger. If you want to cancel a timer without firing any trigger, use [Cancel Timer](cancel-timer.md) instead.
{% endhint %}

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>
