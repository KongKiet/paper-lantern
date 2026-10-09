# How to Display Grafana Dashboards on OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/55447693635731-How-to-Display-Grafana-Dashboards-on-OptiSigns

Article ID: 55447693635731

Locale: en-us

Updated at: 2026-10-08T16:32:47Z

---

### In this article, we'll walk you through setting up Grafana to display on your OptiSigns digital signs.

- [What You'll Need](#WhatYoullNeed)
- [Which Setup Applies to You](#WhichSetupAppliesToYou)
- [Create a Service Account in Grafana](#CreateAServiceAccountInGrafana)
  - [Create the Service Account](#CreateTheServiceAccount)
  - [Generate a Token](#GenerateAToken)
- [Add a Grafana Connection in OptiSigns](#AddAGrafanaConnectionInOptiSigns)
  - [If You Use Grafana Cloud](#GrafanaCloud)
  - [If You Self-Host Grafana](#SelfHostedGrafana)
  - [If Grafana Is on Your Own Network](#GrafanaOnYourOwnNetwork)
  - [If Grafana Is Behind a Firewall](#GrafanaBehindAFirewall)
  - [If You Use a Public Dashboard Link](#PublicDashboardLink)
- [Set Up Live Mode on Your Grafana](#SetUpLiveModeOnYourGrafana)
- [Create a Grafana App in OptiSigns](#CreateAGrafanaAppInOptiSigns)
  - [Display Settings](#DisplaySettings)
  - [Advanced Settings](#AdvancedSettings)
  - [About the Preview](#AboutThePreview)
- [Deploying a Grafana App](#DeployingAGrafanaApp)
  - [How Updates Will Appear Onscreen](#HowUpdatesWillAppearOnscreen)
  - [Which Players Are Supported](#WhichPlayersAreSupported)
- [Frequently Asked Questions](#FrequentlyAskedQuestions)
  - [The connection test says Grafana rejected this token. What's wrong?](#TheConnectionTestSaysGrafanaRejectedThisTokenWhatsWrong)
  - [The connection test says Cloudflare or a firewall blocked our servers. What do I do?](#TheConnectionTestSaysCloudflareOrAFirewallBlockedOurServersWhatDoIDo)
  - [OptiSigns says it can't reach my Grafana. Is that a problem?](#OptiSignsSaysItCantReachMyGrafanaIsThatAProblem)
  - [My dashboard list is empty, or I can't find my dashboard. How can I make it appear?](#MyDashboardListIsEmptyOrICantFindMyDashboardHowCanIMakeItAppear)
  - [OptiSigns won't accept the link I entered. Why?](#OptiSignsWontAcceptTheLinkIEnteredWhy)
  - [The connection test tells me to install Grafana's image renderer. What do I do?](#TheConnectionTestTellsMeToInstallGrafanasImageRendererWhatDoIDo)
  - [The connection test says embedding is disabled on my Grafana. How do I fix it?](#TheConnectionTestSaysEmbeddingIsDisabledOnMyGrafanaHowDoIFixIt)
  - [My screen says Dashboard unavailable. What does that mean?](#MyScreenSaysDashboardUnavailableWhatDoesThatMean)
  - [My screen shows Grafana's login page. Why?](#MyScreenShowsGrafanasLoginPageWhy)
  - [My screen is showing an old picture, or says Data unavailable. Why?](#MyScreenIsShowingAnOldPictureOrSaysDataUnavailableWhy)
  - [The preview says it isn't available. Will my screens work?](#ThePreviewSaysItIsntAvailableWillMyScreensWork)
  - [My Grafana dashboard used to display fine, but stopped all of a sudden. What's wrong?](#MyGrafanaDashboardUsedToDisplayFineButStoppedAllOfASuddenWhatsWrong)

With the Grafana app, you can show a Grafana dashboard on any OptiSigns screen.

Once it is set up, the dashboard appears by itself. Nobody has to log in on the screen.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account with a [Pro Plus Plan or higher](https://www.optisigns.com/pricing)
- A Grafana instance, either [Grafana Cloud](https://grafana.com/products/cloud/) or self-hosted
- Admin rights in Grafana
- A dashboard you want to display
- An OptiSigns-enabled device
- A screen, set up and paired with OptiSigns

Depending on your setup, you may also need a service-account token from Grafana. The next section tells you if you do.

|  |
| --- |
| **NOTE** |
| Only team admins can add a Grafana connection. If you are not a team admin, ask one to add it for you. You can still build the app yourself once the connection exists. |

---

<a name="WhichSetupAppliesToYou"></a>

## Which Setup Applies to You

OptiSigns works out your setup from the Grafana URL you enter, so there's no need to pick one yourself.

|  |  |  |  |
| --- | --- | --- | --- |
| Your Grafana | What you enter | Token needed | What the screen shows |
| Grafana Cloud | Your Grafana Cloud URL | Yes | A screenshot, refreshed on a schedule you choose |
| Self-hosted, reachable from the internet | Your Grafana URL | Yes | The live dashboard |
| On your own network | Your Grafana URL | No | The live dashboard, loaded by the screen on that network |
| Behind a firewall or Cloudflare | Your Grafana URL | Yes | A screenshot, fetched through OptiSigns' fixed IP |
| A public dashboard link | The public link | No | The public dashboard |

If your setup needs a token, start with the next section. If it does not, skip ahead to [Add a Grafana Connection in OptiSigns](#AddAGrafanaConnectionInOptiSigns).

---

<a name="CreateAServiceAccountInGrafana"></a>

## Create a Service Account in Grafana

A service account is what OptiSigns uses to read your dashboard. It is a machine identity that belongs to your Grafana, separate from any person's login, so nobody's password ever reaches a screen.

The **Viewer** role is all OptiSigns needs.

<a name="CreateTheServiceAccount"></a>

### Create the Service Account

In Grafana, open **Administration**, then **Users and access**, then **Service accounts**.

![Grafana left nav with Administration and Users and access open, Service accounts highlighted](https://support.optisigns.com/hc/article_attachments/55447637222419)

Click **Add service account**.

![Grafana Service accounts page with the Add service account button highlighted](https://support.optisigns.com/hc/article_attachments/55447662957459)

Give it a **Display name** you will recognize later, set **Role** to **Viewer**, and click **Create**.

![Grafana Create service account form with the Role dropdown open and Viewer selected](https://support.optisigns.com/hc/article_attachments/55447652730899)

<a name="GenerateAToken"></a>

### Generate a Token

Open the service account you just created and click **Add service account token**.

![Grafana service account page with the Add service account token button highlighted](https://support.optisigns.com/hc/article_attachments/55447652798483)

Give the token a **Display name**. Leave **No expiration** selected, or set an expiration date if your security policy requires one. Then click **Generate token**.

![Grafana Add service account token dialog with No expiration set and Generate token highlighted](https://support.optisigns.com/hc/article_attachments/55447694278931)

Copy the token and store it somewhere safe. You will paste it into OptiSigns in the next step.

![Grafana token created dialog with the token value and Copy to clipboard highlighted](https://support.optisigns.com/hc/article_attachments/55447621366163)

|  |
| --- |
| **IMPORTANT** |
| **The token is shown only once.** If you lose it, you will need to generate a new one and update your OptiSigns connection.  If you set an expiration date, the connection stops working when the token expires. Screens that show screenshots stop updating, and the dashboard list stops loading. Put a reminder in your calendar to replace the token before that date. |

---

<a name="AddAGrafanaConnectionInOptiSigns"></a>

## Add a Grafana Connection in OptiSigns

Go to **Integrations** under your main menu, then click the **Grafana** tab and click **Add Connection**.

![OptiSigns Integrations page on the Grafana tab with the Add Connection button highlighted](https://support.optisigns.com/hc/article_attachments/55447637926547)

|  |
| --- |
| **TIP** |
| You can also create a new connection while you create the app. Open the **Grafana connection** dropdown and choose **New Grafana connection**. |

Fill in the first two fields:

- **Name**: the name of the connection as displayed in OptiSigns. It does not appear on your screen.
- **Grafana URL**: your Grafana's base URL, for example `https://acme.grafana.net`, or a public dashboard link. A link to a regular dashboard won't work here. You'll pick the dashboard later, on the app.

A line then appears under the URL that names your setup. For some addresses, "**Checking where this Grafana runs…"** shows for a few seconds first.

|  |  |
| --- | --- |
| The line under the URL | Your setup |
| "Grafana Cloud. Screens will render images, with nothing to set up." | [Grafana Cloud](#GrafanaCloud) |
| "Self-hosted Grafana. Screens will load the dashboard directly." | [Self-Hosted Grafana](#SelfHostedGrafana) |
| "On your own network. Screens will load the dashboard directly." | [Grafana on Your Own Network](#GrafanaOnYourOwnNetwork) |
| "Behind Cloudflare. Allow OptiSigns' IP so our servers can reach it." or "Behind a firewall. Allow OptiSigns' IP so our servers can reach it." | [Grafana Behind a Firewall](#GrafanaBehindAFirewall) |
| "Public dashboard link. No token needed, and nothing to set up." or "Public dashboard link on your own network." | [Public Dashboard Link](#PublicDashboardLink) |

Follow the section that matches. If the line says our servers can't reach your Grafana, or mentions a login page, follow [Grafana on Your Own Network](#GrafanaOnYourOwnNetwork).

|  |
| --- |
| **NOTE** |
| One connection is one Grafana instance. If you have more than one, add a separate connection for each. A public dashboard link is the exception: each link is its own connection. |

<a name="GrafanaCloud"></a>

### If You Use Grafana Cloud

Paste your token into **Service-account token (Viewer)**.

OptiSigns stores the token encrypted and uses it only on our servers. It is never sent to a screen.

The **Connection test** runs by itself once the URL and token are filled in. A successful test reads "Connection verified. Grafana (version), (number) dashboards." Below it you will see "Grafana Cloud manages the renderer. Nothing to set up."

Click **Add** to save the connection.

![Add Grafana Connection form with name, URL, masked service-account token and connection test](https://support.optisigns.com/hc/article_attachments/55447669482259)

|  |
| --- |
| **NOTE** |
| Grafana Cloud does not support Live mode. Grafana Cloud tells browsers not to embed its pages, so a screen cannot load it directly. OptiSigns shows it as a screenshot instead. |

|  |
| --- |
| **TROUBLESHOOTING** |
| If the test says "We couldn't reach this Grafana Cloud instance. It may be asleep.", open your Grafana in a browser once to wake it, then click **Re-test**. |

<a name="SelfHostedGrafana"></a>

### If You Self-Host Grafana

This is a Grafana you host yourself that our servers can reach from the internet.

Paste your token into **Service-account token (Viewer)**. The **Connection test** runs by itself.

Under the result, one line tells you whether your Grafana is ready for Live mode:

|  |  |  |
| --- | --- | --- |
| The line | What it means | What to do |
| "Signed access token accepted." | Live mode is ready. | You're all set. Click **Add**. |
| "Your Grafana needs to accept a signed access token from OptiSigns." | Live mode is not set up yet. | [Set up Live mode](#SetUpLiveModeOnYourGrafana), then click **Re-test**. |
| "Embedding is disabled on your Grafana." | Your Grafana refuses to load inside another page. | [Set up Live mode](#SetUpLiveModeOnYourGrafana), then click **Re-test**. |
| "Renders through anonymous access. Anyone who can reach this Grafana can read every dashboard in it." | It works, but only because your Grafana is open to anyone. | We recommend you [set up Live mode](#SetUpLiveModeOnYourGrafana) and turn anonymous access off. |

![Add Grafana Connection form with the connection test result and the Set up Live mode link highlighted](https://support.optisigns.com/hc/article_attachments/56227064733331)

Click **Add** to save the connection. You can save it whatever the test says.

<a name="GrafanaOnYourOwnNetwork"></a>

### If Your Grafana Is On Your Own Network

This is a Grafana our servers cannot reach: a private IP address such as `192.168.1.20`, `localhost`, a short name such as `grafana`, a name ending in `.local`, `.lan` or `.internal`, or any address that only answers inside your network.

Your screens load the dashboard themselves, so they need to be on a network that can reach your Grafana.

You won't need a token here, and there's no connection test. Open the **Set up Live mode on your Grafana** block and follow [Set Up Live Mode on Your Grafana](#SetUpLiveModeOnYourGrafana), then click **Add**.

![Add Grafana Connection form with a private address and the Set up Live mode on your Grafana block highlighted](https://support.optisigns.com/hc/article_attachments/56227064734867)

A few things to know:

- Use `https://` where you can. The certificate needs to come from a public certificate authority, because screens won't load a self-signed one.
- `http://` works on Android and Windows/Mac players. It isn't available in the Web Player, which is when you use a browser as your screen.
- A login page in front of Grafana. If the form says "A login page sits in front of this Grafana, so our servers can't reach it.", your screens can only load the dashboard if that login lets them through.
- A firewall instead of a private network. If the form says "Our servers can't reach this Grafana.", you can click **Behind a firewall? Allow OptiSigns' IP.** and follow the next section instead.

<a name="GrafanaBehindAFirewall"></a>

### If Grafana Is Behind a Firewall

This is a Grafana on the internet that only accepts visitors it knows, for example behind Cloudflare Access, a Cloudflare rule, or a firewall allowlist.

You let our servers in by allowing OptiSigns' fixed IP address. Our servers then fetch a screenshot of your dashboard and send it to your screens.

You'll need:

- A **Pro Plus** or **Engage** plan. On other plans the form shows an **Upgrade** button instead.
- An `https://` address on the standard port (443).
- Grafana's [image renderer service](https://grafana.com/docs/grafana/latest/setup-grafana/image-rendering/) installed, because screens show screenshots on this path.

When adding a Grafana Connection, you'll need to Allow our IP. The form shows the IP address with a copy button. Add it to your firewall or Cloudflare rule.

![Add Grafana Connection form for a Grafana behind Cloudflare with the copy button next to the IP address highlighted](https://support.optisigns.com/hc/article_attachments/56227064736275)

|  |  |
| --- | --- |
| What is in front of your Grafana | What to add |
| Cloudflare Access | A **Bypass** rule for the IP on the Access application |
| Other Cloudflare protection | A rule that skips the protection for the IP |
| A firewall, security group or IP allowlist | Allow the IP on port 443 |

Paste your token into **Service-account token (Viewer)**.

Read the test result. The test runs by itself.

|  |  |
| --- | --- |
| The result | What to do |
| "Connected through OptiSigns' fixed IP. Grafana (version), (number) dashboards." | Click **Add**, and you're all set. |
| "Install Grafana's image renderer so screens can show this dashboard." | Install the image renderer service, then click **Re-test**. |
| "Your Grafana is reachable without a fixed IP." | No fixed IP is needed. It's saved as a regular self-hosted Grafana. |
| "Cloudflare still blocks our servers. Check that (IP) is allowed." or "Your firewall still blocks our servers. Check that (IP) is allowed." | Check your rule, then click **Re-test**. |
| "We couldn't reach this Grafana through our fixed IP. Check that it is allowed, then Re-test." | Check your rule, then click **Re-test**. |

![Connection test showing Connected through OptiSigns' fixed IP with the Image mode and Live mode lines below](https://support.optisigns.com/hc/article_attachments/56227064739347)

|  |
| --- |
| **NOTE** |
| If Cloudflare blocks the test, the result includes a **Cloudflare Ray ID**. Give it to whoever manages your Cloudflare account so they can find the block. |

**Can't allow our IP?** Under the test you will see "Can't allow our IP? Screens on an allowed network can load the dashboard directly." Open **Set up Live mode on your Grafana** there and follow [Set Up Live Mode on Your Grafana](#SetUpLiveModeOnYourGrafana). Your screens then load the dashboard themselves, so they need to be on a network your firewall allows.

|  |
| --- |
| **NOTE** |
| The fixed IP can't get past a login page, such as single sign-on or a password prompt in front of Grafana. Cloudflare Access is the exception, because it supports a Bypass rule. |

<a name="PublicDashboardLink"></a>

### If You Use a Public Dashboard Link

A public dashboard link needs no token and no setup in OptiSigns.

In Grafana, share the dashboard externally (older versions call this a public dashboard) and copy its link. See [Grafana's guide to shared dashboards](https://grafana.com/docs/grafana/latest/dashboards/share-dashboards-panels/shared-dashboards/). The link contains `/public-dashboards/`.

Paste that link into **Grafana URL**, then click **Add**.

![Add Grafana Connection form with a public dashboard link in Grafana URL and the Add button highlighted](https://support.optisigns.com/hc/article_attachments/56227064742931)

A few things to know:

- Keep in mind that **anyone who has the link can see the dashboard.**
- The time range, theme and filters are the ones saved on the public dashboard. To change them, edit the public dashboard in Grafana.
- Some public links open as a full page on the screen instead of inside the app: links on Grafana Cloud, links on your own network, and links where the test says "Its Grafana forbids framing, so screens will open it as a full page." These play on Android and Windows/Mac players, not in the Web Player.

---

<a name="SetUpLiveModeOnYourGrafana"></a>

## Set Up Live Mode on Your Grafana

Live mode needs a one-time change to your Grafana configuration. This applies to self-hosted Grafana and Grafana on your own network.

OptiSigns generates the exact configuration for your account.

1. In the Grafana connection form, open **Set up Live mode on your Grafana**. To get back to it later, click **Edit** on the connection.
2. Pick the **grafana.ini** or **Docker / Kubernetes** tab to match how you run Grafana.
3. Click **Copy**.
4. Add it to your Grafana configuration and restart Grafana.
5. If your form has a connection test, click **Re-test**.

It turns on two things:

- JWT authentication, so your Grafana accepts a signed token from OptiSigns instead of a password. Your own Grafana logins are unaffected.
- Embedding, so the dashboard can load in the OptiSigns preview and in the Web Player.

|  |
| --- |
| **IMPORTANT** |
| Make sure to add the whole block, since both parts are needed. If your Grafana also sends a Content-Security-Policy, its frame-ancestors setting has to allow embedding too. |

After the first screen connects, you'll see a user named `optisigns-signage` in your Grafana. That's your OptiSigns screens signing in.

|  |
| --- |
| **NOTE** |
| The block contains an OptiSigns web address, on the line that starts with `jwk_set_url`. Your Grafana server needs to reach that address on the internet to check our signature. |

If you would rather show screenshots from a self-hosted Grafana, install Grafana's image renderer service. The bundled renderer plugin was removed in Grafana 13, so the standalone service is the only option on current versions. See [Grafana's image rendering documentation](https://grafana.com/docs/grafana/latest/setup-grafana/image-rendering/). You can then switch the mode under **Advanced** on the app. This is not available for a Grafana on your own network, because our servers cannot reach it to take the screenshot.

|  |
| --- |
| **NOTE** |
| OptiSigns asks Grafana to hide its own time picker and variable bar, which needs Grafana 11.3 or newer. On older versions those controls may still be visible on the screen. |

---

<a name="CreateAGrafanaAppInOptiSigns"></a>

## Create a Grafana App in OptiSigns

Now that the connection exists, create the asset that your screens will play.

Open OptiSigns and go to **Files/Assets** → **Apps** → **Grafana**.

![OptiSigns Add App dialog with Grafana searched and the Grafana app tile highlighted](https://support.optisigns.com/hc/article_attachments/55447638131475)

The app opens with a live preview on the right, so you can see what the screen will show as you fill in the form.

![Grafana app settings with the Connect and Dashboard sections and the connection picker highlighted](https://support.optisigns.com/hc/article_attachments/55447621822483)

Under **Connect**:

- **Name**: the name of your Grafana app. This is for use in OptiSigns and does not appear on your screen.
- **Grafana connection**: choose one of your Grafana connections (or create a new one)

Under **Dashboard**, what you see depends on the connection:

- **Dashboard**: choose from the list of dashboards your service account can see. This is what most connections show.
- **Dashboard link**: for a Grafana on your own network, there is no list. Open the dashboard in Grafana and copy the link from your browser's address bar, then paste it here.
- For a public dashboard link, there is no dashboard to choose. The link is shown as **Public dashboard URL**.

![Grafana app Dashboard section with a dashboard address pasted into the Dashboard link field](https://support.optisigns.com/hc/article_attachments/56227083628563)

- **Single panel ID (optional)**: leave this blank to show the whole dashboard. Enter a panel's ID to show just that one panel, filling the screen. You can find the ID in Grafana's URL when you view a single panel.

|  |
| --- |
| **NOTE** |
| Shortened Grafana links won't work in **Dashboard link**, so copy the link from your browser's address bar instead. The same goes for snapshot and playlist links. |

<a name="DisplaySettings"></a>

### Display Settings

Open the **Display** section to control how the dashboard looks.

![Grafana app Display section showing the Time range and Theme dropdowns](https://support.optisigns.com/hc/article_attachments/55447653502355)

- **Time range**: how far back the dashboard looks. Last 1 hour, Last 6 hours, Last 24 hours, or Last 7 days. The range always ends at the current moment.
- **Theme**: **Dark** or **Light**. Dark is usually the better choice on a wall-mounted screen.

In Image mode you will also see:

- **Refresh interval**: how often the screen fetches a fresh screenshot, in seconds.
  - The minimum is 300 seconds (5 minutes), the maximum is 3600 seconds (1 hour), and the default is 600 seconds (10 minutes).
- **Image quality**: **Standard** or **High (HiDPI)**. Use High for a 4K screen or when a panel's text looks soft.
- **Show "as of" freshness stamp**: adds a small timestamp so viewers can tell how current the data is.

Public dashboard links have no Display settings.

<a name="AdvancedSettings"></a>

### Advanced Settings

The **Advanced** section holds one setting most screens never need.

![Grafana app Advanced section showing the Render mode dropdown set to Live mode](https://support.optisigns.com/hc/article_attachments/55447638366995)

- **Render mode**: **Image mode (works on Cloud)** or **Live mode (self-hosted)**. OptiSigns sets this from your connection. You'd only need to change it if the mode it chose doesn't work on a particular screen.

Click **Save** when you're done. The dialog stays open so you can keep adjusting. Click **Close** when you're finished.

|  |
| --- |
| **NOTE** |
| Advanced isn't shown for a Grafana on your own network or for a public dashboard link. |

<a name="AboutThePreview"></a>

### About the Preview

- In Live mode and for public links, the preview updates as you fill in the form.
- In Image mode, the preview appears after you click **Save** for the first time.
- For a Grafana on your own network, or an `http://` address, the preview may say **Preview not available**. Click **Open in Browser** from a computer on the same network, or push the app to a device to see it. Your screens can still show the dashboard.

![Grafana app preview showing the Preview not available card with the Open in Browser button highlighted](https://support.optisigns.com/hc/article_attachments/56227064757523)

---

<a name="DeployingAGrafanaApp"></a>

## Deploying a Grafana App

You can deploy your new Grafana app as an individual asset, or as part of a Split Screen.

To get your new Grafana asset to a screen, go to the **Screens** tab, then click **Edit** on the screen you want to assign it to.

![OptiSigns Screens list row with the Edit button highlighted](https://support.optisigns.com/hc/article_attachments/55447653631379)

This brings up the **Edit Screen** dialog:

![Edit Screen dialog with Content Type set to Asset and a Change button beside the selected asset](https://support.optisigns.com/hc/article_attachments/55447653712915)

Here, select **Asset** under **Content Type**. Or, if you already have an Asset displayed, you can hit **Change**.

Then select your created Grafana Asset.

Now hit **Save**. Your Grafana asset will now display on screen.

You can also deploy it as part of a split screen, allowing you to show other assets at the same time. See how in our Split Screen app article. It can also be displayed in a Playlist or Schedule.

<a name="HowUpdatesWillAppearOnscreen"></a>

### How Updates Will Appear Onscreen

In **Image** mode, the screen fetches a fresh screenshot every refresh interval, so a change you make in Grafana appears within one interval. If a screenshot fails, the screen keeps showing the last good one rather than going blank. The "as of" stamp shows when that picture was taken.

In **Live** mode, the dashboard runs on the screen itself, so it updates on whatever refresh your Grafana dashboard is set to. About every 8 hours the screen reloads the dashboard, which shows a blank screen for a few seconds.

For **Public dashboard links**, the screen shows the public dashboard as Grafana serves it.

<a name="WhichPlayersAreSupported"></a>

### Which Players Are Supported

|  |  |  |
| --- | --- | --- |
| Your setup | Android and Windows/Mac players | Web Player |
| Screenshots (Grafana Cloud, Behind a firewall) | Yes | Yes |
| Live mode with an `https://` address | Yes | Only if embedding is allowed and the browser can reach your Grafana |
| Live mode with an `http://` address | Yes | No |
| Public link shown inside the app | Yes | Yes |
| Public link shown as a full page | Yes | No |

---

<a name="FrequentlyAskedQuestions"></a>

## Frequently Asked Questions

Here, we'll answer some frequently asked questions our customers have, and solve some common troubleshooting issues.

<a name="TheConnectionTestSaysGrafanaRejectedThisTokenWhatsWrong"></a>

### The connection test says Grafana rejected this token. What's wrong?

The token is expired, has been revoked, or belongs to a different Grafana than the URL you entered. Generate a new service-account token in Grafana and update the connection. Also check that the **Grafana URL** points at the same instance the service account lives in.

<a name="TheConnectionTestSaysCloudflareOrAFirewallBlockedOurServersWhatDoIDo"></a>

### The connection test says Cloudflare or a firewall blocked our servers. What do I do?

Something in front of your Grafana stopped our servers before Grafana saw the request, so we could not check your token. Follow [Grafana Behind a Firewall](#GrafanaBehindAFirewall) to allow OptiSigns' fixed IP, then click **Re-test**.

<a name="OptiSignsSaysItCantReachMyGrafanaIsThatAProblem"></a>

### OptiSigns says it can't reach my Grafana. Is that a problem?

Not necessarily. It means our servers could not open your Grafana from the internet, which is normal for a Grafana on a private network. Your screens can still load it on your own network.

If you expected it to be reachable, check the URL for typos and confirm the certificate is issued by a public certificate authority. A self-signed certificate will fail. Then enter the URL again.

<a name="MyDashboardListIsEmptyOrICantFindMyDashboardHowCanIMakeItAppear"></a>

### My dashboard list is empty, or I can't find my dashboard. How can I make it appear?

There are three usual causes:

- The service account cannot see the dashboard. In Grafana, check that its role is **Viewer** and that it has permission to view the folder the dashboard lives in.
- Grafana Cloud is asleep. Open your Grafana in a browser once to wake it.
- The connection points at a different Grafana than the one the dashboard lives in.

Then close the app form and open it again, which reloads the list.

<a name="OptiSignsWontAcceptTheLinkIEnteredWhy"></a>

### OptiSigns won't accept the link I entered. Why?

It depends on the field:

- **Grafana URL** (on the connection) takes the base URL of your Grafana, such as `https://acme.grafana.net`, or a public dashboard link. A link to a regular dashboard won't work there, so remove everything after the host name and try again.
- **Dashboard link** (on the app, for a Grafana on your own network) takes the link from your browser's address bar while the dashboard is open. Shortened links, snapshot links, playlist links and public dashboard links won't work there.

<a name="TheConnectionTestTellsMeToInstallGrafanasImageRendererWhatDoIDo"></a>

### The connection test tells me to install Grafana's image renderer. What do I do?

Your screens will show screenshots, and your self-hosted Grafana has no image renderer to take them. Install and configure the [image renderer service](https://grafana.com/docs/grafana/latest/setup-grafana/image-rendering/), then click **Re-test**. The bundled renderer plugin was removed in Grafana 13, so the standalone service is the only option on current versions.

<a name="TheConnectionTestSaysEmbeddingIsDisabledOnMyGrafanaHowDoIFixIt"></a>

### The connection test says embedding is disabled on my Grafana. How do I fix it?

Your Grafana is telling browsers not to load it inside another page. Apply the block under **Set up Live mode on your Grafana** in the connection form, restart Grafana, and click **Re-test**.

If your Grafana also sends a Content-Security-Policy, its frame-ancestors setting has to allow embedding too.

Android and Windows/Mac players open the dashboard as a full page, so they can show it even while embedding is off. The OptiSigns preview and the Web Player need embedding.

<a name="MyScreenSaysDashboardUnavailableWhatDoesThatMean"></a>

### My screen says Dashboard unavailable. What does that mean?

The screen could not load your Grafana. The usual causes are:

- The device cannot reach your Grafana. It may be down, its name may not resolve, or the screen's network may block it.
- Your Grafana's certificate is not from a public certificate authority.

The screen keeps retrying by itself.

<a name="MyScreenShowsGrafanasLoginPageWhy"></a>

### My screen shows Grafana's login page. Why?

Your Grafana is not accepting OptiSigns' signed token yet. Check that you applied the whole block under **Set up Live mode on your Grafana**, that you restarted Grafana afterwards, and that your Grafana server can reach the internet address on the `jwk_set_url` line.

<a name="MyScreenIsShowingAnOldPictureOrSaysDataUnavailableWhy"></a>

### My screen is showing an old picture, or says Data unavailable. Why?

OptiSigns could not get a fresh screenshot from Grafana. If it has an earlier one, it keeps showing it, and the "as of" stamp tells you how old it is. If it never got one, the screen says **Data unavailable**.

Check that Grafana is up and that the service-account token has not expired or been revoked. If you use OptiSigns' fixed IP, also check that the IP is still allowed.

<a name="ThePreviewSaysItIsntAvailableWillMyScreensWork"></a>

### The preview says it isn't available. Will my screens work?

Usually yes. The preview runs in your browser, which often cannot reach a Grafana on a private network.

- In the app form, the preview says **Preview not available**. Click **Open in Browser** from a computer on the same network as your Grafana, or push the app to a device to check it.
- Elsewhere in OptiSigns, such as the Files/Assets and Screens pages, it says "Preview isn't available for this dashboard. Your screens can still show it."

If you see that second sentence in the Web Player, it isn't able to show this dashboard. See [Which Players Are Supported](#WhichPlayersAreSupported).

<a name="MyGrafanaDashboardUsedToDisplayFineButStoppedAllOfASuddenWhatsWrong"></a>

### My Grafana dashboard used to display fine, but stopped all of a sudden. What's wrong?

Check these first:

- The service-account token. If you set an expiration date when you created it, check whether that date has passed. Generate a new token in Grafana and update your OptiSigns connection.
- Your firewall or Cloudflare rule, if you use OptiSigns' fixed IP. Check that the rule still allows the IP and that your plan is still Pro Plus or Engage.
- Your Grafana configuration, if you use Live mode. An upgrade or a new deployment can drop the block you added under **Set up Live mode on your Grafana**.
