# Blazor Circuit

Normal server-sided web application are stateless. After a server gets a requests and sends the rendered page back to the client all state-information (f.e. variables) get wiped out. Cookies, Hidden Fields or URL-Parameters are required to transfer data to the next request.

In Blazor-Projects non of the mentioned techniques are needed because Blazor-Applications are stateful. There is a so-called circuit that stores the states of the components and injected class instances.

Blazor Server -> state is stored in the RAM of the server
Balzor Client -> state is stored in the RAM of the client

***

## Losing the state

- If an instance of a componente no longer belongs to the current view
- when the browser reloads / restarts
- Blazor Server: when the connection is interrupted for a few seconds

A Razor componenet doesn't have to render anything to keep it's state.

***

## Tags

#Programming #CSharp #WEB #Blazor 