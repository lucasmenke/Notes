# C# MVC .NET Framework

## Folder Structure

- App_Data → irrelevant
- App_Start → contains class files that will be executed, when the application starts
- Content → static files like .css
- Controller → contains class files for the controller
- fonts → custome fonts for application
- Models → contains model class files
- Script → contains JS files like bootstrap or jquery
- Views → contains HTML files for the application (.cshtml combines C# & HTML)
	- includes seperate folder for each controller f.e. all Views from the HomeController are in View > Home
	- Views > Shared containes all views that are shared between different Views like Layout or Error
- Global.asax → write code that runs in response to application-level events
- Packages.config → manages NuGet packages / versions
- Web.config → Config file

***

## Routing 

- defines the URL pattern & handler information
![c#-mvc](https://i.imgur.com/DJ5UA35.png)

### Configure Route

 - routes (RouteTable) can be added in App_Start > RouteConfig.cs
![c#-mvc](https://i.imgur.com/sh4Y3FZ.png)

### URL Pattern

![c#-mvc](https://i.imgur.com/GIKXiKY.png)
![c#-mvc](https://i.imgur.com/2jpjFgH.png)

### Multiple Routes

``` C#
    // added second route bevor "Default" route because each route is evaluated in sequence	
    public class RouteConfig 
    { 
	    public static void RegisterRoutes(RouteCollection routes) 
	    { 
		    routes.IgnoreRoute("{resource}.axd/{*pathInfo}"); 
		    routes.MapRoute( 
			    name: "Student", 	
			    // any url starts with "domain/students" must be handled 
			    // by StudentController & no action sprecified because 
			    // the Index() action should always be used
			    url: "students/{id}", 
			    defaults: new { controller = "Student", action = "Index"} 
		    ); 
		    
		    routes.MapRoute( 
			    name: "Default", 
			    url: "{controller}/{action}/{id}", 
			    defaults: new { controller = "Home", action = "Index", id = UrlParameter.Optional } 
		    ); 
	    } 
    }
```
![c#-mvc](https://i.imgur.com/RXLgqxg.png)

### Route Constraints
``` C#
    routes.MapRoute( 
	    name: "Student", 
	    url: "student/{id}/{name}/{standardId}", 
	    defaults: new { controller = "Student", action = "Index", id = UrlParameter.Optional, name = UrlParameter.Optional, standardId = UrlParameter.Optional }, 
	    // limitation, that the id parameter must be numeric constraints: 
	    new { id = @"\d+" } 
    );
```

### Register Routes

 - after configuring routes, they need to be registered in Global.asax Application_Start() event
``` C#
    public class MvcApplication : System.Web.HttpApplication 
    { 
	    protected void Application_Start() 
	    { 
		    RouteConfig.RegisterRoutes(RouteTable.Routes); 
	    } 
    }
```

***

## Controller

- Controller → handles user request (GET, POST…) & returns approprate view as result
- derived from base class System.Web.Mvc.Controller
- Controller classes contain public Methodes named Actions → together with them they handel requests
- every controller must end with name “Controller”, f.e. “StudentController”

### Add Controller

 - right click on folder Controllers > Add > Controller
 - now a template can be selected
``` C#
namespace MVC_BasicTutorials.Controllers 
{ 
	// every controller derives from Controller class -> contains helper methodes
	public class StudentController : Controller 
	{ 
		public ActionResult Index() 
		{
			return View(); 
		} 
	} 
}

namespace MVC_BasicTutorials.Controllers 
{ 
	public class StudentController : Controller 
	{ 
		// returning string instead of ActionResult 
		public string Index() 
		{ 
			return "This is Index action method of StudentController"; 
		} 
	} 
}
```
![csharp-mvc](https://i.imgur.com/L7S8Kqt.png)

***

## Action Methode

- all public classes of controller are action methodes
	- action methodes are public, not overloaded & not static

### Structure

![csharp-mvc](https://i.imgur.com/De9OYgn.png)
 - returned ActionResult using View() → methode from the Controller Base class, which returns the apporpriate view
 - in the RouteConfig class the Index() methode is the default Action methode

### ActionResult → Different Result Returns

 - ActionResult is base class, which can return any of the results below
![csharp-mvc](https://i.imgur.com/PFjYtyN.png)

### ActionMethode Parameters

- every action methode can have input parameters as normal methodes
- parameters can be nullable

### Query String to Action Methode Parameter

- HTTP GET request embeds data into query string (/Student/Edit?id=1) → MVC automatically converts query string to method parameters, when their names are matching
- binding is not case sensitive
 
![csharp-mvc](https://i.imgur.com/hkqbAhw.png)
``` C#
// multiple parameters possible → http://localhost/Student/Edit?id=1&name=John 
public ActionResult Edit(int id, string name) 
{ 
	return View(); 
}
```

***

## Action Selector

- attributes for the action methode, which helps the routing engine to select the correct action methode

### ActionName
 
- allows to rename the action methode name
 ``` C#
 // action methode name changes from "GetById" to "Find" -> http://localhost/student/find/1 
 [ActionName("Find")] 
 public ActionResult GetById(int id) 
 { 
	 return View(); 
 }
 ```

### NonAction

- restrict access to Action Methode, which are by default public → make it private without writing “private”
- bad design → in general private methodes should be in the model
``` C#
// not accesable 
[NonAction] 
public Student GetStudent(int id) 
{ 
	return studentList.Where(s => s.StudentId == id).FirstOrDefault(); 
}
```

### ActionVerbs

- selector that handels different types of HTTP requests
- multiple ActionVerbs can be applied to an action methode
![csharp-mvc](https://i.imgur.com/eyVxbfk.png)
``` C#
// handles GET requests by default 
public ActionResult Index() 
{ 
	return View(); 
} 

// handles POST requests by default 
[HttpPost] 
public ActionResult PostAction() 
{ 
	return View("Index"); 
} 

// handles multiple requestst 
[AcceptVerbs(HttpVerbs.Post | HttpVerbs.Get)] 
public ActionResult GetAndPostAction() 
{ 
	return RedirectToAction("Index"); 
}
```

***

## Model
- represents data & business logic
	- shape of data are public properties
	- business logic are methods

### Adding Model Class

- right click on Model folder > Add > Class
``` C#
// properties must be puplic 
public class Student 
{ 
	public int StudentId { get; set; } 
	public string StudentName { get; set; } 
	public int Age { get; set; } 
}
```

***

## View

- Every view in the ASP.NET MVC is derived from WebViewPage class included in System.Web.Mvc namespace

### Razor View Heading

- client sided html code + server sided special razor syntax
	- @ marks the beginnig of c# server sided code
   
![csharp-mvc](https://i.imgur.com/G5lGcLy.png%29)  

### Create View

- right click inside action methode > Add View
- good practice to keep view name similar to action methode name
- Template & Model class options can be used to scaffold the view → first create model than view

***

## Good to know

### Workflow

1. create Controller
2. create Model
3. create View with template
4. possible changing RouteConfig

### Global Varibales vs Sessions

- static variables are global variables
- Static data will be the same for all users of the application, while session is "per user"