# Razor components (explained with BlazorApp)

- blocks that can be nested reused & packaged
- consists of html & C# + can have references to other components
- can be complete page (folder Pages) or a non-page component (folder Shared)
- parameters can be assigned upon reference or via Routing

***

## Reference

- added new component to \Shared folder that prints the parameter
- added component to \Pages\Counter page and passed parameter to it
![Razor components passing parameter per reference](https://i.imgur.com/mjVppdV.png)
![Razor components passing parameter per reference](https://i.imgur.com/b4dKfAA.png)
![Razor components passing parameter per reference](https://i.imgur.com/RVEoJsn.png)
- support data binding
- allows to bind objects to html elements & every time the state of the object changes the html element gets updated
![Razor data binding](https://i.imgur.com/cdVdL5w.png)
- they have lifecycle related methods which are executed after component initialization
- f.e. OnParametersSet() recives parameters from the parent and assignes it to properties
![Razor lifecycle related methods override](https://i.imgur.com/zs0Y4R9.png)
- components can be disposable -> ```@implements IDisposable```
- possible to write @code{} block to a base class which the component inherits from

***

# Tags

#Programming #WEB #CSharp #Razor