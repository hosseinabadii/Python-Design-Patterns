class Composite:
    '''Concrete class and maintain the tree recursive structure'''

    def __init__(self, *args):
        self.name = args[0]
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def component_function(self):
        print(self.name)

        for child in self.children:

            print(' - ', end='')
            child.component_function()
            

class Child:
    '''Concrete class'''

    def __init__(self, *args):
        self.name = args[0]

    def component_function(self):
        print(f' -- {self.name}')
