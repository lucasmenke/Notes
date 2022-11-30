## HashSet

 - store non-duplicate items
 - after insertion of new items they don`t get sorted like in a SortedSet
 - does not have any maximum capacity for the number of elements stored in it
```
string[] words = new string[] { 
	"test",
	"test",
	"hello,"
	"world"
};

HashSet<string> hSet = newHashSet<string>(words);
```