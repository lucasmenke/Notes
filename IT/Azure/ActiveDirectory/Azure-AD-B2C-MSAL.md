# Azure AD B2C with MSAL

Azure Active Directory B2C is a cloud solution for managing an active directory for applications. 50.000 monthly active users are free to use. After that, a Pay-As-You-Go plan manages the pricing.

Microsoft Guide: https://learn.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-tenant

<br>

## Setting up AD

<ins>Register subscription to use AD</ins>
1. Log in to https://portal.azure.com/#home
2. Click on "All services" (left menu)
3. Click on "Subscriptions"
4. Click on your subscription you want to use for the AD (default "Azure subscription 1")
5. Click on "Resource provider" (left menu near the bottom)
6. Search for "Microsoft.AzureActiveDirectory"
7. Click on "Register"

<ins>Setup AD</ins>
1. Log in to https://portal.azure.com/#home
2. Click on "Create resource (left menu)
3. Search for "Azure Active Directory B2C"
4. Click on "Azure Active Directory B2C"
5. Click on "Create"
6. Click on "Create a new Azure AD B2C Tenant"
7. Fill in information
8. Click on "Review + Create"
9. Click on "Create"

<ins>Switch to AD directory</ins>
1. Log in to https://portal.azure.com/#home
2. Click on Directory-Logo in the top NavBar (Notebook with filter on it)
3. Click on "Switch" next to your newly created AD directory 

<ins>Register AD</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "App registrations" (left menu)
4. Click on "new registration" (top menu)
5. Fill in information
	1. Supported Account types  -> leave the default value ticked (Accounts in any identity provider or organizational directory (for authenticating users with user flows))
	2. Redirect URI -> Platform: Web & for local app developement: https://localhost:{Project-Port-Number}/signin-oidc (e.g. https://localhost:7297/signin-oidc)
	3. Permissions -> Tick "Grant admin consent to openid and offline_access permissions"

<ins>Authentication</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "App registrations" (left menu)
4. Click on newly created registration
5. Click on "Authentication" (left menu)
6. Scroll to "Implicit grant and hybrid flows"
7. Tick "Access tokens (used for implicit flows)"
8. Tick "ID tokens (used for implicit and hybrid flows)"
9. Click on "Save"

<ins>User flows</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "User flows"
4. Click on "New user flow"
5. Click on "Sign up and sign in"
6. Select "Recommended"
7. Fill in information
	1. Name -> susi
	2. Identity providers -> Email signup
	3. Multifactor authentication -> leave defaults as they are (Phone/SMS cost extra money)
	4. Conditional access -> leave empty
	5. User attributes and token claims -> select the ones you need
		1. **TIPP: JobTitle only as Return Claim can be used to identify admins**
8. Click on "Create"
9. Create additional user flows as needed
	1. Name: "reset" for password reset & "edit" for Profile editing

<ins>Test User flow susi</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "User flows"
4. Select susi user flow
5. Click on "Run user flow"
9. Click "Run user flow" -> if everything is ok, a signup page will show up

<br>

## Setup .NET Projekt

<ins>appsettings.json</ins>
1. Add following code to appsettings.json
``` Json
{
  "AzureAdB2C": {
    "Instance": "https://{TENANT-NAME}.b2clogin.com/",
    "ClientId": "<in the secrets.json>",
    "CallbackPath": "/signin-oidc",
    "Domain": "{TENANT-NAME}.onmicrosoft.com",
    "SignUpSignInPolicyId": "B2C_1_susi",
    "ResetPasswordPolicyId": "B2C_1_reset",
    "EditProfilePolicyId": "B2C_1_edit"
  }
}
```

<ins>Find "ClientId"</ins>
1. Search "b2c" in the searchbar on top
2. Click on "App registrations" (left menu)
3. Click on your registration
4. "Application (client) ID" is the ClientId
5. Directory (tenant) ID is the TenantId



