class Persian:
    def __init__(self):
        self.name = 'Persian'
    
    def speak_persian(self):
        return 'Salam!'
    

class English:
    def __init__(self):
        self.name = 'English'
    
    def speak_english(self):
        return 'Hello!'
    

class Adapter:
    def __init__(self, obj, **adapter_method):
        self.name = obj.name
        self.__dict__.update(adapter_method)
        

if __name__ == "__main__":
    persian = Persian()
    persian1 = Adapter(persian, speak=persian.speak_persian())
    english = English()
    english1 = Adapter(english, speak=english.speak_english())

    print(f"{persian1.name} says: {persian1.speak}")
    print(f"{english1.name} says: {english1.speak}")