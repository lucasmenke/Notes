# ASP.NET Core Request Pipeline

A Request Pipeline consists of multiple [Middleware Components](https://github.com/lucasmenke/Notes/blob/main/IT/CSharp/Web/Basics/ASP.NET-Core-Middleware.md). Each incoming request goes through that pipeline and the different middleware components inside it befor it reaches the "main" code like f.e. the controller of the web application.

<br>

## Request Pipeline of a MVC / Razor Application

![](https://i.imgur.com/DTj1uci.png)

1. ExceptionHandler: handles exceptions
2. HTTP Strict Transport Security (HSTS): security enhancement middleware that adds a special response header
3. HttpsRedirection: redirect all HTTP requests to HTTPS
4. Static Files: provides support for serving static files and directory browsing
5. Routing: defines and constrains request routes
6. CORS: configures Cross-Origin Resource Sharing -> Request data on one website from another website
7. Authentication: provides authentication support
8. Authorization: provides authorization support

<br>

## Blazor Apps

Blazor apps run outside of the context of the ASP.NET Core pipeline.

<br>

## Tags

#Programming #CSharp #WEB #ASPDOTNET-Core