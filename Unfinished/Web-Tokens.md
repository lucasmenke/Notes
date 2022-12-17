# Web Tokens

Web tokens are data structures that contain information about a user or client in the form of digitally signed claims. They are typically used to authenticate users and provide access to certain resources or applications on a website or web service. Web tokens are often used in combination with other security measures, such as password authentication or two-factor authentication, to provide a more secure means of accessing online resources.

<br>

## Types of Web Tokens

- JWT (Json Web Token) 
	- widely used and popular standard for web tokenization

<br>

## Transfer

Web tokens are typically transferred between a client and a server in the form of an HTTP header. Often, they are encrypted to protect the sensitive information they contain.

<br>

## Flow between Client and Server

1. Client wants to get protected data from the server
	1. server only gives data to trustwhorty clients
2. Client sends login data to proof their credibility
3. Server dosen't save the credential of the client
	1. instead it creates a web token and return the token to the client
4. Client has to store the token & send it along their future requests to proof their credibility
5. every time a client sends a web token the server checks the token to verify its credibility
6. if the web token from the client gets verified the server response with the requested potected data