# How to Use the Air Quality Index App

Article URL: https://support.optisigns.com/hc/en-us/articles/56498363329683-How-to-Use-the-Air-Quality-Index-App

Article ID: 56498363329683

Locale: en-us

Updated at: 2026-10-16T21:10:49Z

---

### In this article, we'll show how to display live air quality readings and forecasts on your digital signs with OptiSigns.

- [What You'll Need](#WhatYoullNeed)
- [Creating an Air Quality Index App](#CreatingAnAirQualityIndexApp)
  - [Use Device Setting's Location](#UseDeviceSettingsLocation)
- [Display](#Display)
- [Deploying an Air Quality Index App](#DeployingAnAirQualityIndexApp)

With the Air Quality Index app, it's possible to display the current air quality and the coming days' forecast for any location on your digital signs. Show the US AQI, the level of each pollutant, and simple advice, so visitors and staff know at a glance whether it's a good day to be outside.

![Air Quality Index app showing a US AQI of 72, Moderate, with fine particles, coarse dust, ozone and traffic gas levels](https://support.optisigns.com/hc/article_attachments/56498339157267)

Let's get started.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

---

<a name="CreatingAnAirQualityIndexApp"></a>

## Creating an Air Quality Index App

From the OptiSigns portal, go to **Files/Assets** and select **Apps**.

![OptiSigns Files/Assets page with the Apps button highlighted](https://support.optisigns.com/hc/article_attachments/56498339262739)

Search for **Air Quality** and select the **Air Quality Index** app.

![Add App dialog searched for Air Quality, with the Air Quality Index app card highlighted](https://support.optisigns.com/hc/article_attachments/56498348373523)

The **Air Quality Index** app settings will open. Any changes you make show up right away in the **Preview** on the right, which you can switch between **Landscape** and **Portrait**. The preview shows **Sample data**. Once saved, your screens show live readings for your location.

![Location field with Austin, TX typed and a list of matching location suggestions](https://support.optisigns.com/hc/article_attachments/56498348459539)

Start typing your city or address in the **Location** field, then pick it from the list of suggestions.

![Air Quality Index app form with the Name and Location fields filled in and the Display section below](https://support.optisigns.com/hc/article_attachments/56498374868755)

Fill in the following:

- **Name** - The name of your Air Quality Index asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
- **Use device setting's location** - Turn this on to show the air quality for each screen's own location instead. See the section below.
- **Location** - The location whose air quality is displayed. Its name shows at the top right of the app.

<a name="UseDeviceSettingsLocation"></a>

### Use Device Setting's Location

If you show the same app on screens in different places, turn on **Use device setting's location**. Each screen then shows the air quality for the location set on that screen. To set a screen's location, go to the **Screens** tab, click **Edit** on the screen, then open **Advanced**. [Learn more about screen locations](https://support.optisigns.com/hc/en-us/articles/4407068788883).

![Use device setting's location switch turned on, with the Location field below it](https://support.optisigns.com/hc/article_attachments/56498374945043)

|  |
| --- |
| **NOTE** |
| **Location** is still required with this setting on. It becomes the fallback, used by any screen that doesn't have a location set. |

---

<a name="Display"></a>

## Display

The **Display** section controls what the app shows and how it looks.

- **Display Mode** - What the app shows:
- **Cycle (Current & Forecast)** - Switches between the current air quality and the forecast. This is the default.
- **Current Air Quality Only** - Shows only the current reading, as in the example at the top of this article.
- **Forecast Only** - Shows only the forecast for the coming days.
- **Theme** - **Light** (the default) or **Dark**.
- **Speed** - How long each view is shown before the app switches. Only available in **Cycle (Current & Forecast)** mode.

![Display Mode dropdown open, listing Cycle (Current & Forecast), Current Air Quality Only and Forecast Only](https://support.optisigns.com/hc/article_attachments/56498382290067)

The forecast shows the next three days, each with its AQI and level, along with a short outlook such as which day is better for spending time outdoors.

![Air Quality Index forecast view with an AQI and level for each of the next three days](https://support.optisigns.com/hc/article_attachments/56498339980051)

Here's the app with **Theme** set to **Dark**:

![Air Quality Index app in the Dark theme, with the AQI gauge and pollutant levels on a black background](https://support.optisigns.com/hc/article_attachments/56498382469907)

For **Speed**, choose **Fast**, **Medium** (the default) or **Slow**. To set your own timing, choose **Custom** and drag the slider to anywhere between 5 and 30 seconds.

![Speed dropdown open, listing Fast, Medium, Slow and Custom](https://support.optisigns.com/hc/article_attachments/56498340201747)

Now hit **Save**. You'll have created an Air Quality Index app, and it will appear in your **Files/Assets**.

![New Air Quality Index asset shown in Files/Assets](https://support.optisigns.com/hc/article_attachments/56498353442579)

---

<a name="DeployingAnAirQualityIndexApp"></a>

## Deploying an Air Quality Index App

To push your Air Quality Index app to a screen, go to the **Screens** tab, then click **Edit** next to the screen you want to display it on.

![Screens list with the Edit button highlighted on a screen row](https://support.optisigns.com/hc/article_attachments/56498372458003)

The **Edit Screen** pop-up will appear. Select **Asset** under **Content Type**, then hit **Change** next to **Selected Asset**.

![Edit Screen dialog with Content Type set to Asset and the Change button highlighted](https://support.optisigns.com/hc/article_attachments/56498372553875)

The **Select Asset** window will open. Search for your Air Quality Index app, click it, then hit **Select**.

![Select Asset dialog with the Air Quality Index asset selected](https://support.optisigns.com/hc/article_attachments/56498353652115)

Back in **Edit Screen**, hit **Save**. Your air quality readings will now display on your screen.

Your Air Quality Index app can also be displayed in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).
