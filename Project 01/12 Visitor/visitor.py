from abc import ABC, abstractclassmethod

class House:

    def accept(self, visitor):
        '''Interface to accept a visitor'''
        visitor.visit(self)

    def _work_on_hvac(self, hvac_specialist):
        print(f'{self} worked on by {hvac_specialist}')

    def _work_on_electricity(self, electrician):
        print(f'{self} worked on by {electrician}')

    def __str__(self):
        return self.__class__.__name__
    

class Visitor(ABC):
    '''Abstract visitor'''

    @abstractclassmethod
    def visit(self):
        pass

    def __str__(self):
        return self.__class__.__name__
    

class HvacSpecialist(Visitor):
    '''Concrete visitor: HVAC spacialist'''

    def visit(self, house):
        house._work_on_hvac(self)


class Electrician(Visitor):
    '''Concrete visitor: Electrician'''

    def visit(self, house):
        house._work_on_electricity(self)