# LG WebOS Signage (Commercial Grade)

Article URL: https://support.optisigns.com/hc/en-us/articles/4414496579475-LG-WebOS-Signage-Commercial-Grade

Article ID: 4414496579475

Locale: en-us

Updated at: 2026-10-29T16:49:32Z

---

### In this article, we'll install the OptiSigns app on an LG webOS Signage display and pair it with your OptiSigns account.

- [Choose an Install Method](#ChooseAnInstallMethod)
- [Before You Begin](#BeforeYouBegin)
- [Install from a USB Drive](#InstallFromAUSBDrive)
- [Install from the Server](#InstallFromTheServer)
- [Batch Install with a USB Settings File](#BatchInstallWithAUSBSettingsFile)
- [Pair the Display with Your Account](#PairTheDisplayWithYourAccount)
- [How Content and Updates Work](#HowContentAndUpdatesWork)
- [Check Your Firmware Version](#CheckYourFirmwareVersion)
- [Update the LG Firmware](#UpdateTheLGFirmware)
- [Copy Settings to Other Displays](#CopySettingsToOtherDisplays)
- [Next Steps](#NextSteps)

LG commercial displays running webOS Signage are common in hotels, restaurants, retail and other businesses. The OptiSigns app runs directly on these displays, so you don't need a separate player.

On LG webOS Signage, OptiSigns saves your content on the display so it keeps playing if the internet drops, starts by itself when the display turns on, and updates itself.

|  |
| --- |
| **IMPORTANT** |
| This article is only for LG webOS Signage displays, which are sold as "LG Digital Signage". For a regular consumer LG TV with webOS, use the [OptiSigns web player](https://www.optisigns.com/post/how-to-use-optisigns-with-browser) instead. |

---

<a name="ChooseAnInstallMethod"></a>

## Choose an Install Method

You can install OptiSigns in two ways:

- **From a USB drive:** the easiest option. You don't need to type a URL with the remote, and you can reuse the same USB drive to set up many displays.
- From the server: no USB drive needed. You enter the address "https://links.optisigns.com/lg" in the display's SI Server Setting.

If you have many displays, you can also put the server settings in a file on a USB drive. See **Batch Install with a USB Settings File** below.

---

<a name="BeforeYouBegin"></a>

## Before You Begin

Factory reset the display so it starts from basic settings.

![LG Admin settings menu with an arrow on Factory Reset](https://support.optisigns.com/hc/article_attachments/56947928589459)

Connect the display to the internet over Wi-Fi or Ethernet.

Set the date, time and time zone. This makes sure your schedules play at the right local time.

![LG Time & Date settings with arrows on Set Automatically, Time, Date and Time Zone](https://support.optisigns.com/hc/article_attachments/56947928590611)

---

<a name="InstallFromAUSBDrive"></a>

## Install from a USB Drive

[Download the OptiSigns app for LG webOS Signage](https://links.optisigns.com/lg) (**com.lg.app.signage.ipk**) to your computer.

Format a USB drive as **FAT32** if it isn't already.

Create a folder named **application** in the root of the USB drive, then copy the .ipk file into it.

![USB drive in File Explorer with com.lg.app.signage.ipk inside the application folder](https://support.optisigns.com/hc/article_attachments/56947906011795)

Insert the USB drive into the display's USB port.

Press the settings (gear) button on the remote, then go to **EZ Setting** > **SI Server Setting**.

![LG EZ Setting menu with an arrow on the SI Server Setting tile](https://support.optisigns.com/hc/article_attachments/56947906012307)

Select **SI Server Setting**.

![SI Server Setting screen with the SI Server Setting option selected](https://support.optisigns.com/hc/article_attachments/56947928593555)

Set **Application Launch Mode** to **Local** and **Application Type** to **IPK**. Then select **Local Application Upgrade** > **USB**.

![SI Server Setting with arrows on Local, IPK and the USB button for Local Application Upgrade](https://support.optisigns.com/hc/article_attachments/56947906013331)

Select **Confirm** to install the app.

![Application Upgrade prompt saying the app will be upgraded from USB, with an arrow on Confirm](https://support.optisigns.com/hc/article_attachments/56947928595475)

If the USB drive is set up correctly, the display shows **Upgrade Complete**.

![Complete message saying Upgrade Complete on the SI Server Setting screen](https://support.optisigns.com/hc/article_attachments/56947906016275)

Turn the display off, then on again. When it comes back on, it shows that it's upgrading the application.

![Start to upgrade application notice at the top right of the display](https://support.optisigns.com/hc/article_attachments/56947928600083)

When the upgrade finishes, it shows **Complete**.

![Complete notice at the top right of the display after the upgrade](https://support.optisigns.com/hc/article_attachments/56947928601107)

The OptiSigns app opens by itself and shows a pairing code. You can now remove the USB drive.

![OptiSigns app on the LG display showing a pairing code and app.optisigns.com](https://support.optisigns.com/hc/article_attachments/56947928602259)

---

<a name="InstallFromTheServer"></a>

## Install from the Server

Press the settings (gear) button on the remote, then go to **EZ Setting** > **SI Server Setting**.

![LG EZ Setting menu with an arrow on the SI Server Setting tile](https://support.optisigns.com/hc/article_attachments/56947906012307)

Select **SI Server Setting**.

![SI Server Setting screen with the SI Server Setting option selected](https://support.optisigns.com/hc/article_attachments/56947928593555)

Set **Fully Qualified Domain Name** to **On**, then enter `https://links.optisigns.com/lg` in the field below it.

Set **Application Launch Mode** to **Local** and **Application Type** to **IPK**. Then select **Local Application Upgrade** > **REMOTE**.

![SI Server Setting with arrows on Fully Qualified Domain Name, its URL field, Local, IPK and REMOTE](https://support.optisigns.com/hc/article_attachments/56947928604819)

Select **Confirm** to install the app.

![Application Upgrade prompt saying the app will be upgraded from REMOTE, with an arrow on Confirm](https://support.optisigns.com/hc/article_attachments/56947928607123)

If the address is correct, the display shows **Upgrade Complete**. If it shows an error, check the address for typos and try again.

![Complete message saying Upgrade Complete, with an arrow on OK](https://support.optisigns.com/hc/article_attachments/56947928608275)

Turn the display off, then on again. When it comes back on, it shows that it's upgrading the application.

![Start to upgrade application notice at the top right of the display](https://support.optisigns.com/hc/article_attachments/56947928600083)

When the upgrade finishes, it shows **Complete**.

![Complete notice at the top right of the display after the upgrade](https://support.optisigns.com/hc/article_attachments/56947928601107)

The OptiSigns app opens by itself and shows a pairing code.

![OptiSigns app on the LG display showing a pairing code and app.optisigns.com](https://support.optisigns.com/hc/article_attachments/56947928602259)

**Note:** When OptiSigns updates itself, it changes the **Fully Qualified Domain Name** field to the address of the new version. If you see a different OptiSigns address there later, that's expected.

---

<a name="BatchInstallWithAUSBSettingsFile"></a>

## Batch Install with a USB Settings File

Instead of entering the address and settings on each display, you can put them in a file on a USB drive and reuse it.

1. On your computer, create a file named **scap\_installation.json** with this content:

```
{"serverIp": "0.0.0.0", "serverPort": 0, "secureConnection": false, "fqdnMode": true, "fqdnAddr": "https://links.optisigns.com/lg", "appLaunchMode": "local", "appType": "ipk"}
```

2. Copy the file into the root of the USB drive.
3. Insert the USB drive into the display, then turn it on or restart it.
4. When the installation finishes, restart the display. The OptiSigns app starts by itself.

---

<a name="PairTheDisplayWithYourAccount"></a>

## Pair the Display with Your Account

Go to [app.optisigns.com](https://app.optisigns.com/) and log in. If you don't have an account yet, select **Create Account**. You can also log in with Google, Microsoft or Facebook.

![OptiSigns portal log-in page with Google, Microsoft, Facebook and SSO options](https://support.optisigns.com/hc/article_attachments/56947928609171)

On the **Screens** page, select **Add Screen**.

![Screens page toolbar with an arrow on the Add Screen button](https://support.optisigns.com/hc/article_attachments/56947906025619)

Enter the pairing code shown on the display in **Pair code**, then select **Pair**.

![Add Screen dialog with a pair code entered and the Pair button highlighted](https://support.optisigns.com/hc/article_attachments/56947928611475)

|  |
| --- |
| **IMPORTANT** |
| Codes are case-sensitive, and the portal enters them in capitals. If the code on your display has lowercase letters, select "Use lowercase pairing code" and type it exactly as shown. If pairing fails with a case error, the portal switches this on for you, so check the code and select **Pair** again. |

From now on, the OptiSigns app starts by itself whenever the display turns on.

---

<a name="HowContentAndUpdatesWork"></a>

## How Content and Updates Work

- **Offline playback:** OptiSigns downloads your content to the display's storage, so it keeps playing without an internet connection. When the display runs low on space, OptiSigns removes files that are no longer in use.
- **Automatic updates:** OptiSigns checks for new versions of its app and installs them on the display. An update needs about 30 MB of free space.

---

<a name="CheckYourFirmwareVersion"></a>

## Check Your Firmware Version

Press the settings (gear) button on the remote, then go to **General** > **System Information**.

---

<a name="UpdateTheLGFirmware"></a>

## Update the LG Firmware

If your display runs webOS 4.1 or older, you may need to update its firmware before OptiSigns apps such as Weather and Social Media can play.

1. Get the latest firmware file (.epk) from the [LG partner website](https://partner.lge.com/global/portal/main/main/fowardMenuUrl.lge?_MenuId=210099&_MenuLevel=3&_MenuParentId=210021). For help, see [LG's guide to updating software manually](https://www.lg.com/us/support/help-library/lg-tv-how-to-manually-update-software--20154165668198), or contact us or LG.
2. Create a folder named **LG\_MONITOR** in the root of a USB drive, then copy the .epk file into it.
3. Insert the USB drive into the display. The update menu appears by itself.
4. Select **Update** and wait until it finishes.

---

<a name="CopySettingsToOtherDisplays"></a>

## Copy Settings to Other Displays

You can copy one display's settings, including Wi-Fi, the OptiSigns app and time zone, to other displays with a USB drive. This saves time when you set up many displays.

1. Insert a USB drive into the display you've already set up.
2. Press the settings (gear) button on the remote, then go to **EZ Setting** > **Setting Data Cloning**.
3. Select **Export Setting Data**.
4. Insert the USB drive into each of the other displays, go to the same menu, and select **Import Setting Data**.

---

<a name="NextSteps"></a>

## Next Steps

Your display is ready to show content. To get started:

- [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
- [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
- [Creating and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)
- [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)

If you have questions or feedback, contact our support team at support@optisigns.com.
