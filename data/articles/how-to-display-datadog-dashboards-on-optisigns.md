# How to Display Datadog Dashboards on OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/56493703696659-How-to-Display-Datadog-Dashboards-on-OptiSigns

Article ID: 56493703696659

Locale: en-us

Updated at: 2026-10-16T19:51:56Z

---

### In this article, we'll connect your Datadog organization so its dashboards display live on your OptiSigns screens.

- [What You'll Need](#WhatYoullNeed)
- [Prepare Your Datadog Organization](#PrepareYourDatadogOrganization)
  - [Find Your Datadog Site](#FindYourDatadogSite)
  - [Turn On Embed Sharing](#TurnOnEmbedSharing)
  - [Check Your Role's Permissions](#CheckYourRolesPermissions)
  - [Create an API Key](#CreateAnAPIKey)
  - [Create an Application Key](#CreateAnApplicationKey)
- [Add a Datadog Connection in OptiSigns](#AddADatadogConnectionInOptiSigns)
- [Create a Datadog App in OptiSigns](#CreateADatadogAppInOptiSigns)
- [How OptiSigns Displays Your Dashboard](#HowOptiSignsDisplaysYourDashboard)
- [Frequently Asked Questions](#FrequentlyAskedQuestions)

With the Datadog app, you can display a live Datadog dashboard on any OptiSigns screen.

OptiSigns shows your dashboard through Datadog's own secure embed, so it keeps itself up to date with no refresh to set. Nobody has to log in on the screen, and your Datadog keys never reach the device.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account, with a [Pro Plus plan or higher](https://www.optisigns.com/pricing).
- A Datadog account, and a Datadog admin who can turn on embed sharing for your organization
- A Datadog role with the **Dashboards Read** and **Shared Dashboards Embed Write** permissions
- The Datadog dashboard you want to display
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
- A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

Within Datadog, you will collect three values:

- Your **Datadog site**
- An **API key**
- An **Application key**

We will show how to find them in the article below.

|  |
| --- |
| **NOTE** |
| The **Integrations** page is only available to team admins. If you are not a team admin, ask one to add the Datadog connection for you. Once the connection exists, you can still build the app and use it on your screens. |

---

<a name="PrepareYourDatadogOrganization"></a>

## Prepare Your Datadog Organization

<a name="FindYourDatadogSite"></a>

### Find Your Datadog Site

Datadog runs several regional sites, and OptiSigns needs to know which one your organization is on. The quickest way to tell is the address in your browser bar. For example, app.datadoghq.com is **US1**, and us5.datadoghq.com is **US5**.

![Browser address bar showing the Datadog web address app.datadoghq.com](https://support.optisigns.com/hc/article_attachments/56493680004499)

You can also click your avatar in Datadog. The site is shown under **Current Organization,** as in the picture below. This menu is also where you open **Organization Settings** for the next steps.

![Datadog account menu showing the organization's site as US1 - East](https://support.optisigns.com/hc/article_attachments/56493695889427)

|  |
| --- |
| **IMPORTANT** |
| The site cannot be changed after the connection is created. If you pick the wrong one, delete the connection and add it again. |

<a name="TurnOnEmbedSharing"></a>

### Turn On Embed Sharing

This step needs a Datadog admin. Go to **Organization Settings**, then click **Public Sharing**.

![Datadog Organization Settings search for public sharing with the Public Sharing result highlighted](https://support.optisigns.com/hc/article_attachments/56493726680211)

On the **Settings** tab, find **Shared Dashboards** and make sure **Embed** is turned on. OptiSigns only needs **Embed**. The other share types can stay as they are.

![Shared Dashboards share types with the Embed toggle turned on](https://support.optisigns.com/hc/article_attachments/56493704883603)

<a name="CheckYourRolesPermissions"></a>

### Check Your Role's Permissions

The person who creates the keys needs two permissions:

- **Dashboards Read**
- **Shared Dashboards Embed Write**

![Datadog role permissions with Dashboards Read and Shared Dashboards Embed Write enabled](https://support.optisigns.com/hc/article_attachments/56493705076627)

The Datadog Admin and Datadog Standard roles have both. The Datadog Read Only role does not. To check a role, go to **Organization Settings**, then **Roles**, open the role, and filter its permissions by **dashboard**.

<a name="CreateAnAPIKey"></a>

### Create an API Key

Still in Datadog, go to **Organization Settings**, then **API Keys**, and click **New Key**. Give the key a name you will recognize later, such as **OptiSigns**.

![Datadog API Keys page with the New Key button highlighted](https://support.optisigns.com/hc/article_attachments/56493696697619)

Click **Copy** and keep the key somewhere safe. We'll paste it into OptiSigns later.

![New API Key dialog with the key value hidden and the Copy button highlighted](https://support.optisigns.com/hc/article_attachments/56493705344275)

|  |
| --- |
| **NOTE** |
| By default, only Datadog admins can create API keys. If you are not an admin, you can copy an existing API key from the same page instead. |

<a name="CreateAnApplicationKey"></a>

### Create an Application Key

Still in Datadog, go to **Organization Settings**, then **Application Keys**, and click **New Key**. Name it something you will recognize.

Scopes are optional. A key with no scopes has the same permissions as the user who owns it. If you do set scopes, include both of these:

- **dashboards\_read**
- **dashboards\_embed\_share**

![Application key scopes with dashboards_embed_share and dashboards_read selected](https://support.optisigns.com/hc/article_attachments/56493713302419)

Click **Copy** right away. Datadog only shows an application key once, so if you close the dialog without copying it, you will need to create a new one. We'll be pasting this into OptiSigns in a moment.

![New application key dialog with the key hidden, its scopes listed and the Copy button highlighted](https://support.optisigns.com/hc/article_attachments/56493705803795)

|  |
| --- |
| **IMPORTANT** |
| An application key belongs to the Datadog user who created it. If that user is deactivated, Datadog revokes the key and your screens stop showing the dashboard. A key owned by a shared service account avoids this. |

---

<a name="AddADatadogConnectionInOptiSigns"></a>

## Add a Datadog Connection in OptiSigns

Now we will give OptiSigns the three values you collected.

Click your avatar at the top right of OptiSigns, then **Integrations**. Click the **Datadog** tab, then click **Add Connection**.

![OptiSigns Integrations page, Datadog tab, with the Add Connection button highlighted](https://support.optisigns.com/hc/article_attachments/56493706001427)

Fill in the form:

![Add Datadog Connection dialog with Name, Datadog site, API Key and Application Key fields](https://support.optisigns.com/hc/article_attachments/56493706159251)

- **Name** - Anything that tells this connection apart from another one.
- **Datadog site** - The site you found earlier. A complete list of these is shown in the image below.
- **API Key** - The API key you copied.
- **Application Key** - The application key you copied.

![Datadog site list showing US1, US3, US5, EU1, AP1, AP2, UK1 and the government sites](https://support.optisigns.com/hc/article_attachments/56493743701523)

Click **Add**. OptiSigns checks the keys with Datadog as it saves, and tells you if Datadog rejects them. The new connection then appears in the list. Both keys are stored encrypted and are never shown again.

---

<a name="CreateADatadogAppInOptiSigns"></a>

## Create a Datadog App in OptiSigns

Go to **Files/Assets** and click **Apps**.

![Files/Assets page with the Apps button highlighted](https://support.optisigns.com/hc/article_attachments/56493682488211)

Search for **Datadog** and select the **Datadog** app.

![Add App dialog searched for Datadog, with the Datadog app card highlighted](https://support.optisigns.com/hc/article_attachments/56493714519059)

Fill in the form. There are three sections: **Connect**, **Dashboard**, and **Display**. **Display** starts collapsed, so click it to open it.

**Connect**

- **Name** - What the asset is called in your Files/Assets list. This will not appear on your screens.
- **Datadog Connection** - The connection you added. If you have more than one, choose which to use from the dropdown. Team admins can also choose **New Datadog connection** here to add one without leaving the form.

**Dashboard**

- **Dashboard** - Picked from your organization's own list of dashboards.

![Datadog app form with the Connect and Dashboard sections filled in](https://support.optisigns.com/hc/article_attachments/56493728945555)

**Display**

- **Time range** - How much history the dashboard shows, from **Last 15 minutes** to **Last 3 months**. The default is **Last 1 hour**.
- **Theme** - **Dark** (the default), **Light**, or **System**.
- **TV mode** - Fits the whole dashboard on the screen, with no scrolling.

![Datadog app Display section with Time range, Theme and TV mode](https://support.optisigns.com/hc/article_attachments/56493729114771)

Click **Save**. The app stays open after saving and shows a preview of your dashboard, so you can check it before it goes on a screen. Then assign the asset to a screen, or add it to a Playlist or Schedule.

---

<a name="HowOptiSignsDisplaysYourDashboard"></a>

## How OptiSigns Displays Your Dashboard

When you save the app, OptiSigns uses your connection's keys to create a secure embed of the dashboard in Datadog. Your screen shows that embed, and Datadog keeps the data live on its own, so there is no update interval to set. OptiSigns renews the embed's signature before it expires.

Your API key and application key stay on OptiSigns' servers, encrypted. The screen never receives them.

A few limits to know about:

- Every screen showing the same app shows the same dashboard. Template variables are not supported.
- Datadog allows up to 1,000 secure embeds per dashboard.

---

<a name="FrequentlyAskedQuestions"></a>

## Frequently Asked Questions

#### OptiSigns says "Datadog rejected the API key or application key for this site." What is wrong?

One of the keys is wrong, or the connection's **Datadog site** does not match your organization. Check the site in your browser's address bar, and make sure both keys were copied in full. Since the site cannot be changed, a wrong site means deleting the connection and adding it again.

#### OptiSigns says "Datadog rejected this connection." Why?

The application key does not have permission to embed dashboards. Make sure **Embed** is turned on under **Public Sharing**, that the key's owner has the **Shared Dashboards Embed Write** permission, and that a scoped key includes **dashboards\_embed\_share**.

#### My dashboard is not in the Dashboard list. Why?

The list shows the dashboards your application key can read. If a dashboard is missing, the key's owner may not have access to it, or a scoped key may be missing **dashboards\_read**.

#### OptiSigns says "This dashboard has reached the Datadog limit of 1000 secure embeds." What can I do?

Datadog caps secure embeds at 1,000 per dashboard. Remove unused shared embeds of that dashboard in Datadog, under **Public Sharing**, then **Shared Dashboards**. Then save the app again.

#### My screens stopped showing the dashboard. What happened?

The most common cause is that the Datadog user who created the application key was deactivated, which revokes the key. Create a new application key, then go to **Integrations**, open the **Datadog** tab, edit the connection, and paste the new key.

#### OptiSigns says "Could not read the saved keys for this connection." What do I do?

Edit the connection on the **Integrations** page and enter both keys again.

#### OptiSigns says "This Datadog asset was not set up correctly." What do I do?

Delete the asset and create it again.

#### Will my dashboard data be stored anywhere?

No. OptiSigns does not copy your dashboard data. Datadog draws the dashboard directly on your screen through the secure embed. Your keys are stored encrypted on OptiSigns' servers and never reach the device.
