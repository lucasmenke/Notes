# MongoDB

MongoDB is a NoSQL database

***

## Index

<ins>Create unique fields in a collection</ins>

1. create them in your code
``` C#
    private readonly IMongoCollection<UserModel> _collection;
    
    public async Task CreateIndex()
    {
        var index = new BsonDocument
            {
                {"Field1", 1},
                {"Filed2", 1}
            };

        var indexModel = new CreateIndexModel<UserModel>(index, new CreateIndexOptions { Unique = true });
        await _collection.Indexes.CreateOneAsync(indexModel);
    }
```

2. create them in MongoDB Compass
![](https://i.imgur.com/Utnep7Q.png)