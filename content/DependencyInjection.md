# Dependency Injection

- dependency injection provides the objects that an object needs (its dependencies) to work instead of constructing it themself
- one object (or static method) supplies the dependencies of another object
![enter image description here](https://i.imgur.com/aW0yYJM.jpg)

***

## Dependecy Injection Lifetime

>Transient objects are always different; a new instance is provided to every controller and every service.
>
>Scoped objects are the same within a request, but different across different requests (different for each user).
>
>Singleton objects are the same for every object and every request.

### Which one to use

**Transient**

-   since they are created every time they will use **more memory** & Resources and can have a **negative** impact on performance
-   use this for the **lightweight** service with little or **no state**.

**Scoped**

-   better option when you want to maintain state within a request.

**Singleton**

-   memory leaks in these services will build up over time.
-   also memory efficient as they are created once reused everywhere.

_Use Singletons where you need to maintain application wide state. Application configuration or parameters, Logging Service, caching of data is some of the examples where you can use singletons._

<ins>Injecting service with different lifetimes into another</ins>

1.  **Never inject Scoped & Transient services into Singleton service.** ( This effectively converts the transient or scoped service into the singleton.)
    
2.  **Never inject Transient services into scoped service** ( This converts the transient service into the scoped.)

- found on [Stackoverflow](https://stackoverflow.com/questions/38138100/addtransient-addscoped-and-addsingleton-services-differences) from [Bereket Gebredingle](https://stackoverflow.com/users/8954773/bereket-gebredingle)