# How to Display Content From Websites That Require a Login

Article URL: https://support.optisigns.com/hc/en-us/articles/360037391854-How-to-Display-Content-From-Websites-That-Require-a-Login

Article ID: 360037391854

Locale: en-us

Updated at: 2026-10-16T17:01:33Z

---

### In this article, we'll show the best way to put dashboards, boards and reports that sit behind a login on your digital signs with OptiSigns.

- [What You'll Need](#WhatYoullNeed)
- [Option 1: Use a Dedicated App](#Option1UseADedicatedApp)
- [Option 2: Use Web Scripting](#Option2UseWebScripting)
- [Option 3: Use Secured Dashboard](#Option3UseSecuredDashboard)
- [Websites With a Browser Sign-In Pop-up](#WebsitesWithABrowserSignInPopUp)
- [Signing In on the Device](#SigningInOnTheDevice)

A lot of the content worth showing on your screens sits behind a login: a project board in Jira, a sales dashboard in Salesforce, a report in Tableau or Power BI. OptiSigns gives you several ways to display it, and each one keeps your screens signed in without anyone standing at the device.

![Two kinds of login: a browser sign-in pop-up and a website login page](https://support.optisigns.com/hc/article_attachments/360103797493)

Here's how to decide what method to use:

If there is a dedicated OptiSigns app for the service, simply use that app. This is the easiest and most reliable option.

If there's no dedicated app, and the site has a normal login page, use [**Web Scripting**](https://support.optisigns.com/hc/en-us/articles/1500012522362). You'll need a Pro Plus plan for this.

If the login process requieres multi-factor authentication (MFA) on several screens, you have a mix of device types, or the report is slow to load, use [**Secured Dashboard**](https://support.optisigns.com/hc/en-us/articles/19589190970771).

The site asks for a username and password in a browser pop-up, use the [**Website app**](https://support.optisigns.com/hc/en-us/articles/360016382473) with the sign-in details in the URL.

Let's get started.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account. The plan you need depends on the option you use:
- Website app, and most dedicated apps - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- Web Scripting and Secured Dashboard - [**Pro Plus Plan** or higher](https://www.optisigns.com/pricing)
- An account on the website or service you want to display
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

---

<a name="Option1UseADedicatedApp"></a>

## Option 1: Use a Dedicated App

OptiSigns has dedicated apps for many popular services. You sign in once in the OptiSigns portal, and the app keeps your screens up to date. Nobody needs to sign in on the device.

From the OptiSigns portal, go to **Files/Assets** and select **Apps**.

![OptiSigns Files/Assets page with the Apps button highlighted](https://support.optisigns.com/hc/article_attachments/56488921897491)

Search for the service you want to display. If it has a dedicated app, it will appear in the results.

![Add App dialog searched for Jira, with the Jira app card highlighted](https://support.optisigns.com/hc/article_attachments/56488885500819)

Dedicated apps include:

**Project and work management**

- [Jira](https://support.optisigns.com/hc/en-us/articles/360037416494)
- [Trello](https://support.optisigns.com/hc/en-us/articles/360050244454)
- [Asana](https://support.optisigns.com/hc/en-us/articles/1500002233221)
- [Monday.com](https://support.optisigns.com/hc/en-us/articles/11032964830227)
- [Notion](https://support.optisigns.com/hc/en-us/articles/5119724468371)
- [Smartsheet](https://support.optisigns.com/hc/en-us/articles/8399990754195)
- [Airtable](https://support.optisigns.com/hc/en-us/articles/9392587446675)
- [Zendesk](https://support.optisigns.com/hc/en-us/articles/360060919453)

**Dashboards and reports** (Pro Plus Plan or higher)

- [Salesforce](https://support.optisigns.com/hc/en-us/articles/55895814798739)
- [Tableau](https://support.optisigns.com/hc/en-us/articles/39250660729747)
- [Power BI](https://support.optisigns.com/hc/en-us/articles/360024859713)
- [Looker Studio (Data Studio)](https://support.optisigns.com/hc/en-us/articles/360052088413)
- [Grafana](https://support.optisigns.com/hc/en-us/articles/55447693635731)
- [Databricks](https://support.optisigns.com/hc/en-us/articles/53952018650515)
- [Snowflake](https://support.optisigns.com/hc/en-us/articles/53028011485715)

**Microsoft 365 and Google**

- [SharePoint](https://support.optisigns.com/hc/en-us/articles/4414539282067)
- [Excel Online](https://support.optisigns.com/hc/en-us/articles/4529298306963)
- [PowerPoint Online](https://support.optisigns.com/hc/en-us/articles/4414355658899)
- [Google Sheets](https://support.optisigns.com/hc/en-us/articles/360056977214)

Follow the article for your app to set it up.

---

<a name="Option2UseWebScripting"></a>

## Option 2: Use Web Scripting

If there's no dedicated app, Web Scripting can sign in for you. You record the steps you take to log in and reach your page, such as entering your username and password and clicking through to a dashboard. OptiSigns then replays those steps on your screens. It also supports sites that use two-factor authentication (2FA).

Your recorded steps and password are encrypted, and are only decrypted on your device. For extra protection, you can add your own **Master Password**.

From **Files/Assets**, select **Apps**, then search for **Web Scripting** and select the **Web Scripting** app.

![Add App dialog searched for Web Scripting, with the Web Scripting app card highlighted](https://support.optisigns.com/hc/article_attachments/56488921904275)

The Web Scripting app settings will open. Paste your recorded steps into **Recorded Script**, and fill in the 2FA fields if your site uses them.

![Web Scripting app form showing the Name, Master Password, Recorded Script and 2FA fields](https://support.optisigns.com/hc/article_attachments/56488885506579)

To record your steps and fill in each field, follow our guide: [How to use the Web Scripting App](https://support.optisigns.com/hc/en-us/articles/1500012522362).

|  |
| --- |
| **NOTE** |
| Web Scripting isn't supported on Samsung SSSP smart TVs, LG webOS smart TVs or Apple TV devices. |

---

<a name="Option3UseSecuredDashboard"></a>

## Option 3: Use Secured Dashboard

Secured Dashboard uses the same recorded steps as Web Scripting. Instead of signing in on each device, it signs in on a secure OptiSigns server and sends a picture of your page to your screens. We recommend it when:

- You use one account with MFA on several screens. Each MFA code works only once, so several devices signing in at the same time can fail.
- You have a mix of device types, such as Windows and Android, and want your report to look the same on all of them.
- Your report is slow to load, and you don't want the loading screen to show.

From **Files/Assets**, select **Apps**, then search for **Secured Dashboard** and select the **Secured Dashboard** app.

![Add App dialog searched for Secured Dashboard, with the Secured Dashboard app card highlighted](https://support.optisigns.com/hc/article_attachments/56488885509139)

The Secured Dashboard app settings will open. Enter a **Name** and paste your recorded steps into **Recorded Script**.

![Secured Dashboard app form showing the Name and Recorded Script fields](https://support.optisigns.com/hc/article_attachments/56488885510419)

For the full steps, follow our guide: [How to use Secured Dashboard App](https://support.optisigns.com/hc/en-us/articles/19589190970771).

---

<a name="WebsitesWithABrowserSignInPopUp"></a>

## Websites With a Browser Sign-In Pop-up

Some websites ask for your username and password in a small browser pop-up, rather than on a login page. For these, you can add your sign-in details to the start of the URL in the [Website app](https://support.optisigns.com/hc/en-us/articles/360016382473), in this form:

https://username:password@www.example.com/

**For example: https://guest:guest@jigsaw.w3.org/HTTP/Basic/**

|  |
| --- |
| **NOTE** |
| Anyone who can view the asset in your OptiSigns account can see the password in the URL. If that's a concern, use Web Scripting instead. |

---

<a name="SigningInOnTheDevice"></a>

## Signing In on the Device

You can also show a login page in the [Website app](https://support.optisigns.com/hc/en-us/articles/360016382473), then connect a mouse and keyboard to the device and sign in there. On a Fire TV Stick, you can connect them with a [USB hub adaptor](https://support.optisigns.com/hc/en-us/articles/360055080914).

We recommend this only as a last resort:

- It doesn't work with every website or device.
- Someone has to be at the device to sign in.
- If the device's cache is cleared, or the website signs you out, someone has to sign in again.

If you can, use one of the options above instead.
