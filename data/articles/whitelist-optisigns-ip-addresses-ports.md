# Whitelist OptiSigns IP Addresses & Ports

Article URL: https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-Addresses-Ports

Article ID: 360047275934

Locale: en-us

Updated at: 2026-10-30T16:09:57Z

---

### In this article, you'll find every address, IP and port your firewall needs to allow, in lists you can copy and paste straight into your firewall.

- [Ports](#Ports)
- [Option 1: Allow by Domain (Recommended)](#Option1AllowByDomainRecommended)
- [Option 2: Allow Exact Domains](#Option2AllowExactDomains)
  - [Player Updates](#PlayerUpdates)
- [Option 3: Allow by IP Address](#Option3AllowByIPAddress)
- [Features](#Features)
- [Third-Party Services](#ThirdPartyServices)
- [Let OptiSigns Reach Content Behind Your Firewall](#LetOptiSignsReachContentBehindYourFirewall)
- [What Each Address Is For](#WhatEachAddressIsFor)
- [If Your Screen Is Online but Shows a Black Screen](#IfYourScreenIsOnlineButShowsABlackScreen)
- [Next Steps](#NextSteps)

If your network restricts outgoing traffic, allow the addresses below so your screens can download content and your team can use the OptiSigns portal. Each list is one address per line, so you can copy it and paste it straight into your firewall.

---

<a name="Ports"></a>

## Ports

Allow outgoing traffic on this port:

```
443/TCP (HTTPS and secure WebSocket)
```

OptiSigns doesn't need any incoming ports opened on your network.

|  |
| --- |
| **NOTE** |
| Screens keep a live secure WebSocket connection open to OptiSigns, so they update as soon as you change content. If your firewall inspects or cuts off long-lived HTTPS connections, exclude the OptiSigns addresses from that inspection. |

---

<a name="Option1AllowByDomainRecommended"></a>

## Option 1: Allow by Domain (Recommended)

If your firewall supports wildcard domains, this short list covers OptiSigns screens and the portal:

```
*.optisigns.com
*.optisignsapp.com
*.optisigns-cdn.com
signagecloud-prd.nyc3.cdn.digitaloceanspaces.com
optisigns-download.nyc3.digitaloceanspaces.com
identitytoolkit.googleapis.com
securetoken.googleapis.com
```

Then add the lists under **Features** and **Third-Party Services** for anything you use.

---

<a name="Option2AllowExactDomains"></a>

## Option 2: Allow Exact Domains

If your firewall doesn't support wildcards, allow every address in this list. It covers all screens and the portal:

```
api.optisignsapp.com
api.optisigns.com
api-prod-2.optisigns.com
api-prod-3.optisigns.com
api-prod-4.optisigns.com
api-prod-5.optisigns.com
ws-prod-1.optisigns.com
ws-prod-2.optisigns.com
ws-prod-3.optisigns.com
smallapp.optisigns.com
smallapp-api.prod.optisignsapp.com
analytic-api.optisignsapp.com
signagecloud-prd.nyc3.cdn.digitaloceanspaces.com
cdn.optisigns.com
links.optisigns.com
app.optisigns.com
app1.optisigns.com
static.optisigns.com
prd-api-1.optisigns.com
prd-api-2.optisigns.com
auth.optisigns.com
identitytoolkit.googleapis.com
securetoken.googleapis.com
smallapp-request-apis.optisigns.com
canvas.optisigns.com
canvas-v3.optisigns.com
design.optisigns.com
social-player.optisigns.com
transforge-api.optisigns.com
```

Then add the update list for your player type, below.

<a name="PlayerUpdates"></a>

### Player Updates

Add the list for each type of player you use, so it can download updates.

**Windows, Mac, Linux, Raspberry Pi, BrightSign and LG webOS Signage:**

```
optisigns-download.nyc3.digitaloceanspaces.com
download.optisignsapp.com
```

**OptiStick:**

```
download.optisignsapp.com
links.optisigns.com
```

**ProPlayer:**

```
software-update.optisigns.com
software-download.optisigns.com
download.optisigns-cdn.com
```

---

<a name="Option3AllowByIPAddress"></a>

## Option 3: Allow by IP Address

If your firewall only works with IP addresses, allow this list. It covers the OptiSigns servers that use fixed IP addresses:

```
206.189.255.219
45.55.107.209
143.244.213.107
159.203.156.36
143.244.202.223
146.190.198.241
157.230.201.46
137.184.240.154
167.172.3.79
209.38.62.216
24.199.67.135
138.197.240.53
162.243.189.2
67.199.248.12
67.199.248.13
```

For ProPlayer updates, also add:

```
167.172.2.10
159.65.38.66
138.197.50.84
```

|  |
| --- |
| **IMPORTANT** |
| The portal (app.optisigns.com), your uploaded files and several apps are delivered through content delivery networks (Cloudflare and Amazon CloudFront), whose IP addresses change. An IP list can't cover them. Allow those by domain using Option 1 or 2, or allow Cloudflare's and Amazon CloudFront's published IP ranges. |

---

<a name="Features"></a>

## Features

Add a list only if you use that feature.

**Device management (OptiStick and other managed devices):**

```
mdm-ws-prod-1.optisigns.com
mdm-ws-prod-2.optisigns.com
157.230.203.12
24.199.66.255
```

**YouTube:**

```
yt.optisigns.com
yt1.optisigns.com
```

**Sync Play:**

```
spss-ws.optisigns.com
```

**OptiSound background music:**

```
api.optisound.com
smallapp.optisound.com
134.199.178.26
```

**OptiSigns Engage:**

```
engage-admin.optisigns.com
```

---

<a name="ThirdPartyServices"></a>

## Third-Party Services

OptiSigns uses these services for some features. Add the ones you use.

**File uploads (Transloadit):**

```
*.transloadit.com
s3.amazonaws.com
s3-eu-west-1.amazonaws.com
```

**Remote control (RealVNC):**

```
*.services.vnc.com
services.vnc.com
```

**Free images in the Designer (Unsplash):**

```
plus.unsplash.com
images.unsplash.com
```

**Branding portals (Cloudflare Pages):**

```
scio3-prod-branding.pages.dev
```

**Sports feeds (Sport Pulse):**

```
sportpulse.app
```

**Billing (Stripe):**

```
js.stripe.com
```

**AeriCast:**

```
screenshare.aericast.com
present.aericast.com
apps-api-prd.aericast.com
```

**Note:** Apps that show content from social media and other online services, such as Facebook, Instagram, YouTube and Google Calendar, connect to those services directly. They don't publish a fixed set of addresses, so if you restrict HTTPS by IP address, those apps may not work.

---

<a name="LetOptiSignsReachContentBehindYourFirewall"></a>

## Let OptiSigns Reach Content Behind Your Firewall

Some apps can fetch your content from a fixed OptiSigns IP address. This helps when the content sits behind a firewall or an IP allow-list. When you turn on the **Static IP** option for that content in OptiSigns, we fetch it from this address. Allow it on the server that hosts your content:

```
178.128.134.248
```

The static IP connects over HTTPS on port 443 only.

---

<a name="WhatEachAddressIsFor"></a>

## What Each Address Is For

If your security team needs to know why each address is on the list:

- **api.optisignsapp.com, api.optisigns.com and api-prod-2 to api-prod-5 (206.189.255.219, 45.55.107.209, 143.244.213.107):** the OptiSigns service your screens talk to.
- **ws-prod-1 to ws-prod-3 (159.203.156.36, 143.244.202.223, 146.190.198.241):** the live connection that pushes content changes to your screens.
- **smallapp.optisigns.com and smallapp-api.prod.optisignsapp.com (157.230.201.46):** apps and file downloads.
- **analytic-api.optisignsapp.com (137.184.240.154):** proof-of-play and screen analytics.
- **signagecloud-prd.nyc3.cdn.digitaloceanspaces.com and cdn.optisigns.com:** your uploaded files and shared player files.
- **links.optisigns.com (67.199.248.12, 67.199.248.13):** download, update and share links.
- **app.optisigns.com, app1.optisigns.com (24.199.67.135) and static.optisigns.com:** the OptiSigns portal.
- **prd-api-1 and prd-api-2 (167.172.3.79, 209.38.62.216):** the portal's services.
- **auth.optisigns.com, identitytoolkit.googleapis.com and securetoken.googleapis.com:** logging in.
- **smallapp-request-apis, canvas, canvas-v3, design and social-player:** data sources, the Designer, the AI Designer, social media apps and the audit log.
- **transforge-api.optisigns.com (138.197.240.53):** file uploads.
- **optisigns-download.nyc3.digitaloceanspaces.com (162.243.189.2) and download.optisignsapp.com:** player app updates.
- **software-update, software-download (167.172.2.10, 159.65.38.66, 138.197.50.84) and download.optisigns-cdn.com:** ProPlayer updates.

---

<a name="IfYourScreenIsOnlineButShowsABlackScreen"></a>

## If Your Screen Is Online but Shows a Black Screen

OptiSigns uses a content delivery network (CDN) to get files to your screens quickly. Some firewalls block CDNs. If your screen shows as online but stays black after you assign content, it may not be able to download your files.

First, check that your firewall allows every address in Option 1 or Option 2. If it still doesn't work, contact us at support@optisigns.com and we can turn off the CDN for your account. This requires the Engage plan or above.

---

<a name="NextSteps"></a>

## Next Steps

- [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)
- [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)

If you have questions or feedback, contact our support team at support@optisigns.com.
