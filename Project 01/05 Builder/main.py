from builder import Builder, Director

class SkyLarkBuilder(Builder):
    
    def add_model(self):
        self.car.model = 'Skylark'
        
    def add_tires(self):
        self.car.tires = 4
        
    def add_engine(self):
        self.car.engine = 'Turbo Engine'
    

class RenoultBuilder(Builder):
    
    def add_model(self):
        self.car.model = 'Renoult'
        
    def add_tires(self):
        self.car.tires = 4
        
    def add_engine(self):
        self.car.engine = 'Heavy Engine'
    

if __name__ == '__main__':

    builders = [SkyLarkBuilder, RenoultBuilder]
    for builder in builders:
        director = Director(builder())
        car = director.construct_car()
        print(car)