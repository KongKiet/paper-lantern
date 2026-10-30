# Raspberry Pi

Article URL: https://support.optisigns.com/hc/en-us/articles/360034379693-Raspberry-Pi

Article ID: 360034379693

Locale: en-us

Updated at: 2026-10-29T17:18:19Z

---

### In this article, we'll get the OptiSigns player running on a Raspberry Pi and pair it with your OptiSigns account.

- [Choose How to Install OptiSigns](#ChooseHowToInstallOptiSigns)
- [Use the Prebuilt SD Card Image](#UseThePrebuiltSDCardImage)
- [Install the AppImage on Raspberry Pi OS](#InstallTheAppImageOnRaspberryPiOS)
  - [Set Up Raspberry Pi OS](#SetUpRaspberryPiOS)
  - [Install FUSE](#InstallFUSE)
  - [Download the AppImage and Run It](#DownloadTheAppImageAndRunIt)
- [Use the Player Menu](#UseThePlayerMenu)
- [Pair the Player with Your Account](#PairThePlayerWithYourAccount)
- [Choose a Video Player](#ChooseAVideoPlayer)
- [What Your Raspberry Pi Player Does](#WhatYourRaspberryPiPlayerDoes)
- [Limitations of OptiSigns on Raspberry Pi](#LimitationsOfOptiSignsOnRaspberryPi)
- [More Raspberry Pi Guides](#MoreRaspberryPiGuides)
- [Next Steps](#NextSteps)

The OptiSigns player runs on a Raspberry Pi and turns it into a digital signage player. We recommend a Raspberry Pi 3B+ or newer.

---

<a name="ChooseHowToInstallOptiSigns"></a>

## Choose How to Install OptiSigns

There are two ways to get OptiSigns on a Raspberry Pi:

- **Use our prebuilt SD card image.** OptiSigns comes already installed. This is the quickest way to set up a new Raspberry Pi.
- **Install the AppImage on Raspberry Pi OS.** Use this if your Raspberry Pi already runs Raspberry Pi OS.

---

<a name="UseThePrebuiltSDCardImage"></a>

## Use the Prebuilt SD Card Image

1. Download the SD card image for your model: - [Raspberry Pi 4 or older](https://links.optisigns.com/rpi-image) ([MD5 checksum](https://download.optisignsapp.com/RPi/player-2435240-rpi4.zip.md5)) - [Raspberry Pi 5](https://links.optisigns.com/rpi5-image) ([MD5 checksum](https://download.optisignsapp.com/RPi/player-2435240-rpi5.zip.md5))
2. Unzip the download. You'll need an SD card of at least 16 GB.
3. [Download and install balenaEtcher](https://etcher.balena.io/).

![balenaEtcher download page with the Download Etcher button](https://support.optisigns.com/hc/article_attachments/56949247172883)

**Note:** You can use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) instead of balenaEtcher. Raspberry Pi Imager also lets you set up Wi-Fi before you flash the card.

4. Open balenaEtcher, select **Flash from file** and choose the OptiSigns .img file you unzipped.

![balenaEtcher with an arrow on the Flash from file button](https://support.optisigns.com/hc/article_attachments/56949224870547)

5. Select **Select target** and choose your SD card.

![balenaEtcher with an image chosen and an arrow on the Select target button](https://support.optisigns.com/hc/article_attachments/56949247176851)

6. Select **Flash!**.

![balenaEtcher with an image and SD card chosen and an arrow on the Flash button](https://support.optisigns.com/hc/article_attachments/56949247177875)

7. Put the SD card in your Raspberry Pi, start it up and connect it to your network.

OptiSigns is already installed and opens by itself each time the Raspberry Pi starts. It shows a pairing code. Skip to **Pair the Player with Your Account** below.

---

<a name="InstallTheAppImageOnRaspberryPiOS"></a>

## Install the AppImage on Raspberry Pi OS

If your Raspberry Pi already runs Raspberry Pi OS with the desktop, start at **Install FUSE** below.

<a name="SetUpRaspberryPiOS"></a>

### Set Up Raspberry Pi OS

1. Download Raspberry Pi OS with desktop and recommended software: - [64-bit, for Raspberry Pi 5](https://downloads.raspberrypi.com/raspios_full_arm64/images/raspios_full_arm64-2024-07-04/2024-07-04-raspios-bookworm-arm64-full.img.xz) - [32-bit, for Raspberry Pi 4 or older](https://downloads.raspberrypi.com/raspios_full_armhf/images/raspios_full_armhf-2024-07-04/2024-07-04-raspios-bookworm-armhf-full.img.xz)

|  |
| --- |
| **IMPORTANT** |
| For Raspberry Pi 5, use the 64-bit OS for the best performance. For Raspberry Pi 4 or older we recommend the 32-bit OS, but the 64-bit OS also works. |

2. Flash the image to your SD card with balenaEtcher, the same way as above.

![balenaEtcher ready to flash a Raspberry Pi OS image, with an arrow on the Flash button](https://support.optisigns.com/hc/article_attachments/56949247180179)

3. Start the Raspberry Pi. To connect to your network, select the network icon at the top right of the desktop.

![Raspberry Pi OS taskbar with an arrow on the network icon](https://support.optisigns.com/hc/article_attachments/56949247184531)

For more help, see [How To Connect To WiFi For Raspberry Pi](https://support.optisigns.com/hc/en-us/articles/360056627833).

<a name="InstallFUSE"></a>

### Install FUSE

AppImages need FUSE to run. You need a network connection for this step.

1. Open **Terminal** from the taskbar.

![Raspberry Pi OS taskbar with an arrow on the Terminal icon](https://support.optisigns.com/hc/article_attachments/56949247186067)

![Raspberry Pi OS Terminal window with an empty command prompt](https://support.optisigns.com/hc/article_attachments/56949224891027)

2. Run:

```
sudo apt install -y fuse
```

<a name="DownloadTheAppImageAndRunIt"></a>

### Download the AppImage and Run It

1. Download the AppImage that matches your operating system: - **64-bit Raspberry Pi OS** (recommended for Raspberry Pi 5): [Download for ARM64](https://links.optisigns.com/arm64) - **32-bit Raspberry Pi OS** (Raspberry Pi 4 or older): [Download for ARMv7](https://links.optisigns.com/rpi)

An AppImage is a single file that runs the app without installing anything, like an .exe file on Windows.

2. Open the **File Manager** and go to the folder you downloaded the AppImage to.

![Raspberry Pi File Manager showing the OptiSigns AppImage in the Downloads folder](https://support.optisigns.com/hc/article_attachments/56949247188627)

3. Right-click the AppImage and select **Properties**.
4. Open the **Permissions** tab. Set **View content**, **Change content** and **Execute** to **Anyone**, then select **OK**.

![AppImage File Properties, Permissions tab, with View content, Change content and Execute set to Anyone](https://support.optisigns.com/hc/article_attachments/56949224894739)

**Tip:** You can do the same thing in a terminal with `chmod +x optisigns-*.AppImage`.

5. Double-click the AppImage. If you're asked what to do with the file, select **Execute**.

The player can take a few seconds to open on a Raspberry Pi. It opens full screen and shows a pairing code. Keep it on screen; you'll need it to pair.

![OptiSigns player showing a pairing code, with an arrow on the menu button at the top right](https://support.optisigns.com/hc/article_attachments/56949224895763)

---

<a name="UseThePlayerMenu"></a>

## Use the Player Menu

Move the mouse to show three buttons at the top right of the player: **Exit Fullscreen**, **Menu** and **Close**. Select **Menu** to open the side menu.

![OptiSigns player side menu with Orientation, Restart, AutoStart and Fullscreen on Startup](https://support.optisigns.com/hc/article_attachments/56949247196819)

The side menu includes:

- **Orientation:** rotate the content to match how the screen is mounted.
- **Restart:** restart the player at a set time each day.
- **AutoStart:** open the player when the Raspberry Pi starts. On by default.
- **Fullscreen on Startup:** open the player full screen. On by default.
- **Advanced Options:** more settings, including **Video Player**.

Because **AutoStart** is on by default, OptiSigns opens by itself the next time the Raspberry Pi starts.

---

<a name="PairThePlayerWithYourAccount"></a>

## Pair the Player with Your Account

1. Go to [app.optisigns.com](https://app.optisigns.com/) and log in. If you don't have an account yet, select **Create Account**. You can also log in with Google, Microsoft or Facebook.

![OptiSigns portal log-in page with Google, Microsoft, Facebook and SSO options](https://support.optisigns.com/hc/article_attachments/56949224902931)

2. On the **Screens** page, select **Add Screen**.

![Screens page toolbar with an arrow on the Add Screen button](https://support.optisigns.com/hc/article_attachments/56949247199251)

3. Enter the pairing code shown on the player in **Pair code**, then select **Pair**.

![Add Screen dialog with a pair code entered and the Pair button highlighted](https://support.optisigns.com/hc/article_attachments/56949247200531)

**Note:** Codes are case-sensitive, and the portal enters them in capitals. If the code on your player has lowercase letters, select **Use lowercase pairing code** and type it exactly as shown. If pairing fails with a case error, the portal switches this on for you, so check the code and select **Pair** again.

The player changes to show that it's paired.

![OptiSigns player showing Paired](https://support.optisigns.com/hc/article_attachments/56949247201811)

---

<a name="ChooseAVideoPlayer"></a>

## Choose a Video Player

The player picks the video player it uses. To check or change it, open the side menu and go to **Advanced Options** > **Video Player**.

- **MPV Video Player:** appears when mpv is installed. To install it, run `sudo apt install mpv`, then restart the player.
- **OMX Player with hardware acceleration:** appears only when omxplayer is installed on the Raspberry Pi.

**Note:** On Linux, including Raspberry Pi, the player turns off graphics hardware acceleration by default. To give the Raspberry Pi's graphics more memory, see [Adjust the GPU memory on the Raspberry Pi](https://support.optisigns.com/hc/en-us/articles/1500010436341).

---

<a name="WhatYourRaspberryPiPlayerDoes"></a>

## What Your Raspberry Pi Player Does

Once it's set up, your Raspberry Pi works as a digital signage player:

- It starts OptiSigns when it powers on.
- It resumes playing its assigned content after a power cut.
- It keeps the display from going to sleep.
- It keeps playing downloaded content, such as images, videos and documents, when the internet connection drops.

---

<a name="LimitationsOfOptiSignsOnRaspberryPi"></a>

## Limitations of OptiSigns on Raspberry Pi

Raspberry Pi runs OptiSigns well in most cases, but keep these limits in mind:

- **Video decoding:** Raspberry Pi 5 decodes only HEVC video in hardware. Apps such as YouTube and Vimeo use software decoding, so they play in lower quality.
- **Video quality:** Raspberry Pi isn't built for heavy video playback. We don't recommend videos above 1080p.

---

<a name="MoreRaspberryPiGuides"></a>

## More Raspberry Pi Guides

- [Install/Update OptiSigns player on RPi via script](https://support.optisigns.com/hc/en-us/articles/1500009382101)
- [How to mass deploy OptiSigns on Raspberry Pi devices](https://support.optisigns.com/hc/en-us/articles/360063098753)
- [Clean install OptiSigns on Raspberry Pi/Linux](https://support.optisigns.com/hc/en-us/articles/4411956075027)

---

<a name="NextSteps"></a>

## Next Steps

Your player is ready to show content. To get started:

- [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
- [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
- [Creating and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)
- [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)

If you have questions or feedback, contact our support team at support@optisigns.com.
