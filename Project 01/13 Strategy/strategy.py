import types

class Strategy:

    name = 'Default Strategy'

    def __init__(self, function=None):
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print(f'{Strategy.name} is used!')


def strategy_one(obj):
    obj.name = 'Strategy One'
    print(f'{obj.name} is used to execute method 1')

def strategy_two(obj):
    obj.name = 'Strategy Two'
    print(f'{obj.name} is used to execute method 2')