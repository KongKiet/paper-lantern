# How to Use the Weather Radar App

Article URL: https://support.optisigns.com/hc/en-us/articles/55906396437523-How-to-Use-the-Weather-Radar-App

Article ID: 55906396437523

Locale: en-us

Updated at: 2026-09-29T19:04:57Z

---

### In this article, we'll set up the Weather Radar app so a live precipitation radar map plays on your OptiSigns screens.

- [What You'll Need](#WhatYoullNeed)
- [How It Works](#HowItWorks)
- [Create a Weather Radar App](#CreateAWeatherRadarApp)
- [Reading the Map](#ReadingTheMap)
- [Troubleshooting](#Troubleshooting)

With the Weather Radar app, your screens show a live precipitation radar map for any location in the United States, with an optional animated forecast of where the rain and storms are heading.

The map updates on its own. Once it is on a screen, there is nothing to refresh.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account with Standard Plan or higher
- A location in the **United States**
- An OptiSigns-enabled device
- A screen, set up and paired with OptiSigns

|  |
| --- |
| **IMPORTANT** |
| Weather Radar currently covers the United States only. The **Location** search offers US places, and there is no radar coverage outside the US. Results are best inside the continental US, where map detail and lightning are available.  **NOTE:** Looking for the app that showed a windy.com map? That app is now called **Windy**, and it is covered in [How to Use Weather Apps in OptiSigns](https://support.optisigns.com/hc/en-us/articles/360017964153). |

---

<a name="HowItWorks"></a>

## How It Works

The radar comes from the US National Weather Service's precipitation radar. A new radar picture is published every 10 minutes, usually about 3 minutes after it is observed. Your screen checks for new pictures every few minutes and adds them as they arrive.

When the forecast is switched on, the map plays the recent radar and then carries on into the next hour, so viewers can see where the weather is moving.

---

<a name="CreateAWeatherRadarApp"></a>

## Create a Weather Radar App

Go to **Files/Assets**, click **Apps**, and search for **Weather Radar**. Click the **Weather Radar** tile.

![Add App dialog searched for radar, showing a single Weather Radar tile highlighted with an arrow](https://support.optisigns.com/hc/article_attachments/55906459208083)

The Weather Radar form opens, with a live preview on the right.

![Weather Radar form with Name and Location filled in as Houston, TX, with an arrow pointing to the Location field](https://support.optisigns.com/hc/article_attachments/55906396705427)

Fill in the form:

- **Name** - What the asset is called in your Files/Assets list.
- **Location** - The place the map centres on. Start typing a US city or address and pick it from the list.
- **Layer** - Leave this on **Weather Radar**, the default, which shows rain, snow and storms colored by intensity. The other layers in the list are not available yet.
- **Zoom** - How much of the area around your location is shown, from **1** (the widest view, and the default) to **4** (the closest).
- **Play Forecast** - When on (the default), the map plays the last hour of observed radar and then the forecast. When off, the screen shows the latest radar picture instead of a loop, and it still updates as new pictures arrive.
- **Playback Speed** - How fast the loop plays: **0.5x**, **1x** (the default) or **2x**. Only shown when **Play Forecast** is on.
- **Forecast Time** - How far ahead the forecast runs: **20**, **40** or **60 min** (the default). Only shown when **Play Forecast** is on.

The orientation menu at the top right of the form switches the preview between **Landscape (16:9)**, **Portrait (9:16)** and **Custom**, so you can check how the map will look on your screen.

Click **Save**, then assign the asset to a screen, playlist or schedule.

---

<a name="ReadingTheMap"></a>

## Reading the Map

![Radar preview map of the Houston area with the time stamp highlighted, above the timeline and colour legend](https://support.optisigns.com/hc/article_attachments/55906411574931)

- **Color Legend** - Along the bottom, from **Light** through **Moderate** and **Heavy** to **Intense**.
- **Time Stamp** - The time of the picture currently shown. Forecast pictures are shaded differently from observed ones, and the timeline beneath it shows where the observed radar ends and the forecast begins.
- **Lightning** - Inside the continental US, recent lightning strikes are marked on the map.
- **City names** - Nearby towns and cities are labelled. When labels would overlap, the smaller places are hidden.
- **Credits** - A small line along the bottom credits the radar and map data sources. It is required by the data providers and cannot be removed.

---

<a name="Troubleshooting"></a>

## Troubleshooting

**The screen says "Waiting for map data".**

The radar feed has not reported in yet. This usually clears on its own within a few minutes of the asset first playing.

**The screen says "No recent frames".**

No recent radar pictures are available for the map. The app keeps checking and resumes as soon as new pictures arrive.

**The screen says "Map imagery unavailable".**

The screen could not load the map. Check that the device is connected to the internet. The map keeps trying and comes back on its own once it can load again.

**The screen says "Layer not available".**

A layer other than **Weather Radar** was chosen. Only Weather Radar is available for now, so edit the asset, set **Layer** back to **Weather Radar**, and click **Save**.

**The animation looks frozen, or updates less often than usual.**

During very high demand the service may briefly slow or pause new pictures. The screen keeps showing the last good map and catches up automatically.

**The map shows something other than my location.**

The asset does not have a valid location saved. Edit the asset, pick your location from the **Location** list rather than only typing it, and click **Save**.

**My location is outside the United States.**

Weather Radar covers the US only for now. For weather outside the US, use the [Weather Wall app](https://support.optisigns.com/hc/en-us/articles/360017964153).

**The animation is not smooth on an older device.**

The app uses the device's graphics hardware to animate smoothly. Older devices fall back to a simpler animation, which can look less fluid.
