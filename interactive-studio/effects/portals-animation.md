---
icon: film
description: 'Effect: Create a key-frame animation for an object in-game.'
---

# Portals Animation

## Use Cases

***

* Creating cut scene animations (e.g. the dragon eating the explorer in loot park)
* Moving objects in obstacle course

## Configuration

***

| Setting                          | Permitted Values                                                                             | Description                                                                                                                     |
| -------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Add Transform State              | Position, Rotation, Size numerical inputs or set using build tools. Set transition duration. | Setup key frame animation.  When activated the object will move along the transformation states in the order specified.         |
| Preview Transition               | n/a                                                                                          | Press the Preview Transition button to watch the setup of the animation. Helpful for testing.                                   |
| Loop Animation                   | toggle                                                                                       | The animation will loop.                                                                                                        |
| Seamless Loop                    | toggle                                                                                       | \[Only available if Loop Animation is toggled on] This will smooth out the animation loop.                                      |
| Optimize For Collision Detection | toggle                                                                                       | If the object is going to have "On Collision" triggers it is recommended to toggle this on. It will increase load on the space. |

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>
