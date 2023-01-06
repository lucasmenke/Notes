# Azure AD B2C

Azure Active Directory B2C is a cloud solution for managing an active directory for applications. 50.000 monthly active users are free to use. After that, a Pay-As-You-Go plan manages the pricing.

<br>

## Setting AD up

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
	2. Redirect URI -> for local app developement: https://localhost:{yourAppPortNumber}/signin-oidc