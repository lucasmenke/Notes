
# Blazor Program Flow


1. Pages/Host.cshtml
	1. gets always called when a new requests (f.e. for a new page) comes in
	2. renders App.razor component
2. App.razor
	1. like a bootstrapper for Blazor

***

## HttpContext

Basically the HttpContext encapsulates all HTTP-specific information about an individual HTTP request. 

Blazor Server Apps life in server memory. For each new session Blazor constructs a new [circuit](https://github.com/lucasmenke/notes/blob/main/Content/Blazor-Circuit.md).
Each circuit gets its own scoped dependecy injection container (DI Container implements DI automatically when needed).

***



***

## Tags

#Programming #CSharp #WEB #Blazor 