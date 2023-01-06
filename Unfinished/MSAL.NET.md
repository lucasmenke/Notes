# Microsoft Authentication Library

MSAL.NET is the .NET client library for the Microsoft Authentication Library (MSAL). MSAL is a unified library that helps you to develop applications that work with Microsoft identities, including personal, work, or school accounts. MSAL allows you to obtain tokens from the Microsoft identity platform in order to access secure API endpoints.

## Example

In this note I will explain how to create an API that can only be accessed by logged in users. The active directory will be handled via Azure AD B2C.

<ins>ASP.NET Core Web API</ins>
1. Create "ASP.NET Core Web API" project
2. Add following nuget packages
	1. Microsoft.AspNetCore.Authentication.JwtBearer
	2. Microsoft.Identity.Web
	3. Microsoft.Identity.Web.MicrosoftGraph
	4. Microsoft.Identity.Web.UI
3. configure dependency injection ([example]())
4. add Authorize attribute to API controller ([example]())
5. extend appsettings.json (explained [here](https://github.com/lucasmenke/Notes/blob/main/IT/Azure/ActiveDirectory/Azure-AD-B2C.md) under the section "Modify Appsettings")

<ins>Setup Azure AD B2C</ins>
- Guide [here](https://github.com/lucasmenke/Notes/blob/main/IT/Azure/ActiveDirectory/Azure-AD-B2C.md)

<ins>Blazor Server App</ins>
1. Create "ASP.NET Core Web API" project in the same solution
	1. Authentication type -> None
2. Add following nuget packages
	1. Microsoft.Identity.Client
3. Add classes for reading appsettings.json
	1. Settings.cs ([example]())
	2. NestedSettings.cs ([example]())
	3. Extension.cs ([example]())
4. Create folder "MsalClient" & add Interface and classes
	1. IPCAWrapper.cs ([example]())
	2. PCAWrapper.cs ([example]())
	3. PlatformConfig.cs ([example]())
5. Modify "Program.cs"
	1. inject IPCAWrapper ([example]())
6. modify 