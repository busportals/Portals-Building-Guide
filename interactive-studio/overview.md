# 📓 Overview

## The Interactive Studio at a high-level

The Interactive Studio is a no-code tool suite designed to gamify your Portals space. It consists of three main components: Tasks, Triggers, and Effects. This overview will provide a high-level description of each component, with additional details covered in the rest of the documentation.\
\
The basic structure of the interactive studio is as follows:

* Tasks will exist in one of three states (not active, active, or completed)
* Triggers will change the state of a task (e.g. when you click on a cube, a task may change from the not active state to the active state.
* Effects will occur when a task is changed to a specific state. For example, when a task is not active a door may be closed, but when it is active it opens up.

When you combine tasks, triggers, and effects you can create gameplay sequences in your space.

## Tasks

Tasks are the foundation of the Interactive Studio. A task can exist in one of three states at any given time: Not Active, Active, or Completed. All tasks begin in the Not Active state by default, but can be transitioned to any state in any order via triggers.&#x20;

## Triggers

Triggers are used to transition a task from one state to another (e.g., from Not Active to Active). Triggers can take various forms, such as entering an area, clicking on an item, getting hit by an object, and more.&#x20;

## Effects

Effects occur when a task reaches a certain state. For example, when a task reaches the active state, the effect might be a door opening. Each task can have multiple effects associated with any of its states (Not Active, Active, Completed).



<details>

<summary><strong>Example #1 - Interactive Door</strong></summary>

**Objects**

For this example we will us an animated door and a trigger cube placed in the doorway. The door will simply swing open for its animation.

<img src="../.gitbook/assets/ScreenRecording2024-07-16at11.28.58AM-ezgif.com-video-to-gif-converter.gif" alt="" data-size="original">

**Tasks**

We will just one single player task called "door".

**Triggers**

We will setup the following trigger on the _**animated door**_.

<img src="../.gitbook/assets/image (4).png" alt="" data-size="original">&#x20;

This will make it so when a user clicks the door  the task "door" will change from not active to active.

We will setup the following trigger on the _**trigger cube**._

![](<../.gitbook/assets/image (5).png>)

This will make it so when a user exits the trigger cube zone the task "door" will change from active to not active, with a 1 second delay. We add the delay mainly to give users time to get away from the door.

**Effects**

We then will add the following effects to the _**animated door.**_

![](<../.gitbook/assets/image (7).png>)

We setup the animation to play once at the speed and direction of -1 when the task "door" is in the not active state. This will mean the door animation will play in reverse at 100% speed, giving it the appearance of closing.

<img src="../.gitbook/assets/image (6).png" alt="" data-size="original">

We setup the animation to play once at the speed and direction of 1 when the task "door" is in the active state. This will mean the door animation will play in normally at 100% speed, giving it the opening animation.



**Final Result**

We have now setup a door that will open when you click on it and, close when you walk through it.

<img src="../.gitbook/assets/ScreenRecording2024-07-16at11.47.57AM-ezgif.com-video-to-gif-converter.gif" alt="" data-size="original">

</details>
