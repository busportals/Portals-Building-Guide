---
icon: link
description: 'Effect: Attaches an item to a specific part of the player.'
---

# Attach Item To Player

## Use Cases

***

* Attaching weapons, shields, or tools to a player's hand
* Adding cosmetic items to specific body parts (hats, backpacks, etc.)
* Creating gameplay mechanics where items follow the player's skeleton

## Configuration

***

| Setting          | Permitted Values                                                                                                                                                                                                                                                                     | Description                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Attach Point     | Player Root, Hips, Spine, Chest, UpperChest, Neck, Head, LeftShoulder, RightShoulder, LeftUpperArm, RightUpperArm, LeftLowerArm, RightLowerArm, LeftHand, RightHand, LeftUpperLeg, RightUpperLeg, LeftLowerLeg, RightLowerLeg, LeftFoot, RightFoot | The body part on the player's skeleton where the item will be attached.                              |
| Position Offset  | Numerical input (X, Y, Z)                                                                                                                                                                                                                                                           | The local position offset of the attached item relative to the attach point.                         |
| Rotation Offset  | Numerical input (X, Y, Z)                                                                                                                                                                                                                                                           | The local rotation offset of the attached item relative to the attach point.                         |
| Size Offset      | Numerical input (X, Y, Z)                                                                                                                                                                                                                                                           | The local size offset of the attached item.                                                          |
| Networked        | Toggle                                                                                                                                                                                                                                                                               | When enabled, the attachment is synced across all players in the session so everyone can see it.     |

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>
