# MongoDB

MongoDB is a NoSQL database. Through that the database is able to store complete Objects. 

***

## Index

<ins>Create unique fields in a collection</ins>

1. create them in your code
``` C#
	public async Task<bool> CreateUser(UserModel user)
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
			return true;
		}
		catch (Exception)
		{
			return false;
		}
	}
```

*** 

# Tags

#Programming #Database #MongoDB