# Blazor Web Assembly
 Running C# code client sided in the browser
## Folder Structure
 - Connected Services
	 - here goes the connection f.e. with an api or a database
 - Dependencies
	 - package like nuget
 - Properties
	 - launchSettings.json
 - wwwroot
	 - css 
	 - index.html > header & body (loads app) of website + js that downlods boot resources from the server
	 ```<script src="_framework/blazor.webassembly.js"></script>```
		 -  JavaScript code to bootstrap the app
		-  .NET runtime and assemblies
		-   Locale specific data
 - Pages
	 - all Razor app-page components (whole-page)
 - Shared
	 - Shared html snippets like the layout or navbar
	 - non-page Razor components
 - _Imports.razor
	 - all needed packages are imported here f.e. ```@using System.Net.Http```
 - App.razor
	 -	Router (enables to navigate to a specific route of / page)
 - Program.cs
	 - entry point of code
	 - rough order 
		 1. Program.cs: ```builder.RootComponents.Add<App>("#app");```
		 2. App.razor: ```<RouteView RouteData="@routeData" DefaultLayout="@typeof(MainLayout)" />```
		 3. Shared/MainLayout.razor:  html snippet (deault is sidebar & main section)
		 4. wwwroot/index.html: ```<script src="_framework/blazor.webassembly.js"></script>```
# Routing
 - route can be defined on top of the page with
`@page "/your-route"`
# API
 - normaly API's get called to fetch data

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ4MjE2NDQ2N119
-->