# Preventing the OptiSigns App from Turning On your Screen

Article URL: https://support.optisigns.com/hc/en-us/articles/15808407287315-Preventing-the-OptiSigns-App-from-Turning-On-your-Screen

Article ID: 15808407287315

Locale: en-us

Updated at: 2026-10-28T18:52:26Z

---

### In this article, we'll explain which settings make the OptiSigns app turn your TV back on, and how to turn each one off.

- [Why the TV Turns Back On](#WhyTheTVTurnsBackOn)
- [Turn Off Keep Awake on the Device](#TurnOffKeepAwakeOnTheDevice)
- [Check the Screen's Operational Schedule in the Portal](#CheckTheScreensOperationalScheduleInThePortal)
- [Still Turning On?](#StillTurningOn)

If you turn off your TV and it turns itself back on with OptiSigns playing, a setting on the screen is waking it up. This article explains which settings can do that and how to turn each one off.

This applies to the OptiSigns Android app, including Amazon Fire TV Stick, Android TV boxes and TVs with Android built in. Parts of this article (specifically regarding Operational Schedules) applies to OptiSticks and Pro Players, as well.

---

<a name="WhyTheTVTurnsBackOn"></a>

## Why the TV turns back on

The OptiSigns app can wake the TV in two ways:

- **Keep Awake** (Device Side Menu). When the screen turns off, the app wakes the screen and opens itself again. It's meant to stop a screen from going dark by mistake, so it also undoes the TV's power button. This is only available on certain OptiSigns versions. The
- **Operational Schedule** (OptiSigns Portal setting). If the screen has an Operational Schedule, the app sends a power-on command to the TV over HDMI-CEC at the scheduled "on" times. With **HDMI Lock** enabled, it also tells the TV to switch to the OptiSigns input every so often, which turns the TV on if it's off.

If the TV turns on within a second or two of being turned off, the cause is usually Keep Awake. If it turns on at a set time, or some time later, check the Operational Schedule.

---

<a name="TurnOffKeepAwakeOnTheDevice"></a>

## Turn Off Keep Awake on the Device

Open the OptiSigns side menu on the screen:

1. Scroll to **Keep Awake**.
2. Switch **Keep Awake** off.

Now when you turn off the TV, OptiSigns won't turn it back on.

|  |
| --- |
| **IMPORTANT** |
| The "Keep Awake" setting only appears on devices that let OptiSigns open itself in the background: devices running Android 9 or lower, or devices where OptiSigns has the **Display over other apps** permission. If it isn't in the menu, Keep Awake can't turn your TV on, so check the Operational Schedule below. |

|  |
| --- |
| **NOTE** |
| Keep Awake is on by default on Firesticks and Android TV boxes, but off by default on TVs with Android built-in. |

---

<a name="CheckTheScreensOperationalScheduleInThePortal"></a>

## Check the Screen's Operational Schedule in the OptiSigns Portal

Sign in to the OptiSigns portal and go to **Screens**.

Open the screen and select **Edit**.

Find **Operational Schedule**.
![Edit Screen dialog with the Operational Schedule section highlighted](https://support.optisigns.com/hc/article_attachments/56914161601683)

If a schedule is selected, either:

- Change it so the TV is off at the times you want it off
- Turn off **HDMI Lock** on the schedule's events, so the app stops switching the TV to the OptiSigns input
- Set **Operational Schedule** to **None** if you don't need one.
  ![Operational Schedule event form with the HDMI Lock checkbox highlighted](https://support.optisigns.com/hc/article_attachments/56914161603859)

|  |
| --- |
| **NOTE** |
| Operational Schedules need an upgraded plan. If you see **Upgrade Required**, your screen doesn't have one, so this isn't the cause. |

---

<a name="StillTurningOn"></a>

## Still Turning On?

- Check that **Keep on top** isn't reopening the app after you close it. Keep on top only reopens the app; it doesn't turn the TV on by itself.
- Check your TV's own settings for HDMI-CEC (it may be called Anynet+, SimpLink, Bravia Sync or similar). If CEC is off on the TV, the app can't turn the TV on over HDMI. CEC also controls the Operational Schedule's power-off, so turning it off disables that too.

If you have more questions or feedback about OptiSigns, contact our support team at support@optisigns.com.
