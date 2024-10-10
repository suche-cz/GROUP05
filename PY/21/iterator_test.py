# iterator_test.py
import random

class MyIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.max_count:
            self.counter += 1
            return random.randint(1, 100)
        else:
            raise StopIteration()


my_iterator = MyIterator(10)
# print(next(my_iterator))
# print(next(my_iterator))

for item in my_iterator:
    print(item)
