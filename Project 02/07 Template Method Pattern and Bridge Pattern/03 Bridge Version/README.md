# Bridge Pattern

The Bridge Pattern is a structural design pattern that is used to separate the abstraction from its implementation.

Abstraction means the high-level logic and implementation means the low-level details of how that logic is actually carried out.

The Bridge Pattern is useful when you have a class hierarchy that has two independent dimensions of variation, such as two different types of objects that can vary independently. In this pattern, you create an abstraction class that defines the high-level logic and a separate implementation class that defines the low-level details of how that logic is carried out. The abstraction class contains a reference to the implementation class, and delegates the implementation details to it.

By separating the abstraction from its implementation, you can change or modify each independently without affecting the other. This provides a greater degree of flexibility and allows for more efficient reuse of code.

For example, suppose you have a shape hierarchy that includes different types of shapes (such as circles, squares, and triangles) and different types of drawing tools (such as pens, pencils, and brushes) that can be used to draw them. Using the Bridge Pattern, you could create an abstraction class called "Shape" that defines the high-level logic for drawing a shape, and a separate implementation class called "DrawingTool" that defines the low-level details of how that shape is actually drawn. The Shape class would contain a reference to the DrawingTool class, and would delegate the actual drawing to it.

In summary, the Bridge Pattern is a design pattern that separates the abstraction from its implementation, allowing each to vary independently and providing greater flexibility and code reuse.