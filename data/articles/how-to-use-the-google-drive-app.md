# How to Use the Google Drive App

Article URL: https://support.optisigns.com/hc/en-us/articles/360049518313-How-to-Use-the-Google-Drive-App

Article ID: 360049518313

Locale: en-us

Updated at: 2026-10-26T09:22:47Z

---

### In this article, we'll show how to play the images and videos in a Google Drive folder on your digital signs with OptiSigns.

- [What You'll Need](#WhatYoullNeed)
- [Creating a Google Drive App](#CreatingAGoogleDriveApp)
  - [Advanced](#Advanced)
  - [Checking and Refreshing a Sync](#CheckingAndRefreshingASync)
- [Deploying a Google Drive App](#DeployingAGoogleDriveApp)
- [Supported File Types](#SupportedFileTypes)
- [Limitations](#Limitations)

With the Google Drive app, it's possible to play the images and videos in a Google Drive folder on your screens. The app turns the folder into a playlist and keeps it in sync, so when you add, change or remove a file in Google Drive, your screens update too. Your team can update what's on screen without ever signing in to OptiSigns.

Let's get started.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- A Google account with access to the Google Drive folder you want to show
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

---

<a name="CreatingAGoogleDriveApp"></a>

## Creating a Google Drive App

From the OptiSigns portal, go to **Files/Assets** and select **Apps**.

![OptiSigns Files/Assets page with the Apps button highlighted](https://support.optisigns.com/hc/article_attachments/56487902924947)

Search for **Google Drive** and select the **Google Drive** app.

![Add App dialog searched for Google Drive, with the Google Drive app card highlighted](https://support.optisigns.com/hc/article_attachments/56487902926867)

Click **Sign in with Google** and sign in with your Google account.

![Google Drive app window with the sign-in button highlighted](https://support.optisigns.com/hc/article_attachments/56487907860883)

Click **Allow** to let OptiSigns access your Google Drive.

![Google consent screen asking to allow OptiSigns access to Google Drive, with Allow highlighted](https://support.optisigns.com/hc/article_attachments/360072635854)

Choose the folder you want to show on your screens:

![Google Drive folder picker with a folder selected and the Select button](https://support.optisigns.com/hc/article_attachments/360073809813)

The Google Drive app settings will open.

![Google Drive app form showing the account badge, Name, Folder, transition and duration fields](https://support.optisigns.com/hc/article_attachments/56487907868179)

Fill them in:

- **Name** - The name of your Google Drive asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
- **Folder** - The Google Drive folder you chose.
- **Transition Effects** - The effect between each image and video. Choose from **None**, **Fade**, **Slide from Right**, **Slide from Left**, **Rotate In**, **Flip** or **Gallery**.
- **Transition Speed** - How fast the transition plays. Choose **Slow**, **Medium** or **Fast**, or **Custom** to set your own speed.
- **Duration for Image** - How long each image shows, in seconds. The default is **10**.
- **Max Video Duration** - The longest each video plays, in seconds. The default is **0**, which plays every video to the end. For example, at **60**, a 90-second video is cut off after 60 seconds, while a 45-second video plays in full.

<a name="Advanced"></a>

### Advanced

Click **Advanced** for more options:

![Advanced section expanded, showing the Force Sync Interval field](https://support.optisigns.com/hc/article_attachments/56487902930323)

- **Force Sync Interval** - How often, in hours, OptiSigns runs a full sync of your folder. Changes are normally picked up automatically, and this scheduled sync catches anything that was missed. The default is **12**, and you can set any value from **1** to **24**.

Now hit **Save**. You'll have created a Google Drive app, and it will appear in your **Files/Assets**. Depending on how many files are in your folder, the first sync may take a moment, as every file is copied to OptiSigns.

|  |
| --- |
| **TIP** |
| Files play in order by name. To control the order, rename your files in Google Drive, for example by starting each name with **1**, **2**, **3**. |

![Google Drive folder with files numbered 1, 2 and 3 to set the playback order](https://support.optisigns.com/hc/article_attachments/360072641254)

<a name="CheckingAndRefreshingASync"></a>

### Checking and Refreshing a Sync

When files are added, changed or removed in your Google Drive folder, OptiSigns syncs the changes automatically. To see when the last change was synced and which file was synced last, open the app again from **Files/Assets**. To sync right away, click **Refresh Data**.

![Google Drive app settings with the Refresh Data button highlighted](https://support.optisigns.com/hc/article_attachments/56487902930579)

---

<a name="DeployingAGoogleDriveApp"></a>

## Deploying a Google Drive App

To push your Google Drive app to a screen, go to the **Screens** tab, then click **Edit** next to the screen you want to display it on.

![Screens list with the Edit button highlighted on a screen row](https://support.optisigns.com/hc/article_attachments/56487907877651)

The **Edit Screen** pop-up will appear. Select **Asset** under **Content Type**, then hit **Change** next to **Selected Asset**.

![Edit Screen dialog with Content Type set to Asset and the Change button highlighted](https://support.optisigns.com/hc/article_attachments/56487902931987)

The **Select Asset** window will open. Search for your Google Drive app, click it, then hit **Select**.

![Select Asset dialog with the Google Drive asset selected](https://support.optisigns.com/hc/article_attachments/56487907882131)

Back in **Edit Screen**, hit **Save**. Your Google Drive files will now play on your screen.

Your Google Drive app can also be displayed in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).

---

<a name="SupportedFileTypes"></a>

## Supported File Types

The Google Drive app syncs these file types from your folder:

- **Images** - **JPG** (JPEG) and **PNG** only
- **Videos** - **MP4**. For the best compatibility, we recommend MP4 videos encoded in **H.264**. If a video won't play, see [How to re-encode video files](https://support.optisigns.com/hc/en-us/articles/360042143753).

Any other files in the folder, such as documents or spreadsheets, are skipped. For the full list of file types OptiSigns supports on its own, see [What types of files are supported?](https://support.optisigns.com/hc/en-us/articles/360016342373)

---

<a name="Limitations"></a>

## Limitations

- Only the file types listed under **Supported File Types** are synced. Any other files in the folder are ignored.
- Sub-folders aren't supported. Only files directly inside the folder you choose are synced.
- To keep the app running smoothly, keep each file to 100 MB or less, and keep up to 200 files per folder. For large videos, we recommend uploading them directly to OptiSigns. For more than 200 files, split them across several folders.
- Avoid special characters such as **/** in your file names, or the folder may not load.
