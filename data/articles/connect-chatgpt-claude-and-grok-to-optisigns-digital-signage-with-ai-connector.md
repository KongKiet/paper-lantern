# Connect ChatGPT, Claude and Grok to OptiSigns Digital Signage with AI Connector

Article URL: https://support.optisigns.com/hc/en-us/articles/56987330525587-Connect-ChatGPT-Claude-and-Grok-to-OptiSigns-Digital-Signage-with-AI-Connector

Article ID: 56987330525587

Locale: en-us

Updated at: 2026-10-30T19:28:50Z

---

### In this article, we'll turn on the OptiSigns AI Connector, add it to your AI assistant, and show what you can ask it to do.

- [What You'll Need](#WhatYoullNeed)
- [Turn On the AI Connector](#TurnOnTheAIConnector)
- [Add OptiSigns to Your AI Assistant](#AddOptiSignsToYourAIAssistant)
  - [Coding Agents](#CodingAgents)
  - [Sign In and Allow Access](#SignInAndAllowAccess)
  - [Let Claude Upload Files](#LetClaudeUploadFiles)
- [What You Can Ask](#WhatYouCanAsk)
- [Troubleshooting](#Troubleshooting)

With the OptiSigns AI Connector, you can update your screens by asking the AI assistant you already use. Tell ChatGPT, Claude or Grok what you want, and it uploads files, builds playlists, sets schedules and pushes content to your screens for you.

|  |
| --- |
| **IMPORTANT** |
| The assistant always asks you to confirm before it deletes anything, overwrites content, or changes what is playing on a screen. |

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account on **any plan**. The AI Connector is included at no extra cost.
- The **account owner** or a **super admin** to turn on the AI Connector. This is a one-time step for the whole account.
- One of these AI assistants:
  - **ChatGPT**, on any plan, including Free
  - **Claude**, on claude.ai or the Claude desktop app
  - **Grok**
  - The coding agents **Claude Code**, **Codex** or **OpenCode**
- On ChatGPT Business and Enterprise, or Claude Team and Enterprise, an admin may need to add the connector for you.
- A web browser for the one-time sign-in.

---

<a name="TurnOnTheAIConnector"></a>

## Turn On the AI Connector

The AI Connector is off by default. The account owner or a super admin turns it on once for the whole account.

1. In the [OptiSigns portal](https://app.optisigns.com), open your account settings and select **Preferences**.
2. In the **General** section, check **Enable AI connector (MCP)**.

![Preferences General section with the Enable AI connector (MCP) checkbox highlighted](https://support.optisigns.com/hc/article_attachments/56987303229971)

3. Select **Enable**, then select **Save Changes**.

![Enable AI connector (MCP) confirmation window with the Enable button highlighted](https://support.optisigns.com/hc/article_attachments/56987330788627)

---

<a name="AddOptiSignsToYourAIAssistant"></a>

## Add OptiSigns to Your AI Assistant

Each assistant needs this Server URL, with **OAuth** as the authentication:

```
https://optisigns-mcp.optisigns.com/mcp
```

- **ChatGPT:** on [chatgpt.com](https://chatgpt.com), select **Plugins** > **Add** > **Add custom MCP server**. Enter **OptiSigns** as the name and the Server URL, choose **OAuth**, check **I understand and want to continue**, and add the server. On Business and Enterprise plans, a workspace admin may need to allow custom MCP servers first.
- **Claude:** on [claude.ai](https://claude.ai), go to **Settings** > **Connectors** > **Add** > **Add custom connector**. Enter **OptiSigns** and the Server URL, select **Add**, then select **Connect**. This also sets up the Claude desktop app. On Team and Enterprise plans, an organization owner adds the connector.
- **Grok:** on [grok.com](https://grok.com), select **Plugins**, then on the **Connectors** tab select **New Connector** > **Custom**. Enter **OptiSigns** and the Server URL, then select **Add Connector**.

**Tip:** AI assistants change their menus often. If a label doesn't match, look in the assistant's settings for **Plugins**, **Connectors** or **Apps**.

<a name="CodingAgents"></a>

### Coding Agents

Run the command for your agent. It opens your browser to sign in.

**Claude Code** (then type **/mcp** and select **optisigns** to sign in):

```
claude mcp add --transport http optisigns https://optisigns-mcp.optisigns.com/mcp
```

**Codex:**

```
codex mcp add optisigns --url https://optisigns-mcp.optisigns.com/mcp
codex mcp login optisigns
```

**OpenCode:** add this to the **mcp** section of opencode.json, then run **opencode mcp auth optisigns**:

```
"optisigns": {
  "type": "remote",
  "url": "https://optisigns-mcp.optisigns.com/mcp",
  "enabled": true
}
```

<a name="SignInAndAllowAccess"></a>

### Sign In and Allow Access

When you connect, your assistant opens the OptiPrime sign-in page. Log in with your OptiSigns email and password, or with Google or Microsoft.

![OptiPrime sign-in page with Sign in with Google, Sign in with Microsoft and an email field](https://support.optisigns.com/hc/article_attachments/56987308899987)

OptiSigns then lists what the assistant is asking to do in your account. Review it and select **Allow**. The assistant never sees your password, and it can only do what you allow and what your OptiSigns role permits.

![Authorize Claude page listing the permissions Claude is requesting, with the Allow button highlighted](https://support.optisigns.com/hc/article_attachments/56987324207635)

To check that it works, start a new chat and ask: *"Which playlists are in my account?"*

<a name="LetClaudeUploadFiles"></a>

### Let Claude Upload Files

To upload images and videos from Claude, go to **Settings** > **Capabilities** and add this domain to the allowed domains for code execution:

```
transforge-api.optisigns.com
```

---

<a name="WhatYouCanAsk"></a>

## What You Can Ask

Talk to your assistant like you would brief a coworker, and use the names from your account. For example:

- *"Upload this flyer and put it on the break room screen."*
- *"Create a playlist called Weekly Specials from these four images, 10 seconds each."*
- *"Play the Breakfast playlist every day from 6 to 11 and the Lunch playlist from 11 to 3."*
- *"We're closed on Thanksgiving. Skip the lunch menu that day only."*
- *"Are any of my screens offline?"*
- *"Which screens show the Fall Campaign playlist? Duplicate it as Winter Campaign and put it on those same screens."*
- *"Add a Dallas weather app to the Lobby playlist."*

The assistant can add **Weather**, **World Clock**, **Website**, **YouTube** and **Vimeo** apps. Schedules follow each screen's local time. If you belong to more than one team, it works in your default team unless you name another.

Use the portal for everything else, such as the **Designer** and **Templates**, other apps, file start and expiration dates, device settings and remote commands, and users, teams and billing.

To disconnect an assistant, remove OptiSigns from its settings. To turn the AI Connector off for everyone, uncheck **Enable AI connector (MCP)** on the **Preferences** page.

---

<a name="Troubleshooting"></a>

## Troubleshooting

Here are some common issues you may face when setting up the OptiSigns AI Connector.

#### "Connection failed" When Adding the Connector

Check that the Server URL is exactly https://optisigns-mcp.optisigns.com/mcp, with no extra spaces.

#### The Sign-In Page Doesn't Open

Allow pop-ups for your assistant's website, then select **Connect** again.

#### "The AI connector is turned off for this OptiSigns account"

Ask your account owner or a super admin to turn it on.

#### Claude Won't Upload a File

Add transforge-api.optisigns.com to Claude's allowed domains, as described above.

#### Errors After Signing In, or the Assistant Can't Find Something

Use the exact names shown in the portal. If errors continue, remove the connector from your assistant, add it again and sign in again.
