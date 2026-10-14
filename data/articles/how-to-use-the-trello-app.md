# How to Use the Trello App

Article URL: https://support.optisigns.com/hc/en-us/articles/360050244454-How-to-Use-the-Trello-App

Article ID: 360050244454

Locale: en-us

Updated at: 2026-10-13T21:49:36Z

---

### In this article, we'll show how to display your Trello boards and cards on your digital signs with OptiSigns.

- [What You'll Need](#WhatYoullNeed)
- [Creating a Trello App](#CreatingATrelloApp)
- [Displaying a Private Trello Board](#DisplayingAPrivateTrelloBoard)
- [Deploying a Trello App](#DeployingATrelloApp)

With the Trello app, it's possible to display your Trello boards on your digital signs. Keep your team's tasks, priorities and progress in view in the office, on the shop floor or in a meeting room, and let the screen refresh itself as cards move.

Let's get started.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- A Trello account, with access to the board you want to display
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

---

<a name="CreatingATrelloApp"></a>

## Creating a Trello App

First, open the board you want to display at **trello.com**. Copy its address from your browser's address bar. It will look like:

 https://trello.com/b/boardId/board-name

Next, go to the OptiSigns portal. Go to **Files/Assets** and select **Apps**.

![Files/Assets page with an arrow on the Apps button in the left panel](https://support.optisigns.com/hc/article_attachments/56388453766035)

Search for **Trello** and select the **Trello** app.

![Add App dialog searched for Trello, with an arrow on the Trello app card](https://support.optisigns.com/hc/article_attachments/56388453767315)

The Trello app settings will open. Fill in the following:

- **Name** - The name of your Trello asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
- **Type** - **URL** to show a board from its link, or **Embed** to show a single card from its embed code. You can't change this after saving.
  - **URL** - The Trello board address you copied. Card links (https://trello.com/c/…) work too.
- **Update Interval** - How often the app checks Trello for updates, measured in seconds. The default is 600 (every 10 minutes). Set it to 0 to check only when the app first loads.
- **Sign in with Credential** - Turn this on if your board is private. See [**Displaying a Private Trello Board**](#DisplayingAPrivateTrelloBoard) below.

![Trello form with Name, Type, URL and Update Interval boxed and an arrow pointing down to Save](https://support.optisigns.com/hc/article_attachments/56388438446355)

|  |
| --- |
| **NOTE** |
| The URL must be a **trello.com/b/…** (board) or **trello.com/c/…** (card) link. Any other address shows **Please enter a valid Trello URL** and you won't be able to save. |

To show a single card instead of a board, set **Type** to **Embed** and paste the card's Trello embed code into **Embed Code**.

![Trello form with Type switched to Embed, showing the Embed Code box below it](https://support.optisigns.com/hc/article_attachments/56388453768595)

Now hit **Save**. You'll have created a Trello app, and it will appear in your **Files/Assets**.

![The new Trello asset in Files/Assets](https://support.optisigns.com/hc/article_attachments/56388438448275)

---

<a name="DisplayingAPrivateTrelloBoard"></a>

## Displaying a Private Trello Board

If your board isn't public, OptiSigns needs to sign in to Trello to show it.

![Sign in with Credential turned on, showing the Sign In section with Master Password, Username/Email and Password](https://support.optisigns.com/hc/article_attachments/56388438454803)

Turn on **Sign in with Credential** and fill in the **Sign In** section:

- **Username/Email** - The Trello login the screen should use.
- **Password** - The password for that login.
- **Master Password** - Optional. Check **Use master password** to add an extra layer of encryption to the saved login. If you use it, you'll need to enter the master password once in the OptiSigns app on each device.

---

<a name="DeployingATrelloApp"></a>

## Deploying a Trello App

To push your Trello app to a screen, go to the **Screens** tab, then click **Edit** next to the screen you want to display it on.

![Screens list with an arrow on a screen's Edit button](https://support.optisigns.com/hc/article_attachments/56388438455443)

The **Edit Screen** pop-up will appear. Select **Asset** under **Content Type**, then hit **Change** next to **Selected Asset**.

![Edit Screen dialog with Content Type set to Asset and an arrow on Change](https://support.optisigns.com/hc/article_attachments/56388453776787)

The **Select Asset** window will open. Search for your Trello app, click it, then hit **Select**.

![Select Asset dialog with the Trello asset selected](https://support.optisigns.com/hc/article_attachments/56388453777171)

Back in **Edit Screen**, hit **Save**. Your Trello board will now display on your screen.

Your Trello app can also be displayed in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).
