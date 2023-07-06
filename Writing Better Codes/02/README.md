## #1: Large number of arguments

Overall: avoid methods with more than 3 or 4 arguments.

## #2: Too deep nesting

Too deep nesting is generally a sign of code that has low cohesion (too many responsibilities)

## #3: Use the right datastructure

Use the right datastructure: list, dictionary

## #4: Using nested conditional expressions

When you use nested conditional expressions the code becomes really hard to read

Split the conditional expression into two.

Conditional expression is useful if the variable names and results are short so it fits comfortably in a single line.

## #5: Using wildcard imports

Don't do this because it clutters up the namespace and may lead to you accidentally redefining functions or variables that you shouldn't.

Replace the wildcard import by importing the module directly (i.e. `import string`).

## #6: Asymmetrical code

Asymmetrical code is when you have similar code in different places that is named or handled differently.

## #7: Methods that don't need self

If a method doesn't use self, it should be a static method. It's simply part of a class because it makes sense.

## #8: Not using a main function in a module

If you don't use a main function, this means that any variables you declare under the `if __name__ == "__main__":` part are in the global scope of the module, which can lead to unexpected bugs, shadowing variables that you also use somewhere else, etc.
