# How to Use the Local Folder App in OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/1500001985341-How-to-Use-the-Local-Folder-App-in-OptiSigns

Article ID: 1500001985341

Locale: en-us

Updated at: 2026-11-25T18:12:04Z

---

### In this article, we'll explain how to use the Local Folder app in OptiSigns to let you access locally stored files on your device to display.

- [How to Set Up the Local Folder App](#Setup)
  - [For Windows](#Windows)
  - [For Mac/Linux/Ubuntu/Raspberry Pi](#Mac)
  - [For the OptiStick](#Stick)
  - [For the OptiSigns Pro Player](#ProPlayer)

Sometimes, due to network limitations or security reasons, you'll have content you'd rather keep locally at your device. The Local Folder app allows you to access content stored locally.

Major use cases for this app include:

- Sensitive information that should not be transferred via Internet
- Limited network availability locations
- You want to use or mix in contents from USB thumb drives

OptiSigns player is smart enough to scan for changes in these folders. When files are added or removed, it's handled automatically.

You can also use USB thumb drives. OptiSigns detects drives plugged in and scan the folder to play again as long as it's given the correct path.

|  |
| --- |
| **Note:**The Local folder application only currently supports video and image files. |

---

<a name="Setup"></a>

## **How to Set Up the Local Folder App**

First, you will need to have your screens set up and paired. For more information on how to do that, click [here](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv).

Then log on to our portal: <https://app.optisigns.com/>

Go to **Files/Assets** and click on **"Apps"**:

![Files/Assets page with a red arrow pointing at the Apps button in the left sidebar](https://support.optisigns.com/hc/article_attachments/55666381491987)

Find the **Local Folder** app:

![Add App dialog searched for Local Folder, red arrow pointing at the Local Folder app tile](https://support.optisigns.com/hc/article_attachments/55666355587603)

Enter your **local folder path** (detailed instructions per platform below) and configure the app settings:

![Local Folder settings form: Name, Local Folder, transition, duration, scaling and Shuffle fields](https://support.optisigns.com/hc/article_attachments/55666355588627)

- **Name** - Name of your Local Folder app. This will be displayed on your asset list, and will **not** be displayed on your screens.
- **Local Folder** - Path to the folder on your device. We will provide detailed instructions per platform later in this article.
- **Transition Effects** - Transition effect between your images and videos in the folder.
- **Transition Speed** - How fast you want your transitions to animate.
- **Duration for Image** - How long each image should show on your screen, default is 10 seconds.
- **Max Video Duration** - Default is 0, which means the app will play each video till the end. You can set it to some other values to prevent too long videos. For example, if you set this value to 60 seconds. If a video is longer than 60s, it will get cut off at 60s to play next item. If a video is less than 60s, it will play the duration of the video.
- **Scale Image** - select how the player should handle if image's resolution is less than your screen's resolution
- **Scale Video** - select how the player should handle if the video's resolution is less than your screen's resolution
- **Shuffle** - select if you want to shuffle play the content in the folder (Default order is by filename alphabetically)

Click **Save**.

You now can assign the Local Folder app to your device. It can also be placed in a Playlist or Schedule.

<a name="Windows"></a>

## Finding Your Local Folder Path by Operating System

### For Windows:

If using a Windows device to display your content, the path to your Local Folder will be similar to C:\ D:\Media Folder etc. Find the path by looking at the folder's Properties, like so:

![Windows folder Properties dialog, the Location row boxed in red showing the folder's path](https://support.optisigns.com/hc/article_attachments/33807447378707)

You'll then use this path to fill in the Local Folder value within the Local Folder App:

![Local Folder form with Name 'Windows Media Folder' and path C:\Users\OptiSigns\Media](https://support.optisigns.com/hc/article_attachments/55666355590547)

This will vary depending on the location of the folder on your drive.

<a name="Mac"></a>

### For Mac/Linux/Ubuntu/Raspberry Pi:

If using a Mac, Linux, or Ubuntu device, the path to your folder will be similar to /media/path/folder.

For Mac users, find this using **Get Info**. It will look similar to this:

![macOS Get Info window for a folder, red arrow pointing at the Where row showing Users then Desktop](https://support.optisigns.com/hc/article_attachments/33807447394067)

This comes out to /Users/{username}/Desktop as a path filename.

In Linux/Ubuntu, you can find this information in **Properties.**

![Ubuntu folder Properties window, red arrow pointing at the Parent folder row reading /home/optisigns](https://support.optisigns.com/hc/article_attachments/33807672236819)

The path in this example would be /home/optisigns .

For Raspberry Pi, the path can also be found in **Properties**.

![Raspberry Pi File Properties window, red arrow pointing at the Location row reading /home/pi](https://support.optisigns.com/hc/article_attachments/33807431768339)

In this example, that's /home/pi.

You'll then use this path to fill in the Local Folder value within the Local Folder App:

![Local Folder form with Name 'Raspberry Pi Images' and path /home/pi/images](https://support.optisigns.com/hc/article_attachments/55666355590803)

This will vary depending on the location of the folder on your drive. However, it's important to note that Mac, Linux, Ubuntu, and Raspberry Pi paths all have the same format.

<a name="Stick"></a>

### For OptiStick Digital Signage Player

|  |
| --- |
| **IMPORTANT:** To use the Local Folder App on your OptiStick, make sure its firmware version is 5.17.23 or later. |

To use the Local Folder app on an [OptiStick](https://shop.optisigns.com/products/optisigns-android-stick-player-2), first install whatever you'd like to display on a USB drive or MicroSD. Attach the device to your Android stick, then navigate using a [Remote Control](https://support.optisigns.com/hc/en-us/articles/30304278652563-How-to-Use-the-Mobile-App-for-Remote-Control) to **Device Storage** on the side menu:

![optisigns android stick player menu with arrow pointing toward device storage option](https://support.optisigns.com/hc/article_attachments/33807431790995)

Once there, you should be able to see your External storage device listed:

![device storage menu optisigns stick arrow pointing toward external storage path](https://support.optisigns.com/hc/article_attachments/33807431795347)

Simply copy this and place this in your Local Folder value within the Local Folder App:

![Local Folder form with Name 'Android Stick USB' and path /storage/6847-88F0](https://support.optisigns.com/hc/article_attachments/55666355599507)

This path will vary depending on the type of external storage device, and will always be different.

<a name="ProPlayer"></a>

### For OptiSigns Pro and ProMax Digital Signage Player

The OptiSigns Pro/Pro Max Player is an Ubuntu enabled device, so it runs the same way. You'll have a slightly different path depending on whether you're using a USB device or MicroSD card as your external storage, or if you have multiple USB drives plugged into the player.

|  |  |  |
| --- | --- | --- |
| **Devices connected** | **Local Folder path on the Pro player** | **Local Folder path on the Promax player** |
| USB drive #1 | /home/optisigns/external/{USB name}-sdb1 | /home/optisigns/external/{USB name}-sda1 |
| USB drive #2 | /home/optisigns/external/{USB name}-sdc1 | /home/optisigns/external/{USB name}-sdb1 |
| USB drive #3 | /home/optisigns/external/{USB name}-sdd1 | /home/optisigns/external/{USB name}-sdc1 |
| Micro SD card | /home/optisigns/external/{SDcard name}-mmcblk0p1 | |

**Note:** The first USB drive mounts as `sdb1` on Pro players, but as `sda1` on Promax players.

Examples (Assuming 3 USB drives named USB1, USB2, USB3, and an SD card named SDCARD):

|  |  |  |
| --- | --- | --- |
| **Devices connected** | **Local Folder path on the Pro player** | **Local Folder path on the Promax player** |
| 1 USB Connected | /home/optisigns/external/USB1-sdb1 | /home/optisigns/external/USB1-sda1 |
| 2 USBs Connected | /home/optisigns/external/USB1-sdb1  /home/optisigns/external/USB2-sdc1 | /home/optisigns/external/USB1-sda1  /home/optisigns/external/USB2-sdb1 |
| 3 USBs Connected | /home/optisigns/external/USB1-sdb1  /home/optisigns/external/USB2-sdc1  /home/optisigns/external/USB3-sdd1 | /home/optisigns/external/USB1-sda1  /home/optisigns/external/USB2-sdb1  /home/optisigns/external/USB3-sdc1 |
| SD card connectd | /home/optisigns/external/SDCARD-mmcblk0p1 | |

---

## Related Articles

- [How to Use the Dropbox App](https://support.optisigns.com/hc/en-us/articles/360050665413?ref=related)
- [How to Use the Google Drive App](https://support.optisigns.com/hc/en-us/articles/360049518313?ref=related)
- [How to Use the OneDrive App](https://support.optisigns.com/hc/en-us/articles/360050665253?ref=related)
- [What happen if internet connection is lost?](https://support.optisigns.com/hc/en-us/articles/360016376793?ref=related)

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
