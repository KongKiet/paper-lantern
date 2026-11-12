# How to Display Microsoft Power BI Dashboards & Reports with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/360024859713-How-to-Display-Microsoft-Power-BI-Dashboards-Reports-with-OptiSigns

Article ID: 360024859713

Locale: en-us

Updated at: 2026-11-11T20:29:28Z

---

### In this article, we'll show you how to display Microsoft Power BI reports and dashboards on your screens with OptiSigns, including rotating report pages, Kiosk Mode, and filters that target individual screens.

- [What You'll Need and How it Works](#WhatYoullNeed)
- [Preparing Your Power BI Report](#Step1GetYourReportReadyInPowerBI)
- [Creating the Power BI App](#Step2AddThePowerBIApp)
  - [Filter a Report](#FilterAReport)
- [Troubleshooting and Frequently Asked Questions](#Troubleshooting)

Put live Power BI reports and dashboards on any screen. OptiSigns signs in to Power BI through Microsoft's official APIs, keeps the report up to date, and can rotate through the report pages you pick or turn a report into a touch-screen kiosk.

|  |
| --- |
| **NOTE** |
| The Power BI app requires the OptiSigns **Pro Plus** plan or above. See [pricing](https://www.optisigns.com/pricing). |

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account on the [Pro Plus plan](https://www.optisigns.com/pricing) or above.
- A screen [set up and paired](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv) with OptiSigns.
- A published Power BI report or dashboard in the Power BI service (app.powerbi.com or Microsoft Fabric).
- A way to connect:
  - **Direct Login** - A Microsoft account that can open the report in Power BI.
  - **Service Principal** - An Azure app registration set up for Power BI. This needs the Pro Plus, Engage or Enterprise plan. See [How to Set Up a Power BI Service Principal for Use with OptiSigns](https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns).

---

## How It Works

You add a **Power BI** app to your assets, connect it to Microsoft, and choose a report or dashboard. OptiSigns shows it on your screens and checks for updated data on the interval you set. A report can play in one of three ways:

- **One page** - The report opens on its default page.
- **Rotating pages** - You pick which report pages to show and how long each one stays up. The screen cycles through them in order.
- **Kiosk Mode** - The report becomes a touch dashboard. Viewers tap to filter and switch pages themselves.

Dashboards have no pages, so they always show as a single view.

---

<a name="Step1GetYourReportReadyInPowerBI"></a>

## Preparing Your Report in Power BI

If you'll pick your report with **Browse** inside the OptiSigns portal, skip this step and [follow from here](#Step4ChooseYourReportOrDashboard). Otherwise, copy the report's URL.

**Report in the Power BI service.** Open the report in your browser and copy the URL from the address bar. Use the address bar URL, not a **Share** link.

![Power BI report open in the browser with the address-bar URL highlighted](https://support.optisigns.com/hc/article_attachments/55870304499859)

**Report from Power BI Desktop.** Click **Publish** on the **Home** ribbon.

![Power BI Desktop Home ribbon with the Publish button highlighted](https://support.optisigns.com/hc/article_attachments/55870336265107)

Choose the workspace to publish to.

![Publish to Power BI dialog for choosing a destination workspace](https://support.optisigns.com/hc/article_attachments/55870336266131)

When publishing finishes, click **Open in Power BI**.

![Power BI Desktop publish-success dialog with the Open in Power BI link highlighted](https://support.optisigns.com/hc/article_attachments/55870336267539)

Copy the URL of the report that opens.

![Published Power BI report URL highlighted in the browser address bar](https://support.optisigns.com/hc/article_attachments/55870336268435)

---

<a name="Step2AddThePowerBIApp"></a>

## Creating a Power BI app

In the [OptiSigns portal](https://app.optisigns.com/), go to **Files/Assets** and click **Apps**.

![OptiSigns Files/Assets page with the Apps button highlighted](https://support.optisigns.com/hc/article_attachments/55870304503059)

Search for **Power BI** and click the tile.

![Apps dialog searched for Power BI with the Power BI app tile highlighted](https://support.optisigns.com/hc/article_attachments/55870304503699)

The Power BI app opens with four sections: **Connect**, **Dashboard**, **Filters** and **Display**.

![Power BI app setup dialog with the Choose Authentication Method option highlighted](https://support.optisigns.com/hc/article_attachments/55870304504723)

---

## Connect to Microsoft

Under **Choose Authentication Method**, pick **Direct Login** or **Service Principal**. In order to choose a Service Principal, you'll need to have set one up. See [How to Set Up a Power BI Service Principal for Use in OptiSigns](https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-Power-BI-Service-Principal-for-Use-in-OptiSigns).

### Direct Login

Click **Sign in with Microsoft** and sign in with an account that can open the report. When it works, the button reads **Authorized with Microsoft as** followed by your name.

![Button reading Authorized with Microsoft as OptiSigns Demo after signing in](https://support.optisigns.com/hc/article_attachments/55870304505491)

|  |
| --- |
| **NOTE** |
| OptiSigns asks Microsoft only for read access to your reports, dashboards, workspaces and datasets. The first time anyone in your organization connects, a Microsoft admin may need to approve OptiSigns. |

### Service Principal

A service principal lets screens keep showing reports without depending on one person's Microsoft account. Select **Service Principal**, then choose a saved connection from **Select Service Principal Integration**.

![Service Principal selected with the Select Service Principal Integration picker](https://support.optisigns.com/hc/article_attachments/55870336271763)

To add a connection here, open the picker and choose **New Power BI connection**. Only an account Owner, Super Admin, or Teamspace admin can add one.

![Service principal picker open with the New Power BI connection option highlighted](https://support.optisigns.com/hc/article_attachments/55870336273811)

You can also manage connections from **Integrations** → **Power BI** → **Add Azure Service Principal**.

![Power BI integrations tab with the Add Azure Service Principal button highlighted](https://support.optisigns.com/hc/article_attachments/55870304510483)

Enter a **Name**, then the **Application (client) ID**, **Application (client) Secret** and **Directory (tenant) ID** from your Azure app registration, and click **Add**. For the Azure side of the setup, see [How to Set Up a Power BI Service Principal for Use with OptiSigns](https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns).

![Add Azure Service Principal dialog with Name, client ID, client secret and tenant ID fields](https://support.optisigns.com/hc/article_attachments/55870304511123)

---

<a name="Step4ChooseYourReportOrDashboard"></a>

## Choose your Report or Dashboard

In the **Dashboard** section, click **Browse** next to **Select report or Enter URL**. Pick a workspace.

![Select a report dialog listing Power BI workspaces with My Workspace highlighted](https://support.optisigns.com/hc/article_attachments/55870336282003)

Then pick the report or dashboard, and click **Select**.

![Reports in My Workspace with the Competitive Marketing Analysis report highlighted](https://support.optisigns.com/hc/article_attachments/55870336283539)

The URL fills in, and **Name** is filled in from the report's name. The name is what you'll see in your assets list, and you can change it.

![Power BI app with the report URL and name filled in from Browse](https://support.optisigns.com/hc/article_attachments/55870304515475)

You can paste the URL you copied in Step 1 into **Select report or Enter URL** instead. Links from app.powerbi.com and Microsoft Fabric both work.

---

## Choose How the Report Plays

The Power BI app allows several options for how, exactly, the report plays. You can display single pages, or set rotation. You can also set your report to be displayed and optimized for Kiosks.

### Rotate report pages

Under **Select Pages**, tick each page you want to show, and set how many seconds it stays on screen. The default is 60 seconds and the minimum is 30. You can select up to 20 pages, and the header shows the total time for one full rotation.

![Select Pages list with two report pages ticked, each set to 60 seconds](https://support.optisigns.com/hc/article_attachments/55870304516371)

Leave every page unticked to show the report's default page only.

### Kiosk Mode

Turn on **Enable Kiosk Mode** to make the report a touch dashboard, where viewers tap to filter and switch pages. Then choose where Power BI shows its page tabs under **Page Tabs**: **Bottom** or **Left**.

![Enable Kiosk Mode switched on with the Page Tabs options Bottom and Left](https://support.optisigns.com/hc/article_attachments/55870304516755)

|  |
| --- |
| **IMPORTANT** |
| Screens that play a Kiosk Mode report need the Engage add-on. Kiosk Mode works with reports only, not dashboards, and it can't be combined with rotating pages. Unselect all pages to turn it on. |

---

## Set the Update Interval and Save

Open **Display** and set **Update Interval**, which is how often, in seconds, the app checks for updated data. 600 seconds (or 10 minutes) is the fastest interval possible.

![Display section with the Update Interval field highlighted](https://support.optisigns.com/hc/article_attachments/55870304517267)

Click **Save**. Your Power BI app now appears in your assets. You can assign it to a screen directly, or add it to a [Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists) or [Schedule](https://support.optisigns.com/hc/en-us/articles/360016981853-Create-and-Using-Schedules-with-OptiSigns). Kiosk Mode reports go on a screen directly; they can't be playlist items.

|  |
| --- |
| **NOTE** |
| How well a report plays also depends on the device, its memory, and its network and firewall. If a report won't show on a screen, see the Troubleshooting questions at the end of the article. |

---

<a name="FilterAReport"></a>

## Filter a Report

Filters let one report show only the data a screen needs. For example, a sales report can show only the Central region.

### Create a Filter

Open the **Filters** section and click **Add Your First Filter**.

![Filters section with the Add Your First Filter button highlighted](https://support.optisigns.com/hc/article_attachments/55870336288915)

Each filter needs a **Table**, a **Column** and a **Value**. To find them, open the report in Power BI and click **Edit**.

![Power BI report toolbar with the Edit button highlighted](https://support.optisigns.com/hc/article_attachments/55870304522899)

In the **Data** pane, each folder is a table and each field inside it is a column. Select a column to see its values in the **Filters** pane.

In this example, **Manufacturer** is the table, the **Manufacturer** field inside it is the column, and names like **Abbas** are values.

![Power BI edit view showing the Manufacturer table and column in the Data pane and its values in the Filters pane](https://support.optisigns.com/hc/article_attachments/55870304523667)

Enter the table, column and value in the filter. Here, the report shows only rows where **Region** in the **Account** table is **Central**.

![Filter row filled in with table Account, column Region, operator Is and value Central](https://support.optisigns.com/hc/article_attachments/55870304524179)

Change **Is** to a different operator to match values another way. The options include **Contains**, **Starts With**, **Greater Than** and **Is Blank**.

![Filter operator dropdown listing Is, Contains, Starts With and other operators](https://support.optisigns.com/hc/article_attachments/55870336292499)

Click **+** to add another condition to the same filter, then choose **AND** or **OR** under **Condition Logic**.

![Second filter condition added with the Condition Logic AND/OR control highlighted](https://support.optisigns.com/hc/article_attachments/55870336296211)

To filter on a different column, click **Add New Filter**.

![Filter builder with the Add New Filter button highlighted](https://support.optisigns.com/hc/article_attachments/55870304530963)

Each filter gets its own row, numbered in order.

![Two filters configured in the Power BI app Filters section](https://support.optisigns.com/hc/article_attachments/55870336306707)

### Target Individual Screens with One Filter (optional)

To make one Power BI app show different data on different screens, give each screen an attribute and use it as the filter value.

Open the screen, go to **Edit Screen** → **Advanced** → **More**, and click the wrench icon (**Device Additional Attributes**).

![Edit Screen More options with the wrench icon and its Device Additional Attributes tooltip highlighted](https://support.optisigns.com/hc/article_attachments/55870304531987)

Click **New Attribute**.

![Empty Device Additional Attributes dialog with the New Attribute button highlighted](https://support.optisigns.com/hc/article_attachments/55870304532499)

Enter a key and a value, such as **Location** and **Central**, and click **Update**. Repeat for each screen with its own value.

![Device additional attribute row with key Location and value Central](https://support.optisigns.com/hc/article_attachments/55870304533779)

In the Power BI app's filter, enter the key in double curly braces as the **Value**: `{{Location}}`. Each screen then fills in its own value.

![Filter Value field set to the {{Location}} placeholder](https://support.optisigns.com/hc/article_attachments/55870304535571)

For more about attributes, see [Edit Screen — What does each option do](https://support.optisigns.com/hc/en-us/articles/360048914673-Edit-Screen-What-does-each-option-do#attributes).

### Save and reuse filters (optional)

To reuse a set of filters in other Power BI apps, click **Save Filter**.

![Filters section with the Save Filter link highlighted](https://support.optisigns.com/hc/article_attachments/55870336313747)

Give it a **Filter Name** and an optional **Description**, then click **Save My Filters**. Saved filters are available across your account.

![Save Your Filter Settings dialog with the Filter Name and Description fields](https://support.optisigns.com/hc/article_attachments/55870336314515)

To apply a saved filter, click **Load Filter** and choose it from the list. Each saved filter has an edit (pencil) and a delete (trash) icon.

![Load Filter dropdown listing a saved filter with its description, condition count, and edit and delete icons](https://support.optisigns.com/hc/article_attachments/55870336317203)

Editing opens **Edit Filter**, where you can change the name, description and conditions. Click **Update Filter** to save. The changes apply everywhere the filter is used.

![Edit Filter dialog showing the filter name, description and conditions, with the Update Filter button highlighted](https://support.optisigns.com/hc/article_attachments/55870336318611)

---

<a name="Troubleshooting"></a>

## Troubleshooting

**"Please enter a valid Power BI or Fabric URL".**

The link must start with `https://app.powerbi.com/` or `https://app.fabric.microsoft.com/`. Copy it from the browser address bar, or use **Browse**.

**"This link doesn't point to a report or dashboard".**

The URL is from Power BI but isn't a report or dashboard page, such as a workspace or app link. Open the report itself and copy that URL.

**Browse is greyed out.**

Connect first. Sign in with Microsoft, or select a service principal connection in **Connect**.

**"Could not load workspaces".**

The connected account or service principal can't list your workspaces. Sign in again with **Direct Login**. For a service principal, check that it has access to the workspace in Power BI.

**"No pages found for this report".**

The report didn't return any pages. Check that it opens in Power BI, then click **Reload** next to **Select Pages**.

**"These pages are no longer in this report".**

A page you selected was renamed or removed in Power BI. Untick it, or pick its replacement, and save.

**Enable Kiosk Mode is greyed out.**

Kiosk Mode works with reports only, and not while pages are selected. Untick every page under **Select Pages**.

**"Ask a team admin to add a Power BI connection".**

Only team admins can create service principal connections. Ask an admin to add one under **Integrations** → **Power BI**.

For more about publishing in Power BI, see Microsoft's guide [Publish and share in Power BI](https://docs.microsoft.com/en-us/power-bi/guided-learning/publishingandsharing?tutorial-step=11).

---

## Frequently Asked Questions

Here are some of the most commonly asked questions we find with customers using Power BI on OptiSigns.

### How does security work with the Power BI integration?

OptiSigns connects through Microsoft's official Power BI APIs and asks only for read access. With **Direct Login**, you sign in on Microsoft's own page, so OptiSigns never sees your password, and the access tokens it keeps are encrypted. A Microsoft admin may need to approve OptiSigns once for your organization. You can then [manage OptiSigns in your Enterprise App](https://support.optisigns.com/hc/en-us/articles/4403616315539) settings in Azure.

### Should I use Direct Login or a Service Principal?

**Direct Login** is the quickest to set up and works on any plan that includes the Power BI app. The report keeps playing only while that Microsoft account stays valid. A **Service Principal** isn't tied to a person, so it suits organizations that manage many screens. It needs the Pro Plus, Engage or Enterprise plan.

### How do I make the report fit my screen?

In Power BI, open the report in **Edit** mode, go to **View**, and choose **Fit to page**. Then save the report.

![Power BI View menu in Edit mode with Fit to page highlighted](https://support.optisigns.com/hc/article_attachments/55870304545043)

For the best results, we recommend the [OptiSigns Android Player](https://www.optisigns.com/product/hardware/android-player).

### My report shows in the portal but not on my screen.

This is usually a network issue, so check that the screen can reach Microsoft's Power BI sites. Samsung (SSSP) and LG (webOS) displays need a browser engine of Chromium 95 or later to show Power BI, which is a Microsoft requirement. If your display is older, the [Android Player](https://www.optisigns.com/product/hardware/android-player) is a reliable alternative.

### My report lags or crashes.

Large reports need more memory and processing power than many built-in TV players have. We recommend the [OptiSigns Pro Player](https://www.optisigns.com/product/hardware/pro-digital-signage-player) or [ProMax Player](https://www.optisigns.com/product/hardware/promax-digital-signage-player) for large reports.

### Does this work with Power BI for US Government (GCC / GCC High)?

Not directly. Government-cloud Power BI URLs aren't supported by the Power BI app. As a workaround, display the report with the [SharePoint app](https://support.optisigns.com/hc/en-us/articles/4414539282067-Displaying-SharePoint-Sites-on-OptiSigns).
