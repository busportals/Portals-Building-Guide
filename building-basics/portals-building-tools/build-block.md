---
icon: cube
---

# Build Block

### Overview

The Build Block is a resizable cube used for constructing environments or decor. You can apply a custom image texture, select from predefined textures, or use a color picker to choose any solid color.

### Inventory Settings

#### Texture/Color Selection Interface

* Image Texture Cube:
  * Paste Image URL – Apply a texture by pasting a direct image URL.
  * Drag & Drop – Upload a custom image for use as a texture.
  * Browse Files – Select and upload a texture file from your device.
  * Choose From Gallery – Pick from predefined textures
* AI Texture Block
  * Type in the texture you would like and it will be generated with AI
  * Cost: 5 Credits&#x20;
  * **Note:** _Results may very_
* Color Select Cube:
  * Choose the color select cube icon <img src="../../.gitbook/assets/colorcube.png" alt="" data-size="line">

### Placement Settings

Two possible configuration menus depending on selection:

#### _If using a texture (uploaded or predefined):_

* Texture Tiling – Controls how many times the texture repeats across the block’s surface.
* Transparency – Adjusts the cube’s transparency level.
* Collider on – Enables or disables physical collision.
* Emission – Controls glow/light emission from the cube.
* Shadow on – Enables or disables shadows.
* Make AI Walkable – Allows AI characters & Enemy NPCs to walk over the surface.
* Custom Title – Optional field to label the object.

#### _If using the color picker (color cube icon):_

* Cube Color – Sets the block color using a full-spectrum color picker.
* Transparency – Adjusts the cube’s transparency level.
* Collider on – Enables or disables physical collision.
* Emission – Controls glow/light emission from the cube.
* Shadow on – Enables or disables shadows.
* Make AI Walkable – Allows AI characters & Enemy NPCs to walk over the surface.
* Custom Title – Optional field to label the object.

### Common Use Cases

* Building walls, platforms, and architectural structures
* Creating decorative props and themed environments
* Defining invisible collision areas or walkable terrain for NPCs

### Tip: Organizing Triggers with Build Blocks

Triggers can be placed on most objects, not just dedicated trigger cubes. A common organization tactic is to:

1. Place related triggers on **Build Blocks** using the color selector
2. Give the block a distinct color to visually categorize the logic type
3. Add an **On Hover Text Display** effect to the block
4. Label it with a name describing the logic it contains (e.g., "Lobby Controller", "Round Timer", "Win Conditions")

This allows builders to color-code and label their trigger logic for easier navigation and debugging.
