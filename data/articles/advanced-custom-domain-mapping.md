# Advanced: Custom Domain Mapping

Article URL: https://support.optisigns.com/hc/en-us/articles/1500000480302-Advanced-Custom-Domain-Mapping

Article ID: 1500000480302

Locale: en-us

Updated at: 2026-10-28T20:58:49Z

---

- [What You'll Need](#WhatYouNeed)
- [Activate OptiSigns Sub-Domain](#Activate)
- [Map CNAME Alias for Domain / Sub-Domain](#CNAME)
- [Activate SSL for Domain / Sub-Domain and Activating Add-On](#SSL)

OptiSigns lets you can enhance your branding or white label by mapping a custom domain for your OptiSigns Management Portal.

For example: you can map your sub-domain: **login.abcmedia.com** so that your users can log in and use the portal from **login.abcmedia.com** and use the app like the screenshot below.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/1500000517302)

---

<a name="WhatYouNeed"></a>

## What You'll Need

- An [**OptiSigns Pro Plus**](https://www.optisigns.com/pricing) plan or higher
- An active Custom Domain add-on (flat $10/month) or free trial (to create a custom domain)

---

<a name="Activate"></a>

## Activate OptiSigns Sub-Domain

Go to the Branding page of your Account Management Settings:

![](https://support.optisigns.com/hc/article_attachments/53467701208467)

Type in your desired sub-domain for optisigns.net. In this case, we type in "abcmedia".
Don't worry about optisigns.net, you will map your domain in the next step.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/360099399934)

---

<a name="CNAME"></a>

## Map CNAME Alias for Domain / Sub-Domain

In your Domain DNS management, map your desired domain/sub-domain to your OptiSigns sub-domain using CNAME Alias.
In this example, we map: login.abcmedia.com -> abcmedia.optisigns.net

Refer to your domain host documentation for more specific details.

Here are the generic steps:

1. Go to your domain’s DNS records.
2. Add a record to your DNS settings, selecting **CNAME** as the record type.
3. Return to the first window or tab and copy the contents of the **Label/Host** field.
4. Paste the copied contents into the **Label** or **Host** field with your DNS records.
5. Return to the first window or tab and copy the contents of the **Destination/Target** field.
6. Paste the copied contents into the **Destination** or **Target** field with your DNS records.

   Your record should look similar to one of the tables below:

   **CNAME Record**

   | Record type | Label/Host field | Time To Live (TTL) | Destination/Target field |
   | --- | --- | --- | --- |
   | CNAME | login | 3600 or leave the default | abcmedia.optisigns.net |
7. Save your record.
   CNAME record changes can take up to 72 hours to go into effect, but typically they happen much sooner.

Here are links to documentation from some popular domain hosts:

- [GoDaddy](https://www.godaddy.com/help/add-a-cname-record-19236)
- [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain/)
- [Bluehost](https://my.bluehost.com/hosting/help/resource/714)
- [1&1 IONOS](https://www.ionos.com/help/domains/configuring-cname-records-for-subdomains/configuring-a-cname-record-for-a-subdomain/)
- [HostGator](https://www.hostgator.com/help/article/how-to-change-dns-zones-mx-cname-and-a-records)
- [DreamHost](https://help.dreamhost.com/hc/en-us/articles/215414867-How-do-I-add-custom-DNS-records-)
- [Cloudflare](https://support.cloudflare.com/hc/en-us/articles/360020615111-Configuring-a-CNAME-setup)

---

<a name="SSL"></a>

## Activate SSL for Domain / Sub-Domain and Activating Add-On

Next, to activate your domain, you'll need to activate your Custom Domain add-on. This can be done either on the **Subscription Page** or directly from the **Branding Page**.

![](https://support.optisigns.com/hc/article_attachments/53467717890195)![](https://support.optisigns.com/hc/article_attachments/53467701210771)

The price is a flat **$10/month**, and there's a 14-day free trial for this feature as well.

Either way, once the Add-On is active, you can enter the domain/sub-domain you have configured in Step 2 in Your domain section.

In this example, we use: login.abcmedia.com

Then click Activate.

This will trigger the process on OptiSigns side to activate SSL for your sub-domain. This will ensure that your user can use HTTPS: i.e. <https://login.abcmedia.com> to use the app.

This process can take up to 24-48 hours to complete. You will be notified via email once it's done.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/360101613533)

Once you get the notification that your SSL is activated, you can start using your own domain/sub-domain (i.e. <https://login.abcmedia.com>).
