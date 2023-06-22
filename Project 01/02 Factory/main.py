class Dog:
    '''A simpel dog class'''
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return 'Woof!'

 
class Cat:
    '''A simple cat class'''
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return 'MeoW!'
    

def get_pet(pet='dog'):
    '''The Factory Method'''
    
    pets = {
        'dog': Dog('A dog'),
        'cat': Cat('A cat'),
    } 
    
    return pets[pet]


if __name__ == "__main__":
    dog_obj = get_pet()
    print(f"{dog_obj.name} says: {dog_obj.speak()}")

    cat_obj = get_pet('cat')
    print(f"{cat_obj.name} says: {cat_obj.speak()}")