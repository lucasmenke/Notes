# ASP .NET Core Web API Minimal

## Swagger

- visualizes the API
	- displays all the endpoints
	- execute requests to the endpoints
	- displays recived data

***

## Project structure

Their is no Controller folder like in a "normal" ASP .NET Core Web API. The endpoints are located in the Programm.cs

<ins>Programm.cs</ins>
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
// can also execute a function
app.MapGet("api/helloWorld", () => "Hello World");

// starts the app
app.Run();
```