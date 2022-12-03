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

1. Blazor Server UI > has a one sided dependency with the Class Library -> project needs Class Library to build
	1. Components -> my own razor components
	2. Models (UI) -> user interfaces models
	3. GlobalUsings.cs > global using statements
	4. RegisterServices.cs > outsourced the dependency injection from the program.cs to a seperate class
2. Class Library Project
	1. DataAccess/DbConnections.cs -> creates a singleton connection to the database
	2. Models -> contains the backend models

<ins>More in depth explanation / overview how to setup a blazor server project & databse</ins>
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

***

## Data Access

<ins>DbConnection.cs</ins>
It is a dependency which will be injected in BalzorServerProject/RegisterServices.cs 

``` C#
public class DbConnection
{
    private readonly IConfiguration _config;
    private readonly IMongoDatabase _db;
    // default value that matches the appsettings.json ConnectionString key
    private string _connectionId = "MongoDB";
    // stores the name of the MongoDB db that it recives from the appsettings.json with the key "DatabaseName"
    public string DbName { get; private set; }
    public MongoClient Client { get; private set; }

    // constructor gets the IConfiguration from the dependency injection in the RegisterServices class
    // config is comming from the appsettings.json
    public DbConnection(IConfiguration config)
    {
        _config = config;
        Client = new MongoClient(_config.GetConnectionString(_connectionId));
        DbName = _config["DatabaseName"];
        _db = Client.GetDatabase(DbName);
    }
}
```

