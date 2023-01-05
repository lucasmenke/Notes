
# Blazor Server Program Flow


1. Pages/Host.cshtml
	1. gets called once for every HTTP-Request via the [HTTP-Request-Pipeline](https://github.com/lucasmenke/Notes/blob/main/IT/CSharp/Web/Basics/ASP.NET-Core-Request-Pipeline.md) after the app.Run()
	2. renders App.razor component which bootstraps Blazor App
2. App.razor
	1. like a bootstrapper for Blazor
	2. after initialization a new [circuit](https://github.com/lucasmenke/Notes/blob/main/IT/CSharp/Web/Blazor/Blazor-Circuit.md) with its own scoped (just for this instance) dependecy injection container (DI Container implements DI automatically when needed) gets created
		1. because of the circuit / scoped instance the Host.cshtml will not be called again until the webpage gets refreshed
3. Index.razor 
	1. gets called because of the routing -> `@page "/"`

<br>

## Tags

#Programming #CSharp #WEB #Blazor 