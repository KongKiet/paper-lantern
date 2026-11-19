# How to Use the Advanced Website App

Article URL: https://support.optisigns.com/hc/en-us/articles/5149077938835-How-to-Use-the-Advanced-Website-App

Article ID: 5149077938835

Locale: en-us

Updated at: 2026-11-18T16:21:38Z

---

### In this article, we'll show how to display any web page on your digital signs with the Advanced Website app, including long pages and pages that refuse to be embedded.

- [What You'll Need](#WhatYoullNeed)
- [Creating an Advanced Website App](#CreatingAnAdvancedWebsiteApp)
- [Choosing a Display Mode](#ChoosingADisplayMode)
- [Showing a Different Page on Each Screen](#ShowingADifferentPageOnEachScreen)
- [Deploying an Advanced Website App](#DeployingAnAdvancedWebsiteApp)
- [Troubleshooting](#Troubleshooting)

The Advanced Website app shows any web page on your screens, including long pages and pages that refuse to be embedded. You choose how the page is displayed, have it scroll up and down on its own, and can even show a different page on each screen from a single asset.

Let's get started.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))
- The address (URL) of the web page you want to display

---

<a name="CreatingAnAdvancedWebsiteApp"></a>

## Creating an Advanced Website App

From the OptiSigns portal, go to **Files/Assets** and select **Apps**.

![Files/Assets page with the Apps button highlighted in the left sidebar](https://support.optisigns.com/hc/article_attachments/57687886737811)

Search for **Advanced Website** and select the **Advanced Website** app.

![Add App dialog searched for Advanced Website, with the Advanced Website app card highlighted](https://support.optisigns.com/hc/article_attachments/57687886739731)

The Advanced Website app settings will open. Fill in the following:

- **Name** - The name of your Advanced Website asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
- **URL** - The address of the web page you want to display. To show a different page on each screen, see **Showing a Different Page on Each Screen** below.
- **Display mode** - How the page is shown on your screens. **Direct mode (auto page height)** is the default. See **Choosing a Display Mode** below.
- **Update Interval** - How often the app checks the page for updates, measured in seconds. The default is 600 (every 10 minutes). Set it to 0 to check only when the app first loads.

![Advanced Website app form with Name, URL, Display mode and Update Interval filled in](https://support.optisigns.com/hc/article_attachments/57687896707219)

Click **Display Settings** for more options:

![Display Settings with Auto Scroll turned on, showing Scroll Type, Scroll range, Speed and Zoom](https://support.optisigns.com/hc/article_attachments/57687896709011)

- **Auto Scroll** - Turn this on to have the page scroll by itself.
- **Scroll Type** - **Down & Up** scrolls down the page and back up again. **Scroll To** moves to one spot on the page and stays there.
- **Scroll range** - Direct mode only. **Whole page** scrolls all the way to the real bottom of the page, even on feeds that keep loading more posts as you scroll. For a page that never ends, choose **Custom** to stop at a height you set.
- **Speed** - How fast the page scrolls.
- **Zoom** - Makes the page bigger or smaller on the screen, in percent. The default is 100.

Click **Advanced** for more options:

![Advanced section with Preload, Request Desktop Site, Render Engine and Optimize for high resolution screens](https://support.optisigns.com/hc/article_attachments/57687886742035)

- **Preload** - The number of seconds to load the page in the background before it plays, so it appears instantly in a playlist. The default is 0.
- **Request Desktop Site** - Asks the website for its desktop layout instead of its mobile one. On by default.
- **Render Engine** - The browser used to display your page on Amazon FireStick devices (**FireStick Normal**, **FireStick 4K**) and on **Other** devices. Only change this if the page doesn't show correctly.
- **Optimize for high resolution screens** - Keeps the page sharp on 4K screens. On by default.

Now hit **Save**. You'll have created an Advanced Website app, and it will appear in your **Files/Assets**.

---

<a name="ChoosingADisplayMode"></a>

## Choosing a Display Mode

The Advanced Website app has two display modes. Pick the one that matches the website and the devices you play it on.

**Direct mode (auto page height)** shows the full page, even sites that block being embedded in other pages. The app works out how long the page is by itself, so you don't need to enter a page height. Direct mode is supported on **Android**, **Windows**, **Mac** and the **ProPlayer**.

**Standard mode (fixed page height)** also plays on the **Web Player**, **Samsung** and **LG** screens. Because the app can't measure the page in this mode, you set its height yourself under **Display Settings** → **Page Height**, in pixels. The default is 3000.

In Standard mode, a **Verify URL** button appears next to the URL. Click it to check whether the site allows itself to be shown:

- If the site can be shown, the button turns into a check mark and you can save as usual.
- If the site blocks it, you'll see **This website prevents itself from being displayed in an iFrame. Use Direct mode instead.** and **Save** stays greyed out. Switch to **Direct mode**, or choose a different page.

![Standard mode with a blocked site: the Verify URL warning under the URL and Save greyed out](https://support.optisigns.com/hc/article_attachments/57687896710675)

![Display Settings in Standard mode, showing Scroll Type, Speed, Zoom and Page Height](https://support.optisigns.com/hc/article_attachments/57687896712979)

|  |
| --- |
| **NOTE** |
| If your screens are a mix of devices, use Standard mode for any asset that needs to play on the Web Player, Samsung or LG screens. |

---

<a name="ShowingADifferentPageOnEachScreen"></a>

## Showing a Different Page on Each Screen

One Advanced Website asset can show a different page on each screen. Put a screen attribute in double curly brackets (ex. {{Houston}} ) anywhere in the URL: as part of the path, or as a query value. Each screen fills in its own value.

For example, with the URL **https://en.wikipedia.org/wiki/{{city}}**, a screen whose **city** is Houston shows **https://en.wikipedia.org/wiki/Houston**, and a screen whose **city** is Los Angeles shows **https://en.wikipedia.org/wiki/LosAngeles**.

To give a screen its values, go to the **Screens** tab and click **Edit** next to the screen. Open **Advanced** and click **More**. At the bottom of the pop-up, click the wrench icon to open **Device Additional Attributes**.

![Bottom of the Edit Screen dialog with an arrow on the wrench icon that opens Device Additional Attributes](https://support.optisigns.com/hc/article_attachments/57687896713747)

Click **New Attribute**. Enter the attribute name exactly as it appears in your URL, without the brackets, and the value for this screen. Then hit **Update**, and **Save** the screen.

![Device Additional Attributes dialog with a city attribute set to Tokyo](https://support.optisigns.com/hc/article_attachments/57687886748563)

Repeat this for each screen that plays the asset.

---

<a name="DeployingAnAdvancedWebsiteApp"></a>

## Deploying an Advanced Website App

To push your Advanced Website app to a screen, go to the **Screens** tab, then click **Edit** next to the screen you want to display it on.

![Screens page with an arrow on a screen's Edit button](https://support.optisigns.com/hc/article_attachments/57687886749459)

The **Edit Screen** pop-up will appear. Select **Asset** under **Content Type**, then hit **Change** next to **Selected Asset**.

![Edit Screen dialog with Content Type set to Asset and an arrow on Change](https://support.optisigns.com/hc/article_attachments/57687886751635)

The **Select Asset** window will open. Search for your Advanced Website app, click it, then hit **Select**.

![Select Asset dialog searched for an Advanced Website app, with its asset card highlighted](https://support.optisigns.com/hc/article_attachments/57687886752531)

Back in **Edit Screen**, hit **Save**. Your web page will now display on your screen.

Your Advanced Website app can also be displayed in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573). In a Split Screen, the page fits and scrolls inside its own zone, and each zone plays on its own.

---

<a name="Troubleshooting"></a>

## Troubleshooting

If your page doesn't look the way you expect, check these first.

#### The screen is blank, or shows a message that the site can't be displayed

The site is probably blocking embedding. Switch the asset to Standard mode for a moment and click **Verify URL** to check. If the site blocks embedding, switch to **Direct mode** and play it on an Android, Windows, Mac or ProPlayer device.

#### The page stops scrolling before the bottom, or scrolls into empty space

In Standard mode, the app scrolls only as far as **Page Height**. Raise it for a longer page, or lower it if the screen scrolls past the end. In Direct mode, set **Scroll range** to **Whole page** to reach the real bottom.

#### A feed keeps loading and the page never finishes scrolling

Some pages, like social media feeds, never end. In Direct mode, set **Scroll range** to **Custom** and enter the height to stop at.

#### One screen shows the wrong page

Check that the screen has a **Device Additional Attribute** with exactly the same name as the one in your URL, and that its value is filled in.

#### The page looks too small, too big or cut off

Adjust **Zoom** under **Display Settings**. If the page shows its mobile layout, make sure **Request Desktop Site** is on under **Advanced**.
