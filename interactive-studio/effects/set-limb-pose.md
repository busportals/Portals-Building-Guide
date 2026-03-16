---
icon: hand
description: 'Effect: Positions a player limb using inverse kinematics.'
---

# Set Limb Pose

## Use Cases

***

* Pointing a player's arm toward a target or aiming direction
* Creating custom hold poses for weapons or tools
* Animating player limbs to interact with objects in the environment

## Configuration

***

| Setting              | Permitted Values                                    | Description                                                                                      |
| -------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Limb                 | Right Arm, Left Arm, Right Leg, Left Leg            | Which limb to pose using IK.                                                                     |
| Target Position      | Numerical input (X, Y, Z)                           | The IK target position relative to the player.                                                   |
| Target Rotation      | Numerical input (X, Y, Z, W)                        | The IK target rotation (quaternion).                                                             |
| Follow Camera Pitch  | Toggle                                              | When enabled, the limb follows the camera's pitch. Useful for aiming mechanics.                  |

{% hint style="info" %}
Use the [Stop Limb Pose](stop-limb-pose.md) effect with the same limb to release the pose and return to normal animation.
{% endhint %}

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr></tbody></table>
