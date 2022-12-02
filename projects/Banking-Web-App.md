# Banking Web App

The "Banking Web App" allows to create accounts, add  deposits, withdraw money and transfer money to other bank accounts.

Finished date of project: 

***

## Tech Stack

- Blazor Server (.NET 6)
- MongoDB (including Atlas)
- Azure Active Directors B2C

***

## Planing project

1. Features
	- createing accounts
	- see balance
	- add balance
	- transfer balance to other accounts

***

## Data Structure

- User
	- Id 
		- BsonId -> unique id property of class object
		- BsonType.ObjectId ->  automatically assigns value to Id property (leave it blank when creating object)
	- Surname
	- Forname
	- Bank Account Number
	- Balance
	- E-Mail

- Transaction
	- Id
		- BsonId
		- BsonRepresentation(BsonType.ObjectId)
	- FromUserId
	- ToUserId
	- Amount
	- DateCreated

***

## Project Structure

1. Blazor Server UI
	1. has a one sided dependency with the Class Library -> project needs Class Library to build
2. Class Library Project

<ins>More in depth explanation & overwiev here</ins>
- [Blazor Server](https://github.com/lucasmenke/notes/blob/main/content/BlazorServer.md)

***

## Extensions

<ins>Blazor Server project</ins>
- Microsoft.Identity.Web
- Microsoft.Identity.Web.UI

<ins>Class Library</ins>
- Microsoft.Extensions.Caching.Memory
- Microsoft.Extensions.Configuration.Abstract
- MongoDB.Driver

