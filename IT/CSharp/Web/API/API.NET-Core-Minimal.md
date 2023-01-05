# ASP .NET Core Web API Minimal

## Create Project

ASP.NET Core Web API > Uncheck Box: Use controllers

<br>

## Project Structure

Their is no Controller folder like in a "normal" ASP .NET Core Web API. This allows a minimal and clear project structure for small API´s.

<ins>Programm.cs</ins>
- endpoints are located here
``` C#
// creates the application
var builder = WebApplication.CreateBuilder(args);

// dependency injection - swagger
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// builds the application
var app = builder.Build();

// if we are in the development environment swagger will be activated
// environmente can be changed under Properties/launchSettings.json
// json ApiDemo and IIS Express -> "ASPNETCORE_ENVIRONMENT": "Development"
// launchSettings.json is only localy, when publishing the API it will automatically switch to production environmente
// remove if-statement if swagger should be in production
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// redirects from http to https
app.UseHttpsRedirection();

// creates an endpoint (get) that returns Hello World
// can also execute a methode -> don´t put it in this class
app.MapGet("api/helloWorld", () => "Hello World");

// starts the app
app.Run();
```

<br>

## Tags

#Programming #CSharp #WEB #API