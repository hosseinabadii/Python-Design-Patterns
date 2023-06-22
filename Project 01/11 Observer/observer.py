class Subject:
    '''Represent what is being observed'''

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
        else:
            print(f'The {observer} already exists!')

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
                print(f'The {str(observer)} not exists!')

    def notify(self):
        for observer in self._observers:
            if observer._access != True:
                observer.update(self)


class Core(Subject):
    '''Core is an example for Subject'''

    def __init__(self, name=''):
        super().__init__()
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp
    
    def change_temp(self, observer, temp):

        if not isinstance(observer, TempObserver):
            print(f'{str(observer)}: You are not an observer!')
            
        if observer in self._observers:
            if observer._access == True:
                self._temp = temp
                self.notify()
            else:
                print(f'{observer}: You don\'t have access to change the Temperature!')
        else:
            print(f'{observer}: You are not in observers list!')


class TempObserver:
    '''TempObserver objects are observers'''

    def __init__(self, name, access=False):
        self._name = name
        self._access = access
    
    def update(self, subject):
        print(f'{self._name}: {subject._name} Temperature Changed to {subject.temp}')

    def __str__(self):
        return self._name
