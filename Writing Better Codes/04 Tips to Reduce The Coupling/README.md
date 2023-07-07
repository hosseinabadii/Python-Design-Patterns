# 5 tips to reduce coupling

## What is coupling?

Coupling is the degree of interdependence between software modules; a measure of how closely connected two routines or modules are; the strength of the relationships between modules.

You can never completely remove coupling. In fact, without any coupling you'd have a bunch of completely unrelated pieces of code that won't be able to work together. Coupling is needed in some places in your code. And if you're careful about where you introduce coupling, you can really improve your code and make it much easier to maintain later on.

## Tip 1: Avoid deep inheritance hierarchies

Inheritance is one of the strongest form of coupling.

## Tip 2: Separate creation from use

It's good practice to separate creation from use.

## Tip 3: Introduce abstraction

You can use protocol classes to introduce abstraction and remove the direct dependency.

Note that this is why Protocol classes are useful. Sometime you can't use ABCs in this way, because then you would have to change the third-party class to be a subclass of an abstract class. But you can solve it with protocols and structural typing without having to change anything at all in the third-party class.

There are also some design patterns that can help with separating creation from use and introducing abstract, such as the Abstract Factory.

## Tip 4: Avoid inappropriate intimacy

Inappropriate intimacy refers to a method in a class that has too much intimate knowledge of another class. Inappropriate intimacy is a sign of harmful, tight coupling between classes.

## Tip 5: Introduce an intermediate data structure

Sometimes, you have a piece of code that seems really tangled with lots of coupling and you're having a hard time decreasing coupling because the code is quite complex. In this case, it might be very hard to apply the things I mentioned earlier. Something that can work really well in this case is to introduce an intermediate data structure and use that as a separation layer between the different areas of your code.
