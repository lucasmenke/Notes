# Database Transaction

 - a transaction is a unit of work that you can treat as "a whole" 
	- it happens either in full or not at all

**Example: (by sharptooth https://stackoverflow.com/a/974611/16764349)**

Here's a simple explanation. You need to transfer 100 bucks from account A to account B. You can either do:
```
accountA -= 100;
accountB += 100;
```
or
```
accountB += 100;
accountA -= 100;
```
If something goes wrong between the first and the second operation in the pair you have a problem - either 100 bucks have disappeared, or they have appeared out of nowhere.

A transaction is a mechanism that allows you to mark a group of operations and execute them in such a way that either they all execute (commit), or the system state will be as if they have not started to execute at all (rollback).
```
beginTransaction;
accountB += 100;
accountA -= 100;
commitTransaction;
```
It will either transfer 100 bucks or leave both accounts in the initial state.

***

## Tags

#Programming #CSharp #Database
