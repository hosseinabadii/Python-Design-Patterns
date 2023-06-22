class Car:
    
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
        
    def __str__(self):
        return f'{self.model} | {self.tires} | {self.engine}'
    

class Director:
    def __init__(self, builder):
        self._builder = builder
        
    def construct_car(self):
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

        return self._builder.car
    

class Builder:
    '''Abstract Builder'''
    def __init__(self):
        self.car = Car()
        