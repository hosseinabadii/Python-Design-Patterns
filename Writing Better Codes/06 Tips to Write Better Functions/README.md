# The ultimate guide to writing great functions

Writing great, well-designed functions is hard and takes a lot of practice.

## 1. Do one thing and do it well

Your function should do a single task. But some time while doing a single task we indirectly do other sub tasks also. So the question is are we breaching the rule in that case? The answer might be No if we have maintained the same level of abstraction inside that function.

In general, function should change the state of an object or it should return some information about that object, not both.


## 2. Separate Commands from Queries

In general, make sure that a function either retrieves information (does a query) or performs an action (a command), but not both. This is a principle called the Command-Query Separation principle, which was thought by Bertrand Meyer. He’s the one who came up with the idea of Design by Contract, he originated the Open-Closed Principle and he also created a programming language called Eiffel.

## 3. Only request information you actually need

When a function doesn’t need the full information of an object to do some job, try to splitting out the arguments. (this is also called inappropriate intimacy).

If your function has multiple arguments, a great way to make your function clearer is by forcing the use of keyword arguments. You can use the asterisk in Python for this.

## 4. Keep the number of arguments minimal

It is always a good practice to keep arguments to a function minimum. Because it demands a lot of conceptual power if we use many arguments. It is more harder from testing point of view also. Out argument is even more confusing because we do not usually expect information to be going out through the arguments.

## 5. Don’t create and use an object at the same time

It makes the function hard to test. To solve this, use dependency injection to provide the object that the function uses. This also makes testing the function a lot easier. An even better approach is to also introduce abstraction. This way, you can turn dependency injection into dependency inversion. This makes testing the code even easier, because you can easily create your own mock object to replace the class as long as it follows the interface that you specified.

## 6. Remember that functions are objects

Because like anything else in Python, functions are objects, you can compose them in different ways, leading to interesting patterns that are generally shorter than if you would implement those same patterns using object-oriented programming. A function can get another function as an argument, a function can even return another function.

To specify the type, use `Callable`.

You can use **partial function application**. Partial gets a function as an argument + any argument value of that function, and then it returns a new function, with those argument values already applied.

## 7. Don’t use flag arguments

If you see a function that has a flag argument, that’s a serious “red flag”. Most often, it means that the function actually does two things: one thing when the flag is true and another thing when the flag is false. 

Not always, there are cases where a flag is simply a setting that’s passed along. But in many cases, it’s better to split up the function.

## 8. Tips for naming functions and arguments

- If a function has “and” in the name, check that the function does one thing. Names like `create_user_and_store_in_db` or `register_and_send_welcome_email` are red flags. These functions should probably be split up.

- Choosing good argument names helps with readability and allows your function name to be shorter in some cases. For example, `publish_info_to_library(lib)` can be shortened to `publish_info_to(library)`.

- Function names should be actions (there should be a verb in there) and arguments should be nouns. So, instead of `greeting(say_hi_to: str)` use `greet(name: str)`.

- Make sure you use the same vocabulary everywhere. If you call something an `article` somewhere, don’t call it a `story` or an `essay` somewhere else. If you call a collection of articles a `library`, use that everywhere, don’t use `l` or `lib` in half of the places and `library` everywhere else.

- Use the naming scheme that the language prescribes. In case of Python, it’s snake case, not camel case.

- Make sure there are no typos or grammar issues in your function names. Is especially frustrating if you’re a grammar nazi like myself to have to use `is_memebr`or `are_order_paid`. And then you actually have to type that when you call the function.

