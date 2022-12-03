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
- Microsoft.Extensions.Configuration.Abstract
- MongoDB.Driver

***

## Data Access

<ins>DbConnection.cs</ins>
This class is a dependency which will be injected in BalzorServerProject/RegisterServices.cs 

1. Setup the connection to the database
``` C#
// make it a public class
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

2. Get the collections
``` C#
public class DbConnection
{
    // setup db
    private readonly IConfiguration _config;
    private readonly IMongoDatabase _db;
    private string _connectionId = "MongoDB";
    public string DbName { get; private set; }
    public MongoClient Client { get; private set; }

	// setup collections -> collections are like tables in SQL but they store objects
	// hardcoding the name of the colletions because normally they dont change
    public string UserCollectionName { get; private set; } = "users";
    public string TransactionCollectionName { get; private set; } = "transactions";
    public IMongoCollection<UserModel> UserCollection { get; private set; }
    public IMongoCollection<TransactionModel> TransactionCollection { get; private set; }
    
    public DbConnection(IConfiguration config)
    {
        // get db
        _config = config;
        Client = new MongoClient(_config.GetConnectionString(_connectionId));
        DbName = _config["DatabaseName"];
        _db = Client.GetDatabase(DbName);

		// get collections
	    UserCollection = _db.GetCollection<UserModel>(UserCollectionName);
        TransactionCollection = _db.GetCollection<TransactionModel>(TransactionCollectionName);
    }
}
```

3. make an Interfaces out of the class
	1. allows me to reference this class in the data access classes for the specific models

<ins>MongoUserData.cs</ins>
This class communicates with the database (CRUD - create, read, update, delete). The constructor of this class gets called when the dependy is injected into RegisterServices.cs and used on a razor page that gets called > `@inject IUserData userData`

1. create constructor which recvives IDbConnection as parameter
``` C#
// make class public
public class MongoUserData
{
    private readonly IMongoCollection<UserModel> _users;

    // get the UserCollection from the IDbConnection parameter
    public MongoUserData(IDbConnection db)
    {
        _users = db.UserCollection;
    }
}
```

2. create CRUD methods
``` C#
public class MongoUserData : IUserData
{
    private readonly IMongoCollection<UserModel> _users;

    public MongoUserData(IDbConnection db)
    {
        _users = db.UserCollection;
    }

    // create
    public Task CreateUser(UserModel user)
    {
        return _users.InsertOneAsync(user);
    }

    // read
    public async Task<List<UserModel>> GetUsers()
    {
        var results = await _users.FindAsync(_ => true);
        return results.ToList();
    }

    public async Task<UserModel> GetUser(string id)
    {
        var result = await _users.FindAsync(u => u.Id == id);
        return result.FirstOrDefault();
    }


    // update
    public Task UpdateUser(UserModel user)
    {
        var filter = Builders<UserModel>.Filter.Eq("Id", user.Id);
        // IsUpsert false -> if the user doesn´t exist don´t insert it
        return _users.ReplaceOneAsync(filter, user, new ReplaceOptions { IsUpsert = false });
    }


    // delete
    public Task DeleteUser(UserModel user)
    {
        var filter = Builders<UserModel>.Filter.Eq("Id", user.Id);
        return _users.DeleteOneAsync(filter);
    }
}
```

3. create Interface out of the class

<ins>MongoTransactionData.cs</ins>

1. create constructor that recives IDbConnection & IUserData as parameters
``` C#
public class MongoTransactionData : ITransactionData
{
    private readonly IDbConnection _db;
    private readonly IUserData _userData;
    private readonly IMongoCollection<TransactionModel> _transactions;

    // parameters are passed from the dependency injection in the RegisterServices.cs
    public MongoTransactionData(IDbConnection db, IUserData userData)
    {
        _db = db;
        _userData = userData;
        _transactions = db.TransactionCollection;
    }
}
```

2. create CRUD methods
``` C#
public class MongoTransactionData : ITransactionData
{
    private readonly IDbConnection _db;
    private readonly IUserData _userData;
    private readonly IMongoCollection<TransactionModel> _transactions;

    // parameters are passed from the dependency injection in the RegisterServices.cs
    public MongoTransactionData(IDbConnection db, IUserData userData)
    {
        _db = db;
        _userData = userData;
        _transactions = db.TransactionCollection;
    }

    // create
    public async Task CreateTransaction(TransactionModel transaction)
    {
        var client = _db.Client;

        using var session = await client.StartSessionAsync();

        // transaction ensures that when we write to different collection the write completly succeeds or completly fails
        session.StartTransaction();

        try
        {
            // get both parties of the transaction
            var fromUser = await _userData.GetUser(transaction.FromUserId);
            var toUser = await _userData.GetUser(transaction.ToUserId);

            // update their balances
            fromUser.Balance -= transaction.Amount;
            toUser.Balance += transaction.Amount;

            await _userData.UpdateUser(fromUser);
            await _userData.UpdateUser(toUser);

            await _transactions.InsertOneAsync(transaction);

            // commit transaction
            await session.CommitTransactionAsync();
        }
        catch (Exception)
        {
            // in case of an exception the session will be aborted -> no db data changed
            await session.AbortTransactionAsync();
            throw;
        }
    }

    // read
    public async Task<List<TransactionModel>> GetTransactions()
    {
        var results = await _transactions.FindAsync(_ => true);
        return results.ToList();
    }

    public async Task<List<TransactionModel>> GetTransactionsPerTimePeriod(DateTime from, DateTime to)
    {
        var result = await _transactions.FindAsync(t => t.DateCreated >= from && t.DateCreated <= to);
        return result.ToList();
    }

    public async Task<TransactionModel> GetTransaction(string id)
    {
        var result = await _transactions.FindAsync(t => t.Id == id);
        return result.FirstOrDefault();
    }

    public async Task<List<TransactionModel>> GetTransactionsPerUser(string userId)
    {
        var result = await _transactions.FindAsync(t => t.FromUserId == userId);
        return result.ToList();
    }

    public async Task<List<TransactionModel>> GetTransactionsPerUserPerTimePeriod(string userId, DateTime from, DateTime to)
    {
        var result = await _transactions.FindAsync(t => t.FromUserId == userId && t.DateCreated >= from && t.DateCreated <= to);
        return result.ToList();
    }

    // update
    // transactions are unchangable

    // delete
    // transaction are undeletable
}
```

***

## Register Services

When injecting the Interfaces as dependencies, we have to decide between Transient, Scoped and Singleton. Here are more information about [Dependeny Injection Lifetime](https://github.com/lucasmenke/notes/blob/main/content/DependencyInjection.md).

1. Register Services as Singleton, Scoped or Transient
``` C#
public static class RegisterServices
{
    public static void ConfigureServices(this WebApplicationBuilder builder)
    {
        builder.Services.AddRazorPages();
        builder.Services.AddServerSideBlazor();
        builder.Services.AddMemoryCache();

		// 
        builder.Services.AddSingleton<IDbConnection, DbConnection>();
        builder.Services.AddSingleton<IUserData, MongoUserData>();
        builder.Services.AddSingleton<ITransactionData, MongoTransactionData>();
    }
}
```

***

## Create Razor Components