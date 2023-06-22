import time

class Producer:
    '''Define the 'resource-intensive' object to instantiate'''
    
    def produce(self):
        print('Producer is working hard!')
        
    def meet(self):
        print('Producer is available!')


class Proxy:
    '''Define the relatively less resource-intensive proxy'''
        
    def __init__(self):
        self.occupied = 'No'
        self.producer = None
        
    def produce(self):
        print('Artist checking if Producer is available...')
        
        if self.occupied == 'No':
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()  
        else:
            time.sleep(2)
            print('Producer is busy!')


if __name__ == "__main__":
    p = Proxy()
    p.produce()
    print()
    p.occupied = 'Yes'
    p.produce()