# How to Use the CAP Alert App

Article URL: https://support.optisigns.com/hc/en-us/articles/6604468198291-How-to-Use-the-CAP-Alert-App

Article ID: 6604468198291

Locale: en-us

Updated at: 2026-11-25T18:12:16Z

---

### In this article, we will show you how to set up and test the CAP Alert app in OptiSigns.

- [What You'll Need](#WhatYouNeed)
- [How to Set Up a CAP Alert App](#Set)
  - [Theme Settings](#ThemeSettings)
  - [Advanced Settings](#AdvancedSettings)
- [How to Test Your CAP Alert](#Test)

Some Emergency Alert Systems or Emergency Mass Notification Systems (like Everbridge, RAVE. and Alertus) can push CAP (Common Alerting Protocol) and Integrated Public Alert and Warning System (IPAWS) messages to the targets including digital signage when there is an emergency. You can integrate with these systems using the CAP Alert app with OptiSigns.

Using OptiSigns' CAP Alert app, you can generate a webhook and integrate it with the Emergency Alert System. When there is an emergency, the emergency alert system will call the webhook to send the CAP/IPAWS message and trigger the CAP alert app. The CAP/IPAWS alert will take over the target screens and display the emergency message. The screen will resume and play the original content when the emergency is over.

![example of CAP alert with emergency text](https://support.optisigns.com/hc/article_attachments/6605782051731)

---

<a name="WhatYouNeed"></a>

## What You'll Need

- An OptiSigns account - [Pro Plus Plan or higher](https://www.optisigns.com/pricing)
- An Emergency Alert Feed
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653-What-hardware-and-devices-are-supported)
- A screen, [set up and paired with OptiSigns](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)

---

<a name="Set"></a>

## How to Set Up a CAP Alert App

Go to the OptiSigns portal. Go to **Files/Assets → Apps.**

**EDITOR’S NOTE — The route changed. The portal tab is now Files/Assets, and there is no Add Asset button — Apps is a button in the left sidebar. This step should read Files/Assets then Apps. Image 2 is re-shot to the new page. (delete before publishing)**

![Files/Assets page with the Files/Assets tab and the Apps button marked](https://support.optisigns.com/hc/article_attachments/55560067028883)

Select **CAP Alert:**

![Add App dialog searched for CAP, with the CAP Alert card marked](https://support.optisigns.com/hc/article_attachments/55560059898643)

Now you can set up your CAP Alert app:

![CAP Alert dialog: settings on the left, live preview on the right](https://support.optisigns.com/hc/article_attachments/55560067032339)

- **Name** - Name of your assets, this will not be displayed on the screens.
- **Content Type** - Choose between **Post to Webhook** or **XML**.
- **Enable Authentication** - When checked, will add a **Username** and **Password** section to check Authentication.

  ![Enable Authentication ticked, showing the Username and Password fields](https://support.optisigns.com/hc/article_attachments/55560067033107)
- **Webhook / XML** - Depending on whether you've selected "Post to Webhook" or "XML" above, here is where the webhook or XML script will be placed.
- **Target** - Choose whether this alert will target a specific screen, or tag.
- **Screens/Tags** - Select which screens or group of screens (tags) you want to target for this emergency. (i.e. Fire in building/location 1)
- **Status** - Swap between Active or Inactive for this alert.
- **Emergency Duration** - How long the CAP Alert will take over the screen. Measured in seconds.

<a name="ThemeSettings"></a>

### Theme Settings

Click **Theme Settings** to expand the field and provide a slate of additional options:

![Theme Settings expanded, showing background, theme, colour and layout options](https://support.optisigns.com/hc/article_attachments/55560067033875)

- **Background Image:** Lets you choose a Background image for your CAP Alert. When **Custom** is selected, it will give you the opportunity to **Choose Photo:**

  ![Background Image set to Custom, showing the Choose Photo field](https://support.optisigns.com/hc/article_attachments/55560059904403)

  This photo must already exist as an asset within OptiSigns.
- **Theme:** Choose between **Light** and **Dark** theme. This will disappear if Background Image is set to "Custom".
- **Text Color:** Determines the text color. Can be chosen with Hex Code or via color picker.
- **Text Font:** Choose the font for the text.
- **Font Size:** Choose between Default Font Size, or Custom. When Custom is selected, will provide a new option: **Custom Font Size**.
  **![Font Size set to Custom, showing the size box beside the dropdown](https://support.optisigns.com/hc/article_attachments/55560059907859)**
  - **Font Size:** Choose your font size.
- **Text Alignment/Position:** Choose the alignment and position of the CAP Alert text.
- **Max Number of Rows:** Choose the maximum number of rows to dedicate to the CAP Alert feed.

<a name="AdvancedSettings"></a>

### Advanced Settings

Click **Advanced** to expand the field and provide a slate of additional options:

![Advanced expanded, showing lifecycle, tag, location and status options](https://support.optisigns.com/hc/article_attachments/55560059908499)

- **Enable Lifecycle Handling** - When checked, it allows handling of CAP message lifecycle events including Update, Cancel, and All Clear messages. It does this by checking the <identifier> field. **This option is only applied when "Post to Webhook" is set as the Content Type**. It also enables the below options:

![Enable Lifecycle Handling ticked, showing Handle All Clear, Update and Cancel](https://support.optisigns.com/hc/article_attachments/55560067041555)

- **Handle All Clear** - When enabled, if the alert system sends an "All Clear" message, a brief "all clear" notice will display on all screens for 60 seconds by default. Once this time has passed, content will resume as normal.

|  |
| --- |
| **MORE ABOUT ALL CLEAR** |
| OptiSigns handles All Clear messages in this way:   1. First, it finds the <responseType> in the message:  `<responseType>AllClear</responseType>` 2. Then, it checks the <expires>:  `<expires>2027-01-31T11:23:46-05:00</expires>` 3. If AllClear is noted in the response type, it will display the message **until the designated expires time**. If no time is sent, it will default to 60 seconds. |

- **Handle Update -** When enabled, the app will automatically refresh screens with additional information on the emergency alerts as updates become available.
- **Handle Cancel** - When enabled, the app looks for a "Cancel" message referencing a previous alert. If detected, the emergency alert is immediately removed from your screens and normal content resumes.
- **Item Duration** - How long each individual item in the CAP Alert feed will display.
- **Title Tag** - Message title from the CAP/IPAWS message/RSS feed. Default is <headline> - you can change if your feed is different
- **Description Tag** - Message content from the CAP/IPAWS message/RSS feed, default is <description> - you can change if your feed is different
- **Location (Screen Tags)** - If you can match the screen tags with your location passed from the CAP/IPAWS message/RSS feed - you can use it to control the selection of the target screens. By default, it maps to the "areaDesc" attribute from the CAP alert.
- **Status** - Select your CAP Alert status.

|  |
| --- |
| **IMPORTANT** |
| A common issue we find is the screen displays a "No Content Available" message after users push out the CAP alert using the "aeraDesc" attribute. The solution: if you are not intending to use screen tags to map to location, try changing the Location value from "areaDesc" to any other value, like <areaDesc1>. |

![Advanced filters for severity, certainty, urgency, category and codes](https://support.optisigns.com/hc/article_attachments/55560067043987)

- **Severity, Certainty, Urgency** - Standard attributes of CAP / IPAWS messages, these options allow you to control the filter of the messages. By default, the app will be triggered on all values. However, you can set these similar to tags - this will filter out anything that does not include these tags.
- **Filter content containing** - Allows content to be filtered based on specific words in the title or description. I.E: "fire", so if any title or description contains the word "fire" (case insensitive), the app will trigger the screen takeover.
- **Exclude title containing** - Filter only applying to the title. You can hide all the old feeds by filtering with specific words in the title. I.E: “All Clear”, so after the emergency is gone, all the feeds before this title will be hidden, then the screen will revert to the original content or just display the new content after that.
- **Category, Code, Event Code** - Additional filters allowing you to include or exclude certain event categories, codes, or event codes.

When finished, click **Save**.

---

<a name="Test"></a>

## How to Test Your CAP Alert

After Saving, the app will generate a Webhook URL automatically. When this Webhook is called, it will perform the functions designated in your CAP Alert app. If you share the Webhook URL with your Emergency Alert System, it will be able to trigger this Webhook during an emergency and take over the screens.

To test your CAP alert integration, we recommend using [Postman](https://www.postman.com/) to post a CAP/IPAWS message to the Webhook.

First, download or log in to Postman. Once there, navigate to **Home → Send an API request → New Request:**

**![postman with arrows pointing toward Home tab and New Request button](https://support.optisigns.com/hc/article_attachments/33695686427411)**

Once here, change the request type to **POST:**

![postman demonstration of how to select POST option](https://support.optisigns.com/hc/article_attachments/33695686435475)

Input the Webhook URL for your CAP Alert next.

Now, navigate to the **Body** tab. Here, you can send data two ways: **URL encoded** or as a **raw XML file**. Here we will assume you are sending your data as raw XML, as this is the most common format we see from Emergency Alert Services.

CAP/IPAWS Alerts are generally delivered via an external Emergency Alert System, which are saved as **.xml** or **.txt** files. These are broadcast via the [Common Alerting Protocol Version 1.2](https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html). To push an XML file, click the **raw → Dropdown →** select **XML**.

**![postman step by step on selecting XML format](https://support.optisigns.com/hc/article_attachments/33695686448403)**

Then, copy and paste the following piece of test code into the field:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<alert xmlns="urn:oasis:names:tc:emergency:cap:1.2">
    <identifier>ALERTUS_2317_67_20230131_162046</identifier>
    <sender>Tester</sender>
    <sent>2023-01-31T11:20:47-05:00</sent>
    <status>Actual</status>
    <msgType>Alert</msgType>
    <source>Alertus eEAS Server</source>
    <scope>Public</scope>
    <addresses>ALL</addresses>
    <code>IPAWSv1.0</code>
    <info>
        <language>en-US</language>
        <category>Safety</category>
        <event>TEST Event Name Override</event>
        <responseType>None</responseType>
        <urgency>Immediate</urgency>
        <severity>Severe</severity>
        <certainty>Observed</certainty>
        <eventCode>
            <valueName>SAME</valueName>
            <value>LAE</value>
        </eventCode>
        <effective>2023-01-31T11:20:47-05:00</effective>
        <onset>2023-01-31T11:20:47-05:00</onset>
        <expires>2023-01-31T11:23:46-05:00</expires>
        <headline>Test286</headline>
        <description>This is a Test of the Alertus Emergency Notification System. NO ACTION is Needed. In a real emergency, this system will be used to provide emergency information and protective actions. Please return to your normal activities.</description>
        <area>
            <areaDesc1>Tag1</areaDesc1>
            <geocode>
                <valueName>SAME</valueName>
                <value>000000</value>
            </geocode>
        </area>
        <parameter>
            <valueName>duration</valueName>
            <value>30</value>
        </parameter>
    </info>
</alert>
```

It will look something like this:

![postman xml input example](https://support.optisigns.com/hc/article_attachments/33695707719699)

You can set the duration of the CAP/IPAWS alert message as well. In raw XML format, you can pass the duration value through a system parameter in your CAP alert message.

Now, to test the request, hit **Send**. A piece of text should appear on the console below. If the test was successful, it should give a **200 OK code** and say "status": "success":

![postman showing code layout under raw data tab](https://support.optisigns.com/hc/article_attachments/33695707725715)

And this message (assuming all the defaults were kept in the CAP Alert app) will appear on your screen:

![test message for the CAP alert system](https://support.optisigns.com/hc/article_attachments/33695707733779)

#### Creating a Test Request in urlEncoded Format

Using urlEncoded format, the duration can be passed as URL parameter together with data.

![example in postman of urlencoded format](https://support.optisigns.com/hc/article_attachments/33696696479251)

The rest of the test can be performed identically.

---

## Related Articles

- [How to Use the Emergency Feed App](https://support.optisigns.com/hc/en-us/articles/4409673381011?ref=related)
- [How to Use the Emergency Message/Alert App](https://support.optisigns.com/hc/en-us/articles/360052513253?ref=related)
- [How to Use the Flash Message App](https://support.optisigns.com/hc/en-us/articles/360052827713?ref=related)
- [How to Use the Weather Alert App](https://support.optisigns.com/hc/en-us/articles/6757989639827?ref=related)

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
