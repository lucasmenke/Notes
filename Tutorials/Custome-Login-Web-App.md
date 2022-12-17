# Custome Authentication & Authorization with JSON Web Tokens (JWT), Refresh Tokens & Roles

In this project I will create a page for user to create an account and save them in a database using hash & salt. Furthermore registerd users are able to log back in. In addition to that I will use JWT & Refresh Tokens. A registerd user can get a role and based on this role the user will be able to call specific API endpoints.

<br>

## Tech Stack

- ASP.NET Core Web API (.NET 6)
	- Authentication Type -> None
- Class Library (.NET 6)
- Sqlite

<br>

## Project Structure

1. Blazor Client
2. ASP.NET Core Web API
	1. Models / DTO
	2. Services
3. Class Library 
	1. Business Logic Layer
4. Class Library 
	1. Data Access Layer

<br>

## Extensions

<ins>ASP.NET Core Web API</ins>
- Microsoft.EntitiyFrameworkCore
- Microsoft.EntitiyFrameworkCore.Design
- Microsoft.EntitiyFrameworkCore.Sqlite

<ins>DAL</ins>
- Microsoft.EntitiyFrameworkCore
- Microsoft.EntitiyFrameworkCore.Design
- Microsoft.EntitiyFrameworkCore.Sqlite
- Microsoft.Extensions.Configuration.Abstraction

<br>

## Data Structure

- User
	- Id
		- int
	- Username
		- string
	- PasswordHash 
		- byte[]
	- PasswordSalt 
	- byte[]
- UserDTO
	- Username
		- string
	- Password
		- string
- AuthResponseDTO
	- Success
		- bool
	- Message
		- string
	- Token
		- string

<br>

## Setup API

1. delete all WeatherForecast related code
2. add a GlobalUsings.cs
3. add a RegisterServices.cs
	1. allows to outsources the dependency injection from the Program.cs into a seperate class

<br>

## Models

1. UserModel.cs

``` C#
public class UserModel
{
    public int Id { get; set; } 
    public string Username { get; set; } = string.Empty;
    public byte[] PasswordHash { get; set; } = new byte[32];
    public byte[] PasswordSalt { get; set; } = new byte[32];
}
```

2. UserDTOModel.cs (Data Transfer Object)

``` C#
public class UserDTOModel
{
    // will be used for registering & logging in the user
    public string Username { get; set; } = string.Empty;
    public string Password { get; set; } = string.Empty;
}
```

3. AuthResponseDTOModel.cs

``` C#
public class AuthResponseDTOModel
{
    // will be used to transfer a response to the user
    // if the logging was successfull or not
    public bool Success { get; set; } = false;
    public string Message { get; set; } = string.Empty;
    public string Token { get; set; } = string.Empty;
}
```

<br>

## Sqlite

DataAccess Layer ??

<ins>DbContext</ins>
A derived DbContext instance is needed to create the database.

``` C#
public class DataContext : DbContext
{
    public DbSet<UserModel> Users { get; set; }

    public DataContext(DbContextOptions<DataContext> options) : base(options) { }
}
```

Furthermore, the DBContext needs to be added to the RegisterServices.cs which is responsible for the dependency injection

``` C#
public static class RegisterServices
{
    public static void ConfigureServices(this WebApplicationBuilder builder)
    {
        builder.Services.AddControllers();
        builder.Services.AddEndpointsApiExplorer();
        builder.Services.AddSwaggerGen();
        builder.Services.AddDbContext<DataContext>(options => options.UseSqlite("Data Source=auth.db"));
    }
}
```

<ins>Create Database</ins>
1. Open Package Manager Console 
	1. View -> Other Windows -> Package Manager Console
2. cd into ProjectFolder of API (Solution Folder is not enough)
	1. cd .\\AuthenticationWebAPI
3. install EntityFramework
	1. dotnet tool install --global dotnet-ef
4. update ef if it is already installed
	1. dotnet tool update --global dotnet-ef
5. create a migration -> will add a new Migrations folder to the project (specify startup project)
	1. dotnet ef migrations add Initial -s ..\\CustomLoginAPI\\CustomLoginAPI.csproj
6. create database -> creates .db file 
	1. dotnet ef database update -s ..\\CustomLoginAPI\\CustomLoginAPI.csproj
7. add refresh token data to the table
	1. dotnet ef migrations add RefreshTokenData -s ..\\CustomLoginAPI\\CustomLoginAPI.csproj
	2. dotnet ef database update -s ..\\CustomLoginAPI\\CustomLoginAPI.csproj
8. add user roles to table
	1. dotnet ef migrations add UserRole -s ..\\CustomLoginAPI\\CustomLoginAPI.csproj
	2. dotnet ef database update -s ..\\CustomLoginAPI\\CustomLoginAPI.csproj
9. download & install [SqliteBrowser](https://sqlitebrowser.org/dl/)
10. open db in SqliteBrowser

<br>

## Services

Create an Authentication Service that can be injected in the controller, so the controller stays clean & simple.

1. create a new Services/AuthService/AuthService.cs

<br>

## Controllers

1. AuthController.cs -> started as Empty API Controller

<br>

## JWT

<ins>Key</ins>
A key is needed to create the JSON Web Token. A simple way to create that key, which is the same for all JWT's, is to put it in the appsettings.json. 

``` JSON
{
  "AppSettings": {
    "Key": "This is my top secret key for my JWT token"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

<br>

## Program.cs

<br>

## Notes

- the frontend has to check if the refresh token is expired or close to expiring to request a new one