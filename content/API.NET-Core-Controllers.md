
# ASP .NET Core Web API with controller

## Swagger

- visualizes the API
	- displays all the endpoints
	- execute requests to the endpoints
	- displays recived data

***

## Project structure

<ins>Program.cs</ins>
- similar to other ASP.NET-Core project types
``` C#
// creates the application
var builder = WebApplication.CreateBuilder(args);

// dependency injection - adds the controllers from Controller folder
builder.Services.AddControllers();
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

// ability to use authorization
app.UseAuthorization();

// maps the controllers -> routing of the different controllers
app.MapControllers();

// starts the app
app.Run();
```

<ins>Controller folder</ins>
- all controllers are located in this folder
- Add > Controller > API > API Controller with read/write actions is a good template
``` C#
using Microsoft.AspNetCore.Mvc;

namespace EngbersGewinnspieleApi.Controllers
{
    // uses http verbs (get, post...) to identify the controller and doing the routing
    // /api/... is standard route for api´s
    [Route("api/[controller]")]
    [ApiController]
    public class UsersController : ControllerBase
    {
        // GET: api/Users
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/Users/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return $"value {id}";
        }

        // POST api/Users
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/Users/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/Users/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
```

***

## Clean up project

1. delete WeatherForecast.cs
2. delete Controllers/WatherForecastController.cs

***