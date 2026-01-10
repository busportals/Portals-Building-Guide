---
icon: frame
---

# Using Iframes in Portals

Portals supports embedding external web pages via iframes, enabling communication between your content and the Portals interactive studio. This is ideal for interactive overlays, web-based tasks, mini-games, or integrated user flows.

***

### Basic Setup

To enable iframe communication, include the Portals SDK script on your embedded web page:

```
<script src="https://portals-labs.github.io/portals-sdk/portals-sdk.js?v=10005456"></script>
```

This loads the PortalsSdk object, which provides functions to send messages to Unity and control iframe behavior.

***

### Sending Messages to Unity

To send a message from the iframe to Unity, use:

```
PortalsSdk.sendMessageToUnity(json);
```

{% hint style="info" %}
Important: json must be a stringified JSON object.
{% endhint %}

{% hint style="info" %}
Use JSON.stringify() to convert your JavaScript object before passing it in.
{% endhint %}

#### ✅ Correct Usage:

```
const message = {
  TaskName: "exampleTask",
  TaskTargetState: "SetNotActiveToCompleted"
};

PortalsSdk.sendMessageToUnity(JSON.stringify(message));
```

#### ❌ Incorrect Usage (will fail):

```
PortalsSdk.sendMessageToUnity({
  TaskName: "exampleTask",
  TaskTargetState: "SetNotActiveToCompleted"
});
// ❗ Error: [object Object] is not a supported type
```

Passing a raw JavaScript object will result in runtime errors, as Unity expects a string, not an object reference.

***

### JSON Message Structure

The stringified message sent to Unity must follow this structure:

```
{
  "TaskName": "string",           // e.g., "level1_intro"
  "TaskTargetState": "string"     // see valid values below
}
```

#### Valid TaskTargetState Values

* ToNotActive
* SetNotActiveToActive
* SetActiveToCompleted
* SetCompletedToActive
* SetAnyToCompleted
* SetAnyToActive
* SetActiveToNotActive
* SetCompletedToNotActive
* SetNotActiveToCompleted

***

### Closing the Iframe from Code

You can programmatically close the iframe from inside your content using:

```
PortalsSdk.closeIframe();
```

#### Example: Button to Close Iframe

```
<button onclick="PortalsSdk.closeIframe()">Close</button>
```

#### Example: Send Message and Close Iframe

```
PortalsSdk.sendMessageToUnity(JSON.stringify({
  TaskName: "taskExample",
  TaskTargetState: "SetActiveToCompleted"
}));

PortalsSdk.closeIframe();
```

***

### Query String Options

You can customize the iframe UI behavior using URL query parameters:

| Query Parameter          | Effect                                    |
| ------------------------ | ----------------------------------------- |
| ?noCloseBtn=true         | Hides the close (X) button                |
| ?hideMaximizeButton=true | Hides the maximize button                 |
| ?hideRefreshButton=true  | Hides the refresh button                  |
| ?maximized=true          | Opens the iframe in full-screen mode      |
| ?forceClose=true         | Clicking X will close instead of minimize |

#### Example Iframe URL with Options

```
https://example.com/page.html?noCloseBtn=true&maximized=true
```

***

### Full Example

```
<!DOCTYPE html>
<html>
  <head>
    <script src="https://portals-labs.github.io/portals-sdk/portals-sdk.js?v=10005456"></script>
    <script>
      function sendMessage(taskName, targetState) {
        const message = {
          TaskName: taskName,
          TaskTargetState: targetState
        };
        PortalsSdk.sendMessageToUnity(JSON.stringify(message));
      }

      window.onload = () => {
        sendMessage("my-task", "SetActiveToCompleted");
      };

      function closeIframe() {
        PortalsSdk.closeIframe();
      }
    </script>
  </head>
  <body>
    <h1>Welcome to the Task Page</h1>
    <button onclick="sendMessage('my-task', 'SetActiveToCompleted')">Complete Task</button>
    <button onclick="closeIframe()">Close</button>
  </body>
</html>
```

***

### Troubleshooting

#### ❗ Error: \[object Object] is not a supported type

* Cause: You passed a raw object instead of a string.
* Fix: Use JSON.stringify(message) before calling sendMessageToUnity.

#### ❗ Error: Failed to launch 'uniwebview://...' because the scheme does not have a registered handler

* Cause: You’re testing in a regular web browser.
* Fix: Test inside a Unity WebView (e.g., on a mobile device or emulator where uniwebview:// is supported).

#### ❗ Error: Not allowed to launch 'uniwebview://'... because a user gesture is required

* Cause: The SDK function was triggered outside of a user interaction (e.g., setTimeout).
* Fix: Wrap calls like sendMessageToUnity or closeIframe inside a user event handler (onclick, etc.).

***
