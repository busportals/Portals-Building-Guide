---
icon: eye
description: 'Effect: Spectate other players in the session.'
---

# Spectate Player

## Use Cases

***

* Allowing eliminated players to watch remaining players in a competitive game
* Spectating specific teams or roles by filtering on a variable
* Creating observation modes for admins or judges

## Configuration

***

| Setting         | Permitted Values | Description                                                                                                                                     |
| --------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Filter Variable | String (optional) | The name of a player variable to filter by. Only players with this variable matching the Filter Value will be available to spectate.            |
| Filter Value    | String (optional) | The value that the Filter Variable must match for a player to be included in the spectate rotation.                                            |

{% hint style="info" %}
Calling this effect multiple times will rotate through the available players that match the filter criteria.
{% endhint %}

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>
