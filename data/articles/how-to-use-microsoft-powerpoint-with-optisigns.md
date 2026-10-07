# How to Use Microsoft PowerPoint with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/4414355658899-How-to-Use-Microsoft-PowerPoint-with-OptiSigns

Article ID: 4414355658899

Locale: en-us

Updated at: 2026-09-30T15:53:27Z

---

### Microsoft PowerPoint is an incredibly popular way to create and share your presentations. With OptiSigns, you can bring these presentations to your digital screens in a variety of ways.

---

**In this article:**

- [How to Use Your PowerPoint With OptiSigns](#1)
  - [Option 1: Upload a PowerPoint File](#1) **(Easiest & Recommended)**
  - [Option 2: Sign in with Your Microsoft Account](#2) **(PPT changes auto sync to your screens)**
  - [Option 3: Embed Your PowerPoint](#3)
- [Best Practices for Using PowerPoint With OptiSigns](#Best)
- [FAQs](#FAQs)

![PowerPoint Online editor with a presentation open](https://support.optisigns.com/hc/article_attachments/4414348181267)

---

<a name="1"></a>

## Option 1: Upload a PowerPoint File

***We highly recommend this method!***

Depending on how you download your PowerPoint, this option can be useful if you want your videos, animations or transitions to work. You can either download your PowerPoint as:

- **A Video/MP4:** This **will play** any videos, transitions, or animations your PowerPoint may have.
- **A PPT File:** Videos, transitions, and animations will not play, but you can adjust the duration of slides.

**That said, let's get started!**

1. Download your PowerPoint to your device.
2. Log in to the **OptiSigns** portal.
3. Navigate to the **Files/Assets** page.
4. Click [**Upload Files**](https://support.optisigns.com/hc/en-us/articles/360016247974).
5. **Drag** in or **select** your PowerPoint file from your device.
6. Click **Upload**.
   **![Upload Files dialog with Quarterly-Update.pptx selected and the Upload 1 file button highlighted](https://support.optisigns.com/hc/article_attachments/55936724803603)**
7. Either: **Assign** to a screen on the Screens Management page or **push** the asset to your screen.
   - If downloaded as a **PDF,** select the **Duration (seconds)**of the entire document. *(Min. 4/page)*
     ![Push To Screens dialog for a PDF, with the Duration (seconds) field highlighted](https://support.optisigns.com/hc/article_attachments/55936724805139)

### Limitations

- Videos, transitions, and animations will not play if downloaded as a PDF or PPT file. It will just be a slideshow.

---

<a name="2"></a>

## Option 2: Sign in with Your Microsoft Account

This option allows you to access private PowerPoint files directly from your Microsoft account. With this option, your PowerPoint will update in our portal with any changes you make to it.

|  |
| --- |
| **NOTE** |
| The first time you sign in, your account will require Administrator access.   - If you are using a school/work Microsoft account, your IT admin may need to approve the permission the first time. - If you see a message like “Need admin approval” or you cannot accept the permission screen, please forward that screen to your IT admin and ask them to approve the OptiSigns access request for your tenant. |

1. **Log in** to the OptiSigns portal.
2. Go to **Files/Assets**, then **Apps,** and search for the **PowerPoint Online** app.
   ![PowerPoint Online app with Enter Embed Code and the Microsoft Sign in button highlighted](https://support.optisigns.com/hc/article_attachments/55936724806291)
3. Click “**Sign In**” in the OptiSigns app.
4. **Select the PowerPoint file** you wish to display.
   ![PowerPoint Online app signed in with Microsoft: Name, URL, Speed, and Force Sync Interval under Advanced](https://support.optisigns.com/hc/article_attachments/55936708676243)
5. **Name your asset** for easy identification (this name will not be shown on the screen).
6. **Adjust the speed** of slide transitions.
   - **Slow:** 19 seconds
   - **Medium:** 14 seconds
   - **Fast:** 9 seconds
   - **Custom:** Choose how fast your slide transitions will go.
7. Optionally, **customize the Update Interval** by changing the Force Sync Interval (default: 12 hours).
8. Click **Save** to finalize your settings.
9. Push to Screens

### Limitations

- Does not have animations or transitions, making it a regular slideshow
- Videos will not play and will only show the thumbnail

---

<a name="3"></a>

## Option 3: Embed Your PowerPoint

*We do not currently recommend this option unless you are displaying one page.*

1. **Upload your PowerPoint file** to Microsoft OneDrive and **open it**.
2. Navigate to the **File** tab, select **Share**, and then click **Embed**.
   ![PowerPoint Online File menu with Share selected and the Embed option highlighted](https://support.optisigns.com/hc/article_attachments/32753260331411)
3. **Copy** the HTML embed code.
   ![PowerPoint Embed window with the embed code selected and a Copy button](https://support.optisigns.com/hc/article_attachments/32753266835731)
4. Next, **Share** your presentation publicly by clicking the **Share** button in PowerPoint Online.
5. Select **Copy Link**
   - Make sure that the link is accessible to anyone!
     ![PowerPoint Share menu and Link settings with Anyone selected and Apply highlighted](https://support.optisigns.com/hc/article_attachments/32753266842003)
6. **Replace** the URL in the generated embed code with the **public** **URL** of your PowerPoint that you just copied**,** as shown below. This ensures that the presentation is accessible without requiring a login.

   ```html
   <iframe src="https://Your-Public-URL&amp;action=embedview&amp;wdAr=1.7777777777777777&amp;wdEaa=1" width="476px" height="288px" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>
   ```
7. **Log in** to the OptiSigns portal.
8. Go to **Files/Assets**, then **Apps,** and search for the **PowerPoint Online** app.
   ![Add App dialog searched for PowerPoint, with the PowerPoint Online app card highlighted](https://support.optisigns.com/hc/article_attachments/55936724808595)
9. Paste the **modified embed code.**
   **![PowerPoint Online app form with the embed code pasted and Update Interval 600 under Advanced](https://support.optisigns.com/hc/article_attachments/55936708681363)**
10. Optionally, **customize the Update** **Interval** (default: 600 seconds).
11. Click **Save.**
12. [**Push to Screens**](https://support.optisigns.com/hc/en-us/articles/18988049363859)

### Limitations

- Auto-advancing does not work.
- Needs a stable internet connection to display.
- Only works when the PowerPoint URL is accessible to anyone.
- PowerPoint UI will appear instead of being in seamless presentation mode.

---

<a name="Best"></a>

## Best Practices for Using PowerPoint with OptiSigns

- **File Size:** Keep your PowerPoint file under **25MB** for optimal performance. Complete app size **cannot exceed 105MB**.
- **Avoid Embedded Videos:** Videos can increase file size and cause performance issues. Instead, consider exporting your presentation as a video if animations or video playback are essential.
- **Use Simple Transitions:** Complex animations and transitions may not render properly. Stick to basic transitions or upload a video version of your presentation if needed.

---

<a name="FAQs"></a>

## FAQs

#### Why does using PowerPoint with OptiSigns require admin permission?

OptiSigns uses Microsoft APIs for integration. In order for our integrations to work, the integration has to be approved by an administrator. This is the same across all integrations using Microsoft APIs.

This administrator access is only needed for first time access. Once the OptiSigns app is approved for use, other users can use OptiSigns directly.

#### I want to log in to PowerPoint directly through my Microsoft account, but I don't see the option! What's going on?

If you're setting up the app but can't log in directly through Microsoft, you're likely logged on through a **Branded Portal.**

To use Microsoft single sign-on, sign in through [app.optisigns.com](http://app.optisigns.com) rather than your Branded Portal.

## That's it!

You've now successfully uploaded your PowerPoint file to OptiSigns!
