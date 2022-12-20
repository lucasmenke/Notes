
# Hash & Salt

Hash & Salt is a security technique that combines a password with a random string (salt) and hashes the result to create a unique, secure password representation.

<br>

## Hash

In computer science, a hash is a function that takes in data of any size and produces a fixed-size string of characters, known as a "hash value" or "digest," that represents the data. The goal of a hash function is to produce a unique hash value for each unique piece of data, so that if the data changes even slightly, the hash value will also change significantly.

<br>

## Salt

Salt is a random string of characters that is generated and added to the data being hashed. The salt is then hashed along with the data, and the resulting hash value is stored. The purpose of adding a salt to the data before hashing it is to make it more difficult for an attacker to crack the password or to create a "rainbow table" that could be used to quickly look up the hash value for a given password.

<br>

## Use cases

One common use of hash and salt is in the storage of passwords. When a user creates a new account and sets a password, the password is hashed and salted before it is stored in the database. When the user logs in, the system retrieves the stored hash value, hashes the password entered by the user along with the salt, and compares the resulting hash value to the stored hash value. If the two hash values match, the password is considered correct and the user is granted access.

<br>

## Tags

#Programming #Authentication #Authorization