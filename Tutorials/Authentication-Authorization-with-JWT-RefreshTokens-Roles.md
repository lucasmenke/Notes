# Authentication & Authorization in with JSON Web Tokens (JWT), Refresh Tokens & Roles

In this project I will create a page for user to create an account and save them in a database using hash & salt. Furthermore registerd users are able to log back in. In addition to that I will use JWT & Refresh Tokens. A registerd user can get a role and based on this role the user will be able to call specific API endpoints.

***

## Tech Stack

- ASP.NET Core Web API (.NET 6)
	- Authentication Type -> None

***

## Project Structure

1. Blazor Client
2. ASP.NET Core Web API
	1. Models / DTO
	2. Services

***

## Extensions


***

## Data Structure

- User
	- Id
	- Username
	- PasswordHash 
		- byte[]
	- PasswordSalt 
	- byte[]
- UserDTO
	- Username
		- string
	- Password
		- string

***

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

***

## SQL

***

## Services

Create an Authentication Service that can be injected in the controller, so the controller stays clean & simple.

1. create a new Services/AuthService/AuthService.cs

***

## Controllers

1. AuthController.cs -> started as Empty API Controller