# Server Side 

- code is getting renderd on the server
- user never sees the 'real' code
	- just html, css & js code is getting send to the user
- if a user ask for a page with specific information the server will build the webpage specificly for this request and sends the user the html, css & js code to render the page
	- this allows fast display times of the page because the user doesn't need to render unnecessary code (provided that the server is fast)
	- the higher the user requests the more workload the server has to handle
- less interactive because new display elements needs to be requested, processed & renders by the server before it can be downloaded by the client + page needs to be refreshed

***Examples:*** C# MVC, PHP, Blazor (server side & client side)