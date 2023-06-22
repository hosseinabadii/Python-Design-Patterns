import copy

class Prototype:
    
    def __init__(self):
        self._objects = {}
        
    def register_object(self, name, obj):
        self._objects[name] = obj
        
    def unregister_object(self, name):
        del self._objects[name]
        
    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(**kwargs)
        return obj
    

class Car:
    
    def __init__(self):
        self.name = 'Renoult'
        self.color = 'Red'
        self.tires = 'Ex'
        
    def __str__(self):
        return f'{self.name} | {self.color} | {self.tires}'
    

if __name__ == "__main__":
    car = Car()
    prototype = Prototype()
    prototype.register_object(car.name, car)
    new_car = prototype.clone('Renoult')
    print(car)
    print(new_car)