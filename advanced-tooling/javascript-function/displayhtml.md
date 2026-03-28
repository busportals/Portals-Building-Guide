# displayHtml

### Render HTML Overlays

`displayHtml` is a JavaScript function that renders arbitrary HTML/CSS as a fullscreen overlay on top of the 3D game scene. Use it to create custom HUDs, menus, forms, animations, and interactive UI elements.

```javascript
displayHtml('<html string>');
```

**Single argument:** An HTML string containing valid HTML, CSS, and optional `<script>` tags.

***

## Where to use it

`displayHtml` is called inside the **Javascript Function** effect's code field. It can be triggered by:

* **Click** trigger (click interactions)
* **Player Login** trigger (requires **Activate on Start** enabled on the effector)
* **Reactive tasks** (re-renders when referenced variables change)

***

## Supported features

### HTML & CSS

* Full CSS: flexbox, grid, fixed positioning, animations, keyframes, transitions
* `backdrop-filter` (blur, grayscale, sepia, contrast, saturate, hue-rotate, invert, brightness)
* `mix-blend-mode`
* `pointer-events: none/auto` for click-through control
* `<canvas>` with 2D drawing API
* `<svg>` elements
* Forms: `<input>`, `<select>`, `<textarea>`, `<button>`
* CSS gradients, `radial-gradient`
* Base64 data URIs for inline images
* `AudioContext` / WebAudio API
* Multiple `position: fixed` panels in one call
* `z-index` layering
* Transparent backgrounds

### JavaScript in scripts

Code after `displayHtml()` in the same code field executes directly and can manipulate the rendered HTML. Inside `<script>` tags you can use:

* `onclick`, `onmousedown`, `onmouseup` handlers
* `setTimeout`, `setInterval`, `requestAnimationFrame`
* DOM APIs (`getElementById`, `createElement`, `addEventListener`)
* `Math.*` functions and `window.*` globals

### Engine integration

* `SetVariable('name', value, scope)` — set game variables from HTML
* `UseEffector('itemId', 'EffectName', '{jsonParams}')` — trigger effectors from HTML

***

## Escaping rules

Since the HTML string lives inside a JavaScript string delimited by single quotes:

| Need | Escape as | Context |
|------|-----------|---------|
| Double quotes for HTML attributes | `\"` | `<div id=\"myid\">` |
| Single quotes inside onclick | `\\&#39;` | `onclick="SetVariable(\\&#39;name\\&#39;, 1.0, 0.0)"` |

**Tip:** Inside `<script>` IIFE tags, use double quotes for all string literals — they are safe because the `displayHtml('...')` wrapper uses single quotes as its delimiter.

***

## Examples

### Basic text overlay

```javascript
displayHtml('<div style="font:18px monospace;color:#fff;padding:20px">Hello World</div>');
```

### Interactive button with SetVariable

```javascript
displayHtml('<button onclick="SetVariable(\\&#39;score\\&#39;, 10.0, 0.0)">Add Score</button>');
```

### Transparent HUD (click-through)

```javascript
displayHtml('<style>body{margin:0;background:transparent;pointer-events:none}</style><div style="position:fixed;top:10px;left:10px;color:#fff;font:14px monospace;pointer-events:none">HP: 100</div>');
```

### Self-contained timer with IIFE

```javascript
displayHtml('<div id="out">0</div><script>(function(){var n=0;setInterval(function(){n++;document.getElementById("out").textContent=n;},1000);})();</script>');
```

### Trigger an effector from HTML

```javascript
displayHtml('<button onclick="UseEffector(\\&#39;itemId123\\&#39;, \\&#39;MyEffect\\&#39;, \\&#39;{}\\&#39;)">Fire Effect</button>');
```

***

## Important rules

* **Lowercase variable names only** — Variable names with uppercase letters (e.g., `bX`, `hitCount`) cause `EvaluateAsync` errors. Use all-lowercase: `ballx`, `hitcount`.
* **Pre-initialize reactive variables** — Variables read with `$N{varName}` in reactive tasks must exist before the task evaluates. Initialize them in a separate Player Login task with **Activate on Start** enabled on an item that loads first.
* **Single argument only** — `displayHtml()` takes exactly one argument: the HTML string.
