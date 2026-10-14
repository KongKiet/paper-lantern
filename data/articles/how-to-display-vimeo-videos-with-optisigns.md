# How to Display Vimeo Videos with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/360016254994-How-to-Display-Vimeo-Videos-with-OptiSigns

Article ID: 360016254994

Locale: en-us

Updated at: 2026-10-13T17:40:15Z

---

### In this article, we'll show how to display Vimeo videos on your digital signs with OptiSigns, including private videos and videos with captions.

- [What You'll Need](#WhatYoullNeed)
- [Creating a Vimeo App](#CreatingAVimeoApp)
- [Displaying a Private Vimeo Video](#DisplayingAPrivateVimeoVideo)
- [Displaying Vimeo Videos with Captions](#DisplayingVimeoVideosWithCaptions)
- [Deploying a Vimeo App](#DeployingAVimeoApp)

With the Vimeo app, it's possible to play any Vimeo video on your digital signs. Paste the video's link into OptiSigns and it's ready to go on a screen, in a playlist or on a schedule. This article also covers how to play a video you've kept private on Vimeo, and how to show captions.

Let's get started.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- The link to the Vimeo video you want to display
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

---

<a name="CreatingAVimeoApp"></a>

## Creating a Vimeo App

First, open the video you want to display on **vimeo.com**. Copy its address from your browser's address bar. The number at the end is the video's ID.

![Vimeo video page with an arrow pointing to the video ID at the end of the vimeo.com URL](https://support.optisigns.com/hc/article_attachments/56378620575891)

|  |
| --- |
| **NOTE** |
| The Vimeo app accepts **vimeo.com** video links, such as **https://vimeo.com/449787858**. Links from **player.vimeo.com**, showcases or folders aren't accepted, and the app shows **Please enter a valid Vimeo video URL**. |

Next, go to the OptiSigns portal. Go to **Files/Assets** and select **Apps**.

![Files/Assets page with the Apps button highlighted](https://support.optisigns.com/hc/article_attachments/56378607718419)

Search for **Vimeo** and select the **Vimeo** app.

![Add App dialog searched for Vimeo, with the Vimeo app card highlighted](https://support.optisigns.com/hc/article_attachments/56378620578835)

The Vimeo app settings will open. Fill in the following:

- **Name** - The name of your Vimeo asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
- **URL** - The Vimeo video link you copied in the first step.

![Vimeo app form with Name and URL filled in and an arrow on Save](https://support.optisigns.com/hc/article_attachments/56378607720211)

Now hit **Save**. You'll have created a Vimeo app, and it will appear in your **Files/Assets**.

![New Vimeo asset shown in Files/Assets](https://support.optisigns.com/hc/article_attachments/56378620583443)

---

<a name="DisplayingAPrivateVimeoVideo"></a>

## Displaying a Private Vimeo Video

You don't have to make a video public on Vimeo to play it on your screens. In the video's privacy settings on Vimeo:

1. Under **Link**, select **Hide from Vimeo**.
2. Under **Embed**, set **Where can the video be embedded?** to **Specific domains** and add **social-player.optisigns.com**.

![Vimeo privacy panel with Hide from Vimeo and Embed: Specific domains highlighted](https://support.optisigns.com/hc/article_attachments/56378620584723)

The video stays hidden on Vimeo, but your OptiSigns screens can still play it. Then create and deploy the Vimeo app as normal.

---

<a name="DisplayingVimeoVideosWithCaptions"></a>

## Displaying Vimeo Videos with Captions

The Vimeo app doesn't have a captions setting. To show captions, use the **Streaming App** with a Vimeo player link that turns them on.

First, build the link from your video's ID (the number at the end of its vimeo.com link):

- **Captions you uploaded** - https://player.vimeo.com/video/VIDEO\_ID?autoplay=1&loop=1&texttrack=en
- **Vimeo's auto-generated captions** - https://player.vimeo.com/video/VIDEO\_ID?autoplay=1&loop=1&texttrack=en-x-autogen

Replace **VIDEO\_ID** with your video's ID. For another language, replace **en** with that language's code, as long as the video has captions in that language on Vimeo.

Next, go to **Files/Assets**, select **Apps**, then search for and select the **Streaming App**.

![Add App dialog searched for Streaming App, with its card highlighted](https://support.optisigns.com/hc/article_attachments/56378607725971)

Give the app a **Name**, paste your link into the **URL** field, then hit **Save**.

![Streaming App form with a Vimeo player URL filled in and an arrow on Save](https://support.optisigns.com/hc/article_attachments/56378607729299)

Deploy it to your screen the same way as a Vimeo app, described in **Deploying a Vimeo App** below.

---

<a name="DeployingAVimeoApp"></a>

## Deploying a Vimeo App

To push your Vimeo app to a screen, go to the **Screens** tab, then click **Edit** next to the screen you want to display it on.

![Screens list with an arrow on a screen's Edit button](https://support.optisigns.com/hc/article_attachments/56378620587283)

The **Edit Screen** pop-up will appear. Select **Asset** under **Content Type**, then hit **Change** next to **Selected Asset**.

![Edit Screen dialog with Content Type set to Asset and an arrow on Change](https://support.optisigns.com/hc/article_attachments/56378607735187)

The **Select Asset** window will open. Search for your Vimeo app, click it, then hit **Select**.

![Select Asset dialog with the Vimeo asset selected](https://support.optisigns.com/hc/article_attachments/56378607736339)

Back in **Edit Screen**, hit **Save**. Your Vimeo video will now play on your screen. This same process can be applied to a Streaming app if you're wanting to display your Vimeo video with captions.

Your Vimeo app can also be displayed in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).
