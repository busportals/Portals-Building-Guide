---
icon: person-walking-arrow-right
description: 'Effect: Moves an object to the player''s position with optional offset.'
---

# Move Item to Player

## Use Cases

***

* Moving a bomb or object into position relative to the player
* Creating a pin point marker showing the player's location on a map
* Attaching items that follow the player's position and rotation

## Configuration

***

| Setting                    | Permitted Values    | Description                                                                                                         |
| -------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Offset X                   | Numerical input     | Horizontal offset from the player's position along the X axis.                                                      |
| Offset Y                   | Numerical input     | Vertical offset from the player's position along the Y axis.                                                        |
| Offset Z                   | Numerical input     | Depth offset from the player's position along the Z axis.                                                           |
| Offset From Player Direction | Toggle            | When enabled, the offset is applied relative to the direction the player is facing rather than world coordinates.   |
| Match Player Rotation      | Toggle              | When enabled, the object will rotate to match the player's current rotation.                                        |

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>
