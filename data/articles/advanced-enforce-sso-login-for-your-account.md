# Advanced: Enforce SSO login for your account

Article URL: https://support.optisigns.com/hc/en-us/articles/360061576673-Advanced-Enforce-SSO-login-for-your-account

Article ID: 360061576673

Locale: en-us

Updated at: 2026-10-19T18:53:23Z

---

### In this article, we'll explain how to enforce SSO logins for your OptiSigns account.

- [Setting Up Basic SSO Enforcement (Microsoft, Facebook, Google)](#BasicSSO)
- [Setting Up SAML SSO Enforcement (MS Entra ID, Okta, OneLogin, Google Workspace)](#SAML)

By default, OptiSigns allows the use of Google, Facebook, or Microsoft accounts to access the OptiSigns portal:

![OptiSigns sign-in page with the Google, Facebook and Microsoft sign-in buttons boxed](https://support.optisigns.com/hc/article_attachments/55875919338515)

However, some organizations have requirements to enforce SSO login for two-factor authentication and password protection purposes. OptiSigns supports this through Microsoft AD and Google GSuite, as well as various SAML options requiring custom branding.

|  |
| --- |
| **NOTE** |
| The ability to enforce SSO on your account requires a [Pro Plus plan subscription or above.](https://www.optisigns.com/pricing) |

---

<a name="BasicSSO"></a>

## Setting Up Basic SSO Enforcement

To set up basic SSO enforcement, go to the **Preferences** page in your OptiSigns portal:

![User menu opened from the avatar at top right, with Preferences highlighted](https://support.optisigns.com/hc/article_attachments/55875903528595)

You'll find the **Enforce Account SSO** option under the "General" section.

![Preferences page, General card, with the Enforce Account SSO field set to None](https://support.optisigns.com/hc/article_attachments/55875903531283)

Clicking on this will display several drop down options:

![Enforce Account SSO list open, showing None, Google GSuite and Microsoft AD](https://support.optisigns.com/hc/article_attachments/55875903531667)

Selecting either option will require any users logging on to OptiSigns to do so with their Google or Microsoft account. If a user tries to log in in any other way, they'll receive this error:

![Sign-up page error saying the organization only allows new accounts through Microsoft log in](https://support.optisigns.com/hc/article_attachments/1500001233801)

For more information, see our guide on [**User Management**](https://support.optisigns.com/hc/en-us/articles/360046356113-Advanced-Security-Managing-User-Roles#AddingorInviting).

**Notes:** You will have to use the official <https://app.optisigns.com/> to log in to enforce SSO. You cannot use a custom domain with Enforce SSO, as the custom domain URL does not have an SSO login.

---

<a name="SAML"></a>

## Setting Up SAML SSO Enforcement (MS Entra ID, Okta, OneLogin, Google Workspace)

Setting up SAML SSO enforcement requires setting up a subdomain, then configuring your settings on your client of choice.

We have numerous articles covering this process, as well as general best practices:

- [**SAML Integration Strategy and Best Practices**](https://support.optisigns.com/hc/en-us/articles/4407128433299-SAML-integration-strategy-best-practice)
- [**Microsoft Entra ID SAML 2.0 SSO Setup**](https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD)
- [**Okta SAML 2.0 SSO Setup**](https://support.optisigns.com/hc/en-us/articles/4404590815635-How-to-set-up-SAML-2-0-with-OptiSigns-and-Okta)
- [**OneLogin SAML 2.0 SSO Setup**](https://support.optisigns.com/hc/en-us/articles/4407386819731-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin)
- [**Google Workspace SAML 2.0 SSO Setup**](https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace)

Please follow one of these guides to set up SSO via SAML.
