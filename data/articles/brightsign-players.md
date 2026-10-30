# BrightSign Players

Article URL: https://support.optisigns.com/hc/en-us/articles/5090125683219-BrightSign-Players

Article ID: 5090125683219

Locale: en-us

Updated at: 2026-10-29T17:44:28Z

---

### In this article, we'll install the OptiSigns player on a BrightSign player and pair it with your OptiSigns account.

- [Set Up with BSN.Cloud](#SetUpWithBSNCloud)
- [Set Up in Standalone Mode](#SetUpInStandaloneMode)
- [Pair the Player with Your Account](#PairThePlayerWithYourAccount)
- [Keep the Player Up to Date](#KeepThePlayerUpToDate)
- [Update the BrightSign Registry to Use a Newer Chromium](#UpdateTheBrightSignRegistryToUseANewerChromium)
- [Next Steps](#NextSteps)

BrightSign makes commercial-grade digital signage players known for their reliability. OptiSigns runs on BrightSign players, and we recommend the HD, XD and XT product lines for the best performance.

You can set up OptiSigns on a BrightSign player in two ways:

- **With BSN.Cloud:** create a setup file in BrightAuthor:connected that installs OptiSigns as a partner application.
- **Standalone:** copy the OptiSigns autorun file to an SD card.

Either way, the player downloads your content to its own storage, so it keeps playing if the internet drops for a while.

---

<a name="SetUpWithBSNCloud"></a>

## Set Up with BSN.Cloud

Download and install [BrightAuthor:connected](https://www.brightsign.biz/resources/software-downloads/) from BrightSign.

Open BrightAuthor:connected and sign in to your BSN.Cloud account.

Go to **Admin** > **Device Setup**.

![BrightAuthor:connected Admin menu open with an arrow on Device Setup](https://support.optisigns.com/hc/article_attachments/56950016554515)

Enter a **Package Name** and a **Device Name**.

Under **Device Type**, select **Partner Application**, then select **Select a Partner Application** and choose **OptiSigns**.

![Select a Partner Application window with an arrow on the OptiSigns tile](https://support.optisigns.com/hc/article_attachments/56950004468115)

Select **Save Setup Files** to save the setup files.

![New Device Setup with OptiSigns as the partner application and an arrow on Save Setup Files](https://support.optisigns.com/hc/article_attachments/56950004469907)

Copy the setup files to the root folder of your SD card.

![SD card in File Explorer with the BrightSign setup files in its root folder](https://support.optisigns.com/hc/article_attachments/56950004471315)

Make sure the BrightSign player is connected to the internet, then insert the SD card and power it on.

The player reads the setup files and installs OptiSigns. This takes a few minutes, and the player may restart a few times. When it's done, OptiSigns opens and shows a pairing code. Then pair the player with your account, as shown below.

---

<a name="SetUpInStandaloneMode"></a>

## Set Up in Standalone Mode

[Download the OptiSigns autorun file](https://links.optisigns.com/brightsign) (**autorun.zip**).

Copy **autorun.zip** to the root folder of your SD card. Don't unzip it.

|  |
| --- |
| **IMPORTANT** |
| The SD card must be formatted as FAT32. NTFS doesn't work for this setup. |

![SD card in File Explorer with autorun.zip in its root folder](https://support.optisigns.com/hc/article_attachments/56950016562579)

Make sure the BrightSign player is connected to the internet, then insert the SD card and power it on.

The player unpacks the file, installs OptiSigns and restarts. This takes a few minutes, and the player may restart more than once. When it's done, OptiSigns opens and shows a pairing code.

![OptiSigns player showing a six-character pairing code and app.optisigns.com](https://support.optisigns.com/hc/article_attachments/56950004474003)

---

<a name="PairThePlayerWithYourAccount"></a>

## Pair the Player with Your Account

Go to [app.optisigns.com](https://app.optisigns.com/) and log in. If you don't have an account yet, select **Create Account**. You can also log in with Google, Microsoft or Facebook.

![OptiSigns portal log-in page with Google, Microsoft, Facebook and SSO options](https://support.optisigns.com/hc/article_attachments/56950016564627)

On the **Screens** page, select **Add Screen**.

![Screens page toolbar with an arrow on the Add Screen button](https://support.optisigns.com/hc/article_attachments/56950016566163)

Enter the pairing code shown on the player in **Pair code**, then select **Pair**.

![Add Screen dialog with a pair code entered and the Pair button highlighted](https://support.optisigns.com/hc/article_attachments/56950004482451)

**Note:** Codes are case-sensitive, and the portal enters them in capitals. If the code on your player has lowercase letters, select **Use lowercase pairing code** and type it exactly as shown. If pairing fails with a case error, the portal switches this on for you, so check the code and select **Pair** again.

---

<a name="KeepThePlayerUpToDate"></a>

## Keep the Player Up to Date

OptiSigns starts by itself every time the BrightSign player powers on, so you don't need to open it after a restart.

With **Auto Update** on, the player downloads new OptiSigns versions by itself and restarts to install them. You'll find **Auto Update** in the player's side menu under **Advanced Options**.

If you still have trouble running OptiSigns, your BrightSign software may be out of date. Download the latest version from [BrightSign software downloads](https://www.brightsign.biz/resources/software-downloads/) and update the player.

---

<a name="UpdateTheBrightSignRegistryToUseANewerChromium"></a>

## Update the BrightSign Registry to Use a Newer Chromium

Some content, especially Power BI, needs a newer version of Chromium than the BrightSign player uses by default. You can switch it with a registry command.

Open BrightAuthor:connected and select **Admin**.

![BrightAuthor:connected home page with the Admin menu outlined](https://support.optisigns.com/hc/article_attachments/56950016569363)

Find your BrightSign player's IP address.

On a computer on the same network as the player, enter the IP address in your browser. The player's settings page opens.

Then, select the **Registry** tab.

![BrightSign player settings page with the Registry tab outlined](https://support.optisigns.com/hc/article_attachments/56950016570515)

![Registry tab with an empty Command field and a Submit button](https://support.optisigns.com/hc/article_attachments/56950004487571)

5. In **Command**, enter `registry write html widget_type chromium110`.

![Command field with the registry write html widget_type chromium110 command entered](https://support.optisigns.com/hc/article_attachments/56950004489363)

Select **Submit**. The result shows `widget_type = 'chromium110'`.

![Registry result showing widget_type set to chromium110](https://support.optisigns.com/hc/article_attachments/56950004490259)

Restart the player. It doesn't restart by itself after a registry change, so restart it manually or select **Reboot Player** on the **Control** tab.

---

<a name="NextSteps"></a>

## Next Steps

Your player is ready to show content. To get started:

- [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
- [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
- [Creating and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)
- [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)

If you have questions or feedback, contact our support team at support@optisigns.com.
