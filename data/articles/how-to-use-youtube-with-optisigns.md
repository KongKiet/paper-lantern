# How to Use YouTube with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/360051014713-How-to-Use-YouTube-with-OptiSigns

Article ID: 360051014713

Locale: en-us

Updated at: 2026-10-30T20:44:00Z

---

### In this article, we'll show how to display a YouTube video or Short on your digital signs with OptiSigns.

- [What You'll Need](#WhatYoullNeed)
- [Which YouTube App Should I Use?](#WhichYouTubeAppShouldIUse)
- [Creating a YouTube App](#CreatingAYouTubeApp)
  - [Display Options](#DisplayOptions)
  - [Playback Options](#PlaybackOptions)
- [Deploying a YouTube App](#DeployingAYouTubeApp)
- [Troubleshooting](#Troubleshooting)

With the YouTube app, you can play any public YouTube video or Short on your digital signs. Paste the video's link, choose which part of it to play, and assign it to your screens or add it to a Playlist.

Let's get started.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account - any plan
- A link to a public or unlisted YouTube video or Short
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

---

<a name="WhichYouTubeAppShouldIUse"></a>

## Which YouTube App Should I Use?

OptiSigns has five YouTube apps. Pick the one that matches what you want to show:

![Add App dialog searched for YouTube, showing the five YouTube apps](https://support.optisigns.com/hc/article_attachments/56995007312531)

- **YouTube** - Plays a single video or Short. You paste the video's link. This is the app covered in this article.
- **YouTube Playlist** - Plays every video in a YouTube playlist, in order or shuffled. You paste the playlist's link. See [How to Use the YouTube Playlist App with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360059386254).
- **YouTube Channel** - Plays the videos from a YouTube channel. You paste the channel's link. See [How to Use YouTube Channel with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360060202914).
- **YouTube Live Schedule** - Switches your screens to a channel's live stream at the times you schedule. You paste the channel's link or sign in with Google. See [How to Use YouTube Live Schedule with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360060284174).
- **YouTube Dashboard** - Shows your channel's YouTube Analytics as a dashboard. You sign in with Google. Requires the Standard plan or higher. See [How to Use the YouTube Dashboard App](https://support.optisigns.com/hc/en-us/articles/48626115821459).

|  |
| --- |
| **TIP** |
| To show a stream that is live right now, paste its link into the YouTube app like any other video. To have your screens tune in whenever a channel goes live, use YouTube Live Schedule. |

---

<a name="CreatingAYouTubeApp"></a>

## Creating a YouTube App

From the OptiSigns portal, go to **Files/Assets** and select **Apps**.

![OptiSigns Files/Assets page with the Apps button highlighted](https://support.optisigns.com/hc/article_attachments/56994997158675)

Search for **YouTube** and select the **YouTube** app.

The YouTube app settings will open. Fill in the following:

![YouTube app form with a video link in the URL field and the Name filled in with the video's title](https://support.optisigns.com/hc/article_attachments/56994997159315)

- **Name** - The name of your YouTube asset. This is for organizational purposes within OptiSigns only and will not display on your screens. It fills in with the video's title as soon as you paste the link, and you can change it to anything you like.
- **URL** - The link to your YouTube video. This is the only required field. You can paste:
  - A regular video link
  - A share link
  - A YouTube Shorts link

Links with extra parts work as pasted.

|  |
| --- |
| **NOTE** |
| A timestamp in the link does not set where the video starts. It is removed when you paste the link. To start partway through, use **Start At** under Playback Options below. |

Once the link is recognized, the video loads in the preview on the right, paused on its first frame. Click the play button to watch it and check it's the right one.

![The YouTube video loaded in the preview pane, paused with a play button in the center](https://support.optisigns.com/hc/article_attachments/56995007323923)

Use the picker at the top right to see how the video will look on your screen: **Landscape (16:9)**, **Portrait (9:16)** or **Custom**. The picker only changes the preview. It is not saved with the video.

![Preview orientation picker open, showing Landscape (16:9), Portrait (9:16) and Custom](https://support.optisigns.com/hc/article_attachments/56995007325459)

<a name="DisplayOptions"></a>

### Display Options

Click **Display options** for more options:

![Display options section open, showing the Caption and Mute toggles, both off](https://support.optisigns.com/hc/article_attachments/56994997162771)

- **Caption** - Show the video's closed captions on your screen. Captions must be added to the video by its owner. When Caption is off, YouTube's auto-generated captions are hidden too. Learn more about [showing YouTube captions](https://support.optisigns.com/hc/en-us/articles/360051014773).
- **Mute** - Play the video without sound.

Both are off by default.

<a name="PlaybackOptions"></a>

### Playback Options

Playback Options lets you play just part of a video. It appears once the video has loaded:

![Playback options with Start At set to 0:30 and End At set to 2:00, the filmstrip bar highlighting that part of the video](https://support.optisigns.com/hc/article_attachments/56994997166867)

- **Start At** - Skip the beginning of the video.
- **End At** - Stop the video before it ends. It starts out set to the full length of the video.

Type a time in seconds or in minutes and seconds, such as `90`, `1:30` or `1m30s`. You can also drag the handles on the filmstrip bar below to choose the part you want. Click **Reset** to go back to the full video.

On its own, the video loops back to Start At each time it reaches End At. In a Playlist, it plays only the part you chose, and the Playlist counts just that part toward its length.

|  |
| --- |
| **NOTE** |
| Playback Options does not appear for a live stream, as a live stream has no fixed length. |

Now hit **Save**. You'll have created a YouTube app, and it will appear in your **Files/Assets**.

![The saved YouTube video, Mondo Cool Video, shown as a card in Files/Assets](https://support.optisigns.com/hc/article_attachments/56995007328403)

---

<a name="DeployingAYouTubeApp"></a>

## Deploying a YouTube App

To push your YouTube app to a screen, go to the **Screens** tab, then click **Edit** next to the screen you want to display it on.

![Screens list with the Edit button highlighted on a screen row](https://support.optisigns.com/hc/article_attachments/56994997171603)

The **Edit Screen** pop-up will appear. Select **Asset** under **Content Type**, then hit **Change** next to **Selected Asset**.

![Edit Screen dialog with Content Type set to Asset and the Change button highlighted](https://support.optisigns.com/hc/article_attachments/56995007331347)

The **Select Asset** window will open. Search for your YouTube app, click it, then hit **Select**.

![Select Asset dialog with the Mondo Cool Video YouTube asset selected](https://support.optisigns.com/hc/article_attachments/56995007332243)

Back in **Edit Screen**, hit **Save**. Your YouTube video will now play on your screen.

Your YouTube app can also be displayed in a [Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843) or [Schedule](https://support.optisigns.com/hc/en-us/articles/360016981853), or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).

---

<a name="Troubleshooting"></a>

## Troubleshooting

These are some of the messages that may appear when setting up a YouTube app, and how to solve them.

#### "Please enter a valid YouTube URL"

The link is not one the app accepts. Use a regular video, share or Shorts link. Live and embed links are not accepted. Open the stream on YouTube and copy its regular "watch" link instead.

#### "Couldn't find YouTube video"

The link is missing the video's ID. Copy the link again from YouTube and check it is complete.

#### "YouTube doesn't allow embedding, please contact the owner of the Video."

The video's owner has turned off embedding, so it can't play outside YouTube. Ask the owner to allow embedding, or choose another video.

#### "Longer than the video" or "Past the end of the video"

A Start At or End At time is past the end of the video, so the app changed it for you. Check both times before you save.

#### "You have both Background Music and YouTube or other streaming content in this playlist."

This is a warning, not an error. Your Playlist will still play, but its Background Music may not play while the YouTube video is playing.

#### The video doesn't play on my screen

Check that the video is public or unlisted, not private or deleted, and that the device is connected to the internet.
