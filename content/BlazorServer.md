# Blazor Server (Server Side)

- code gets renderd on the server side
- client side is connected to a server in a way where only the changes will be recived by the server (small exchange of information not whole html, css & js code)
- for the user it appears the same way as they were using client side rendering
- downside is that it needs a connection

***

## Prepare project

<ins>I prefere to set up 2 projects under one solution. </ins>
1. Project: Blazor Server -> UI
2. Project: Class Library -> Data Access

<ins>After that I clean up my Blazor Server App</ins>
1. remove Pages/FetchData.razor
2. remove Pages/Counter.razor
3. remove Shared/SurveyPrompt.razor
	1. remove Pages/Index.razor <SurveyPrompt />
4. remove Shared/NavMenu.razor
5. remove following from Shared/MainLayout.razor
	1. `<div class="sidebar><NavMenu /></div>"`
	2. remove "About" div
6. remove following from Program.cs
	1. `builder.Services.AddSinlgeton<WeatherForecastService>();`
	2. `using ProjectName.Data;`
7. remove Data Folder

<ins>New folders added to Balzor Server Projekt</ins>
1. add folder "Components" -> contains Razor components
2. add folder "Models" -> holds UI models

<ins>Now the class library can be set up</ins>
1. add folder "DataAccess" -> talks to DB
2. add folder "Models" -> contains the backend models

<ins>Setting up Dependencies</ins>
It has to be a one-sided relationship between the projects. A two-sided relationship create a closed circul of dependencies and now project could be build.
1. right-click on Blazor Server Project -> Dependencies -> Add project Reference -> select the Class Library

<ins>Set up Global Usings</ins>
1. create a new class in the projects where you want to have global using
2. add usings	`global using MongoDB.Bson;`

<ins>Outsource dependency injection to a seperate class</ins>
1. add new class to the Blazor Server Project called "RegisterServices"
2. add following code
```C#
public static class RegisterServices
{
    // extension methode for the WebApplicationBuilder
    public static void ConfigureServices(this WebApplicationBuilder builder)
    {
        builder.Services.AddRazorPages();
        builder.Services.AddServerSideBlazor();
    }
}
```
3. change the Program.cs
	1. cut out the dependency injection
	2. add `using BlazorProjectname;`
	3. add `builder.ConfigureServices();` under `var builder = WebApplication.CreateBuilder(args);`
	4. clean Solution
