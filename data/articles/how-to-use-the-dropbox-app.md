# How to Use the Dropbox App

Article URL: https://support.optisigns.com/hc/en-us/articles/360050665413-How-to-Use-the-Dropbox-App

Article ID: 360050665413

Locale: en-us

Updated at: 2026-10-16T16:32:20Z

---

### In this article, we'll show how to play the images and videos in a Dropbox folder on your digital signs with OptiSigns.

- [What You'll Need](#WhatYoullNeed)
- [Creating a Dropbox App](#CreatingADropboxApp)
  - [Advanced](#Advanced)
  - [Checking and Refreshing a Sync](#CheckingAndRefreshingASync)
- [Deploying a Dropbox App](#DeployingADropboxApp)
- [Supported File Types](#SupportedFileTypes)
- [Limitations](#Limitations)

With the Dropbox app, it's possible to play the images and videos in a Dropbox folder on your screens. The app turns the folder into a playlist and keeps it in sync, so when you add, change or remove a file in Dropbox, your screens update too. Your team can update what's on screen without ever signing in to OptiSigns.

Let's get started.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- A Dropbox account with access to the folder you want to show
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

---

<a name="CreatingADropboxApp"></a>

## Creating a Dropbox App

From the OptiSigns portal, go to **Files/Assets** and select **Apps**.

![OptiSigns Files/Assets page with the Apps button highlighted](https://support.optisigns.com/hc/article_attachments/56487883115411)

Search for **Dropbox** and select the **Dropbox** app.

![Add App dialog searched for Dropbox, with the Dropbox app card highlighted](https://support.optisigns.com/hc/article_attachments/56487883117331)

Click **Sign in with Dropbox**.

![Dropbox app window with the sign-in button highlighted](https://support.optisigns.com/hc/article_attachments/56487855829523)

Sign in to Dropbox and allow OptiSigns to access your Dropbox.

![Dropbox sign-in page for linking OptiSigns Digital Signage](https://support.optisigns.com/hc/article_attachments/360075537234)

Choose the folder you want to show on your screens:

![Dropbox folder chooser with a folder checked and the Choose button](https://support.optisigns.com/hc/article_attachments/55999066628627)

The Dropbox app settings will open.

![Dropbox app form showing the account badge, Name, Folder, transition and duration fields](https://support.optisigns.com/hc/article_attachments/56487883123475)

Fill them in:

- **Name** - The name of your Dropbox asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
- **Folder** - The Dropbox folder you chose.
- **Transition Effects** - The effect between each image and video. Choose from **None**, **Fade**, **Slide from Right**, **Slide from Left**, **Rotate In**, **Flip** or **Gallery**.
- **Transition Speed** - How fast the transition plays. Choose **Slow**, **Medium** or **Fast**, or **Custom** to set your own speed.
- **Duration for Image** - How long each image shows, in seconds. The default is **10**.
- **Max Video Duration** - The longest each video plays, in seconds. The default is **0**, which plays every video to the end. For example, at **60**, a 90-second video is cut off after 60 seconds, while a 45-second video plays in full.

<a name="Advanced"></a>

### Advanced

Click **Advanced** for more options:

![Advanced section expanded, showing the Force Sync Interval field](https://support.optisigns.com/hc/article_attachments/56487883123859)

- **Force Sync Interval** - How often, in hours, OptiSigns runs a full sync of your folder. Changes are normally picked up automatically, and this scheduled sync catches anything that was missed. The default is **12**, and you can set any value from **1** to **24**.

Now hit **Save**. You'll have created a Dropbox app, and it will appear in your **Files/Assets**. Depending on how many files are in your folder, the first sync may take a moment, as every file is copied to OptiSigns.

|  |
| --- |
| **TIP** |
| Files play in order by name. To control the order, rename your files in Dropbox, for example by starting each name with **1**, **2**, **3**. |

![Dropbox folder with files numbered 1, 2 and 3 to set the playback order](https://support.optisigns.com/hc/article_attachments/360076677073)

<a name="CheckingAndRefreshingASync"></a>

### Checking and Refreshing a Sync

When files are added, changed or removed in your Dropbox folder, OptiSigns syncs the changes automatically. To see when the last change was synced and which file was synced last, open the app again from **Files/Assets**. To sync right away, click **Refresh Data**.

![Dropbox app settings with the Refresh Data button highlighted](https://support.optisigns.com/hc/article_attachments/56487855832467)

---

<a name="DeployingADropboxApp"></a>

## Deploying a Dropbox App

To push your Dropbox app to a screen, go to the **Screens** tab, then click **Edit** next to the screen you want to display it on.

![Screens list with the Edit button highlighted on a screen row](https://support.optisigns.com/hc/article_attachments/56487855833747)

The **Edit Screen** pop-up will appear. Select **Asset** under **Content Type**, then hit **Change** next to **Selected Asset**.

![Edit Screen dialog with Content Type set to Asset and the Change button highlighted](https://support.optisigns.com/hc/article_attachments/56487883132051)

The **Select Asset** window will open. Search for your Dropbox app, click it, then hit **Select**.

![Select Asset dialog with the Dropbox asset selected](https://support.optisigns.com/hc/article_attachments/56487883136403)

Back in **Edit Screen**, hit **Save**. Your Dropbox files will now play on your screen.

Your Dropbox app can also be displayed in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).

---

<a name="SupportedFileTypes"></a>

## Supported File Types

The Dropbox app syncs these file types from your folder:

- **Images** - **JPG**, **PNG**, **BMP** and **GIF**
- **Videos** - **MP4**. For the best compatibility, we recommend MP4 videos encoded in **H.264**. If a video won't play, see [How to re-encode video files](https://support.optisigns.com/hc/en-us/articles/360042143753).

Any other files in the folder, such as documents or spreadsheets, are skipped. For the full list of file types OptiSigns supports on its own, see [What types of files are supported?](https://support.optisigns.com/hc/en-us/articles/360016342373)

---

<a name="Limitations"></a>

## Limitations

- Only the file types listed under **Supported File Types** are synced. Any other files in the folder are ignored.
- Sub-folders aren't supported. Only files directly inside the folder you choose are synced.
- To keep the app running smoothly, keep each file to 100 MB or less, and keep up to 200 files per folder. For large videos, we recommend uploading them directly to OptiSigns. For more than 200 files, split them across several folders.
- Dropbox Teams folders use a different API from personal accounts. As a workaround, create a folder in your personal Dropbox space, upload your content there, and choose that folder in OptiSigns.
