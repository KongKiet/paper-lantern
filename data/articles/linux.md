# Linux

Article URL: https://support.optisigns.com/hc/en-us/articles/360034379573-Linux

Article ID: 360034379573

Locale: en-us

Updated at: 2026-10-28T20:03:55Z

---

### In this article, we'll install the OptiSigns player on a Linux computer and get it ready to pair with your account.

- [Download the AppImage](#DownloadTheAppImage)
- [Make the AppImage Executable](#MakeTheAppImageExecutable)
- [Ubuntu 24.04 and Later: Install libfuse2](#Ubuntu2404AndLaterInstallLibfuse2)
- [Open the Player and Pair It](#OpenThePlayerAndPairIt)
- [Use the Player Menu](#UseThePlayerMenu)
- [Configure AutoStart on Ubuntu 24.04 and Later](#StartThePlayerAutomaticallyOnUbuntu2404AndLater)
- [Play Video with mpv](#PlayVideoWithMpv)
- [Hide the Ubuntu Dock and Top Bar](#HideTheUbuntuDockAndTopBar)
- [Next Steps](#NextSteps)

The OptiSigns player runs on any Linux computer and turns it into a digital signage player. It comes as an AppImage, a single file that runs on all major distributions, including Ubuntu, Debian, Fedora, Red Hat and Arch Linux, without installing anything.

---

<a name="DownloadTheAppImage"></a>

## Download the AppImage

Download the AppImage that matches your computer's processor:

- **64-bit PC (Intel or AMD):** [Download for x86\_64](https://links.optisigns.com/linux-64)
- **ARM 64-bit** (for example a Raspberry Pi running a 64-bit OS): [Download for ARM64](https://links.optisigns.com/arm64)
- **ARM 32-bit** (for example a Raspberry Pi running a 32-bit OS): [Download for ARMv7](https://links.optisigns.com/rpi)

**Note:** There is no version for 32-bit Intel or AMD PCs.

---

<a name="MakeTheAppImageExecutable"></a>

## Make the AppImage Executable

1. Open the folder you downloaded the AppImage to.

![Ubuntu Files app showing the downloaded OptiSigns AppImage in the Downloads folder](https://support.optisigns.com/hc/article_attachments/56917158194451)

2. Right-click the AppImage and select **Properties**.

![Right-click menu on the OptiSigns AppImage with Properties highlighted](https://support.optisigns.com/hc/article_attachments/56917158197139)

3. Make sure **Permissions** is set to **Read and Write**, and switch **Executable as Program** on.

![AppImage Properties with Permissions set to Read and Write and Executable as Program switched on](https://support.optisigns.com/hc/article_attachments/56917158198163)

**Tip:** You can do the same thing in a terminal with `chmod +x optisigns-*.AppImage`.

---

<a name="Ubuntu2404AndLaterInstallLibfuse2"></a>

## Ubuntu 24.04 and Later: Install libfuse2

AppImages need the libfuse2 library, which Ubuntu 24.04 and later don't include. If you're on one of these versions, open a terminal and run:

```
sudo apt install libfuse2
```

![Ubuntu Terminal with the command sudo apt install libfuse2](https://support.optisigns.com/hc/article_attachments/56917158202131)

On other distributions, install your distribution's FUSE 2 package if the AppImage doesn't open.

---

<a name="OpenThePlayerAndPairIt"></a>

## Open the Player and Pair It

1. Double-click the AppImage.
2. Your desktop may ask whether to integrate the AppImage with your system. Select **Yes** to add OptiSigns to your applications menu. This is optional; you can always open the player by double-clicking the AppImage.

![Install prompt asking to integrate the OptiSigns AppImage with the system, with an arrow on Yes](https://support.optisigns.com/hc/article_attachments/56917158204307)

3. The player opens full screen and shows a pairing code. Go to [app.optisigns.com](https://app.optisigns.com/) and add a screen with this code. For the details, see [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813).

![OptiSigns player showing a pairing code, with an arrow on the menu button at the top right](https://support.optisigns.com/hc/article_attachments/56917175998099)

---

<a name="UseThePlayerMenu"></a>

## Use the Player Menu

Move the mouse to show three buttons at the top right of the player: **Exit Fullscreen**, **Menu** and **Close**. Select **Menu** to open the side menu.

![OptiSigns player side menu with Orientation, Restart, AutoStart and Fullscreen on Startup](https://support.optisigns.com/hc/article_attachments/56917158208915)

The side menu includes:

- **Orientation:** rotate the content to match how the screen is mounted.
- **Restart:** restart the player at a set time each day.
- **AutoStart:** open the player when the computer starts. On by default.
- **Fullscreen on Startup:** open the player full screen. On by default.
- **Advanced Options:** more settings, including **Video Player**.

---

<a name="StartThePlayerAutomaticallyOnUbuntu2404AndLater"></a>

## Configure AutoStart on Ubuntu 24.04 and Later

**AutoStart** is on by default, so the player normally starts with the computer. On Ubuntu 24.04 and later, the player also needs the `--no-sandbox` option to start, which the AutoStart entry doesn't include. Add your own startup entry instead:

1. Open **Startup Applications**. You'll see the player's own entry, **OptiSigns Digital Signage**.

![Startup Applications Preferences listing the OptiSigns Digital Signage startup script](https://support.optisigns.com/hc/article_attachments/56917176003603)

2. Select **Add**.
3. Enter any **Name** and **Comment**. In **Command**, enter the full path to the AppImage followed by `--no-sandbox`, for example:

```
/home/<your-user>/Downloads/optisigns-5.6.33-x86_64.AppImage --no-sandbox
```

![Add Startup Program dialog with the OptiSigns AppImage command ending in --no-sandbox](https://support.optisigns.com/hc/article_attachments/56917176007571)

4. Select **Add**.
5. In the player's side menu, switch **AutoStart** off. This removes the player's own entry, so only yours starts the player.

**Note:** Don't just delete the player's own entry in Startup Applications. While **AutoStart** is on, the player adds it back every time it opens.

---

<a name="PlayVideoWithMpv"></a>

## Play Video with MPV

If videos stutter, or you play several high-resolution videos at once, install the MPV video player. OptiSigns finds it automatically and uses it to play video.

1. If your computer has an Intel processor, install Intel's video driver:

```
sudo apt install intel-media-va-driver-non-free
```

2. Install MPV:

```
sudo apt install mpv
```

3. Restart the player. To check which video player it uses, open the side menu and go to **Advanced Options** > **Video Player**. Select **MPV Video Player**.

---

<a name="HideTheUbuntuDockAndTopBar"></a>

## Hide the Ubuntu Dock and Top Bar

So the desktop doesn't show around your content:

1. Open **Settings** > **Ubuntu Desktop** and switch **Auto-hide the Dock** on.

![Ubuntu Settings, Ubuntu Desktop page, with Auto-hide the Dock switched on](https://support.optisigns.com/hc/article_attachments/56917176008851)

2. Install the Extension Manager:

```
sudo apt install gnome-shell-extension-manager
```

3. Open **Extension Manager**, select **Browse** and search for **Hide Top Bar**. Select **Install**.

![Extension Manager search results with Install highlighted on the Hide Top Bar extension](https://support.optisigns.com/hc/article_attachments/56917158214931)

---

<a name="NextSteps"></a>

## Next Steps

Now that your player is paired, add content to it:

- [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
- [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
- [Creating and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)

If you have questions or feedback, contact our support team at support@optisigns.com.
