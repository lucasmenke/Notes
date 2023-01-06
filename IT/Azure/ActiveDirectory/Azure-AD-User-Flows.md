# AD User Flows

In this guide I will explain how to set up three different user flows with the Azure AD. Here is a [Link](https://github.com/lucasmenke/Notes/blob/notes/IT/Azure/ActiveDirectory/Azure-AD-B2C.md) to set up an Azure Active Direcory.

## 1. SignUp / SignIn

1. Search "b2c" in the searchbar on top
2. Click on "User flows" (left menu)
3. Click on "New user flow" (top menu)
4. Click on "Sign up and sign in"
5. Select "Recommended"
6. Click on "Create"
7. Fill in information
	1. Name -> susi
	2. Identity providers -> depends on website (Email signup is default)
	3. Multifactor Auth -> depends on website (SMS/Phone cost extra money)
	4. Conditional access -> gives access based on SignUp methode (no tick is default)
	5. User attributes and token claims -> depends on website
		1. use "return claim" "Job Title" to give users admin role
8. Click on "Create"

<br>

## 2. Edit user information

1. Search "b2c" in the searchbar on top
2. Click on "User flows" (left menu)
3. Click on "New user flow" (top menu)
4. Click on "Profile editing"
5. Select "Recommended"
6. Click on "Create"
7. Fill in information
	1. Name -> edit
	2. Rest -> similar to susi-Flow
8. Click on "Create"

<br>

## 3. Password reset

1. Search "b2c" in the searchbar on top
2. Click on "User flows" (left menu)
3. Click on "New user flow" (top menu)
4. Click on "Password reset"
5. Select "Recommended"
6. Click on "Create"
7. Fill in information
	1. Name -> reset
	2. Identity provider -> tick "Reset password using email address"
	3. Rest -> similar to susi-Flow
8. Click on "Create"

<br>

## Modify Code

