# Custome Authentication & Authorization with JSON Web Tokens (JWT), Refresh Tokens & Roles

In this project I will create a page for user to create an account and save them in a database using hash & salt. Furthermore registerd users are able to log back in. In addition to that I will use JWT & Refresh Tokens. A registerd user can get a role and based on this role the user will be able to call specific API endpoints.

<br>

## Tech Stack

- ASP.NET Core Web API (.NET 6)
	- Authentication Type -> None
- Sqlite

<br>

## Project Structure

1. Blazor Client
2. ASP.NET Core Web API
	1. Models / DTO
	2. Services

<br>

## Extensions

<ins>ASP.NET Core Web API</ins>
- Microsoft.EntitiyFrameworkCore
- Microsoft.EntitiyFrameworkCore.Design
- Microsoft.EntitiyFrameworkCore.Sqlite
- Microsoft.IdentityModel.Tokens
- System.IdentityModel.Tokens.Jwt
- Microsoft.AspNetCore.Authentication.JwtBearer
- Swashbuckle.AspNetCore.Filters
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


<ins>Create Database</ins>
1. Open Package Manager Console 
	1. View -> Other Windows -> Package Manager Console
2. cd into ProjectFolder of API (Solution Folder is not enough)
	1. cd .\\AuthenticationWebAPI
3. install EntityFramework
	1. dotnet tool install --global dotnet-ef
4. create a migration -> will add a new Migrations folder to the project
	1. dotnet ef migrations add Initial
5. create database -> creates .db file 
	1. dotnet ef database update
6. add refresh token data to the table
	1. dotnet ef migrations add RefreshTokenData
	2. dotnet ef database update
7. add user roles to table
	1. dotnet ef migrations add UserRole
	2. dotnet ef database update
8. download & install [SqliteBrowser](https://sqlitebrowser.org/dl/)
9. open db in SqliteBrowser
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