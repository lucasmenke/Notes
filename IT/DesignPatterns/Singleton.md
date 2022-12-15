# Singleton

- class which only allows a single instance of itself to be created
- Mostly, singletons don't allow any parameters to be specified when creating the instance 
	- otherwise a second request for an instance but with a different parameter could be problematic

***

## 1. Version - not thread-safe

Don't use this code. Two different threads could both have evaluated the test `if (instance==null)` and see it as true, then both create instances, which violates the singleton pattern.

``` C#
// code from [Mustafa Mbari](https://www.codegrepper.com/profile/mustafa-mbari)

using System;  

namespace Singleton 
{  
	// The Singleton class defines the `GetInstance` method that serves as an  
	// alternative to constructor and lets clients access the same instance of  
	// this class over and over.  
	class  Singleton  
	{  
		// The Singleton's constructor should always be private to prevent  
		// direct construction calls with the `new` operator.  
		private  Singleton()  {  }  

		// The Singleton's instance is stored in a static field. There are  
		// multiple ways to initialize this field, all of them have various pros  
		// and cons. In this example we'll show the simplest of these ways,  
		// which, however, doesn't work really well in multithreaded programs.  
		private  static  Singleton _instance;  
		
		// This is the static method that controls the access to the singleton  
		// instance. On the first run, it creates a singleton object and places  
		// it into the static field. On subsequent runs, it returns the client  
		// existing object stored in the static field.  
		public  static  Singleton  GetInstance()  
		{  
			if  (_instance ==  null)  
			{ 
				_instance =  new  Singleton();  
			}  return _instance;  
		}  
		
		// Finally, any singleton should define some business logic, which can  
		// be executed on its instance.  
		public  static  void  someBusinessLogic()  
		{  
			// ...  
		}  
	}  
	
--------------------------------------------------------------------------- 

	class  Program  
	{  
		static  void  Main(string[] args)  
		{  
			// The client code.  
			Singleton s1 = Singleton.GetInstance();  
			Singleton s2 = Singleton.GetInstance();  

			if  (s1 == s2)  
			{ 
				Console.WriteLine("Singleton works, both variables contain the same instance.");  
			}  
			else  
			{ 
				Console.WriteLine("Singleton failed, variables contain different instances.");  
			}  
		}  
	}  
}  
=======OUTPUT======= 
Output >>  Singleton works, both variables contain the same instance.
```

***

## Lazy Singleton

``` C#
    public sealed class Singleton
    {
        private static readonly Lazy<Singleton> lazy = 
            new Lazy<Singleton>(() => new Singleton());

        public static Singleton Instance { get { return lazy.Value; } }

        private Singleton()
        {
        }
    }
```

***

## Tags

#Programming #DesignPatterns