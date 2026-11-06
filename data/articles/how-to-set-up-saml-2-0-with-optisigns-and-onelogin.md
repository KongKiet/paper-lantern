# How to Set Up SAML 2.0 with OptiSigns and OneLogin

Article URL: https://support.optisigns.com/hc/en-us/articles/4407386819731-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-OneLogin

Article ID: 4407386819731

Locale: en-us

Updated at: 2026-11-05T16:05:04Z

---

### In this article, we'll show how to sign your team in to OptiSigns with OneLogin over SAML 2.0, using either OneLogin's standard SAML connector or its Shibboleth connector, and how to map OneLogin groups to OptiSigns roles and teams.

- [What You'll Need](#WhatYoullNeed)
- [Set Up Your Domain in OptiSigns](#SetUpYourDomainInOptiSigns)
- [Turn On SAML Single Sign On](#TurnOnSAMLSingleSignOn)
- [Add OptiSigns as an App in OneLogin](#AddOptiSignsAsAnAppInOneLogin)
- [Finish the Setup in OptiSigns](#FinishTheSetupInOptiSigns)
- [Map OneLogin Groups to OptiSigns Roles and Teams](#MapOneLoginGroupsToOptiSignsRolesAndTeams)
- [Send Names and Groups from OneLogin](#SendNamesAndGroupsFromOneLogin)
- [Using the Shibboleth Connector](#UsingTheShibbolethConnector)
- [Sign In with SAML](#SignInWithSAML)
- [Troubleshooting](#Troubleshooting)

Let your team sign in to OptiSigns with their OneLogin accounts. OneLogin acts as the Identity Provider (IdP) and OptiSigns as the Service Provider (SP).

SAML Single Sign On is available on the Pro Plus and Enterprise plans.

---

<a name="WhatYoullNeed"></a>

## What You'll Need

- An OptiSigns account on the Pro Plus or Enterprise plan, signed in as the account Owner or an Admin
- Admin access to your OneLogin portal
- A subdomain or custom domain for your OptiSigns portal (set up below)

---

<a name="SetUpYourDomainInOptiSigns"></a>

## Set Up Your Domain in OptiSigns

SAML needs your own sign-in address, such as `yourcompany.optisigns.net`. This is the URL you share with your users once the integration is set up.

Click your profile icon in the top-right corner of the portal and select **Branding** (**Branding Settings** in the settings menu, [app.optisigns.com/app/s/branding-settings](https://app.optisigns.com/app/s/branding-settings)). Type a name in the **Subdomain** field and click **Activate**.

![Branding settings with the Subdomain field highlighted next to its Activate button](https://support.optisigns.com/hc/article_attachments/57179103611027)

You can also map your own domain, such as `digitalsigns.yourcompany.com`, under **Your domain**. See [Advanced: Custom Domain Mapping](https://support.optisigns.com/hc/en-us/articles/1500000480302).

---

<a name="TurnOnSAMLSingleSignOn"></a>

## Turn On SAML Single Sign On

Click your profile icon in the top-right corner and select **SAML Single Sign On** ([app.optisigns.com/app/s/saml-settings](https://app.optisigns.com/app/s/saml-settings)) and turn on **Enable SAML**.

|  |
| --- |
| **NOTE** |
| Until your domain is set up, the page shows "Please set up your domain in Branding Settings before configuring SAML SSO." and the **Enable SAML** switch stays greyed out. |

![SAML Single Sign On page with the notice asking you to set up your domain first, above the Enable SAML switch](https://support.optisigns.com/hc/article_attachments/57179082921619)

Once SAML is on, the **Settings** section shows these switches. Hover the info icon next to each one for a reminder of what it does.

- **Enable Username & Password login** - Lets users also sign in with a username and password. Turn it off once the integration works, but keep at least one Owner or Admin account that can sign in with a password, so you can always get back in at app.optisigns.com to fix the setup.
- **Enable User Creation** - Creates an OptiSigns user the first time someone signs in through SAML. Leave it on unless you want to review each user's role before they can use OptiSigns.
- **Enable User Override** - Updates the user's role and team each time they sign in, if their group in OneLogin has changed.

Under **Configure Identity Provider**, note the **Single Sign On URL** and the **Audience URI (SP Entity ID)**. You'll paste them into OneLogin next.

---

<a name="AddOptiSignsAsAnAppInOneLogin"></a>

## Add OptiSigns as an App in OneLogin

Sign in to your OneLogin portal as an admin, go to **Applications** and click **Add App**.

![OneLogin Applications page with the Applications menu and the Add App button highlighted](https://support.optisigns.com/hc/article_attachments/57179103616915)

Search for **SAML** and select **SAML Custom Connector (Advanced)**. To use Shibboleth instead, see [Using the Shibboleth Connector](#UsingTheShibbolethConnector).

![OneLogin Find Applications search for SAML with SAML Custom Connector (Advanced) highlighted](https://support.optisigns.com/hc/article_attachments/57179082926483)

Enter **OptiSigns** as the **Display Name** and click **Save**. You can also upload the OptiSigns logo here.

![OneLogin Add SAML Custom Connector page with OptiSigns as the display name and the Save button highlighted](https://support.optisigns.com/hc/article_attachments/57179082930323)

After saving, open the **Configuration** page and fill in the values from your OptiSigns SAML Single Sign On page:

- **Audience (EntityID)** and **Login URL** - The **Audience URI (SP Entity ID)** from OptiSigns.
- **Recipient**, **ACS (Consumer) URL Validator** and **ACS (Consumer) URL** - The **Single Sign On URL** from OptiSigns.
- **SAML initiator** - Set to **Service Provider**.

![OneLogin Configuration page with arrows on the Audience, Recipient, ACS URL, Login URL and SAML initiator fields](https://support.optisigns.com/hc/article_attachments/57179082932243)

Then open the **SSO** page. Copy the **Issuer URL** and the **SAML 2.0 Endpoint (HTTP)**, then click **View Details** under **X.509 Certificate** to see the certificate's content.

![OneLogin SSO page with arrows on View Details, the Issuer URL and the SAML 2.0 Endpoint](https://support.optisigns.com/hc/article_attachments/57179103628179)

---

<a name="FinishTheSetupInOptiSigns"></a>

## Finish the Setup in OptiSigns

Back on the OptiSigns SAML Single Sign On page, fill in **Setup SAML Authentication**:

- **SAML 2.0 Endpoint (HTTP)** - The **SAML 2.0 Endpoint (HTTP)** from OneLogin.
- **Identity Provider Issuer** - The **Issuer URL** from OneLogin.
- **Public Certificate** - The whole X.509 certificate from OneLogin.
- **Sign In Button label** - Optional. The text on the sign-in button of your login page.

![OptiSigns Setup SAML Authentication fields for the SAML 2.0 endpoint, issuer and public certificate](https://support.optisigns.com/hc/article_attachments/57179103630483)

Click **Save**. Your sign-in page and the integration are now set up.

---

<a name="MapOneLoginGroupsToOptiSignsRolesAndTeams"></a>

## Map OneLogin Groups to OptiSigns Roles and Teams

Mapping is optional, but recommended: it gives each user the right role and team automatically.

|  |
| --- |
| **IMPORTANT** |
| If you don't set up a mapping, every user who signs in through SAML gets the User role in the Default Team. |

On the SAML Single Sign On page, scroll to **Advanced Settings**. Under **Group Mapping**, click **Add** and enter a **Group Name** from OneLogin, then choose the OptiSigns **Role** and **Team** for it.

![Group Mapping with group names mapped to an OptiSigns role and team](https://support.optisigns.com/hc/article_attachments/57179103634323)

It's good practice to create OneLogin groups just for OptiSigns, with an `optisigns-` prefix:

- **optisigns-admins** - Mapped to the Admin role.
- **optisigns-users** - Mapped to the User role.
- **optisigns-custom-role** - Mapped to a custom role you've created.

The first row, **\*Unmapped users/groups\***, decides what happens to users whose group isn't mapped. Set its **Team** to **No Team (Disable)** and those users get an error when they try to sign in and have to ask an admin for access. This is a useful safeguard if someone is given the OptiSigns app in OneLogin without the right group.

![Unmapped users/groups row with No Team (Disable) selected as the team](https://support.optisigns.com/hc/article_attachments/57179082951699)

|  |
| --- |
| **NOTE** |
| If you map a group to a team and later delete that team, new users from that group get No Team and must ask you to assign one. |

---

<a name="SendNamesAndGroupsFromOneLogin"></a>

## Send Names and Groups from OneLogin

In OneLogin, open the **Parameters** page of the OptiSigns app. Click **+** to add a custom parameter for each value OptiSigns reads: first name, last name and groups. Name each parameter the same as the attribute OptiSigns expects, and set its value to the matching OneLogin field.

![OneLogin Parameters page with the add parameter button and the firstName, groups and lastName parameters](https://support.optisigns.com/hc/article_attachments/57179082953235)

OptiSigns reads the attributes named in **Advanced Settings**: **First Name SAML Attribute**, **Last Name SAML Attribute** and **Groups SAML Attribute**. They default to `firstName`, `lastName` and `groups`. If your OneLogin parameters use other names, change these fields to match instead.

![OptiSigns Advanced Settings with the first name, last name and groups SAML attribute fields](https://support.optisigns.com/hc/article_attachments/57179103649555)

---

<a name="UsingTheShibbolethConnector"></a>

## Using the Shibboleth Connector

Shibboleth is based on SAML, so the setup is the same as above with these differences.

When you add the app in OneLogin, select **SAML Custom Connector (SP Shibboleth)**.

![OneLogin Find Applications search with SAML Custom Connector (SP Shibboleth) highlighted](https://support.optisigns.com/hc/article_attachments/57179103656211)

On the **Configuration** page:

- **Login URL** - The **Audience URI (SP Entity ID)** from OptiSigns.
- **ACS (Consumer) URL** and **ACS (Consumer) URL Validator** - The **Single Sign On URL** from OptiSigns. The validator is a regular expression, so escape the special characters in the URL, for example `https:\/\/`.

![OneLogin Shibboleth Configuration page with the Login URL, ACS URL and ACS URL Validator fields highlighted](https://support.optisigns.com/hc/article_attachments/57179103658387)

The **SSO** page has the same **Issuer URL**, **SAML 2.0 Endpoint (HTTP)** and certificate to copy into OptiSigns.

![OneLogin Shibboleth SSO page with the certificate View Details link, Issuer URL and SAML 2.0 Endpoint highlighted](https://support.optisigns.com/hc/article_attachments/57179082965523)

Shibboleth comes with predefined standard attributes on the **Parameters** page. `givenName` carries the first name and `surname` the last name.

![OneLogin Shibboleth Parameters page listing standard attributes such as givenName, groups and surname](https://support.optisigns.com/hc/article_attachments/57179082968211)

Shibboleth sends these attributes by their standard ids, so enter the ids in OptiSigns **Advanced Settings**:

- **First Name SAML Attribute** - `urn:oid:2.5.4.42` (givenName)
- **Last Name SAML Attribute** - `urn:oid:2.5.4.4` (surname)

![OptiSigns Advanced Settings with urn:oid:2.5.4.42 and urn:oid:2.5.4.4 entered as the first and last name attributes](https://support.optisigns.com/hc/article_attachments/57179082970643)

---

<a name="SignInWithSAML"></a>

## Sign In with SAML

Your users can now sign in at your subdomain, for example `https://yourcompany.optisigns.net/signIn`, with their OneLogin credentials. Share that URL with them.

---

<a name="Troubleshooting"></a>

## Troubleshooting

Here are some common potential issues you may run into when attempting to set up a SAML configuration, and how to solve them.

#### "Please set up your domain in Branding Settings before configuring SAML SSO."

SAML needs a subdomain or custom domain. See [Set Up Your Domain in OptiSigns](#SetUpYourDomainInOptiSigns).

#### A user gets an error when signing in

Their OneLogin group isn't mapped and **\*Unmapped users/groups\*** is set to **No Team (Disable)**, or their group is mapped to a team that has been deleted. Add their group to **Group Mapping**, or assign them a team.

#### Every user signs in with the User role in the Default Team

No group mapping matches. Check that the group names in **Group Mapping** match OneLogin exactly, and that the **Groups SAML Attribute** matches the parameter name in OneLogin. See [Map OneLogin Groups to OptiSigns Roles and Teams](#MapOneLoginGroupsToOptiSignsRolesAndTeams).

#### Users' names are blank in OptiSigns

The name attributes don't match. See [Send Names and Groups from OneLogin](#SendNamesAndGroupsFromOneLogin), or for Shibboleth use the `urn:oid` ids in [Using the Shibboleth Connector](#UsingTheShibbolethConnector).
