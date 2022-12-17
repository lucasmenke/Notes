# Session

When you log in to a website, a session is a way for the server to store information about your visit and track your activity as you navigate through the site. 

<br>

## Flow

1. When you log in, the server creates a new session and assigns a unique session ID to the client 
	2. the session Id is stored server sided
2. This session ID is then sent to the clients browser as a cookie
3. with every new request the client does, the cookie will automatically be send within the Cookie HTTP header
4. the session ID from the cookie will be compared with the session ID on the server
	1. if they match and the session ID isn't already expired on the server the client will be authorized

<br>

## Usage of Sessions

As a client navigates through the site, the server uses a session ID to identify the client and keeps track of their activities. For example, if the client adds items to a shopping cart or customize their account settings, the server will store this information in their session so that it can be accessed and used as they continue to interact with the site.

Sessions are often used to store user information and preferences, as well as to track user activity and provide a personalized experience. They can also be used for security purposes, such as to prevent unauthorized access to certain areas of the site or to ensure that sensitive information is only accessed by the correct user.

<br>

## Tags

#Programming #Authentication #Authorization