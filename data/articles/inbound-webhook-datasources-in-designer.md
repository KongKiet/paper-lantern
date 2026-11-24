# Inbound Webhook DataSources in Designer

Article URL: https://support.optisigns.com/hc/en-us/articles/55719322614803-Inbound-Webhook-DataSources-in-Designer

Article ID: 55719322614803

Locale: en-us

Updated at: 2026-11-23T16:23:26Z

---

### In this article, we'll create an Inbound Webhook DataSource in Designer, send data to it from your own app or automation, and show that data on your screens.

- [How It Works and What You'll Need](#HowItWorks)
- [Create an Inbound Webhook DataSource](#CreateAnInboundWebhookDataSource)
- [Send Data to Your Webhook](#SendDataToYourWebhook)
  - [Limits](#Limits)
- [Change or Reopen a Webhook](#ChangeOrReopenAWebhook)
- [Troubleshooting](#Troubleshooting)

Most DataSources in Designer go out and fetch your data on a schedule. An **Inbound Webhook** works the other way round. Your own system sends data to a private URL the moment something happens, and your screens show it within seconds. You don't need a spreadsheet, a polling interval or a manual refresh.

---

<a name="HowItWorks"></a>

## How It Works

When you create an Inbound Webhook DataSource, Designer gives you a private **Webhook URL**. Anything that can send an HTTP `POST` can use it: Zapier, Make, Shopify, a point-of-sale system, or a script you write yourself. Each request carries JSON, and that JSON becomes rows in the DataSource. You show those rows on screen with a Repeater, the same way you would with any other DataSource.

Each Inbound Webhook DataSource runs in one of two display modes, which you choose when you create it:

- **State** - Replace the whole value each time. Every request overwrites what was there before, and nothing expires on its own. Use it for things that have one current value, such as a KPI, a total, a menu, a roster or a scoreboard.
- **Event** - Append each row. Every request adds to the feed, newest first, and every row expires automatically after a set time. Use it for things that happen, such as new orders, alerts, check-ins or a "now serving" number.

|  |
| --- |
| **IMPORTANT** |
| Display mode is fixed once the DataSource exists. To use the other mode, create a new DataSource. |

---

## What You'll Need

- An OptiSigns **Pro Plus,** **Engage**, or **Enterprise** plan. Inbound Webhooks are part of Dynamic Data Mapping. On other plans, the DataSource panel shows "Dynamic Data Mapping is available for Pro Plus & Enterprise plan".
- A design open in [Designer](https://support.optisigns.com/hc/en-us/articles/42087942047379). The steps below are the same in the New Designer.
- A system that can send an HTTP "POST" or "PUT" with a JSON body.

---

<a name="CreateAnInboundWebhookDataSource"></a>

## Create an Inbound Webhook DataSource

In Designer, click **DataSource** in the left-side menu to open the **DataSources** panel, then click **Add DataSource**.

![DataSources panel in Designer with the Add DataSource button highlighted](https://support.optisigns.com/hc/article_attachments/57745029347347)

Under **Nested, JSON format**, click the **Inbound Webhook** card ("Push data in from any app or automation that can POST").

![Add DataSource picker with the Inbound Webhook card under Nested, JSON format highlighted](https://support.optisigns.com/hc/article_attachments/57745051101331)

Enter a **DataSource Name**, then choose **State** or **Event** under **Display mode**. If you chose **Event**, set how the feed behaves:

- **Keep at most** - The most rows the feed keeps, 20 by default and up to 200. When a new row arrives and the feed is full, the oldest row is dropped.
- **Default expire after** - How many minutes a row stays live, 30 by default. This can be anywhere from 1 minute to 24 hours. A single row can override it (see [Set an Expiry on Individual Rows](#SetAnExpiryOnIndividualRows)).

Click **Generate Webhook**.

![Add DataSource form with a name, Event display mode, Keep at most and Default expire after, and Generate Webhook highlighted](https://support.optisigns.com/hc/article_attachments/57745051105171)

Designer creates the DataSource and shows its **Webhook URL (key included)** and its **Key**. Click the copy icon next to the URL and paste it into the system that will send the data. The URL looks like this:

```
https://smallapp.optisigns.com/api/request-apis/dataSourceDatas/<DataSource ID>/webhook?key=<your key>
```

Below the Key, a status line tells you what has arrived so far. It starts as "No delivery yet. Point your sender at the URL above." and, once data comes in, shows the time of the **Last delivery** and whether its rows are still live on screen.

![Webhook URL and Key, blurred, with the URL copy icon highlighted and the Last delivery status line below](https://support.optisigns.com/hc/article_attachments/57745029349651)

|  |
| --- |
| **IMPORTANT** |
| Treat this URL like a password. Anyone who has it can send data to this DataSource. If it leaks, click the regenerate icon next to the **Key** and confirm **Regenerate**. The old link stops working immediately, and your column mapping and existing rows are kept. |

![Regenerate key confirmation dialog warning that the current link stops working, with the Regenerate button highlighted](https://support.optisigns.com/hc/article_attachments/57745029350291)

### Detect Your Payload

Designer needs to know which fields your data contains before you can place them on the canvas. Under **Detect Payload (Optional)**, either click **Listen for a delivery** and send one real request from your system, or click **Paste sample JSON**, paste an example of your payload, and click **Detect columns**. If you send a list of rows, Designer reads the fields from every row in it.

Designer lists what it found under **Detected fields (example values)**. You can run either option again later (**Listen again to add fields** or **Re-detect columns**) to pick up new fields. New fields are added to the ones Designer already knows, so your existing mapping stays in place.

![Detect Payload with sample JSON pasted, Re-detect columns highlighted, and the detected fields order, customer and status](https://support.optisigns.com/hc/article_attachments/57745051110035)

Click **Save** to finish.

### Put the Data on Your Design

Drag a field from the DataSource card onto the canvas. Designer asks "Would you like to use this data in a Repeater or on its own?" Click **Use in a Repeater** so the design shows one item per row. **Use on its own** places a single value instead.

![Dialog asking whether to use the dragged field in a Repeater or on its own, with Use in a Repeater highlighted](https://support.optisigns.com/hc/article_attachments/57745051111699)

Save the design and push it to your screens. For more on laying out repeated data, see [How to Set Up Dynamic Data Mapping with OptiSync](https://support.optisigns.com/hc/en-us/articles/29217646663187).

---

<a name="SendDataToYourWebhook"></a>

## Send Data to Your Webhook

Send JSON to your Webhook URL with the `Content-Type: application/json` header. A screen picks up a change within about 20 seconds. A successful request returns `{"status":"success","message":"OK"}`.

### What POST and PUT Do

What each request does depends on the display mode:

- **Event mode**
  - **POST** - Adds one row. Send a list (a JSON array) to add several rows at once.
  - **PUT** - Replaces every row with the rows you send. Send the rows as a list, even when there is only one: `[{"order": "1042"}]`. A single object without the brackets is rejected.
  - **PUT with an empty body** - Removes every row. Send `{}`, `[]` or `{"data": []}`.
- **State mode**
  - **POST** or **PUT** - Either one replaces the current values. Any field you leave out is cleared, and an empty body (`{}`) clears everything.

For example, this request adds one order to an Event feed:

```
curl -X POST "https://smallapp.optisigns.com/api/request-apis/dataSourceDatas/<DataSource ID>/webhook?key=<your key>" \
  -H "Content-Type: application/json" \
  -d '{"order": "1042", "customer": "Sam", "status": "Ready"}'
```

To add several rows in one request, send a JSON array:

```
[
  {"order": "1042", "status": "Ready"},
  {"order": "1043", "status": "Preparing"}
]
```

To replace every row with `PUT`, send an array like the one above, or wrap it as `{"data": [ ... ]}`.

|  |
| --- |
| **NOTE** |
| With `POST`, a body shaped `{"data": [ ... ]}` is treated as one row with a field called `data`. To send several rows with `POST`, send a plain array. |

<a name="SetAnExpiryOnIndividualRows"></a>

### Set an Expiry on Individual Rows

In Event mode, each row expires after the DataSource's **Default expire after** time. To give one row its own lifetime, add `__opti_ttl` with a number of seconds:

```
{"alert": "Lane 3 closed", "__opti_ttl": 300}
```

This row expires after 5 minutes, whatever the default is. If your sender can't add a field to the body, add ?ttl=300 to the URL instead, and it applies to every row in that request. A \_\_opti\_ttl in the body wins over ?ttl=. Either way, the shortest expiry is 60 seconds and the longest is 24 hours, and \_\_opti\_ttl isn't stored as a column.

Expired rows stop showing on your screens straight away. In Designer, they stay on the DataSource card, marked **(expired)**, until the next request arrives and clears them out. To check which rows are live, open the DataSource's **⋮** menu and click **Edit Data**. The **Status** column shows **Live** or **Expired** for each row. This view is read-only, because the data comes from your sender.

![Edit Data grid for a webhook DataSource with a Status column showing one Expired row and one Live row](https://support.optisigns.com/hc/article_attachments/57745051112083)

When a feed has no live rows left, your screens follow the DataSource's **Empty Data Handling** setting.

|  |
| --- |
| **TIP** |
| Avoid starting your own field names with \_\_opti\_. That prefix is reserved for OptiSigns, so fields that use it are not shown in Designer. |

### Send the Key in a Header

The URL Designer gives you carries the key in the query string (?key=...). If your sender lets you set custom headers, you can remove ?key=... from the URL and send the key in an X-Webhook-Key header instead. Web servers and tools often log full URLs, so keeping the key out of the URL means it won't end up in those logs.

```
curl -X POST "https://smallapp.optisigns.com/api/request-apis/dataSourceDatas/<DataSource ID>/webhook" \
  -H "X-Webhook-Key: <your key>" \
  -H "Content-Type: application/json" \
  -d '{"order": "1042", "status": "Ready"}'
```

<a name="Limits"></a>

### Limits

Your webhook checks every request against these limits:

- **Rows** - A feed holds up to 200 rows, or fewer if you set a lower **Keep at most**.
- **Request size in Event mode**
  - **One row** - Up to 64 KB per request.
  - **A list of rows, or any PUT** - Up to 256 KB per request, with each row still up to 64 KB.
- **Request size in State mode** - Up to 256 KB per request.
- **Rate** - Up to 120 requests per minute for each webhook.

In Designer, hover over the **ⓘ** next to **Keep at most** or **Webhook URL (key included)** to see the row and list limits for your DataSource. The 64 KB row limit isn't shown there.

For scale, a typical e-commerce order notification is 10 to 40 KB, so one order fits comfortably in a single row.

A request over a limit is rejected as a whole, and nothing from it is saved. Rows are never cut off partway.

|  |
| --- |
| **IMPORTANT** |
| A payload that passes **Detect columns** or **Listen for a delivery** can still be too large to deliver. Check your real payload size against the limits above, especially for large records such as full e-commerce orders. |

---

<a name="ChangeOrReopenAWebhook"></a>

## Change or Reopen a Webhook

To see your Webhook URL again, rename the DataSource, or change its Event settings, open the **DataSources** panel and click your DataSource to open its card. Click the **⋮** menu on the card and click **Edit Settings**. The **Edit DataSource** dialog opens with the same fields you set up, plus the URL, the Key and the latest delivery.

![Inbound Webhook DataSource card with its menu open and Edit Settings highlighted](https://support.optisigns.com/hc/article_attachments/57745051113875)

---

<a name="Troubleshooting"></a>

## Troubleshooting

Here are a few of the more common issues our customers may face when using Inbound Webhook DataSources, and how to solve them.

#### My System Got a Success Response, but Nothing Changed in Designer

Designer doesn't refresh its view of a DataSource on its own. Open the DataSource's **⋮** menu and click **Refresh data (in Design Mode only)**, or reload the page. Your screens update on their own.

#### The DataSource Says "This Feed Is Empty"

The full message is "This feed is empty. Send a POST to this webhook URL to fill it." Nothing has arrived yet, or the feed was cleared by a `PUT` with an empty body. Check that your sender is using the current Webhook URL from **Edit Settings**.

#### Rows Are Listed in Designer but Don't Show on the Screen

The rows have expired. Check **Default expire after** and any `__opti_ttl` or `?ttl=` values you send. If a value like a menu or a KPI keeps disappearing, it was probably built in Event mode, where every row expires by design. Create a new DataSource in **State** mode for it.

#### I See Duplicate Rows

When a sender retries a `POST`, each retry adds a row. To prevent duplicates, send a unique `X-Request-Id` header with each request; a retry with the same ID is answered "OK (duplicate ignored)" and adds nothing. Shopify webhooks are recognized automatically by their `X-Shopify-Webhook-Id` header.

#### My Sender Gets an Error

The status code and the message in the response tell you why:

- **401 Unauthorized** - The key is wrong, or it was regenerated. Copy the current URL from **Edit Settings**.
- **404 Not found** - The DataSource ID in the URL is wrong, or the DataSource was deleted.
- **413 Payload too large** - The request is over the size limit for its type. See [Limits](#Limits).
- **429 Too many requests** - You sent more than 120 requests in a minute. Slow down, or send several rows in one request instead.
- **400** - The body isn't valid JSON or isn't a shape the webhook accepts (for example, a `PUT` with a single object instead of a list), it has more rows than the feed can hold, or one row is over 64 KB. The message says which.
- **503 Inbound Webhook is temporarily disabled** - The service is paused on our side. Try again later, and contact support if it continues.

---

## Related Articles

- [Widgets in Designer](https://support.optisigns.com/hc/en-us/articles/42436941395475)
- [How to Set Up Dynamic Data Mapping with OptiSync](https://support.optisigns.com/hc/en-us/articles/29217646663187)
- [How to Add Google Sheets as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29838866920211)
