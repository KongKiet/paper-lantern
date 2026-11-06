# Video Codec or Video Playback Issues and How to Re-encode Videos

Article URL: https://support.optisigns.com/hc/en-us/articles/360038992973-Video-Codec-or-Video-Playback-Issues-and-How-to-Re-encode-Videos

Article ID: 360038992973

Locale: en-us

Updated at: 2026-11-05T22:37:38Z

---

### In this article, we'll explain why a video may not play, or play slowly, on your screen, and show how to fix it by switching video players or re-encoding the video.

- [What You'll Need](#WhatYoullNeed)
- [Try a Different Video Player](#TryADifferentVideoPlayer)
  - [Linux Players, Including the OptiSigns Pro Player and Raspberry Pi](#LinuxPlayersIncludingTheOptiSignsProPlayerAndRaspberryPi)
  - [Android Devices](#AndroidDevices)
- [Re-Encode the Video](#ReEncodeTheVideo)

Videos are compressed with a codec, such as H.264, HEVC (H.265), VP9, MPEG-4 or AV1. Whether a device can play a codec depends on its hardware. When your device can't decode a video, OptiSigns shows this message instead of the video:

![OptiSigns error screen saying the codec is not supported on your device and to encode the video in a supported format](https://support.optisigns.com/hc/article_attachments/57195697970707)

You may also see a video that plays slowly or drops frames. That happens when the device falls back to software decoding, or when the video's resolution or bit rate is too high for the hardware.

There are two ways to fix this: try a different video player, or re-encode the video into a format your device supports.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- Access to the screen in the OptiSigns portal, to change its video player
- To re-encode: a Windows, Mac or Linux computer and the free [HandBrake](https://handbrake.fr/) app

---

<a name="TryADifferentVideoPlayer"></a>

## Try a Different Video Player

Some OptiSigns players let you choose which video player plays your videos. A different player may support more codecs or play more smoothly on your hardware.

<a name="LinuxPlayersIncludingTheOptiSignsProPlayerAndRaspberryPi"></a>

### Linux Players, Including the OptiSigns Pro Player and Raspberry Pi

In the OptiSigns portal, edit the screen and open the **Advanced** section. Under **Video Player**, choose **HTML5 Video Player** or **MPV Player with hardware acceleration**, then save.

![Edit Screen Advanced section with the Video Player list open, showing Default, HTML5 Video Player and MPV Player](https://support.optisigns.com/hc/article_attachments/57195667168531)

|  |
| --- |
| **NOTE** |
| **Video Player** appears only for screens running the OptiSigns Linux player, and only on plans that include advanced device management. |

<a name="AndroidDevices"></a>

### Android Devices

On the screen, open the OptiSigns app's side menu and go to **Video Player Settings**. Under **Render Type**, switch from the default **Texture View** to **Surface View**. Some hardware is optimized only for Surface View, so this can improve playback.

![Video Player Settings dialog with Render Type set to Texture View and the Surface View option below](https://support.optisigns.com/hc/article_attachments/57195697973011)

---

<a name="ReEncodeTheVideo"></a>

## Re-Encode the Video

H.264 is the most widely supported codec, and VP9 and HEVC (H.265) are supported by most hardware too. Even so, a device may not support a particular video file. Amazon Fire TV, Android and Roku devices rely on hardware decoding, so they're the most likely to have trouble. Check the supported formats for [Amazon Fire TV](https://developer.amazon.com/docs/fire-tv/device-specifications.html) or [Roku](https://developer.roku.com/en-gb/docs/specs/streaming.md).

To fix it, re-encode the video into a format your device supports. [HandBrake](https://handbrake.fr/) is a free, popular app that does this on Windows, Mac and Linux.

Download HandBrake and open it. Drag your video file onto the **Or drop a file or folder here** area.

![HandBrake Source Selection screen with the Or drop a file or folder here area](https://support.optisigns.com/hc/article_attachments/57195697975315)

Open **Presets**, then **Devices**, and choose a preset for your device, such as **Amazon Fire**, **Android** or **Roku**. Pick the resolution you want, for example **1080p30**. The **General** presets work for most devices too.

![HandBrake Presets menu open on Devices, with arrows pointing to the Amazon Fire, Android and Roku presets](https://support.optisigns.com/hc/article_attachments/57195667175059)

Next to **Save As**, click **Browse** and choose where to save the new file. Then click **Start Encode**.

![HandBrake main window with arrows pointing to Start Encode and the Browse button next to Save As](https://support.optisigns.com/hc/article_attachments/57195697978003)

Encoding can take a while, depending on the video's length and quality and how fast your computer is.

When it's done, upload the new file to OptiSigns and add it to your playlists or screens. See [How to Upload & Manage Your Files and Assets](https://support.optisigns.com/hc/en-us/articles/360016247974).
