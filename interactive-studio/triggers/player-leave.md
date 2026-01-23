---
icon: user-xmark
description: Trigger that fires when a user leaves the room.
---

# On Player Leave

This trigger fires when any player disconnects from the room. When triggered, it fires for ALL players currently in the room, not just the disconnecting player.

## Configuration

***

No additional configuration beyond the base configuration parameters.

## Behavior

***

When a player leaves the room (closes browser, navigates away, or loses connection), this trigger activates on all remaining players' clients simultaneously. This broadcast behavior makes it useful for:

- Updating UI elements to reflect the player count change
- Triggering cleanup effects visible to all players
- Synchronizing game state across remaining players

## Compatibility

***

<table><thead><tr><th width="210">Object Type</th><th width="199" align="center">Compatibility</th></tr></thead><tbody><tr><td>Trigger Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Building Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Nine Cube</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Custom Import</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>NPC</td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>
