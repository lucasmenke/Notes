# IoC

An Inversion of Control (IoC) container is a software design pattern that allows for the externalization of a component's dependencies. This means that instead of a component being responsible for creating and managing its own dependencies, the dependencies are provided to the component by an external entity, the IoC container.

<br>

## Advantages

The IoC container is responsible for managing the lifecycle of the dependencies and injecting them into the component when it is needed. This helps to improve the modularity and testability of the component by decoupling it from its dependencies.

<ins>Code example</ins>

``` C#
// Create the IoC container
var container = new Container();

// Register the dependencies
container.Register<ILogger, Logger>();
container.Register<IUserService, UserService>();

// Verify the container
container.Verify();

// Resolve a component and its dependencies
var userService = container.GetInstance<IUserService>();

```

<ins>Explanation</ins>

In this example, the `IUserService` class has a dependency on the `ILogger` interface. The IoC container is responsible for creating an instance of the `Logger` class and injecting it into the `UserService` class when the `UserService` is resolved from the container. This decouples the `UserService` from the concrete implementation of the `Logger`, allowing it to be easily unit tested and swapped out for a different implementation if necessary.

<br>

## Tags

#Programming #DesignPatterns