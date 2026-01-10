---
icon: browser
description: Fix iframe display and communication issues
---

# Iframe Debugging

Iframes embed external web pages in your Portals space. Issues typically involve display, SDK communication, or browser restrictions.

## Quick Checklist

- [ ] **Iframe is an Effect** - Added via trigger, not a building tool
- [ ] **SDK script loaded** - Include the Portals SDK in your HTML
- [ ] **JSON.stringify()** - Always stringify messages to Unity
- [ ] **User gesture required** - Some actions need click handlers
- [ ] **Test in Portals** - Browser preview won't work for SDK features

---

## Iframe Not Appearing

**Symptom:** Trigger fires but no iframe is visible.

### Step 1: Verify Iframe is an Effect

Iframe is NOT a building tool. You add it as an effect on a task.

**Correct setup:**
1. Create a task (e.g., "showHUD")
2. Add a trigger (e.g., Player Login)
3. Add Iframe effect to the trigger
4. Configure URL and positioning

### Step 2: Check Positioning Values

| Setting | Issue if Wrong |
|---------|----------------|
| Left/Right Position | Iframe off-screen horizontally |
| Top/Bottom Position | Iframe off-screen vertically |
| Width/Height | Too small to see, or zero |
| Layer Order | Behind other elements |

**Test with centered values:**
```
Left: 400
Top: 200
Width: 400
Height: 300
Layer Order: 100
```

### Step 3: Verify URL is Accessible

- URL must be HTTPS (not HTTP)
- URL must allow iframe embedding (no X-Frame-Options deny)
- Test the URL directly in a browser first

---

## SDK Not Loading

**Symptom:** `PortalsSdk` is undefined in JavaScript.

### Verify Script Tag

Add this to your HTML `<head>`:

```html
<script src="https://portals-labs.github.io/portals-sdk/portals-sdk.js?v=10005456"></script>
```

**Common mistakes:**
- Script tag in wrong location (must be before your code)
- Typo in URL
- Missing `https://`

### Test SDK is Available

```javascript
if (typeof PortalsSdk !== 'undefined') {
    console.log('SDK loaded');
} else {
    console.error('SDK not loaded');
}
```

---

## Error: "[object Object] is not supported"

**Cause:** Sending a JavaScript object directly instead of a JSON string.

**Wrong:**
```javascript
PortalsSdk.sendMessageToUnity({
    TaskName: "quest1",
    TaskTargetState: "SetActiveToCompleted"
});
```

**Correct:**
```javascript
PortalsSdk.sendMessageToUnity(JSON.stringify({
    TaskName: "quest1",
    TaskTargetState: "SetActiveToCompleted"
}));
```

---

## Error: "Failed to launch uniwebview"

**Cause:** Testing in a regular browser instead of the Portals environment.

**Solution:**
- SDK features only work inside Portals
- Deploy your iframe and test in the actual Portals space
- Browser console testing won't work for Unity communication

---

## Error: "User gesture required"

**Cause:** Calling certain SDK functions without a user interaction.

**Solution:** Wrap the call in a click handler:

```javascript
// Wrong - runs automatically
PortalsSdk.closeIframe();

// Correct - runs on user click
document.getElementById('closeBtn').onclick = function() {
    PortalsSdk.closeIframe();
};
```

---

## Messages Not Sending to Unity

**Symptom:** `sendMessageToUnity` runs but nothing happens in Portals.

### Verify Message Format

```javascript
// Correct format for task state change
PortalsSdk.sendMessageToUnity(JSON.stringify({
    TaskName: "exactTaskName",     // Must match exactly
    TaskTargetState: "SetActiveToCompleted"
}));
```

### Valid TaskTargetState Values

| Value | Effect |
|-------|--------|
| `ToNotActive` | Set to NotActive from any state |
| `SetNotActiveToActive` | Activate from NotActive |
| `SetActiveToCompleted` | Complete from Active |
| `SetCompletedToActive` | Reactivate from Completed |
| `SetAnyToCompleted` | Complete from any state |
| `SetAnyToActive` | Activate from any state |
| `SetActiveToNotActive` | Deactivate from Active |
| `SetCompletedToNotActive` | Deactivate from Completed |
| `SetNotActiveToCompleted` | Complete from NotActive |

### Check Task Name

Task names are case-sensitive and space-sensitive:
```javascript
// If task is named "Player Quest"
TaskName: "Player Quest"    // Correct
TaskName: "player quest"    // Wrong
TaskName: "PlayerQuest"     // Wrong
```

---

## Messages Not Receiving from Unity

**Symptom:** "Send Message to Iframes" effect fires but iframe doesn't respond.

### Set Up Message Listener

```javascript
PortalsSdk.setMessageListener(function(message) {
    console.log('Received from Portals:', message);

    // Parse if it's a string
    let data = message;
    if (typeof message === 'string') {
        try {
            data = JSON.parse(message);
        } catch (e) {
            console.log('Not JSON:', message);
            return;
        }
    }

    // Handle the message
    if (data.action === 'updateScore') {
        updateScoreDisplay(data.score);
    }
});
```

### Send Message from Portals

Use the "Send Message to Iframes" effect:
```json
{"action":"updateScore","score":$N{playerScore}}
```

**Note:** Variables like `$N{playerScore}` are replaced with actual values before sending.

---

## Transparent Background Not Working

**Symptom:** Iframe has white/solid background instead of transparent HUD.

### CSS Requirements

```css
html, body {
    background: transparent !important;
    margin: 0;
    padding: 0;
}

/* Apply visible background only to content */
.hud-container {
    background: rgba(0, 0, 0, 0.8);
    border-radius: 8px;
    padding: 10px;
}
```

### Sizing

Size the iframe to exactly match your content:
- No extra space around elements
- Width/Height in Portals should match content dimensions

---

## Close Button Issues

### Hide UI Elements

Add URL parameters to control iframe chrome:

```
https://yoursite.com/page.html?noCloseBtn=true&hideMaximizeButton=true&hideRefreshButton=true
```

| Parameter | Effect |
|-----------|--------|
| `?noCloseBtn=true` | Hide close button |
| `?hideMaximizeButton=true` | Hide maximize button |
| `?hideRefreshButton=true` | Hide refresh button |
| `?maximized=true` | Open fullscreen |
| `?forceClose=true` | X closes instead of minimizes |

### Programmatic Close

```javascript
// Must be in a user-initiated event handler
document.getElementById('myCloseBtn').addEventListener('click', function() {
    PortalsSdk.closeIframe();
});
```

---

## Debugging Workflow

1. **Browser Console (F12)**
   - Check for JavaScript errors
   - Verify SDK loaded: `console.log(PortalsSdk)`
   - Test message parsing

2. **Network Tab**
   - Verify iframe URL loads (200 status)
   - Check for CORS errors

3. **Task Debug Panel (in Portals)**
   - Verify task state changes when messages are sent
   - Check if triggers are firing

4. **Simplify and Test**
   ```javascript
   // Minimal test - just send a simple message
   document.body.onclick = function() {
       PortalsSdk.sendMessageToUnity(JSON.stringify({
           TaskName: "test",
           TaskTargetState: "SetAnyToActive"
       }));
       console.log('Message sent');
   };
   ```
