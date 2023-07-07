## #1: Abusing types for something else

  - Using a `str` type to distinguish between roles. But str can basically be anything. For example Use `enum` instead of `str`.

## #2: Duplicate code

  - Remove duplicate code from your program.

## #3: Not using available built-in functions

  - Python has lots of built-in methods to make your life easier. Use `list comprehensions`, `map`, `filter` and etc. 

## #4: Vague identifiers

  - Don't use vague name that doesn't explain at all what the variable means and what the unit is.

## #5: Using isinstance to separate behavior

  - Don't use isinstance because it leads to a lot of coupling in your code.

## #6: Using boolean flags to make a method do 2 different things

  - Don't use the approach This because it leads to low cohesion (one method having too many responsibilities), and methods that are harder to understand what they do.

## #7: Empty catch/except clause

  - Don't use empty catch/except clause, because exceptions are now ignored completely, and can't be handled outside of the method call anymore. Even worse: these kinds of catch-all blocks can even ignore SyntaxError or KeyboardInterrupt exceptions in some cases.
  - If you can't do anything with an exception, don't catch it and ignore it, another part of your program might be able to deal with it

## #8 Use custom exceptions

- Create a custom exceptions containing useful error data.
