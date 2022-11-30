***

The "Suggestion Web App" is a server-sided webpage where users can create accounts to post and vote on suggestions. The website allows the administator of the page to review each suggestions befor it will be published on the side.

***
## Suggestion Website

Following components will be used:
 - Blazor Server (.NET 6)
 - MongoDB (including Atlas)
 - Azure Active Directors B2C

***

## 1 Lesson: Planning process

> First, we have to have a clear picture of our endgoal 
 
- using WOULD Framework for planning
	1. Walk through application
		- decide on primary goal & focus on that
		- ask questions (they bring out features)
			- *Do we want authentication?*
			- *Offensive content filter? *
		- not every feature / idea must be in the first version of the project
			-  *Add content / status filters -> Maybe in Version 1.1*
	2. Open up the requirements
		- Question form requirements 
			 - *Do we want authentication? -> Authentication / Login*
			 - *Offensive content filter? -> Approve questions as admin*
	3. UI design 
		- note down elements (sketching with pen & paper) 
		- user flow of the app (wireframing) (figma)
		- design for mobil, tablets & monitors
	4. Logic design (big picture)
		- Blazor Server (can talk directly to a database + client side feeling)
		- Scalability / Efficency
			- aiming for a spot in the middle between mvp & can handle thousands of people at the same time
			- use Virtualize (lazy load)
			- In-Memory Caching
		- Azure Active Directory B2C for authentification & authorization
		- Store Data (MongoDB -> NoSql DB)
	5. Data design 	 
		- outline the bigger design pieces & how they work together
			- pieces:
				- *category*
					- CategoryName
					- CategoryDescription
				- *status*
					- StatusName
					- StatusDescription
				- *user*
					- ObjectId
					- FirstName
					- LastName
					- DisplayName
					- E-Mail
					- AuthoredSuggestions
					- VotedOnSuggestions
				- *suggestion*
					- Suggestion
					- Description
					- DateCreated
					- Category
					- Author
					- UserVotes
					- SuggestionStatus
					- OwnerNotes
					- ApprovedForRelease
					- Rejected
					- Archived

***

## Project Structure 

<ins>Two projects under one solution</ins>
1. Blazor Server App for the Frontend
	 - Dependency Injections moved out from the Program.cs to a seperate class (RegisterServices.cs)
2. Class Library for the Backend 
	- Data Access classes
	- Backend model classes

 <ins>Relathionship of the projects</ins>
 - one-sided relationship between the projects
	 - Blazor Server App knows the Class Library but the Class Library doesn't know the Blazor Server App
	 - Blazor Server App relies on Class Library because Class Library has to be build before the Blazor Server App to get the .dll to use it as a dependency in the Blazor Server App
	 - don't create circular / two-sided dependency
		 - couldn't build anything because both projects would rely on each other

<ins>Usings</ins>
 - Both have a GlobalUsings.cs in the root
	 - [global using directive](https://github.com/dotnet/csharplang/blob/main/proposals/csharp-10.0/GlobalUsingDirective.md) are usings that the compiler uses for the whole project
