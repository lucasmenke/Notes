# AuthenticationStateProvider Service

AuthenticationStateProvider is the underlying service used by the [AuthorizeView](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.authorization.authorizeview) component and [CascadingAuthenticationState](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.authorization.cascadingauthenticationstate) component to get the authentication state.

<br>

## Set it up

1. Install Nuget Package "Microsoft.AspNetCore.Components.Authorization" on the client sided project
2. Add package to the "Imports.razor" file
3. Add global using statement
4. Create new Class which create a new ClaimsPrincipal
	1. The `ClaimsPrincipal` class represents the security context for a user and contains a collection of `Claim` objects that represent the claims made about the user by an external entity, such as a trusted security token service (STS). These claims may include information such as the user's name, email address, and role within the application.
```C#
public class CustomAuthStateProvider : AuthenticationStateProvider
{
    private readonly ILocalStorageService _localStorage;
    private readonly HttpClient _http;

    public CustomAuthStateProvider(ILocalStorageService localStorage, HttpClient http)
    {
        _localStorage = localStorage;
        _http = http;
    }
    
    // gets the auth token (jwt) from local storage,
    // passs the claims & create a new ClaimsIdentity
    public override async Task<AuthenticationState> GetAuthenticationStateAsync()
    {
        string authToken = await _localStorage.GetItemAsStringAsync("authToken");

        // by default create empty ClaimsIdentity & set Authorization to not authorized
        var identity = new ClaimsIdentity();
        _http.DefaultRequestHeaders.Authorization = null;

        if (!string.IsNullOrEmpty(authToken))
        {
            try
            {
                // if token is there set new ClaimsIdentity & authentication 
                identity = new ClaimsIdentity(ParseClaimsFromJwt(authToken), "jwt");
                _http.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", authToken.Replace("\"",""));
            }
            catch
            {
                await _localStorage.RemoveItemAsync("authToken");
                identity = new ClaimsIdentity();
            }
        }

        // set state of authentication
        var user = new ClaimsPrincipal(identity);
        var state = new AuthenticationState(user);

        NotifyAuthenticationStateChanged(Task.FromResult(state));

        return state;
    }

    private IEnumerable<Claim> ParseClaimsFromJwt(string jwt)
    {
        var payload = jwt.Split('.')[1];
        var jsonBytes = ParseBase64WithoutPadding(payload);
        var keyValuePairs = JsonSerializer.Deserialize<Dictionary<string, object>>(jsonBytes);
        var claims = keyValuePairs.Select(kvp => new Claim(kvp.Key, kvp.Value.ToString()));

        return claims;
    }

    private byte[] ParseBase64WithoutPadding(string base64)
    {
        switch (base64.Length % 4)
        {
            case 2:
                base64 += "==";
                break;
            case 3:
                base64 += "=";
                break;
        }
        return Convert.FromBase64String(base64);
    }
}
```
5. add following to configure services
```C#
builder.Services.AddOptions();
builder.Services.AddAuthorizationCore();
builder.Services.AddScoped<AuthenticationStateProvider, CustomAuthStateProvider>();
```
6. Wrap App.razor into CascadingAuthenticationState & change RouteView to AuthorizeRouteView
```C#
<CascadingAuthenticationState>
<Router AppAssembly="@typeof(App).Assembly">
    <Found Context="routeData">
        @*<RouteView RouteData="@routeData" DefaultLayout="@typeof(ShopLayout)" />*@
        <AuthorizeRouteView RouteData="@routeData" DefaultLayout="@typeof(ShopLayout)" />
        <FocusOnNavigate RouteData="@routeData" Selector="h1" />
    </Found>
    <NotFound>
        <PageTitle>Not found</PageTitle>
        <LayoutView Layout="@typeof(ShopLayout)">
            <p role="alert">Sorry, there's nothing at this address.</p>
        </LayoutView>
    </NotFound>
</Router>
</CascadingAuthenticationState>```

<br>

## Use it

1. inject AuthenticationStateProvider into razor component
2. get authentication information -> `await authStateProvider.GetAuthenticationStateAsync();`
3. now we can display code based on authorization status
```C#
        <AuthorizeView>
            <Authorized>
                <button class="dropdown-item" @onclick="Logout">Logout</button>
            </Authorized>
            <NotAuthorized>
                <a href="login" class="dropdown-item">Login</a>
                <a href="register" class="dropdown-item">Register</a>
            </NotAuthorized>
        </AuthorizeView>  
```

<br>

## Tags

#Programming #Authentication #Authorization