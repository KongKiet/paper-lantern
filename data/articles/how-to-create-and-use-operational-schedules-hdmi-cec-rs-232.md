# How To Create and Use Operational Schedules (HDMI-CEC, RS-232)

Article URL: https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232

Article ID: 28598173096723

Locale: en-us

Updated at: 2026-11-06T15:07:59Z

---

### Do you want your screen to automatically turn on and off according to a schedule to save time and energy? Operational Schedule, an all-in-one feature, makes this easier than ever before!

|  |
| --- |
| Use Case |
| In a corporate office setting, this feature can be employed to control the power, volume, and brightness settings of digital displays across multiple conference rooms and common areas, ensuring they operate only during designated business hours or specific events. |

**In this article:**

1. [Introduction to Operational Scheduling](#Introduction)
   - [Schedules vs. Operational Schedules](#VS)
2. [Assigning Operational Schedules to Screens](#Assigning)
3. [Create Your Own Advanced Schedule](#Create)

## <a name="Introduction"></a> **Introduction to Operational Scheduling**

Operational Schedule allows you to schedule when your TV powers on/off and to control the volume and brightness through the device level, HDMI-CEC, or RS-232 connections. HDMI-CEC is a popular feature available on most consumer TVs right now, while RS-232 is useful for commercial-grade displays.

|  |
| --- |
| Limitations |
| - You will need the **Pro+ Plan** or above to have access to this HDMI-CEC and RS-232 feature. The HDMI-CEC or RS-232 capabilities allow you to Power On/Off your TV using the Operational Schedule, and change the volume or mute the screen. |
| - If you have the **Free** or **Standard** plan and create an Operational Schedule, the player will display black to save power and device life. Free and Standard plan users will not have access to the "Advanced Scheduling" option: Advanced Scheduling toggle in the Operational Schedule dialog header, switched off |
| - To access Operational Schedule with an HDMI-CEC port, you will need our [**OptiStick**](https://shop.optisigns.com/products/optisigns-android-stick-player-2), [**Pro Signage Player**](https://shop.optisigns.com/products/optisigns-digital-signage-player), [**ProMax Player**](https://support.optisigns.com/hc/en-us/articles/38680194603155-OptiSigns-ProMax-Player). The player will need to be plugged in to an HDMI-CEC port to function. RS-232 functionality can be used with any device which supports it.   - Please ensure your Android Player device is ***powered from an outlet, not the screen's USB port.***If plugged into the USB port, the act of turning off the screen will also power off the device - meaning, it will not be able to turn the screen back on.   - Operational Scheduling is not supported on Roku nor Samsung Tizen devices. The option will not be visible. |

**One last important note:**

HDMI-CEC is referred to by numerous names. Depending on the brand of your TV or device, it might be called something else, and may need to be enabled in the device software.

Here is a complete list of [**TV Manufacturer CEC Names**](https://support.klipsch.com/hc/en-us/articles/360045728971-TV-Manufacturer-CEC-Names). Simply find your device on the list and enable HDMI-CEC, if necessary.

<a name="VS"></a>

### Schedules vs. Operational Schedules

**Operational Schedules** are distinct from **Schedules**, which allow you to schedule the actual content which appears on a digital sign.

- **Operational Schedules** are for turning *on and off the actual display*.
- **Schedules** are for displaying *what content or playlists will display on the display*.

For more on Schedules, see our article on [**Creating and Using Schedules**](https://support.optisigns.com/hc/en-us/articles/360016981853-Creating-and-Using-Schedules-with-OptiSigns).

---

## <a name="Assigning"></a> **Assigning Operational Schedules to Screens**

**1. Navigate** to [**Screens Management**](https://app.optisigns.com/app/screenManagement), then select **Edit** on your desired screen.

![Screens list with the Edit button on a screen row highlighted](https://support.optisigns.com/hc/article_attachments/55337755006483)

**2.**Select **Operational Schedule**, then select your schedule from the dropdown menu:

1. **Default Schedule**: Screen is on, 4:00AM - 11:59PM, every day
2. **New:** Create your own schedule

![Operational Schedule dropdown open, with + New at the top above None](https://support.optisigns.com/hc/article_attachments/55337722711059)

**3.**If **Default Schedule** is selected, the time and days can adjusted by clicking **Edit**.

|  |
| --- |
| **Note:** ***Advanced Scheduling** will allow you to create your own schedule.* |

![Operational Schedule dialog in simple mode, showing Active Days and Active Hours](https://support.optisigns.com/hc/article_attachments/55337755008531)

**4.**Select your **Operational Schedule**, assign your desired content, then click **Save.**

![Edit Screen dialog with an operational schedule selected and Save enabled](https://support.optisigns.com/hc/article_attachments/55337755009683)

**5.** Once saved, your TV power will be on during the operational schedule and will be turned off or display black outside of the operational schedule.

|  |
| --- |
| Note: If there is nothing scheduled, your screen will automatically turn off or display a black screen during that time. You don't need to set a specific schedule for this function to activate. |

---

## <a name="Create"></a> **Create Your Own Advanced Schedule**

**1.**Navigate to your [**Screens Management**](https://app.optisigns.com/app/screenManagement), select your desired screen, click **Operational Schedule**, select **+ New** from the Operational Schedule dropdown menu.

![Operational Schedule dropdown open, with + New at the top of the list](https://support.optisigns.com/hc/article_attachments/55337722713875)

**2.** Select your desired event time by clicking on a time, then drag-and-dropping to create an event.

On the side menu, you can customize your schedule with the following options:

![Advanced event form: Name, Schedule, Repeat, Power State, Control Method, Volume, Brightness](https://support.optisigns.com/hc/article_attachments/55337755013139)

- **Name:** Create a name for your schedule. We ***highly recommend*** doing this so as to differentiate it from other Operational Schedules you may wish to make.
- **Schedule:**Where you schedule the time of your Operational Schedule.![Schedule time picker, setting the event from and to times](https://support.optisigns.com/hc/article_attachments/55337755013907)
- **Repeat:**Choose whether you'd like your event to repeat from the available options, or create your own custom repeat.![Repeat dropdown open: Daily, Weekly, Every weekday, Every Weekend, Custom](https://support.optisigns.com/hc/article_attachments/55337722716051)
- **Power State:** Choose from On, Off, or None.
  - **On:** Sends a signal to turn the screen **ON** during the designated hours. This will be through RS-232 first if available, then through HDMI-CEC. This is our ***recommended option.***
  - **Off:**Sends a signal to turn the screen **OFF**during the designated hours. This will be through RS-232 first if available then through HDMI-CEC.
  - **None:** Will not power on/off your screen.

    ![Power State dropdown open, showing On, Off and None](https://support.optisigns.com/hc/article_attachments/55337722717203)
- **Control Method:** Choose which method you'd like to power on or off your screen.
  - **Auto:** Will automatically detect which method you have (RS232 or HDMI-CEC)
  - **RS232:** Will exclusively attempt to power on/off your device via RS232 connection.
  - **HDMI-CEC:** Will exclusively attempt to power on/off your device via HDMI-CEC connection.

|  |
| --- |
| **Note:** On Auto, y*our device will try RS-232 first if available, then HDMI-CEC command to turn off TV/Monitor. Your TV/Monitor model and player needs to support this feature for it to work. Players sold by OptiSigns support HDMI-CEC and RS-232.* |

- **Mute:**Choose if you'd like your screen to be mute or not if sound is available.
- **Volume:**Adjust the volume of the screen.
- **Brightness:** Adjust the brightness of the screen, with 100% being your screen's current brightness.
- **RS-232 Commands:** If you have already configured [**RS-232 commands**](https://support.optisigns.com/hc/en-us/articles/9061950942995-Using-RS-232-to-Schedule-TV-Power-On-Off-or-other-commands), you can select them from this dropdown.
- **HDMI Lock:**If checked, the system will periodically check which HDMI input the TV is using. If it detects that the TV has been switched away from the OptiSigns HDMI-CEC input, it will automatically switch back. This check runs approximately once every hour.

**3.**Make sure to **Save** your event at the bottom so that it will assign the event to the schedule. Then, click "**Apply**" to assign it to your screen.

![Week calendar showing the saved event, with Apply at the bottom right](https://support.optisigns.com/hc/article_attachments/55337755018259)

**4.**Once applied, click **Save** to apply and activate all changes to your screens.

![Operational Schedule set on the screen, with the Save button highlighted](https://support.optisigns.com/hc/article_attachments/55337722720275)

With that, you've created your Operational Schedule. This schedule can be ***reused as often as you like***, and can be applied to numerous screens. Simply select it from your Edit Screen tab for each screen you'd like to apply it to.

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
