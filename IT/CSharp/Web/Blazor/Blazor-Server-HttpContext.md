# Blazor Server HttpContext

Using HttpContext the wrong way in Blazor Server Apps can lead to security vulnerabilities. 

<br>

## HttpContext

HttpContext encapsulates all information about an individual HTTP request and response. An HttpContext instance is initialized when an HTTP request is received and is accessible by middleware and app frameworks such as Web API controllers, Razor Pages and more.

<br>

## Security Issues

Using HttpContext the wrong way in Blazor Server Apps can lead to security vulnerabilities because  Blazor server apps live in server memory. That means that there are multiple apps hosted within the same process. Apps that share their state using a singleton can leak sensitive information across apps / [circuits](https://github.com/lucasmenke/Notes/blob/main/IT/CSharp/Web/Blazor/Blazor-Circuit.md).

<br>

## Using HttpContext safely

1. create folder  /Services
2. add class /Services/IdentitiyInformation.cs
3. add class /InitialApplicationState.cs
4. modifiy Pages/Host.cshtml to save HttpContext information
``` C#
@page "/"
@namespace BlazorApp1.Pages
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
@{
    Layout = "_Layout";
    // this file only gets called when a new HTTP request comes in 
    // so we are kind of in the HTTP-Request-Pipeline
    var state = new InitialApplicationState();
    // get information from HttpContext and pass it to our newly created class
    state.IsAuthenticated = HttpContext.User.Identity.IsAuthenticated;
    state.UserName = HttpContext.User.Identity.Name;
}

@*param-initialState="state" to pass the state values to the App.razor file*@
<component type="typeof(App)" param-initialState="state" render-mode="ServerPrerendered" />
```
5. modifiy Program.cs 
``` C#
// add IdentityInformation to use this services as a dependecy injection
// scoped because it souldn't be shared with other circuits
builder.Services.AddScoped<IdentityInformation>();
```
6. modifiy App.razor
``` C#
@using BlazorApp1.Services;
@*inject dependency*@
@inject IdentityInformation identitiy

<Router AppAssembly="@typeof(App).Assembly">
    <Found Context="routeData">
        <RouteView RouteData="@routeData" DefaultLayout="@typeof(MainLayout)" />
        <FocusOnNavigate RouteData="@routeData" Selector="h1" />
    </Found>
    <NotFound>
        <PageTitle>Not found</PageTitle>
        <LayoutView Layout="@typeof(MainLayout)">
            <p role="alert">Sorry, there's nothing at this address.</p>
        </LayoutView>
    </NotFound>
</Router>

@code{
    // pass information from Host.cshtml to our Blazor Application through a Parameter
    // after the Host.cshtml the App.razor gets called
    [Parameter]
    public InitialApplicationState initialState { get; set; }
    protected override void OnInitialized()
    {
        // save data to service
        // because it is scoped it will only have this one instance 
        // throughout the lifetime of the Blazor app
        // the service can now be injected somewhere else and the 
        // information is easily accesible
        identitiy.IsAuthenticated = initialState.IsAuthenticated;
        identitiy.UserName = initialState.UserName;
    }
}
```
7. check if everything works -> Pages/Index.razor
``` C#
@page "/"
@using BlazorApp1.Services;
@*inject dependency*@
@inject IdentityInformation identitiy

<PageTitle>Index</PageTitle>

<h1>Hello, world!</h1>

Welcome to your new app.

<SurveyPrompt Title="How is Blazor working for you?" />
<br/>
<br/>

@*check if everything works*@
<p>User is authenticated: @identitiy.IsAuthenticated</p>
<p>UserName: @(identitiy.UserName ?? "Not logged in")</p>
```

<br>

## Tags

#Programming #CSharp #WEB #Blazor 