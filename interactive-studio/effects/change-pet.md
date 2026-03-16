---
icon: paw
description: 'Effect: Changes or assigns a pet that follows the player.'
---

# Change Pet

## Use Cases

***

* Giving the player a pet companion that follows them around
* Changing a pet's appearance as a reward for completing objectives
* Adjusting pet speed and size for different gameplay contexts

## Configuration

***

| Setting | Permitted Values    | Description                                                                          |
| ------- | ------------------- | ------------------------------------------------------------------------------------ |
| URL     | URL to a GLB file   | The URL of the pet's avatar model. Must be a rigged avatar GLB — static models will not work. |
| Speed   | Float               | The pet's movement speed.                                                            |
| Scale   | Float               | The pet's scale multiplier.                                                          |

{% hint style="warning" %}
The GLB file must be a **rigged avatar** — static or unrigged models will not work as pets.
{% endhint %}

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr></tbody></table>
