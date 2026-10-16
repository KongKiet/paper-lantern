# Device Management and Mass Provisioning

Article URL: https://support.optisigns.com/hc/en-us/articles/53497007807251-Device-Management-and-Mass-Provisioning

Article ID: 53497007807251

Locale: en-us

Updated at: 2026-10-15T16:10:20Z

---

- [What You'll Need](#WhatYouNeed)
- [Devices Tab](#DevicesTab)
  - [Individual Device Management](#IndividualDevice)
    - [Sending Remote Commands](#SendingRemoteCommands)
    - [Overview](#Overview)
    - [Content](#Content)
    - [Activity](#Activity)
    - [Troubleshooting](#Troubleshooting)
- [Fleets](#Fleets)
- [Room Integrations](#RoomIntegrations)
- [Provisioning Templates and Enterprise WiFi](#Provisioning&amp;WiFi)

Managing large numbers of devices can seem overwhelming. That's why we've introduced the **Devices** tab, where you can easily organize and troubleshoot your devices from a single location.

This tab and interface is largely designed for IT personnel and becomes available to OptiSigns Pro Plus plan subscribers once they've set up and registered 5 screens or more on OptiSigns. Only Owners and Super Admins can access the Devices tab.

---

<a name="WhatYouNeed"></a>

## What You'll Need

- An OptiSigns [**Pro Plus plan or higher**](https://www.optisigns.com/pricing)
- 5 or more screen licenses, set up and paired with OptiSigns
- An Owner or Super Admin login account

---

<a name="DevicesTab"></a>

## Devices Tab

Clicking the **Devices** tab at the top of your screen will bring up an overview of all your devices.

![Devices tab showing device summary cards and the list of devices](https://support.optisigns.com/hc/article_attachments/53497007791891)

This article will be going over each of the tabs on the left of the screen in detail.

<a name="IndividualDevice"></a>

### Individual Device Management

Clicking on any device on the list will open up a more in-depth field on the right of the screen.

|  |
| --- |
| **IMPORTANT NOTE** |
| Significantly more information is available for OptiSigns Devices (the OptiStick, Pro Player, or ProMax Player) as opposed to others. Please see the image below for an example of this. |

|  |  |
| --- | --- |
| **OptiSigns Devices** | **Other Devices** |
| Device panel for an OptiSigns device, showing remote command buttons and the Overview tab | Device panel for a non-OptiSigns device, showing Device Info only |

Non-OptiSigns devices are still able to see Device Info and the Activity Tabs. For the purposes of this article, we will assume you are using an OptiSigns device, and go over each area in turn.

<a name="SendingRemoteCommands"></a>

#### Sending Remote Commands

Above the main tabs, you'll see a handful of options:

![Remote command buttons: Identify Screen, Enable Remote Control, Reboot, and Refresh & Relaunch](https://support.optisigns.com/hc/article_attachments/53497007795603)

These are remote commands that can be sent to your online devices.

- **Identify Screen -** Clicking this button will place a marker on your screen, allowing you to identify the screen associated with the device.
- **Enable Remote Control -** This command must be sent before anyone is allowed to **Remote** into the device.
- **Reboot -** This command will reboot the device remotely.
- **Refresh & Relaunch** - This command will refresh and relaunch your content remotely.

Next to these is the **More** option, which will expand to encompass numerous additional options:

![More menu listing additional remote commands](https://support.optisigns.com/hc/article_attachments/53496976226067)

- **Remote -** Allows you to remote into the device and access the Side Menu. Requires the **Enable Remote Access** command be sent to the device before this can be enabled.
- **Take Screenshot -** Allows a quick screenshot to be taken of the screen, generally for troubleshooting.
- **Send HDMI CEC -** Sends a command via HDMI-CEC, enabling you to test that connection.
- **Send RS232 -** Sends a command via RS232, enabling you to test that connection.
- **Storage Details -** Clicking this button will display the Storage Details of your device on screen.
- **Install OptiSigns Versions -** Opens a window allowing you to choose which version of OptiSigns to install on your device, including old and beta versions.

  ![Install OptiSigns Versions dialog listing available app versions](https://support.optisigns.com/hc/article_attachments/53510275338387)
- **OTA Update (Pro/ProMax Player only) -** Begins an OTA update for your Pro or ProMax player, which will update the player's general firmware. This is separate from your OptiSigns version.
- **Update Time Zone -** Allows you to update the time zone of the OS on the device.
- **Add/Remove WiFi -** Lets you add or remove a WiFi connection from the device. Requires an initial WiFi setup for this to work.
- **View Device Info -** Lets you check device info:

  ![View Device Info dialog showing network, memory and storage details](https://support.optisigns.com/hc/article_attachments/53510275339283)
- **Remote Command History -** Displays the Remote Command history. This information can also be found on the **Activity** tab.
- **Execute Remote Commands** - Lets you execute remote commands via a direct input command.
- **Enable/Disable Auto Update** - Lets you enable or disable the ability of this device to receive automatic updates from OptiSigns.
- **Install APK -** Allows you to install an APK remotely.

<a name="Overview"></a>

#### Overview

Under the **Overview** tab, you can check all kinds of information. Note that the information displayed is most accurate when the screen is **Live**:

![Overview tab with storage, memory, display output and uptime cards](https://support.optisigns.com/hc/article_attachments/53507223295507)

- **Storage -** Shows the total amount of storage used, and how much is available.
- **Memory -** Shows the total amount of memory being used to display content, and how much is available.
- **Display Output -** Shows the resolution of the content being displayed.
- **Uptime -** Shows how long this device has been continuously live.
- **Active Since -** Shows how long the device has been registered within OptiSigns.
- **Time zone -** Allows you to quickly check the internal time zone of your device.
- **Temperature -** Shows the internal temperature of the device.
- **Live Device State -** Shows when the last time the live device state was pulled.

![Device info list and Enterprise Wi-Fi details on the Overview tab](https://support.optisigns.com/hc/article_attachments/53496976227475)

The below area will provide Device Info for use primarily in OptiSigns:

- **Screen ID -** The unique ID assigned to your device as a screen within OptiSigns.
- **Serial -** The serial number specific to your device.
- **MAC Address -** The unique, 12-character code assigned to your device's network adapter.
- **Operating System -** The Operating System currently running on this device.
- **Browser -** The version number of the browser running on the device.
- **OS Time Zone -** The time zone being used on the device clock. This is useful information for using OptiSigns, primarily its scheduling feature.
- **Created -** The date this device was paired with OptiSigns.
- **Last Seen -** The last time this device checked in with OptiSigns servers.

Any relevant Enterprise WiFi information will be put here.

<a name="Content"></a>

#### Content

|  |
| --- |
| **NOTE** |
| Only available on OptiSigns devices. |

![Content tab showing a screenshot of the screen, Now playing and Player details](https://support.optisigns.com/hc/article_attachments/53507207857555)

This displays a recent screenshot of the content playing on your device. A new one can be captured by clicking the **Capture Screenshot** (or **Recapture)** button.

**Now Playing:**

- **Since -** When the content started playing.
- **Type -** The type of content being displayed (asset, playlist, schedule). Note that this doesn't show the asset or playlist name.
- **Duration -** The duration of the content being displayed.
- **Expired -** Whether or not this content has expired via Live / Expire.

**Player -** This is specifically information about the OptiSigns app running on the device.

- **Player version -** Shows the current OptiSigns player / app version.
- **OS -** The operating system the OptiSigns app is running on.
- **WebView -** URL and browser version on which the OptiSigns webplayer will play.

<a name="Activity"></a>

#### Activity

The **Activity** tab shows the device's history:

![Activity tab with the Edits filter selected, listing edits made to the device](https://support.optisigns.com/hc/article_attachments/56449435728659)

Here, you can see every change made to any individual device from within OptiSigns. This will show every command sent to the screen, and every organizational or content-related edit. You can filter by these options as well.

<a name="Troubleshooting"></a>

#### Troubleshooting

|  |
| --- |
| **NOTE** |
| Only available on OptiSigns devices. |

The **Troubleshooting** tab will allow an AI agent to SSH into your device and troubleshoot any problems by hitting **Start Session**.

![Troubleshooting tab with the Start session button](https://support.optisigns.com/hc/article_attachments/53507207858195)

This allows for greater, more in-depth Troubleshooting than would be capable by simply issuing commands. This can only be done by Super Admins or the account Owner.

Records of any troubleshooting sessions will be recorded here.

---

<a name="Fleets"></a>

## Fleets

**Fleets** are essentially groups of managed devices:

![Fleets page listing fleets and their device counts](https://support.optisigns.com/hc/article_attachments/53497007799571)

You can use Fleets to quickly cascade content or WiFi information to numerous devices simultaneously, which is extremely valuable for provisioning numerous devices.

To create a new fleet, hit **New Fleet**.

![New fleet dialog with name, description and tags fields](https://support.optisigns.com/hc/article_attachments/53497007800467)

Fill in the name, description, and any relevant tags you wish, then hit **Create Fleet**.

Your new fleet will appear below. Once you click into it, you can add devices to it by hitting **Add Device:**

![Devices page with the Add device button highlighted](https://support.optisigns.com/hc/article_attachments/53532869746323)

You can also export a report on any Fleet devices by hitting the **Export** button, which will automatically download the Fleets report as a .csv file. To export devices, use the **Export** button on the main Devices page.

---

<a name="RoomIntegrations"></a>

## Room Integrations

The Room Integrations tab allows you to integrate OptiSigns into your existing Meeting Rooms devices.

Please see our individual articles for more information:

- [**Connect Zoom Rooms to OptiSigns**](https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage)
- [**Connect Cisco Webex Rooms to OptiSigns**](https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage)
- [**Connect Microsoft Teams Rooms to OptiSigns**](https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage)
- [**Connect Google Meet Hardware to OptiSigns**](https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage)

---

## Provisioning Templates and Enterprise WiFi

On the bottom section of the left sidebar are the **Provisioning Templates** and **Wi-Fi & 802.1x** sections.

#### Provisioning Templates

If running a large deployment of digital signs, mass provisioning will save a lot of time and effort. It is supported on the OptiStick, Pro Player, ProMax Player, Android OS devices, Windows, Linux, Raspberry Pi, ChromeOS, or AppleTV.

Before provisioning can occur, you must meet a few prerequisites:

- The device needs to support using a USB drive or SD card. Or there is a way you can push the configuration file to a specific location in the OS.
- The user using the OS has the privilege to run the installation and access the USB drive or SD card.

![Provisioning Templates page listing saved templates](https://support.optisigns.com/hc/article_attachments/53507207858707)

Create a new provisioning template by clicking the **Create templates** button.

![Create New Provisioning Template dialog with the template fields](https://support.optisigns.com/hc/article_attachments/53507207859091)

- **Template Name -** Name of your template, this is for you to distinguish it when you have multiple provisioning templates.
- **Device Name Prefix -** This is used to generate the device name during provisioning.
- **Device Name Suffix -** This is used to generate the device name during provisioning, the default setting will add timestamps as a suffix.
- **Folder -** The folder you want to have the provisioned devices to be created.
- **Network -** Select from the stored WiFi, which needs to be created first in the Wi-Fi & 802.1X section.
- **Time Zone -** Specify the time zone of the device.
- **Tags -** Specify the tags you want to associate with the devices.
- **Initial Default Content Type -** Used to set the initial content on the device after provisioning.
- **Orientation -** Set the orientation, landscape is the default.
- **Sync Play -** Used to set the turn on/off of the sync play feature. For more details on the Sync Play feature, please click [here](https://support.optisigns.com/hc/en-us/articles/4412065189267-Synchronized-playback-Sync-Play-feature).
- **Location -** Set the location of the device.

Once the template is created, it will be available under the list of provisioning templates. Download the config file for use during deployment. The configuration file's name is "provisioning-template-<Your Template Name>.cfg"

#### Wi-Fi & 802.1X

Here, you can configure Wi-Fi networks to quickly assign them to your devices or fleets.

![Wi-Fi & 802.1X page listing saved network profiles](https://support.optisigns.com/hc/article_attachments/53507223300883)

To do this, click **Add Network**.

![Add Network dialog for entering Wi-Fi details](https://support.optisigns.com/hc/article_attachments/53507223301651)

Here, put in your Wi-Fi information. These networks can then be pre-assigned to new devices you add, or plan to add, and assigned as tags to Fleets.
