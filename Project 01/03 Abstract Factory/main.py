class Dog:
    '''One of the objects to be returned'''
    food='dog food'
        
    def speak(self):
        return 'Woof'
    
    def __str__(self):
        return self.__class__.__name__
    
#----------------------------------
class DogFactory:
    '''Concrete Factory'''
    
    def get_pet(self):
        '''Returns a Dog Object'''
        return Dog()
    
    def get_food(self):
        '''Returns a Dog Food Object'''
        return Dog.food
    
#-----------------------------------
class Cat:
    '''One of the objects to be returned'''
    food='cat food'
        
    def speak(self):
        return 'Meow'
    
    def __str__(self):
        return self.__class__.__name__
    
#----------------------------------
class CatFactory:
    '''Concrete Factory'''
    
    def get_pet(self):
        '''Returns a Dog Object'''
        return Cat()
    
    def get_food(self):
        '''Returns a Dog Food Object'''
        return Cat.food

#--------------------------------------
class PetStore:
    '''PetStore houses our Abstract Factory'''
    
    def __init__(self, pet_factory=None):
        '''pet_fatcory is our Abstract Factory'''
        self._pet_factory = pet_factory
        
    def show_pet(self):
        '''Utility method to display the details
        of the objects returned'''
        
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print(f'{"Our pet is ":.<18} {str(pet)!r}')
        print(f'{"Our pet says ":.<18} {pet.speak()!r}')
        print(f'{"Its food is ":.<18} {pet_food!r}')


if __name__ == "__main__":
    # Create a pet store
    shop1 = PetStore(DogFactory())
    shop1.show_pet()
    print()
    shop2 = PetStore(CatFactory())
    shop2.show_pet()