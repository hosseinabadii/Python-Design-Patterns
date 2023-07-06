## #1 Wrong/too elaborate data structure

Try to use the best structure for the data

## #2 Misleading names

It's hard to name things. Methods are often called add_something, create_something, get_something, etc. Are we really adding something? Or creating it? Or getting it? It's important to have method names reflect what the method actually does.

## #3 Classes with way too many instance variables

When a class contains too many instance variables, this is often a sign that the class has too many responsibilities.

## #4 VerbSubject / Ask Don't Tell

Whenever you encounter a method that gets a single object as a parameter and then does something with that object and nothing else, this is called the VerbSubject smell (the method name is the verb, the subject is the object). The positively worded principle is: "ask don't tell". Instead of asking for details and performing a computation yourself, simply ask the object to do it. In many cases, this means that the method should actually belong to the object it's doing something with.

## #5 Backpedalling / Law of Demeter

Backpedalling means that you call a method, but then not provide the data it needs, so that the method needs to find all the stuff it requires elsewhere, often leading to the method needing implemenation details of another object. A related principle is the Law of Demeter: the principle of least knowledge.

## #6 Hardwired sequences with a single order:

What you can do is make sure that the extra work you need to do only happens in a single place. 

## #7 Comments

Use comments to describe what a module or a class does. If a module only contains a single class, then put a comment either at the module or at the class level, both is not needed. Don't have comments at the top of methods or functions, but use clear names, so you always understand what a function or method does. Use single line comments in the function body to clarify aspects of the code as needed. Write those comments at the start of the line, not behind a line of code. If you need too many comments, you probably need to split the function or methods into separate parts to increase clarity.

## #8 Clarify function calls with keyword arguments

When you call a function that has more than a single parameter, use keyword arguments to clarify what each argument is.

## #9 Final thoughts

A note about dataclasses. They help reduce boilerplate so you don't have to write explicit initializers. The onyl issue is that they potentially decrease encapsulation, because you might want to directly access and modify the objects. You can combat this by adding methods to classes to do that job for you.
