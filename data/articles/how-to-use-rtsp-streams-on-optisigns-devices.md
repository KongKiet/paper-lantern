# How to Use RTSP Streams on OptiSigns Devices

Article URL: https://support.optisigns.com/hc/en-us/articles/8098889840531-How-to-Use-RTSP-Streams-on-OptiSigns-Devices

Article ID: 8098889840531

Locale: en-us

Updated at: 2026-11-05T22:28:24Z

---

### In this article, we'll show how to display a live RTSP camera stream on your screens with the RTSP Stream app, on Android and Fire TV devices and on Windows or Raspberry Pi.

- [What You'll Need](#WhatYoullNeed)
- [Add the RTSP Stream App](#AddTheRTSPStreamApp)
- [Show an RTSP Stream on Windows or Raspberry Pi](#ShowAnRTSPStreamOnWindowsOrRaspberryPi)
  - [Convert the Stream in VLC](#ConvertTheStreamInVLC)
  - [Add the Stream to OptiSigns](#AddTheStreamToOptiSigns)
- [Troubleshooting](#Troubleshooting)

Show a live feed from an IP camera on your digital signs. The RTSP Stream app plays any RTSP stream, and once you've added it you can put it on as many screens as you like.

How you set it up depends on the device that plays it:

- **Android and Fire TV devices** - Play RTSP streams directly. You only need to add the RTSP Stream app.
- **Windows and Raspberry Pi** - Can't play RTSP directly, so the stream is first converted to HTTP with VLC Media Player.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- The RTSP URL of your camera or stream
- An OptiSigns device on the same network as the camera
- For Windows or Raspberry Pi: OptiSigns player version 5.3.2 or newer - [download the latest version](https://www.optisigns.com/download) - and a computer on the same network that can run [VLC Media Player](https://www.videolan.org/vlc/index.html)

---

<a name="AddTheRTSPStreamApp"></a>

## Add the RTSP Stream App

Sign in to [app.optisigns.com](https://app.optisigns.com), go to **Files/Assets** and click **Apps**. Search for **RTSP** and click **RTSP Stream**.

![Files/Assets page with the Add App dialog open, RTSP typed in search and the RTSP Stream app card](https://support.optisigns.com/hc/article_attachments/57195372552467)

Fill in the RTSP Stream settings:

- **Name** - The name you'll see in your asset list. It is not shown on your screens.
- **URL** - The RTSP URL of your stream, for example `rtsp://username:password@192.168.1.20:554/stream1`. The exact format depends on your camera; check its manual.

![RTSP Stream settings with Name and URL fields and a notice that the app plays on Android and Fire TV devices only](https://support.optisigns.com/hc/article_attachments/57195362992531)

Click **Save**. Your RTSP Stream is now an asset you can assign to screens, or add to a Playlist or Schedule. To change it later, click it in **Files/Assets**.

|  |
| --- |
| **NOTE** |
| The camera must be on the same network as your digital signage device. |

---

<a name="ShowAnRTSPStreamOnWindowsOrRaspberryPi"></a>

## Show an RTSP Stream on Windows or Raspberry Pi

![RTSP Stream app icon plus the OptiSigns icon, with Windows and Raspberry Pi logos](https://support.optisigns.com/hc/article_attachments/57195372555155)

Windows and Raspberry Pi players can't play RTSP directly. Instead, VLC Media Player on a computer on your network converts the RTSP stream to an HTTP stream, and OptiSigns plays that.

|  |
| --- |
| **IMPORTANT** |
| Keep VLC running on that computer. If VLC closes, the stream stops on your screens. |

<a name="ConvertTheStreamInVLC"></a>

### Convert the Stream in VLC

Open VLC Media Player, go to **Media** and click **Open Network Stream**.

![VLC Media menu with Open Network Stream highlighted](https://support.optisigns.com/hc/article_attachments/57195372555667)

On the **Network** tab, type your RTSP URL in **Please enter a network URL**.

![VLC Open Media dialog on the Network tab with an RTSP URL entered](https://support.optisigns.com/hc/article_attachments/57195372556051)

Click the arrow next to **Play** and select **Stream**.

![VLC Open Media dialog with the Play dropdown open and Stream highlighted](https://support.optisigns.com/hc/article_attachments/57195362997523)

Click **Next**.

![VLC Stream Output source step showing the RTSP URL with an arrow on Next](https://support.optisigns.com/hc/article_attachments/57195362998291)

In **New destination**, select **HTTP** and click **Add**.

![VLC Stream Output destination step with HTTP selected in the New destination list](https://support.optisigns.com/hc/article_attachments/57195363004435)

Type **9999** in **Port** and **/stream.ogv** in **Path**, then click **Next**. Your stream will be available at `http://<the computer's IP address>:9999/stream.ogv`.

![VLC HTTP destination with port 9999 and path /stream.ogv entered](https://support.optisigns.com/hc/article_attachments/57195363005203)

Under **Profile**, select **Video - Theora + Vorbis (OGG)** and click **Next**.

![VLC transcoding options with the Video - Theora + Vorbis (OGG) profile selected](https://support.optisigns.com/hc/article_attachments/57195363005587)

Check **Generated stream output string**: it must contain **vcodec=theo** and **mux=ogg**. Change it by hand if it doesn't. Then click **Stream**.

![VLC option setup showing the generated stream output string with Stream button](https://support.optisigns.com/hc/article_attachments/57195372563091)

VLC starts converting. The progress bar moves while it streams.

![VLC converting the RTSP stream with the progress bar running](https://support.optisigns.com/hc/article_attachments/57195363006483)

<a name="AddTheStreamToOptiSigns"></a>

### Add the Stream to OptiSigns

Add the RTSP Stream app as described in [Add the RTSP Stream App](#AddTheRTSPStreamApp). In **URL**, enter the HTTP address from VLC, `http://<the computer's IP address>:9999/stream.ogv`, instead of the RTSP URL.

![RTSP Stream settings with Mondo Cool as the name and an HTTP stream URL entered](https://support.optisigns.com/hc/article_attachments/57195363008403)

Click **Save**, then assign the RTSP Stream to your Windows or Raspberry Pi screen.

---

<a name="Troubleshooting"></a>

## Troubleshooting

Here are a few common issues our customers run into when using the RTSP app, and how to solve them.

#### The Stream Stays Black on an Android or Fire TV Device

Check that the RTSP URL plays in VLC on a computer on the same network. If it doesn't play there, the URL, the username and password, or the camera's network settings are wrong.

#### The Stream Doesn't Play on Windows or Raspberry Pi

Check that VLC is still running and streaming on the computer, that you entered the HTTP address rather than the RTSP URL, and that the player is version 5.3.2 or newer.

#### The Stream Plays in VLC but Not on the Screen

Check that the signage device is on the same network as the camera, or as the computer running VLC, and that no firewall blocks port 9999 on that computer.
