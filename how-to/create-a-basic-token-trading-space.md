# Create a basic token trading space

<figure><img src="../.gitbook/assets/tradingfinal.png" alt=""><figcaption></figcaption></figure>

For this tutorial we will show how to setup a very basic trading space. This tutorial will include how to setup a buy and sell swap effect and 3D chart.

### Setting up a token swap

1. First I will setup a trigger cube that covers the area where players will go to buy tokens.

<figure><img src="../.gitbook/assets/buysetup3.gif" alt=""><figcaption></figcaption></figure>

2. Next I will add a basic interaction with the following configuration:
   1. Trigger: User Enter Trigger
   2. Effect: Show Token Swap
   3. Buy: Toggled On
   4. Sell: Toggled Off
   5. Token Address: 52Rh8epudA3qvLmyP1YCavRWrNV8As1JcW5xMU7mJEj9
   6. Wallet Address: \[my wallet]

<figure><img src="../.gitbook/assets/buysetup2.gif" alt=""><figcaption></figcaption></figure>

3.  Lastly, I will setup one more effect with the following configuration:

    1. Trigger: User Exit Trigger
    2. Effect: Hide Token Swap

    The purpose of this effect is so when a player walks off the button it will close the swap modal automatically.

<figure><img src="../.gitbook/assets/buysetup.gif" alt=""><figcaption></figcaption></figure>

3. Now I will repeat steps 1-3 on the other side of the room with the only difference being instead of toggling on buy in the show token swap effect we will toggle on sell (and buy will be toggled off).
   1. Trigger: User Enter Trigger
   2. Effect: Show Token Swap
   3. Buy: Toggled Off
   4. Sell: Toggled On
   5. Token Address: 52Rh8epudA3qvLmyP1YCavRWrNV8As1JcW5xMU7mJEj9
   6. Wallet Address: \[my wallet]

<figure><img src="../.gitbook/assets/sellsetup.gif" alt=""><figcaption></figcaption></figure>

### Setting up a 3D Candlestick Chart

To create a 3D chart in your space for the token you are trading the setup is very simple.

1. Copy the CA for the token you want to display
2. Open the inventory and click on the chart item
3. Paste the CA and click spawn chart
4. Place the chart in the space

<figure><img src="../.gitbook/assets/chartsetup.gif" alt=""><figcaption></figcaption></figure>
