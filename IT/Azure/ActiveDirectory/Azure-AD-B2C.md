# Azure AD B2C

Azure Active Directory B2C is a cloud solution for managing an active directory for applications. 50.000 monthly active users are free to use. After that, a Pay-As-You-Go plan manages the pricing.

Microsoft Guide: https://learn.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-tenant

<br>

## Setting up AD

<ins>Register subscription to use AD</ins>
1. Log in to https://azure.microsoft.com
2. Click on "All services" (left menu)
3. Click on "Subscriptions"
4. Click on "Azure subscription 1"
5. Click on "Resource provider" (left menu bottom)
6. Search for "Microsoft.AzureActiveDirectory"
7. Click on "Register"

<ins>Setup AD</ins>
1. Log in to https://azure.microsoft.com
2. Click on "Create resource (left menu)
3. Search for "Azure Active Directory B2C"
4. Click on "Azure Active Directory B2C"
5. Click on "Create"
6. Click on "Create a new Azure AD B2C Tenant"
7. Fill in information
8. Click on "Review + Create"
9. Click on "Create"

<ins>Switch to AD directory</ins>
1. Log in to https://azure.microsoft.com
2. Click on Directory-Logo in the top NavBar (Notebook with filter on it)
3. Click on "Switch" next to your newly created AD 

<ins>Register AD</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "App registrations" (left menu)
4. Click on "new registration" (top menu)
5. Fill in information
	1. Supported Account types (leave the default value ticked)
	2. Redirect URI -> SPA & for local app developement: http://localhost

<ins>Authentication</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "Authentication" (left menu)
4. Click on "Add a platform"
5. Click on "Web"
6. Add URL -> https://{TENANT-NAME}.b2clogin.com/{TENANT-NAME}.onmicrosoft.com/oauth2/authresp
7. Scroll to "Implicit grant and hybrid flows"
8. Tick "Access tokens (used for implicit flows)"
9. Tick "ID tokens (used for implicit and hybrid flows)"
10. Scroll to "Advanced settings"
11. Allow public client flows -> Yes
12. Click on "Save"


<br>

## Modify Appsettings

1. Add following code to appsettings.json
``` Json
{
  "AzureAd": {
    "Instance": "https://{YOUR-TENANT-NAME-HERE}.b2clogin.com/",
    "Domain": "{YOUR-TENANT-NAME-HERE}.onmicrosoft.com",
    "TenantId": "{REPLACE-WITH-YOUR-TENANT-ID}",
    "ClientId": "{REPLACE-WITH-YOUR-CLIENT-ID}",
    "CallbackPath": "/signin-oidc",
    "Scopes": "access_as_user",
    "ClientSecret": "{REPLACE-WITH-YOUR-CLIENT-SECRET}",
    "ClientCertificates": [],
    "SignUpSignInPolicyId": "b2c_1_social_susi"
  },
  "MicrosoftGraph": {
    "BaseUrl": "https://graph.microsoft.com/v1.0",
    "Scopes": "user.read"
  },
  "DownstreamApi": {
    "BaseUrl": "{REPLACE-WITH-YOUR-SECURE-WEB-API-URL}",
    "Scopes": "user.read"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

<ins>Find "ClientId" & "TenantId"value</ins>
1. Search "b2c" in the searchbar on top
2. Click on "App registrations" (left menu)
3. Click on your registration
4. "Application (client) ID" is the ClientId
5. Directory (tenant) ID is the TenantId

<ins>Find "Domain" value</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Overview" (left menu)
3. "Domain name" is Domain value

<ins>Find "Instance" value</ins>
1. Add to value of Domain "https://" at the front & change "onmicrosoft" to b2clogin
	1. e.g. sampledomain.onmicrosoft.com -> https://sampledomain.b2clogin.com

