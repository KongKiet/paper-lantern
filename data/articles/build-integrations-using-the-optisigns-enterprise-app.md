# Build Integrations Using the OptiSigns Enterprise App

Article URL: https://support.optisigns.com/hc/en-us/articles/13320135306515-Build-Integrations-Using-the-OptiSigns-Enterprise-App

Article ID: 13320135306515

Locale: en-us

Updated at: 2026-10-30T17:06:59Z

---

### In this article, we'll build a custom page with the Enterprise App, send data to a screen from another system, and check the data that arrived.

- [How It Works](#HowItWorks)
- [Create an Enterprise App](#CreateAnEnterpriseApp)
- [Connect Your System](#ConnectYourSystem)
- [Send Data to a Screen](#SendDataToAScreen)
- [Check the Data on the Screen](#CheckTheDataOnTheScreen)
- [Next Steps](#NextSteps)

The Enterprise App lets your own systems send live data to your screens. You build a web page that shows the data, and your system sends the data to a screen whenever it needs to. The screen switches to your page straight away and shows what you sent.

For example, a car dealership's service system can tell a customer their car is ready. It sends the customer's name, car and service advisor to a screen in the waiting room, and the screen shows a personal message:

![Data sent from a system on the left, and the screen showing the personalized message it produced on the right](https://support.optisigns.com/hc/article_attachments/56986530466323)

You can use the Enterprise App to:

- Show a custom page on a screen, filled in with data from any system you connect.
- Send freeform data from your business applications to your screens.
- Build your own single-purpose app for managing your screens and content.

**Note:** The Enterprise App is available for Enterprise accounts. If you can't open it, contact us at support@optisigns.com.

---

<a name="HowItWorks"></a>

## How It Works

Setting up an integration takes three steps:

1. Create an Enterprise App and build the page your screen will show.
2. Connect your system. In this guide, we use the demo **Control Center** in place of your own system.
3. Send data to a screen and check that it arrived.

---

<a name="CreateAnEnterpriseApp"></a>

## Create an Enterprise App

Go to [app.optisigns.com](https://app.optisigns.com/) and log in.

Select **Files/Assets**, then select **Apps**.

Search for **Enterprise**, then select **Enterprise App**.

![Add App dialog with Enterprise in the search box and the Enterprise App tile highlighted](https://support.optisigns.com/hc/article_attachments/56986530467859)

Choose how to create your page:

- **Start from the template:** select the template picture under **Template - URL Display App**. This opens a code editor with sample code you can change

- **Use a page you already have:** enter a **Name** and the page's **Url**, then select **Create**.

![Enterprise App editor with the Name and Url fields, the Create button and the URL Display App template](https://support.optisigns.com/hc/article_attachments/56986530469011)

If you started from the template, change the sample code to set how the page looks and how it uses the data it receives. You can use the sample code as it is to try things out.

![Code editor with the template's sample code and the page preview](https://support.optisigns.com/hc/article_attachments/56986536771475)

Select **Save & Deploy**. Your page is ready to use.

---

<a name="ConnectYourSystem"></a>

## Connect Your System

Your own system, or an app you build for it, sends data to your screens. To see how that works, use the demo **Control Center**, which does the same job.

In the Enterprise App editor, select **Control Center**. The demo Control Center opens in a new tab.

![Enterprise App editor toolbar with an arrow on the Control Center button](https://support.optisigns.com/hc/article_attachments/56986536771987)

Log in with your OptiSigns account. The Control Center uses your OptiSigns permissions, so it only shows the screens you're allowed to manage. Your own integrations work the same way.

The Control Center lists your screens. Search for the screen you want to control, then select its **Edit** button.

![Demo Control Center listing a connected screen, with an arrow on its Edit button](https://support.optisigns.com/hc/article_attachments/56986536772755)

The **Edit Device** page opens. This is where you choose what data to send to the screen.

![Edit Device page in the demo Control Center with Name, Expire Time, Data and Type fields](https://support.optisigns.com/hc/article_attachments/56986536778387)

---

<a name="SendDataToAScreen"></a>

## Send Data to a Screen

Your screen can be playing anything: an asset, a playlist or a schedule. When you send data, the screen switches to your Enterprise App and shows the data.

In **Data**, enter the data you want to send. It can be plain text or JSON.

In **Type**, select **Send Data & Assign**.

In **Asset Id**, enter the ID of your Enterprise App.

Select **Save**. The screen switches to your Enterprise App and shows your data.

![Edit Device page with JSON data entered, Send Data & Assign selected and an Asset Id, with arrows on the data and Save](https://support.optisigns.com/hc/article_attachments/56986530473235)

To end the takeover and go back to the screen's usual content, select **Stop**.

---

<a name="CheckTheDataOnTheScreen"></a>

## Check the Data on the Screen

To see the data a screen received, open the screen in the OptiSigns portal:

Go to **Screens**, then select **Edit** on the screen.

Expand **Advanced**, then select **More**.

At the bottom of the section, select the **Device Extension Data** button.

![Edit Screen panel with an arrow on the Device Extension Data button at the bottom of the advanced settings](https://support.optisigns.com/hc/article_attachments/56986536780435)

The **Device Extension Data** window shows the data the screen received. Select **Copy** to copy it, or **Edit** to change it.

![Device Extension Data window with a data box and Cancel, Copy and Edit buttons](https://support.optisigns.com/hc/article_attachments/56986536781331)

The screen shows your data in the page you built. In this example, it shows the customer's name, car, service advisor and a photo of the car:

![Screen showing the personalized car-ready message built from the data that was sent](https://support.optisigns.com/hc/article_attachments/56986530475411)

---

<a name="NextSteps"></a>

## Next Steps

- [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
- [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)

If you have questions or feedback, contact our support team at support@optisigns.com.
