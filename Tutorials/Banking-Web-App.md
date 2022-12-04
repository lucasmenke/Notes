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

## Data Structure

- User
	- Id 
		- BsonId -> unique id property of class object
		- BsonType.ObjectId ->  automatically assigns value to Id property (leave it blank when creating object)
	- Surname
	- Forname
	- E-Mail
	- Bank Account Number
	- Balance
	- DateCreated
	- ActiveAccount

- Transaction
	- Id
		- BsonId
		- BsonRepresentation(BsonType.ObjectId)
	- FromUserId
	- ToUserId
	- Amount
	- DateCreated

***

## Models

1. UserModel.cs

``` C#
public class UserModel
{
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string Id { get; set; }
    public string Surname { get; set; }
    public string Forname { get; set; }
    public string Email { get; set; }
    public int BankAccountNumber { get; set; }
    public double Balance { get; set; } = 0;
    public DateTime DateCreated { get; set; } = DateTime.UtcNow;
    public bool ActiveAccount { get; set; } = true;
}
```

2. TransactionModel.cs

``` C#
public class TransactionModel
{
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string Id { get; set; }
    public string FromUserId { get; set; }
    public string ToUserId { get; set; }
    public double Amount { get; set; }
    public DateTime DateCreated { get; set; } = DateTime.UtcNow;
}
```

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
    private readonly IMemoryCache _cache;
    private const string CacheName = "BankAccountNumber";

    public MongoUserData(IDbConnection db, IMemoryCache cache)
    {
        _users = db.UserCollection;
        _cache = cache;
    }
}
```

2. create CRUD methods
``` C#
public class MongoUserData : IUserData
{
    private readonly IMongoCollection<UserModel> _users;
    private readonly IMemoryCache _cache;
    private const string CacheName = "BankAccountNumber";

    public MongoUserData(IDbConnection db, IMemoryCache cache)
    {
        _users = db.UserCollection;
        _cache = cache;
    }

    // create
    public async Task CreateUser(UserModel user)
    {
        try
        {
            var index = new BsonDocument
            {
                {"Email", 1}
            };
            var indexModel = new CreateIndexModel<UserModel>(index, new CreateIndexOptions { Unique = true });
            await _users.Indexes.CreateOneAsync(indexModel);
            await _users.InsertOneAsync(user);
        }
        catch (Exception)
        {
            return;
        }
    }

    // read
    public async Task<List<UserModel>> GetUsers()
    {
        var results = await _users.FindAsync(_ => true);
        return results.ToList();
    }

    public async Task<UserModel> GetUserById(string id)
    {
        var result = await _users.FindAsync(u => u.Id == id);
        return result.FirstOrDefault();
    }

    public async Task<UserModel> GetUserByEmail(string mail)
    {
        var result = await _users.FindAsync(u => u.Email == mail);
        return result.FirstOrDefault();
    }

    public async Task<UserModel> GetUserByBankAccountNumber(int bankAccountNumber)
    {
        var result = await _users.FindAsync(u => u.BankAccountNumber == bankAccountNumber);
        return result.FirstOrDefault();
    }

    public async Task<int> GetNewBankAccountNumber()
    {
        var output = _cache.Get<int>(CacheName);
        if (output == 0)
        {
            UserModel user = await _users
                .Find(_ => true)
                .SortByDescending(u => u.DateCreated)
                .Limit(1)
                .FirstOrDefaultAsync();

            if (user is null)
            {
                output = 1000000;
            }
            else
            {
                output = user.BankAccountNumber + 1;
            }

            _cache.Set(CacheName, output, TimeSpan.FromDays(90));

            return output;
        }
        else
        {
            return output + 1;
        }
    }

    // update
    public Task UpdateUser(UserModel user)
    {
        var filter = Builders<UserModel>.Filter.Eq("Id", user.Id);
        // IsUpsert false -> if the user doesn´t exist don´t insert it
        return _users.ReplaceOneAsync(filter, user, new ReplaceOptions { IsUpsert = false });
    }

    // delete -> users can't be deleted they can just be set to unactive
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

    public MongoTransactionData(IDbConnection db, IUserData userData)
    {
        _db = db;
        _userData = userData;
        _transactions = db.TransactionCollection;
    }

    // create
    public async Task CreateMultiTransaction(TransactionModel transaction)
    {
        var client = _db.Client;

        using var session = await client.StartSessionAsync();

        session.StartTransaction();

        try
        {
            var fromUser = await _userData.GetUserById(transaction.FromUserId);
            var toUser = await _userData.GetUserById(transaction.ToUserId);

            fromUser.Balance -= transaction.Amount;
            toUser.Balance += transaction.Amount;

            await _userData.UpdateUser(fromUser);
            await _userData.UpdateUser(toUser);

            await _transactions.InsertOneAsync(transaction);

            await session.CommitTransactionAsync();
        }
        catch (Exception)
        {
            await session.AbortTransactionAsync();
            return;
        }
    }

    public async Task CreateSingleTransaction(TransactionModel transaction)
    {
        var client = _db.Client;

        using var session = await client.StartSessionAsync();

        session.StartTransaction();

        try
        {
            var fromUser = await _userData.GetUserById(transaction.FromUserId);

            fromUser.Balance += transaction.Amount;

            await _userData.UpdateUser(fromUser);

            await _transactions.InsertOneAsync(transaction);

            await session.CommitTransactionAsync();
        }
        catch (Exception)
        {
            await session.AbortTransactionAsync();
            return;
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

## Create Sample Data

This pages allows us to add some sample data to test our database access methodes and insert our first dummy data. Don't put business logic in here. This page is only for testing the data access.

1. create UI Models under Blazor Server Project/Models
	1. allows a cleaner speration from Fontend Data and Backend Data
		1. f.e. wo don´t want the user to choose a bank account number so we don´t include it in the UI Model
		2. we can add Data Annotations to UI Model
``` C#
public class CreateUserModel
{
    [Required]
    [MaxLength(50, ErrorMessage = "Surname is too long.")]
    public string Surname { get; set; }

    [Required]
    [MaxLength(50, ErrorMessage = "Forname is too long.")]
    public string Forname { get; set; }

    [Required]
    [EmailAddress]
    [DisplayName("E-Mail")]
    public string Email { get; set; }
}
```

2. create razor page for sample data
3. create input form
``` C#
@page "/SampleData"
@using BankingAppUI.Models;
@inject IUserData userData
@inject ITransactionData transactionData
@inject NavigationManager navManager

<h3>Sample Data</h3>

<EditForm Model="user" OnValidSubmit="CreateUser">
    <DataAnnotationsValidator />
    <ValidationSummary />
    <div>
        <label for="forname">Forname</label>
        <InputText id="forname" @bind-Value="user.Forname"></InputText>
    </div>
    <div>
        <label for="surname">Surname</label>
        <InputText id="surname" @bind-Value="user.Surname"></InputText>
    </div>
    <div>
        <label for="email">E-Mail</label>
        <InputText id="email" @bind-Value="user.Email"></InputText>
    </div>
    <div>
        <button type="submit">Create User</button>
    </div>
</EditForm>

<div>
    <button @onclick="ClosePage">Close Page</button>
</div>
```

4. create methode to insert the user into the database
	1. we have to map the UI Model to the Backend  -> happens in CreateUser()
``` C#
@code {
    private CreateUserModel user = new();
    private CreateDeposit deposit = new();
    string createUserReturnMsg = string.Empty;

    private void ClosePage()
    {
        navManager.NavigateTo("/");
    }

    private async Task CreateUser()
    {
        UserModel u = new()
            {
                Surname = user.Surname,
                Forname = user.Forname,
                Email = user.Email,
                BankAccountNumber = await userData.GetNewBankAccountNumber()
            };

        await userData.CreateUser(u);
    }
}
```

More methodes & input forms for testing the data access can be found in the [GitHub Repository](https://github.com/lucasmenke/banking-web-app/blob/master/BankingAppUI/Pages/SampleData.razor) of this project.

***

## Create Razor Components