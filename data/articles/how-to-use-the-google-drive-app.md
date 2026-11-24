# How to Use the Google Drive App

Article URL: https://support.optisigns.com/hc/en-us/articles/360049518313-How-to-Use-the-Google-Drive-App

Article ID: 360049518313

Locale: en-us

Updated at: 2026-11-23T23:38:33Z

---

### In this article, we'll show how to play the files in a Google Drive folder on your digital signs, choose what plays and for how long, and fix a folder that stops syncing.

- [What You'll Need and How It Works](#WhatYoullNeed)
- [Creating a Google Drive App](#CreatingAGoogleDriveApp)
- [Playback, Scale and Advanced Settings](#PlaybackScaleAndAdvancedSettings)
- [Managing the Files in Your Folder](#ManagingTheFilesInYourFolder)
- [Supported Files and Limits](#SupportedFilesAndLimits)
- [Troubleshooting](#Troubleshooting)

With the Google Drive app, you can play the files in a Google Drive folder on your screens: images, videos, and documents such as PDFs, PowerPoint, Word and Excel files. The app keeps the folder in sync, so when you add, change or remove a file in Google Drive, your screens update too. Your team can change what's on screen without ever signing in to OptiSigns.

Let's get started.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- A Google account that can open the Google Drive folder you want to show
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

---

## How It Works

You connect a Google account and pick one folder. OptiSigns copies the folder's files and plays them one after another, like a playlist. Images and video clips play for the time you set, and documents play one page at a time.

When something changes in the folder, Google tells OptiSigns and the change syncs right away. A full sync also runs on a schedule you choose, to catch anything that was missed.

---

<a name="CreatingAGoogleDriveApp"></a>

## Creating a Google Drive App

From the OptiSigns portal, go to **Files/Assets** and select **Apps**.

![Files/Assets page with the Apps button highlighted in the left sidebar](https://support.optisigns.com/hc/article_attachments/57873456329363)

Search for **Google Drive** and select the **Google Drive** app.

![Add App dialog searched for Google Drive, with the Google Drive app card highlighted](https://support.optisigns.com/hc/article_attachments/57873519204883)

The Google Drive app settings will open on **Account & folder**.

![Google Drive app form with Google account, Name and File types, plus Playback, Scale Settings and Advanced](https://support.optisigns.com/hc/article_attachments/57873456330387)

Under **Google account**, click **Sign in with Google** and sign in. Google will ask you to let OptiSigns see your Google Drive files. Click **Allow**.

![Google's consent screen asking to let OptiSigns access your Google Drive, with an arrow on Allow](https://support.optisigns.com/hc/article_attachments/57873519206547)

Right after you sign in, choose who can use this Google account:

- **Only me** - Only you can use the account in your assets. This is the default.
- **Share with team** - Your teammates can sync folders this account can open, in their own assets. To use the folder picker, they also need to be signed in to this Google account in their browser.

OptiSigns remembers the account, so next time you can pick it from **Google account** without signing in again. To use a different account, click **Add another Google account**.

Google's **Select a folder** window will open. Choose the folder you want to show. You can pick from **My Drive**, **Shared drives** or **Shared with me**.

|  |
| --- |
| **IMPORTANT** |
| You can't change the folder after the asset is saved. To show a different folder, create a new Google Drive app. |

Then fill in the rest:

- **Name** - The name of your Google Drive asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
- **File types** - Which kinds of files in the folder play on screen: **Images**, **Videos**, **PDF**, **PowerPoint**, **Word** and **Excel**. All six are on for a new asset. Remove any you don't want to play.

Set any **Playback**, **Scale Settings** and **Advanced** options you want (see below), then hit **Save**. You'll have created a Google Drive app, and it will appear in your **Files/Assets**. Depending on how many files are in your folder, the first sync may take a moment, as every file is copied to OptiSigns.

---

<a name="PlaybackScaleAndAdvancedSettings"></a>

## Playback, Scale and Advanced Settings

Click **Playback** to choose what plays, in which order and for how long.

![Playback section with Always play new files, image, page and video durations, Play order and transitions](https://support.optisigns.com/hc/article_attachments/57873519206803)

- **Always play new files** - On by default: new files in the folder start playing as soon as they sync. Turn it off to approve new files first. They then stay hidden until you show them (see **Managing the Files in Your Folder** below).
- **Duration for Image** - How long each image shows, in seconds. The default is 10.
- **Default duration per page** - How long each page of a document shows, in seconds. The default is 15. You can set a different time for a single file, too.
- **Max Video Duration** - The longest each video plays, in seconds. The default is 0, which plays every video to the end. For example, at 60, a 90-second video is cut off after 60 seconds, while a 45-second video plays in full.
- **Play order** - **Name (A–Z)**, **Name (Z–A)**, **Newest first**, **Oldest first** or **Random**. Newest and oldest use the date the file last changed in Google Drive. Random reshuffles each time the folder syncs.
- **Transition Effects** - The effect between each file: **None**, **Fade**, **Slide from Right**, **Slide from Left**, **Rotate In**, **Flip** or **Gallery**.
- **Transition Speed** - How fast the transition plays, from slow to fast.

|  |
| --- |
| **TIP** |
| To control the order by name, rename your files in Google Drive, for example by starting each name with 1, 2, 3, and leave **Play order** on **Name (A–Z)**. |

![A Google Drive folder with files named 1, 2 and 3 to set their play order](https://support.optisigns.com/hc/article_attachments/57873519207187)

Click **Scale Settings** to choose how images, videos and documents fit your screen.

![Scale Settings with Scale Image, Scale Video and Scale Document all set to Fit](https://support.optisigns.com/hc/article_attachments/57873456338195)

**Scale Image**, **Scale Video** and **Scale Document** each offer:

- **Fit** - Keeps the original shape, with no distortion. This is the default.
- **Stretch** - Fills the screen, and can distort the file.
- **Zoom** - Fills the screen, and crops the edges.
- **None** - Shows the file at its original size.

Click **Advanced** for one more option:

![Advanced section with Force Sync Interval set to 12 hours](https://support.optisigns.com/hc/article_attachments/57873456338963)

- **Force Sync Interval** - How often, in hours, OptiSigns runs a full sync of your folder. Changes are normally picked up right away, and this scheduled sync catches anything that was missed. The default is 12, and you can set any value from 1 to 24.

---

<a name="ManagingTheFilesInYourFolder"></a>

## Managing the Files in Your Folder

To see what your asset will play, open it from **Files/Assets**. You'll see every file OptiSigns synced from the folder.

![An open Google Drive asset showing its synced files, with Preview, Edit Settings and Close at the top](https://support.optisigns.com/hc/article_attachments/57873519208211)

Click **Preview** to see the files in the order they'll play, how long each one shows, and the total time.

![Preview window listing each file in play order with its duration, and the total time and number of items at the top](https://support.optisigns.com/hc/article_attachments/57873519209107)

To keep a file off your screens without deleting it from Google Drive, hover over it and click the eye icon (**Hide file**). Click it again (**Show file**) to put the file back. If you turned off **Always play new files**, this is also how you approve a new file: it arrives hidden, and you show it when it's ready.

![A file card with the Hide file eye icon highlighted in its top-right corner](https://support.optisigns.com/hc/article_attachments/57873519220755)

To find files quickly, use the filter at the top to show **All** files, only the ones **Playing**, or only the **Hidden** ones.

For a document, you can set how long each of its pages shows. Click the **Page durations** button on the document, or right-click it and choose **Page durations**. Then change **Default per page (seconds)** for the whole file, or set a time for each page. These times apply to this file only.

![Page durations window for a spreadsheet, with Default per page set to 15 seconds and the total playback time](https://support.optisigns.com/hc/article_attachments/57873519221139)

To change the asset's settings, click **Edit Settings**. Here you'll also see when the last change was synced and which file was synced last. To sync right away, click **Refresh Data** next to the folder.

![Google Drive settings for a saved asset, with the folder, Refresh Data, and the last change synced and last file synced](https://support.optisigns.com/hc/article_attachments/57873456341267)

---

## Managing Your Google Accounts

Team admins can see and manage every saved Google Drive account in one place. Go to **Integrations** under your main menu and click the **Google Drive** tab.

![Integrations page on the Google Drive tab, with an arrow on Add Connection](https://support.optisigns.com/hc/article_attachments/57873456341651)

From **Google Drive Auth Connections**, admins can:

- Add an account with **Add Connection**.
- See each account's status, and turn sharing with the team on or off with the **Shared** switch.
- Edit an account to reauthorize it.
- Click **⋮** next to an account to **Revoke** it, see **Where Used**, or **Delete** it. Assets that use a revoked or deleted account keep playing their last synced files but stop syncing.

---

## Deploying a Google Drive App

To show your folder on a screen, go to the **Screens** tab and click **Edit** next to the screen. Select **Asset** under **Content Type**, click **Change** next to **Selected Asset**, pick your Google Drive asset, and click **Select**. Then hit **Save**.

Your Google Drive app can also play in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).

---

<a name="SupportedFilesAndLimits"></a>

## Supported Files and Limits

The Google Drive app syncs these files from your folder, as long as their type is on under **File types**:

- **Images** - Common image files such as JPG and PNG.
- **Videos** - Video files. For the best compatibility, we recommend MP4 videos encoded in H.264. If a video won't play, see [Video Codec or Video Playback Issues and How to Re-encode Videos](https://support.optisigns.com/hc/en-us/articles/360038992973).
- **PDF**, **PowerPoint**, **Word** and **Excel** - These play one page at a time.

Any other files in the folder are skipped. For the full list of file types OptiSigns supports on its own, see [What types of files are supported?](https://support.optisigns.com/hc/en-us/articles/360016342373)

Keep these limits in mind:

- Only files directly inside the folder you chose are synced. Files in sub-folders are skipped.
- Google Docs, Sheets and Slides files aren't synced. To show one, download it as a PDF, PowerPoint, Word or Excel file and add that to the folder, or use the [Google Sheets app](https://support.optisigns.com/hc/en-us/articles/360056977214) for a sheet.
- Each file must be 100 MB or smaller. Larger files are skipped. For large videos, we recommend uploading them directly to OptiSigns.
- Up to 200 files per folder are synced. If a folder has more, the 200 oldest files are synced. For more than 200 files, split them across several folders.

---

<a name="Troubleshooting"></a>

## Troubleshooting

Here are a few of the more common issues our customers may face when using the Google Drive app, and how to solve them.

#### My Folder Stopped Syncing, and the Asset Says "Connection Stopped Working"

The Google account behind the asset can no longer connect. This happens when someone changes the account's password, removes OptiSigns from the account's Google settings, or a Google Workspace admin blocks access. Your screens keep playing the last synced files in the meantime.

![A Google Drive asset card with the Connection stopped working badge](https://support.optisigns.com/hc/article_attachments/57873519222291)

When you open the asset, a banner explains the problem.

![Banner reading Google connection stopped working. Files no longer sync.](https://support.optisigns.com/hc/article_attachments/57873456343187)

Click **Edit Settings** and choose another account under **Google account**. Or ask a team admin to reconnect the account from **Integrations** > **Google Drive**.

#### The Asset Says "No Folder Access"

The Google account can no longer open this folder. The folder may have been unshared from that account, moved or deleted. In Google Drive, share the folder with the account again. Or click **Edit Settings**, choose another account that has access, and hit **Save**. The asset keeps the same folder.

#### The Asset Says "Account Revoked" or "Account Removed"

A team admin turned off or deleted the Google account this asset used. Click **Edit Settings** and choose another account to resume syncing, or ask a team admin to turn the account back on from **Integrations** > **Google Drive**.

#### A File in My Folder Isn't Playing

Check these, in order:

- The file may be hidden. Open the asset and filter by **Hidden**. If it's there, click the eye icon to show it. If **Always play new files** is off, every new file arrives hidden.
- Its type may be off. Click **Edit Settings** and check **File types**.
- It may not be supported. Google Docs, Sheets and Slides files, files in sub-folders, and files over 100 MB are skipped.
- The folder may have more than 200 files. Only the 200 oldest are synced.

#### A New or Changed File Hasn't Shown Up Yet

Changes usually sync within a minute or two. To sync right away, open the asset, click **Edit Settings**, then click **Refresh Data**. A full sync also runs at every **Force Sync Interval**.

#### My Screen Shows Old Files While It's Offline

If a screen loses its internet connection, it keeps playing the files it already has. It catches up once it's back online.

---

## Related Articles

Explore what else you can do with OptiSigns:

- [How to Use the OneDrive App](https://support.optisigns.com/hc/en-us/articles/360050665253)
- [How to Use the Dropbox App](https://support.optisigns.com/hc/en-us/articles/360050665413)
- [How to Use Google Sheets with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360056977214)
- [How to Use Google Slides with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360050642833)
- [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
- [Creating and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)
- [How to Create and Use the Split Screen App](https://support.optisigns.com/hc/en-us/articles/360026559573)
