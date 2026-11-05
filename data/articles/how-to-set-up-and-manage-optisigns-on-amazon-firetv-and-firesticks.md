# How to Set Up and Manage OptiSigns on Amazon FireTV and Firesticks

Article URL: https://support.optisigns.com/hc/en-us/articles/360016174554-How-to-Set-Up-and-Manage-OptiSigns-on-Amazon-FireTV-and-Firesticks

Article ID: 360016174554

Locale: en-us

Updated at: 2026-11-04T17:44:59Z

---

### In this article, we'll show how to set up OptiSigns on an Amazon Fire TV or Fire TV Stick, and how to look after the device from its own Settings menu.

- [Which Fire TV Devices Work with OptiSigns?](#WhichFireTVDevicesWorkWithOptiSigns)
- [What You'll Need](#WhatYoullNeed)
- [Setting Up Your Fire TV](#SettingUpYourFireTV)
- [Installing the OptiSigns App](#InstallingTheOptiSignsApp)
- [Pairing Your Fire TV with OptiSigns](#PairingYourFireTVWithOptiSigns)
- [Managing Your Fire TV](#ManagingYourFireTV)
  - [Keep OptiSigns Running](#KeepOptiSignsRunning)
  - [Allow OptiSigns to Use Storage](#AllowOptiSignsToUseStorage)
  - [Clear the OptiSigns App's Cache or Data](#ClearTheOptiSignsAppsCacheOrData)
  - [Turn On Automatic App Updates](#TurnOnAutomaticAppUpdates)
  - [Update Fire OS](#UpdateFireOS)
  - [Change the Time Zone](#ChangeTheTimeZone)
  - [Reinstall the OptiSigns App](#ReinstallTheOptiSignsApp)
  - [Install the OptiSigns App from an APK File](#InstallTheOptiSignsAppFromAnAPKFile)
  - [Factory Reset Your Fire TV](#FactoryResetYourFireTV)
- [Connecting a Keyboard and Mouse](#ConnectingAKeyboardAndMouse)
- [Restarting OptiSigns Remotely](#RestartingOptiSignsRemotely)
- [Troubleshooting](#Troubleshooting)

Turn a TV with an Amazon Fire TV Stick into a digital sign. Install the OptiSigns app from the Amazon Appstore, pair it with your account, and manage what it shows from the OptiSigns portal.

This article also covers the Fire TV settings that keep OptiSigns running smoothly, from clearing the app's cache to a full factory reset.

|  |
| --- |
| **IMPORTANT** |
| Amazon is removing digital signage support from Fire TV devices, and OptiSigns will end support for Fire TV Sticks in the near future. For a new screen, we recommend the [OptiSigns Android Stick Player](https://links.optisigns.com/szzk) or the [Amazon Signage Stick](https://support.optisigns.com/hc/en-us/articles/34087061669523). |

---

<a name="WhichFireTVDevicesWorkWithOptiSigns"></a>

## Which Fire TV Devices Work with OptiSigns?

Whether a Fire TV can run OptiSigns unattended depends on its operating system:

- **Fire OS 7** - Works, including starting OptiSigns automatically when the device powers on. This covers the Fire TV Stick 4K (Gen 1), older Fire TV Sticks and the [Fire TV Stick Lite](https://www.amazon.com/fire-tv-stick-lite-latest-alexa-voice-remote-lite/dp/B091G4YP57/). The Lite is slow, so we don't recommend it even though it works. Amazon may update these devices to a newer OS in the future.
- **Fire OS 8** - Not supported. Since October 2024, [Amazon no longer lets apps start automatically](https://www.aftvnews.com/amazon-blocks-long-running-fire-tv-capability-breaking-popular-apps-with-no-warning-and-giving-developers-the-runaround/) on Fire OS 8. This covers the current [Fire TV Stick 4K](https://www.amazon.com/all-new-amazon-fire-tv-stick-4k/dp/B0BP9MDCQZ/), the [Fire TV Stick 4K Max](https://www.amazon.com/all-new-amazon-fire-tv-stick-4k-max/dp/B0BP9SNVH9/) and TVs with Fire TV built in. If you are comfortable with ADB commands, see [How to Enable Auto-Start on Fire OS 8 Devices](https://support.optisigns.com/hc/en-us/articles/23274673797139).
- **Vega OS** - Works with limits. This covers the [Fire TV Stick 4K Select](https://amzn.to/3PaJaRD) and the [Fire TV Stick HD](https://amzn.to/4efNBop). OptiSigns must be opened by hand each time the device starts, and the app goes to sleep unless a video plays every few minutes, so it can't show images on their own. Add at least one video to your Playlist, between your images.

If you already have a Fire OS 7 device, read on to set it up.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account - any plan
- An Amazon Fire TV Stick or Fire TV running Fire OS 7 or Vega OS
- The power adapter and cable that came with your Fire TV
- A Wi-Fi connection and an Amazon account
- A TV with a free HDMI port

---

<a name="SettingUpYourFireTV"></a>

## Setting Up Your Fire TV

Plug the Fire TV Stick into your TV's HDMI port and connect it to power.

|  |
| --- |
| **NOTE** |
| Use the power adapter and cable that came with the Fire TV. It's tempting to power it from the TV's USB port, but a TV's USB port can't supply enough power to keep a Fire TV running reliably. |

![Hand plugging an Amazon Fire TV Stick into an HDMI port on the back of a TV](https://support.optisigns.com/hc/article_attachments/57143071744147)

Turn on the Fire TV and follow the on-screen instructions to connect to Wi-Fi and sign in with your Amazon account. The Fire TV needs an internet connection to work.

---

<a name="InstallingTheOptiSignsApp"></a>

## Installing the OptiSigns App

On the Fire TV home screen, go to **Find** and select **Search**.

![Fire TV home screen with Find selected and the Search tile highlighted](https://support.optisigns.com/hc/article_attachments/57143071745939)

Type **OptiSigns**. Fire TV search can be fiddly while you type, so once you've entered the name, press down on the remote until **Optisigns** is highlighted, then select it.

![Fire TV on-screen keyboard with Optisigns typed and the Optisigns search suggestion below](https://support.optisigns.com/hc/article_attachments/57143088510099)

Select **Download** on the OptiSigns Digital Signage app.

![OptiSigns Digital Signage app page in the Amazon Appstore with the Download button highlighted](https://support.optisigns.com/hc/article_attachments/57143088511763)

Once the app is installed, open it. It asks whether to start automatically when the device starts up. Select **Yes**, unless you want to open the app by hand every time.

---

<a name="PairingYourFireTVWithOptiSigns"></a>

## Pairing Your Fire TV with OptiSigns

When the app opens, it shows a pairing code:

![OptiSigns pairing screen on the TV showing a six-character pair code and app.optisigns.com](https://support.optisigns.com/hc/article_attachments/57143088512147)

On your computer, go to [app.optisigns.com](https://app.optisigns.com/app/screenManagement) and sign in. If you don't have an account yet, you can create one, or sign in with Google, Facebook or Microsoft.

![OptiSigns portal sign-in page with Google, Facebook, Microsoft and email sign-in options](https://support.optisigns.com/hc/article_attachments/57143071757331)

On the **Screens** page, click **Add Screen**.

![OptiSigns Screens page with the Add Screen button highlighted](https://support.optisigns.com/hc/article_attachments/57143088512915)

Type the pair code shown on your TV, then click **Pair**.

![Add Screen dialog with a pair code entered in the Pair code field](https://support.optisigns.com/hc/article_attachments/57143088513939)

The TV now shows **Paired**, and you're ready to assign content.

![TV screen showing Paired after the Fire TV was paired with OptiSigns](https://support.optisigns.com/hc/article_attachments/57143088514323)

To get content onto your new screen, see:

- [Set Up & Add a Screen](https://support.optisigns.com/hc/en-us/articles/360016374813)
- [How to Upload & Manage Your Files/Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
- [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
- [Creating and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)

---

<a name="ManagingYourFireTV"></a>

## Managing Your Fire TV

Everything in this section starts from the Fire TV's **Settings**. Press **Home** on the remote, then select the gear icon at the right of the menu bar.

![Fire TV home screen with the Settings gear icon highlighted at the right of the menu bar](https://support.optisigns.com/hc/article_attachments/57143088514963)

<a name="KeepOptiSignsRunning"></a>

### Keep OptiSigns Running

A Fire TV can pause OptiSigns after 4 hours without a button press and ask "Are you still watching?". To stop it, turn off **Still Watching**.

In **Settings**, select **Preferences**.

![Fire TV Settings with the Preferences tile highlighted](https://support.optisigns.com/hc/article_attachments/57143071762963)

Select **Data Usage Monitoring**.

![Fire TV Preferences menu with Data Usage Monitoring highlighted](https://support.optisigns.com/hc/article_attachments/57143071763347)

Select **Still Watching** to turn it **OFF**.

![Data Usage Monitoring menu with Still Watching set to OFF](https://support.optisigns.com/hc/article_attachments/57143088517523)

Open OptiSigns again. It won't be interrupted by the prompt anymore.

<a name="AllowOptiSignsToUseStorage"></a>

### Allow OptiSigns to Use Storage

OptiSigns downloads your images and videos to the device before playing them. If it isn't allowed to use the Fire TV's storage, your screen can stay black.

In **Settings**, select **Applications**.

![Fire TV Settings with the Applications tile highlighted](https://support.optisigns.com/hc/article_attachments/57143071769619)

Select **Manage Installed Applications**.

![Fire TV Applications menu with Manage Installed Applications highlighted](https://support.optisigns.com/hc/article_attachments/57143071770643)

Select **OptiSigns**.

![Manage Installed Applications list with OptiSigns highlighted](https://support.optisigns.com/hc/article_attachments/57143071771411)

Select **Permissions**.

![OptiSigns app menu on Fire TV with Permissions highlighted](https://support.optisigns.com/hc/article_attachments/57143071773843)

**Storage** is set to **DENY**. Select it to change it to **ALLOW**.

![OptiSigns Permissions menu with Storage set to ALLOW](https://support.optisigns.com/hc/article_attachments/57143071776019)

Open OptiSigns again, and your content will start playing.

<a name="ClearTheOptiSignsAppsCacheOrData"></a>

### Clear the OptiSigns App's Cache or Data

If OptiSigns is slow or not working correctly, its cached data may be corrupted or too large. Clearing the cache usually fixes it.

In **Settings**, go to **Applications** > **Manage Installed Applications** > **OptiSigns**, as in the steps above. Select **Clear cache**.

![OptiSigns app menu on Fire TV with Clear cache highlighted](https://support.optisigns.com/hc/article_attachments/57143071777683)

If the app still doesn't work correctly, come back to the same menu and select **Clear data**. This removes the app's downloaded content too, so it downloads everything again.

![OptiSigns app menu on Fire TV with Clear data highlighted](https://support.optisigns.com/hc/article_attachments/57143088528147)

|  |
| --- |
| **NOTE** |
| If OptiSigns still doesn't work after clearing its data, [Reinstall the OptiSigns App](#ReinstallTheOptiSignsApp). As a last resort, [Factory Reset Your Fire TV](#FactoryResetYourFireTV). |

<a name="TurnOnAutomaticAppUpdates"></a>

### Turn On Automatic App Updates

The Fire TV keeps OptiSigns up to date by itself, as long as automatic updates are on. They are on by default.

To check, go to **Settings** > **Applications** and select **Appstore**.

![Fire TV Applications menu with Appstore highlighted](https://support.optisigns.com/hc/article_attachments/57143071781267)

Make sure **Automatic Updates** is **ON**. If it isn't, select it to turn it on.

![Fire TV Appstore settings with Automatic Updates set to ON](https://support.optisigns.com/hc/article_attachments/57143071782035)

<a name="UpdateFireOS"></a>

### Update Fire OS

If apps such as weather or social media don't display correctly, the Fire TV's own software may be out of date.

In **Settings**, select **My Fire TV**.

![Fire TV Settings with the My Fire TV tile highlighted](https://support.optisigns.com/hc/article_attachments/57143071782803)

Select **About**.

![My Fire TV menu with About highlighted](https://support.optisigns.com/hc/article_attachments/57143071783955)

Select **Install Update**. If there's no update waiting, this option reads **Check for Updates** instead.

![Fire TV About menu with Install Update highlighted and a message that an update is available](https://support.optisigns.com/hc/article_attachments/57143088535571)

The update downloads and installs, then the Fire TV restarts by itself. If it doesn't restart, press and hold **Select** and **Play/Pause** on the remote together for 5 seconds.

<a name="ChangeTheTimeZone"></a>

### Change the Time Zone

If your Schedules start or end at the wrong time, check the Fire TV's time zone.

In **Settings**, select **Preferences**, then **Time Zone**.

![Fire TV Preferences menu with Time Zone highlighted](https://support.optisigns.com/hc/article_attachments/57143071786643)

Select **Time Zone** again.

![Fire TV Time Zone menu with Time Zone highlighted and the current time zone shown](https://support.optisigns.com/hc/article_attachments/57143071788691)

Select your region, then your time zone. The Fire TV sets its clock from your choice.

![Fire TV list of time zone regions with North America highlighted](https://support.optisigns.com/hc/article_attachments/57143071790995)

<a name="ReinstallTheOptiSignsApp"></a>

### Reinstall the OptiSigns App

Reinstalling OptiSigns is a common fix when the app keeps misbehaving.

In **Settings**, go to **Applications** > **Manage Installed Applications** > **OptiSigns**, as in the steps above. Select **Uninstall**.

![OptiSigns app menu on Fire TV with Uninstall highlighted](https://support.optisigns.com/hc/article_attachments/57143071791891)

Select **Uninstall** again to confirm.

![Fire TV confirmation asking whether to uninstall OptiSigns, with Uninstall highlighted](https://support.optisigns.com/hc/article_attachments/57143088542483)

Then install the app again from the Appstore, as in [Installing the OptiSigns App](#InstallingTheOptiSignsApp) above. The Fire TV keeps its pairing, so you don't need to pair it again.

<a name="InstallTheOptiSignsAppFromAnAPKFile"></a>

### Install the OptiSigns App from an APK File

We strongly recommend installing OptiSigns from the Amazon Appstore, so Amazon keeps it up to date for you. If you can't use the Appstore, you can install the app file (APK) directly.

In **Settings**, select **My Fire TV**, then **Developer options**.

![My Fire TV menu with Developer options highlighted](https://support.optisigns.com/hc/article_attachments/57143088544147)

Select **Apps from Unknown Sources**.

![Fire TV Developer options with Apps from Unknown Sources highlighted and set to OFF](https://support.optisigns.com/hc/article_attachments/57143071797907)

Select **Turn On** to accept the warning.

![Fire TV warning about apps from unknown sources with the Turn On button highlighted](https://support.optisigns.com/hc/article_attachments/57143088547475)

From the Appstore, install the free **Downloader** app.

![Downloader app page in the Amazon Appstore with the Get button](https://support.optisigns.com/hc/article_attachments/57143088549651)

Open Downloader and enter `https://links.optisigns.com/fireos`. When the file has downloaded, select **Install**. OptiSigns then appears with your other apps on the Fire TV home screen.

<a name="FactoryResetYourFireTV"></a>

### Factory Reset Your Fire TV

If nothing else has worked, a factory reset returns the Fire TV to the state it left the factory in.

|  |
| --- |
| **IMPORTANT** |
| A factory reset deletes all of your apps, data and settings, including your Amazon sign-in. You'll need to set up the Fire TV, install OptiSigns and pair it again. |

In **Settings**, select **My Fire TV**, then **Reset to Factory Defaults**.

![My Fire TV menu with Reset to Factory Defaults highlighted](https://support.optisigns.com/hc/article_attachments/57143088551059)

Select **Reset**. The reset takes a few minutes.

![Fire TV confirmation to reset to factory defaults with the Reset button highlighted](https://support.optisigns.com/hc/article_attachments/57143071805075)

---

<a name="ConnectingAKeyboardAndMouse"></a>

## Connecting a Keyboard and Mouse

To sign in to content behind a login, such as a Jira board or a Power BI or Tableau dashboard, you need to type on the Fire TV. Pair a [Bluetooth keyboard](https://www.amazon.com/Logitech-Illuminated-Living-Room-Keyboard-Touchpad/dp/B00ZOPVSKW/), or use a [USB hub adapter](https://www.amazon.com/gp/product/B00LTHBCNM/) to connect a wired or wireless USB keyboard and mouse.

![USB hub adapter with ports labeled for a wired keyboard, a wired mouse, a power cable and the Fire TV Stick](https://support.optisigns.com/hc/article_attachments/57143088561683)

|  |
| --- |
| **NOTE** |
| Set the switch on the USB hub adapter to **OTG**. |

---

<a name="RestartingOptiSignsRemotely"></a>

## Restarting OptiSigns Remotely

If you're not on site, you can check whether a Fire TV is on and restart OptiSigns from your phone with the Amazon Fire TV app, available for iPhone and Android.

Set this up while you're on site:

- The Fire TV must be signed in to your Amazon account.
- Sign in to the Fire TV app on your phone with the same Amazon account.
- Write down each device's name, so you know which is which.

The app lists the Fire TVs it can reach. If a device isn't listed, it's powered off or has lost its Wi-Fi connection.

![Fire TV phone app listing the Fire TV devices available to connect to](https://support.optisigns.com/hc/article_attachments/57143071808403)

To restart OptiSigns, select the Fire TV in the list. Press **Back** to close OptiSigns, then open your apps list.

![Fire TV phone remote with arrows pointing to the Back button and the apps button](https://support.optisigns.com/hc/article_attachments/57143071811475)

Select OptiSigns to open it again.

![Fire TV phone app showing Your Apps & Games with an arrow pointing to the OptiSigns app](https://support.optisigns.com/hc/article_attachments/57143088566931)

---

<a name="Troubleshooting"></a>

## Troubleshooting

For black screens, network problems and power issues, start with the [Amazon TV / FireStick Troubleshooting Guide](https://support.optisigns.com/hc/en-us/articles/27463953562899). These are the fixes covered in this article:

#### "Are you still watching?" appears, or OptiSigns stops after 4 hours

Turn off Still Watching. See [Keep OptiSigns Running](#KeepOptiSignsRunning).

#### The screen stays black

Allow OptiSigns to use the Fire TV's storage. See [Allow OptiSigns to Use Storage](#AllowOptiSignsToUseStorage).

#### Weather or social media apps don't display correctly

Update the Fire TV's software. See [Update Fire OS](#UpdateFireOS).

#### Schedules start or end at the wrong time

Check the Fire TV's time zone. See [Change the Time Zone](#ChangeTheTimeZone).

#### OptiSigns is slow or stops working

Work through these in order, checking after each one: [Clear the OptiSigns App's Cache or Data](#ClearTheOptiSignsAppsCacheOrData), then [Reinstall the OptiSigns App](#ReinstallTheOptiSignsApp), and finally [Factory Reset Your Fire TV](#FactoryResetYourFireTV).
