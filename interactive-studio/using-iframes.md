# 🖼️ Using Iframes

Portals supports embedding interactive content via iframes. This allows external web pages to send messages to the Portals Unity environment, enabling powerful integrations like custom UI layers, external task flows, and embedded games.

To enable communication between your iframe content and the Portals Unity engine, include the Portals SDK script on your webpage:

```
<script src="https://portals-labs.github.io/portals-sdk/portals-sdk.js?v=10005456"></script>
```

Once the SDK is loaded, you can send messages to Unity using:

```
PortalsSdk.sendMessageToUnity(json);
```

#### Message Format

The message must be a JSON object with the following structure:

```
{
  "TaskName": "YourTaskName",
  "TaskTargetState": "SetActiveToCompleted"
}
```

#### Available TaskTargetState Values

* ToNotActive
* SetNotActiveToActive
* SetActiveToCompleted
* SetCompletedToActive
* SetAnyToCompleted
* SetAnyToActive
* SetActiveToNotActive
* SetCompletedToNotActive
* SetNotActiveToCompleted

These states define how tasks in Unity should transition when the message is received.

### Example: Sending a Task Message 

Here’s a basic example of sending a task state change when a page or component loads:

```
<script>
  function sendMessage(taskName, taskTargetState) {
    const message = {
      TaskName: taskName,
      TaskTargetState: taskTargetState
    };
    PortalsSdk.sendMessageToUnity(message);
  }

  // Send message when iframe content is ready
  window.onload = () => {
    sendMessage("my-task", "SetActiveToCompleted");
    console.log("Message sent to Unity");
  };
</script>
```

### Closing the Iframe from Code

You can programmatically close the iframe using:

```
PortalsSdk.closeIframe();
```

This is useful for exit buttons, form submissions, or completing tasks within the iframe.

#### Example: Close Iframe on Button Click

```
<button onclick="PortalsSdk.closeIframe()">Close</button>
```

You can also combine it with message sending:

```
PortalsSdk.sendMessageToUnity({
  TaskName: "example-task",
  TaskTargetState: "SetActiveToCompleted"
});
PortalsSdk.closeIframe();
```

### Query String Options

Customize iframe behavior using the following query string parameters:

| Option                   | Description                                                    |
| ------------------------ | -------------------------------------------------------------- |
| ?noCloseBtn=true         | Hides the close (X) button.                                    |
| ?hideMaximizeButton=true | Hides the maximize button.                                     |
| ?hideRefreshButton=true  | Hides the refresh button.                                      |
| ?maximized=true          | Opens the iframe in full-screen mode by default.               |
| ?forceClose=true         | Clicking the X will close the iframe instead of minimizing it. |

#### Example URL with Options

```
https://example.com/my-game.html?noCloseBtn=true&maximized=true
```

This URL will load the iframe without a close button and in full-screen mode.
