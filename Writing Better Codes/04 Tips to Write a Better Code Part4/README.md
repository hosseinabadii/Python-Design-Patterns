# Tips to Write a Better Code

## Tip #1: Group side effects and use pure functions

In general a side effect is when a function or method relies on modify something on the outside of that function. For example:
- printing something
- reading from and writing to a file
- interacting with a database or another service over a network

Side effects make your code harder to maintain and make things harder to test because you can't isolate a function or method properly. 

If a function doesn't have side effects and the return value is only determined by its input values then the function is called a **pure function**.

As opposed to functions with side effects pure functions are easy to test and they're easier to use in different parts of your software because there are no outside dependencies.

If you want to write software that's easy to work on and needs to test take a look at your code and see whether you can turn some of your functions into pure functions. If you focus on putting all those side effects in a single place they're much easier to manage.

## Tip #2: Functions are first-class citizens

The second takeaway from functional programming is that functions are first class citizens. They're not just groups of statements with input arguments and return value.

There are things that you can compose deconstruct, pass to other functions and return as a value from a function. If a function receives a function as an argument or it returns a function as a result it's called a **higher order** function.

With higher order functions instead of providing values to functions, you can provide functions to functions.

Another concept from functional programming is **partial function application** and that means that you create a new function that's based on an original function but with some of the arguments already applied. You can import `partial` from functools module.

## Tip #3: Use immutability to your advantage

In imperative languages like python variables can be accessed or changed anytime you like, in declarative languages variables are generally bound to expressions and keep a single value during their entire lifetime.

The advantage of having immutable variables contains:
- It solves many multi-threading problems where we might have multiple threads trying to change a single shared variable at the same time.
- Another benefit is that if we have a guarantee that a variable never changes, our programs become a lot easier to understand and are also much easier to test. 