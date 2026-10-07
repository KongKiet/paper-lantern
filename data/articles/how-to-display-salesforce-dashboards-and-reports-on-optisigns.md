# How to Display Salesforce Dashboards and Reports on OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/55895814798739-How-to-Display-Salesforce-Dashboards-and-Reports-on-OptiSigns

Article ID: 55895814798739

Locale: en-us

Updated at: 2026-09-29T19:44:32Z

---

### In this article, we'll connect your Salesforce organization so its dashboards and reports display on your OptiSigns screens.

- [What You'll Need](#WhatYoullNeed)
- [Check Your Salesforce Licensing First](#CheckYourSalesforceLicensingFirst)
  - [Check the License](#CheckTheLicense)
  - [Enable the Slack Apps](#EnableTheSlackApps)
- [Who Does What in Salesforce](#WhoDoesWhatInSalesforce)
- [Create an External Client App in Salesforce](#CreateAnExternalClientAppInSalesforce)
  - [Open Setup](#OpenSetup)
  - [Open the External Client App Manager](#OpenTheExternalClientAppManager)
  - [Create the App](#CreateTheApp)
  - [Set Up OAuth](#SetUpOAuth)
  - [Leave the Security Settings Alone](#LeaveTheSecuritySettingsAlone)
  - [Set the Run As User](#SetTheRunAsUser)
  - [Copy the Consumer Key and Secret](#CopyTheConsumerKeyAndSecret)
- [Add a Salesforce Connection in OptiSigns](#AddASalesforceConnectionInOptiSigns)
  - [Find Your My Domain URL](#FindYourMyDomainURL)
  - [Fill In the Connection and Sign In to Salesforce](#FillInTheConnection)
- [Create a Salesforce App in OptiSigns](#CreateASalesforceAppInOptiSigns)
- [How OptiSigns Renders Your Dashboard](#HowOptiSignsRendersYourDashboard)
- [Frequently Asked Questions](#FrequentlyAskedQuestions)
  - [My screen says CRM Analytics required. What does that mean?](#MyScreenSaysCRMAnalyticsRequiredWhatDoesThatMean)
  - [My screen says Sign-in required, or Needs reconnecting. What do I do?](#MyScreenSaysSignInRequiredOrNeedsReconnectingWhatDoIDo)
  - [My screen says a Salesforce security policy blocked the image. Why?](#MyScreenSaysASalesforceSecurityPolicyBlockedTheImageWhy)
  - [OptiSigns says Enter a valid My Domain URL. What is wrong?](#OptiSignsSaysEnterAValidMyDomainURLWhatIsWrong)
  - [Sign-in fails with redirect\_uri\_mismatch on a blank page. How do I fix it?](#SignInFailsWithRedirectUriMismatchOnABlankPageHowDoIFixIt)
  - [OptiSigns refused my report when I pressed Save. Why?](#OptiSignsRefusedMyReportWhenIPressedSaveWhy)
  - [Can I connect a sandbox org?](#CanIConnectASandboxOrg)
  - [Do I have to use Slack?](#DoIHaveToUseSlack)
  - [My dashboard is showing old numbers. Why?](#MyDashboardIsShowingOldNumbersWhy)
  - [Will my dashboard data be stored anywhere?](#WillMyDashboardDataBeStoredAnywhere)

With the Salesforce app, you can display a Salesforce dashboard or report on any OptiSigns screen.

Once set up, the picture updates automatically. Nobody has to log in on the screen, and no Salesforce credentials ever reach the device.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account with a [Pro Plus Plan or higher](https://www.optisigns.com/pricing)
- A Salesforce org on **Enterprise**, **Performance** or **Unlimited** with the CRM Analytics add-on, or a **Developer Edition** org
- Admin rights in Salesforce, so you can create an External Client App
- A dashboard or report you want to display
- An OptiSigns-enabled device
- A screen, set up and paired with OptiSigns

Within Salesforce, you will collect three values:

- Your **My Domain URL**
- A **Consumer Key**
- A **Consumer Secret**

We will show how to find them in the article below.

|  |
| --- |
| **NOTE** |
| The **Integrations** page is only available to team admins. If you are not a team admin, ask one to add the Salesforce connection for you. Once the connection exists, you can still build the app and use it on OptiSigns. |

---

<a name="CheckYourSalesforceLicensingFirst"></a>

## Check Your Salesforce Licensing First

Salesforce renders these pictures through its own CRM Analytics service. An org without CRM Analytics is refused, and your screens will say **CRM Analytics required**. This is the most common reason the app does not work, so it is worth confirming before you set anything up.

<a name="CheckTheLicense"></a>

### Check the License

In Salesforce, go to **Setup**, then **Company Information**, and look through the license list for one of these:

- **CRM Analytics Growth**
- **CRM Analytics Plus**
- **Analytics Cloud Einstein Analytics Platform**

If none of them is there, your org does not have CRM Analytics. It is a paid add-on — contact your Salesforce Account Executive to have it provisioned.

|  |
| --- |
| **IMPORTANT** |
| CRM Analytics is sold as an add-on for Enterprise, Performance and Unlimited Editions, and is included in Developer Edition. It is not available on Professional, Starter or Essentials, so those editions cannot use this app. |

<a name="EnableTheSlackApps"></a>

### Enable the Slack Apps

Salesforce also requires **Slack for Salesforce** and **CRM Analytics for Slack** to be enabled for the image service to work.

Go to **Setup**, then **Slack Apps Setup**. In section 2, review and accept the terms and conditions. In section 3, enable **CRM Analytics for Slack** — it has its own page, so open it and click **Agree and enable Slack integration**.

|  |
| --- |
| **NOTE** |
| You do not have to use Slack, and nobody needs a Slack account. The apps only have to be enabled in your org. |

---

<a name="WhoDoesWhatInSalesforce"></a>

## Who Does What in Salesforce

Three different people can be involved, and it helps to know which is which before you start. They can all be the same person, but they do not have to be.

- **The admin who creates the External Client App** - Needs the **Create, edit, and delete External Client Apps** permission. Does not need access to any dashboard.
- **The Run As user** - An active user whose profile or permission set has **API Enabled**. Never opens a browser. A dedicated integration user is ideal, and an **API Only User** is fine for this role.
- **The user who signs in to OptiSigns** - A real, licensed Salesforce user who can view every dashboard and report you intend to display. This must **not** be an API-only user, because OptiSigns needs to open a session as this person. Your screens show exactly the data this user can see.

---

<a name="CreateAnExternalClientAppInSalesforce"></a>

## Create an External Client App in Salesforce

An External Client App is the identity OptiSigns uses to talk to your org. You create it in your own Salesforce, so nothing is shared with other customers.

<a name="OpenSetup"></a>

### Open Setup

Click the gear icon at the top right, then **Setup**. On some editions the gear opens a **Quick Settings** panel first — if it does, click **Open Advanced Setup**.

![Salesforce Quick Settings panel with Open Advanced Setup highlighted](https://support.optisigns.com/hc/article_attachments/55895827092115)

<a name="OpenTheExternalClientAppManager"></a>

### Open the External Client App Manager

In Setup, type `external` into the **Quick Find** box, then click **External Client App Manager**.

![Salesforce Setup with external typed in Quick Find and External Client App Manager highlighted](https://support.optisigns.com/hc/article_attachments/55895853980051)

<a name="CreateTheApp"></a>

### Create the App

Click **New External Client App**.

![Salesforce External Client App Manager with the New External Client App button highlighted](https://support.optisigns.com/hc/article_attachments/55895827293843)

Under **Basic Information**, fill in the required fields. Name the app something you will recognize later.

<a name="SetUpOAuth"></a>

### Set Up OAuth

Expand **API (Enable OAuth Settings)** and tick **Enable OAuth**. Then fill in the settings below.

For **Callback URL**, enter exactly this:

```
https://smallapp.optisigns.com/api/salesforce/integration/user-auth/callback
```

For **OAuth Scopes**, move these three across to **Selected OAuth Scopes**:

- **Manage user data via APIs (api)**
- **Manage user data via Web browsers (web)**
- **Perform requests at any time (refresh\_token, offline\_access)**

Under **Flow Enablement**, tick **Enable Client Credentials Flow**. Leave the other flows unticked.

The standard sign-in flow OptiSigns also uses is switched on automatically once OAuth is enabled with a Callback URL, so there is no separate box for it.

![Salesforce OAuth settings with Enable OAuth ticked, the OptiSigns callback URL and three selected scopes highlighted](https://support.optisigns.com/hc/article_attachments/55895827366163)

|  |
| --- |
| **IMPORTANT** |
| Salesforce compares the Callback URL character for character. A trailing slash, `http` instead of `https`, or an extra space will make sign-in fail later with a blank page and a `redirect_uri_mismatch` error. The field accepts several URLs, one per line, so an existing one can stay alongside it. |

<a name="LeaveTheSecuritySettingsAlone"></a>

### Leave the Security Settings Alone

Nothing in the **Security** section needs changing. The greyed-out settings are set by Salesforce and work with OptiSigns as they are.

Two settings must stay switched off: **Issue JSON Web Token (JWT)-based access tokens** and **Enforce Refresh Token IP Allowlist**. The sections below Security — SAML, Canvas, Mobile, Push and Notification — are for other kinds of app, so leave them collapsed.

Click **Create**.

![Salesforce Flow Enablement section with only Enable Client Credentials Flow ticked](https://support.optisigns.com/hc/article_attachments/55895871975955)

<a name="SetTheRunAsUser"></a>

### Set the "Run As" User

Open the External Client app you just created and go to the **Policies** tab, then **OAuth Policies**, then **OAuth Flows and External Client App Enhancements**.

Because you enabled the Client Credentials flow, Salesforce requires a **Run As (Username)**. Enter the username of an active user whose profile or permission set has **API Enabled** — a dedicated integration user, or simply the admin doing this setup. The username looks like an email address.

Leave the rest of the tab as it is, then click **Save**.

![Salesforce Policies tab with Enable Client Credentials Flow ticked and the Run As Username field highlighted](https://support.optisigns.com/hc/article_attachments/55895866473875)

|  |
| --- |
| **NOTE** |
| The "Run As" user needs no dashboard access at all. OptiSigns uses it to ask Salesforce to recalculate a dashboard before each picture is taken, so your screens show current numbers even when nobody has opened that dashboard in Salesforce. Reports are run fresh every time and do not need it. |

<a name="CopyTheConsumerKeyAndSecret"></a>

### Copy the Consumer Key and Secret

Go to the **Settings** tab, open **OAuth Settings**, and click **Consumer Key and Secret**. Salesforce may ask you to verify your identity first.

Copy both values and keep them somewhere safe. You will paste them into OptiSigns in the next step.

![Salesforce app Settings tab with the Consumer Key and Secret button highlighted](https://support.optisigns.com/hc/article_attachments/55895854470419)

---

<a name="AddASalesforceConnectionInOptiSigns"></a>

## Add a Salesforce Connection in OptiSigns

Now we will give OptiSigns the three values you collected.

<a name="FindYourMyDomainURL"></a>

### Find Your My Domain URL

OptiSigns needs your **My Domain** login host, which is not the address in your browser bar. Lightning shows `yourcompany.lightning.force.com` up there, but the login host is `yourcompany.my.salesforce.com`.

The quickest way to find it: click your **avatar** at the top right of Salesforce. It is printed under your name.

![Salesforce avatar menu with the My Domain host shown under the user's name](https://support.optisigns.com/hc/article_attachments/55895827826323)

You can also find it in **Setup**, under **My Domain**, as **Current My Domain URL**.

<a name="FillInTheConnection"></a>

### Fill In the Connection and Sign-in to Salesforce

Go to **Integrations** under your main menu, click the **Salesforce** tab, then click **Add Connection**. Fill in the form:

![OptiSigns Add Salesforce Connection dialog with Name, My Domain URL, Consumer Key and Consumer Secret fields](https://support.optisigns.com/hc/article_attachments/55899805157139)

- **Name** - Anything that tells this org apart from another one.
- **My Domain URL** - The host you just found, with https:// in front of it. For example, https://yourcompany.my.salesforce.com.
- **Consumer Key** - From the External Client App.
- **Consumer Secret** - From the External Client App. It is stored encrypted and never shown again.

Click **Add,** and you'll be taken to a sign-in screen.

As soon as the connection is saved, the same dialog opens a Salesforce sign-in window. Sign in as a real, licensed user who can see the dashboards you want to display, and approve the access request.

![Salesforce sign-in window opened over the OptiSigns Salesforce connection dialog](https://support.optisigns.com/hc/article_attachments/55895827934611)

This is a one-time step. Afterwards OptiSigns keeps the connection alive on its own, so you do not have to sign in again unless Salesforce refuses the login. This will only happen if the user is revoked or the account is deactivated.

![OptiSigns Integrations page, Salesforce tab, with a connection showing Signed in](https://support.optisigns.com/hc/article_attachments/55908508001683)

|  |
| --- |
| **NOTE** |
| Until this sign-in is complete, the connection row says **Sign-in required** and you will not be able to save a Salesforce asset. To sign in later, or to reconnect, use the connection row's menu and choose **Sign-in**. |

---

<a name="CreateASalesforceAppInOptiSigns"></a>

## Create a Salesforce App in OptiSigns

Go to **Files/Assets**, click **Apps**, and choose **Salesforce**.

![OptiSigns Salesforce app form filled in, with a connection and a dashboard selected](https://support.optisigns.com/hc/article_attachments/55908507931539)

Fill in the form:

- **Name** - What the asset is called in your Files/Assets list. This will not appear on your screens.
- **Salesforce Connection** - The Salesforce connection. If you have multiple connections, choose which one to use from the dropdown.
- **Content Type** - **Dashboard** or **Report**.
- **Dashboard** or **Report** - Picked from your organization's own list. The list shows what the signed-in user can see.
- **Update Interval** - How often OptiSigns takes a fresh picture, in seconds. Between 5 minutes and 12 hours; the default is 10 minutes.
- **Theme** - **Dark**, **Light** or **High Contrast**.
- **Image fit** - **Fit** (the default) shows the whole picture, adding bars if its shape does not match the screen. **Fill** covers the screen and crops the edges. **Stretch** fills the screen and distorts the picture.

Click **Save**, then assign the asset to a screen.

|  |
| --- |
| **NOTE** |
| A report is rendered as its saved chart, so it needs a chart and at least one row of data. Tabular reports cannot be displayed. OptiSigns checks this against your org when you press **Save** and tells you if the report will not work, rather than letting the screen fail later. |

---

<a name="HowOptiSignsRendersYourDashboard"></a>

## How OptiSigns Renders Your Dashboard

OptiSigns does not embed Salesforce and does not run a browser on your screen. It asks Salesforce to draw the dashboard, and shows that picture. The screen receives only a short-lived link to the image — no token, no org address, nothing that could be used to reach your data.

Nothing is written back to your org. The app only reads, plus the standard request asking Salesforce to recalculate its own dashboard.

The shape of the picture is decided in Salesforce, not in OptiSigns.

- A dashboard about **two rows tall** fills a 16:9 TV from edge to edge.
- A dashboard with **many rows** comes back tall and narrow, so it is shown whole with bars at the sides and the tiles look smaller. Splitting it across two dashboards usually looks better.
- A **one-row** dashboard is a wide strip, which suits a zone in a split-screen layout.
- **Reports** come back wide and short, which often fits a landscape screen better than a dashboard does.

If a refresh fails, the screen keeps the last good picture and shows how long ago it was taken, rather than going blank.

---

<a name="FrequentlyAskedQuestions"></a>

## Frequently Asked Questions

<a name="MyScreenSaysCRMAnalyticsRequiredWhatDoesThatMean"></a>

#### My screen says "CRM Analytics required." What does that mean?

Salesforce refused to draw the picture for licensing reasons. Your org either does not have a CRM Analytics license, or does not have **Slack for Salesforce** and **CRM Analytics for Slack** enabled. This is a change your Salesforce Administrator has to make.

<a name="MyScreenSaysSignInRequiredOrNeedsReconnectingWhatDoIDo"></a>

### My screen says "Sign-in required, or Needs reconnecting". What do I do?

The Salesforce sign-in was never completed, or Salesforce has refused it since. That usually means the login was revoked, the user was deactivated or frozen, an API-only user was used by mistake, or your admin changed who is allowed to authorise the app.

Go to **Integrations**, open the **Salesforce** tab, and use the connection row's menu to choose **Sign-in**. Sign in again as a real, licensed user who can see the dashboards.

<a name="MyScreenSaysASalesforceSecurityPolicyBlockedTheImageWhy"></a>

### My screen says a Salesforce security policy blocked the image. Why?

Your org has a policy that will not allow a session to be opened without a person present. The usual causes are step-up authentication on report exports, a High Assurance session requirement on that user's profile, or Login IP Ranges that do not include our servers.

All three are settings inside your Salesforce, so your Salesforce admin will need to permit it for the user who signed in. Contact OptiSigns support and we can tell you exactly what your screens are reporting.

<a name="OptiSignsSaysEnterAValidMyDomainURLWhatIsWrong"></a>

### OptiSigns says "Enter a valid My Domain URL." What is wrong?

You have most likely pasted the address from your browser bar, which ends in lightning.force.com. OptiSigns needs the login host, which ends in my.salesforce.com. Click your avatar in Salesforce to see it.

<a name="SignInFailsWithRedirectUriMismatchOnABlankPageHowDoIFixIt"></a>

### Sign-in fails with "redirect\_uri\_mismatch" on a blank page. How do I fix it?

The **Callback URL** on your External Client App does not exactly match the one OptiSigns uses. Open the app in Salesforce and check it character for character against the URL in [Set Up OAuth](#SetUpOAuth) above — watch for a trailing slash or a stray space.

<a name="OptiSignsRefusedMyReportWhenIPressedSaveWhy"></a>

### OptiSigns refused my report when I pressed Save. Why?

Salesforce renders a report as its saved chart, so the report needs a chart on it and at least one row of data. Tabular reports can never carry a chart and cannot be displayed.

In Salesforce, open the report, choose **Edit**, then **Add Chart**, and save it. Then save the OptiSigns asset again.

<a name="CanIConnectASandboxOrg"></a>

### Can I connect a sandbox org?

Yes. There is nothing extra to switch on — paste the sandbox's own My Domain URL, which looks like `https://yourcompany--sandbox.sandbox.my.salesforce.com`. Salesforce recognises it from the address.

<a name="DoIHaveToUseSlack"></a>

### Do I have to use Slack?

No. Salesforce requires the two Slack apps to be **enabled** in your org because its image service is part of that integration, but nobody needs a Slack account and nothing is posted to Slack.

<a name="MyDashboardIsShowingOldNumbersWhy"></a>

### My dashboard is showing old numbers. Why?

A Salesforce dashboard shows the results from the last time it was run, so OptiSigns asks Salesforce to recalculate it before taking each picture. That request is made by the **Run As** user on your External Client App, so check that one is set — see [Set the Run As User](#SetTheRunAsUser).

Reports are not affected: Salesforce runs a report fresh every time it draws one.

<a name="WillMyDashboardDataBeStoredAnywhere"></a>

### Will my dashboard data be stored anywhere?

The picture is stored so your screens can load it quickly, and it is replaced at every update. Your screens receive only a short-lived link to that picture. No Salesforce credentials are stored on the device, and nothing is written back to your Salesforce org.

---
