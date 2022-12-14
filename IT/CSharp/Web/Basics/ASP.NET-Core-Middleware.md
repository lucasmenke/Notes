# ASP.NET Core Middleware

Middleware Components are assembled into the appplication to handle a HTTP request and respond to it. Each Middleware Components performs the following task:

1. choose whether to pass the HTTP Request to the next component in the pipeline
	1. can be achieved by calling the next() method within the middleware
2. can perform work before and after the next component in the pipeline.

***

## Middleware Properties

- each Middleware should only have one specific purpose -> single responsibility
	- f.e. authenticate user
	- f.e. log request

***

## Process Flow

The middleware components can be found in the Program.cs

![](https://i.imgur.com/COSDTV1.png)
![](https://i.imgur.com/Xug06fJ.png)
![](https://i.imgur.com/xIGSNr1.png)

***

## Tags

#Programming #CSharp #WEB #ASPDOTNET-Core