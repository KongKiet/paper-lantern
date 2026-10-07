# Displaying SharePoint Sites on OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/4414539282067-Displaying-SharePoint-Sites-on-OptiSigns

Article ID: 4414539282067

Locale: en-us

Updated at: 2026-10-01T16:01:20Z

---

### In this article, we will show how to display an internal SharePoint site on OptiSigns digital signage.

- [What You Need](#WhatYouNeed)
- [Setting Up the SharePoint App](#SettingUp)
- [Frequently Asked Questions](#FAQs)

|  |
| --- |
| **NOTE** |
| The **SharePoint app** is available to customers with a **Standard plan or above**. |

With OptiSigns, it's possible to showcase your SharePoint site on any of your screens. Even gated sites requiring login can be shown. All you'll need is a URL to your SharePoint site and a valid Microsoft account.

![SharePoint communication site home page with hero tiles and a News section](https://support.optisigns.com/hc/article_attachments/4414531378451)

Note that if you want to display SharePoint News, you'll want to check out our article on [Connecting SharePoint News to OptiSigns](https://support.optisigns.com/hc/en-us/articles/55450681344915).

---

<a name="WhatYouNeed"></a>

## What You Need

- An OptiSigns [Standard plan subscription](https://www.optisigns.com/pricing) or above
- A screen, [set up and paired](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv) with OptiSigns
- A valid Microsoft username and password
- A SharePoint URL

---

<a name="SettingUp"></a>

## Setting Up the SharePoint App

First, head to the SharePoint webpage you'd like to display on your screens.

![SharePoint site page with the Share button in the top-right toolbar](https://support.optisigns.com/hc/article_attachments/37403530778515)

Next, hit **Share**. Click **Copy link to page**.

![SharePoint Share menu open with Copy link to page selected](https://support.optisigns.com/hc/article_attachments/37403516098835)

The below screen should appear. Hit **Copy**.

![SharePoint Link created dialog with an arrow on the Copy button](https://support.optisigns.com/hc/article_attachments/37403530789651)

This is the URL you will be using to set up a SharePoint app within OptiSigns.

Next, log on to the [OptiSigns Portal](http://app.optisigns.com/).

Go to **Files/Assets**, then click the **Apps** button on the left side of the screen.

![OptiSigns Files/Assets page with the Files/Assets tab and the Apps button highlighted](https://support.optisigns.com/hc/article_attachments/55984266866963)

Find and click on **SharePoint.**

![Add App dialog searched for SharePoint, with the SharePoint app highlighted](https://support.optisigns.com/hc/article_attachments/55984266868883)

Enter details for your SharePoint site. The URL will be the one you copied earlier.

![SharePoint app settings with Name, URL and the Sign in with Credential switch turned on](https://support.optisigns.com/hc/article_attachments/55984259183123)

- **Name -** Name of your app asset, this is the name of the wall in your asset list. It will **not** be displayed on your screens.
- **URL -** The URL address to your SharePoint site. This is the URL we copied earlier.

Click **Sign In with Credential** to open a Sign In section. Most SharePoint sites require a Sign In. This is where you'll input that information.

- **Master Password -** When checked, this will prompt you to enter a Master Password for use on OptiSigns.
  - While your password is encrypted with OptiSigns, this adds an extra layer of encryption. This way, even OptiSigns cannot decrypt your password. We will go into more detail on our encryption methods in our [FAQ section.](#FAQs)
- **Username/Email -** Your Microsoft account username.
- **Password -** Your Microsoft account password.

Please note that the Username and Password input will need access to the SharePoint document URL.

Finally, click **Save**.

You've successfully created a SharePoint asset! This asset can be manipulated on your screen as you would a regular web page.

---

<a name="FAQs"></a>

## Frequently Asked Questions

Here we'll tackle the most common issues and questions we get regarding displaying SharePoint on OptiSigns.

#### **I tried to get SharePoint on my screen, but it's prompting me to Sign In! What's going on?**

The first time OptiSigns connects to SharePoint, it will use a Web Scripting feature to automatically log you on using the Username and Password you input in the app. You'll know it's working when your Username will automatically populate in the proper field after a few seconds.

This process takes about a minute for first time logins using the asset. Afterwards, it should remember your login and work thereafter.

#### **I want to display multiple SharePoint pages. How can I do that?**

The easiest way to display several SharePoint pages is to create several SharePoint assets, then utilize them [in a Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists).

#### **I'd like to display only SharePoint News, and have it automatically update. Can I do that?**

Yes! Please see our complete article on [Creating Custom News Feeds with SharePoint](https://support.optisigns.com/hc/en-us/articles/35337746613139-How-to-Create-Custom-News-Feeds-with-SharePoint-or-Other-Sources-Using-OptiSync) for more information.

#### **I'm trying to display SharePoint on my Samsung SSSP or LG WebOS TVs and all I'm seeing is a blank screen. Why won't it work?**

Microsoft requires a minimum Chromium version of 95 for their apps to display. These TVs typically don't update very often. This is a Microsoft issue, and there is little we can do on our end.

If you have one of these TVs and wish to display SharePoint, we recommend our [Pro Player](https://shop.optisigns.com/products/optisigns-digital-signage-player).

#### **How does the encryption of my password work at OptiSigns? If I input it, will I be at risk?**

Here's how the encryption flow works:

[![Diagram of your login script encrypted in the portal, stored on OptiSigns servers and decrypted on the player](https://support.optisigns.com/hc/article_attachments/37403516119187)](https://support.optisigns.com/hc/article_attachments/37403516119187)

When you input your Username and Password into the OptiSigns SharePoint app, it is being utilized as a [Web Script](https://support.optisigns.com/hc/en-us/articles/1500012522362-How-to-use-the-Web-Scripting-App). This script is encrypted at your browser, and transferred securely using HTTPS/SSL during transits and stored on our servers.

It is then sent via the same method to devices, and decrypted at device level before executing on the target website. In this case, that's SharePoint.

If you want to add additional security by utilizing a Master Password and our Zero Knowledge Encryption framework, you will have to enter your Master Password when:

- Creating/editing assets
- One time on each device, so it will know how to decrypt

The Master Password can be input on each device under the **Advanced Options** menu under **Master Password**.

![OptiSigns player Advanced Options menu with Master Password highlighted](https://support.optisigns.com/hc/article_attachments/37403530810387)

The Master Password can then be input. It will need to match the Master Password field input on your assets.

**![OptiSigns player Master Password prompt with Cancel and OK buttons](https://support.optisigns.com/hc/article_attachments/37403516129043)**

This will ensure no one, not even OptiSigns, can decrypt your password under any circumstance.
