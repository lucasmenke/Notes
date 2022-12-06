# Setup Blazor Server Project

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
1. add new Project "Class Library" 
2. delete "Class1.cs"
3. add folder "DataAccess" -> talks to DB
4. add folder "Models" -> contains the backend models

<ins>Setting up Dependencies</ins>
It has to be a one-sided relationship between the projects. A two-sided relationship create a closed circul of dependencies and now project could be build.
1. right-click on Blazor Server Project -> Dependencies -> Add project Reference -> select the Class Library

<ins>Set up Global Usings</ins>
1. create a new class in the projects where you want to have global using
2. f.e. add usings	`global using MongoDB.Bson;`

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
	2. add `using BlazorProjectname;
	4. add `builder.ConfigureServices();` under `var builder = WebApplication.CreateBuilder(args);`
	5. delete obsolete dependency injections
	6. clean Solution

***

## Models

After preparing my new solution I like to start the coding process by adding models.

<ins>Adding Models to Class Library</ins>
1. add "NameModel.cs" to DataAccess -> f.e. "UserModel.cs"
2. remove usings
3. make class public
4. add properties
5. optional: remove `<Nullable>enable</Nullable>` in the project settings of Class Library (double-click on project in the Solution Explorer)

``` C#
namespace ProjectName.Models;

public class TransactionModel
{
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string Id { get; set; }
    public string FromUserId { get; set; }
    public string ToUserId { get; set; }
    public double Amount { get; set; 
	public DateTime DateCreated { get; set; } = DateTime.UtcNow;
}
```

***

## Add DB Connection

<ins>MongoDB</ins>
1. go do MongoDB webside & create a new project
2. create DB: Database > Build a Database > Shared (free) > Create Cluster
3. create User: under Quickstart
4. add IP: under Quickstart
5. get ConnectionString: Database > Connect > Connect your Appliaction > C# / .NET > 2.13 or later 
6. modify appsettings.json: add `"DatabaseName":  "DevProjectName"`
	1. switch databses with this setting -> f.e add production database
7. add ConnectionString to secrets.json
	1. right click on project > Manage User Secrets
	2. add ConnectionString
``` JSON
  "ConnectionStrings": {
    "MongoDB": "mongodb+srv://<ClusterName>:<Password>@<clustername>.esxafcq.mongodb.net/?retryWrites=true&w=majority"
  }
```


***

## Data Access

This folder contains classes that take care of the connection to the database & provides classes to talk to the database.

1. create a class in the Class Library folder "DataAccess" called "DbConnection.cs"
2. create a class for each Model that handles CRUD (create, read, update, delete) requests
3. extract Interfaces out of each class to easily reference them througout the Solution

<ins>For an in depth view how to create classes for MongoDB data access refere to this sample project</ins>
- [Banking Web App](https://github.com/lucasmenke/notes/blob/main/Tutorials/Banking-Web-App.md)

***

## Register Services

Here you want to add the DataAccess Interfaces to the dependency injection

<ins>For an in depth view how to create classes for MongoDB data access refere to this sample project</ins>
- [Banking Web App](https://github.com/lucasmenke/notes/blob/main/Tutorials/Banking-Web-App.md)

***

# Tags

#Programming #WEB #CSharp #Blazor #Razor