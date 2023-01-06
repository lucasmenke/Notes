# Azure AD B2C with MSAL

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
3. Click on "App registrations" (left menu)
4. Click on newly created registration
5. Click on "Authentication" (left menu)
6. Click on "Add a platform"
7. Click on "Web"
8. Add URL -> https://{TENANT-NAME}.b2clogin.com/{TENANT-NAME}.onmicrosoft.com/oauth2/authresp
9. Scroll to "Implicit grant and hybrid flows"
10. Tick "Access tokens (used for implicit flows)"
11. Tick "ID tokens (used for implicit and hybrid flows)"
12. Scroll to "Advanced settings"
13. Allow public client flows -> Yes
14. Click on "Save"

<ins>Scopes</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "App registrations" (left menu)
4. Click on newly created registration
5. Click on "Expose an API"
6. Click on "Add a scope"
7. Click on "Save and continue"
8. Fill in information
	1. Scope name -> access_as_user
	2. State -> Enabled
9. Click on "Add scope"
10. Value is ClientSecret

<ins>API permissions</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "App registrations" (left menu)
4. Click on newly created registration
5. Click on "API permissions"
6. Click on "Add a permission"
7. Click on "My APIs"
8. Select your API
9. Tick "access_as_user" permission
10. Click on "Add permissions"
11. Click on "Grant admin consent for {Tenant-Name}"
12. Click on "Yes"

<ins>Identity providers</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "Identity providers"
4. Click on provider you want to add
5. Fill in informtion
	1. Name -> Name of provider
	2. Client Id -> I explain it in this document how to get it (Section "Modify Appsettings "-> "Find "ClientId" & "TenantId"value")
	3. Client secret -> explantaion can be found unter Section "Modify Appsettings "-> "Find ClientSecret"
6. Click "Save"

<ins>User flow susi</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "User flows"
4. Click on "New user flow"
5. Click on "Sign up and sign in"
6. Select "Recommended"
7. Fill in information
	1. Name -> social_susi
	2. Identity providers -> Email signup
	3. Social identity providers -> select create ones
	4. Multifactor authentication -> leave defaults as they are
	5. Conditional access -> leave empty
	6. User attributes and token claims -> select the ones you need
8. Click on "Create"

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

<ins>Find "Domain" value</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "App registrations" (left menu)
4. Click on newly created registration
5. Click on "Branding & properties"
6. "Publisher domain" is "Domain"

<ins>Set "Instance"</ins>
1. insert tenant name -> e.g. https://examplename.b2clogin.com/

<ins>Find "ClientId" & "TenantId"value</ins>
1. Search "b2c" in the searchbar on top
2. Click on "App registrations" (left menu)
3. Click on your registration
4. "Application (client) ID" is the ClientId
5. Directory (tenant) ID is the TenantId

<ins>Find "ClientSecret"</ins>
1. Search "b2c" in the searchbar on top
2. Click on "Azure AD B2C"
3. Click on "App registrations" (left menu)
4. Click on newly created registration
5. Click on "Certificates & secrets"
6. Click on "New client secret"
7. Fill in information
8. Click on "Add"
9. Value is ClientSecret

<ins>Find "BaseUrl"</ins>
- you get this after publishing the app to azure
- e.g. https://{publishing-name}.azurewebsites.net
1. In VS right click on project
2. Click on "Publish..."
3. Select "Azure" & click on "Next"
4. Select Service & click on "Next"
5. Click on "Create new"
6. Fill in information
	1. Name will be {publishing-name} in URL
7. Click on "Create"
8. Click "Next"
9. Under "API Management" select "Skip this step"
10. Click next & chose your deployment type
11. Click "Finish"
12. Click "Publish"



