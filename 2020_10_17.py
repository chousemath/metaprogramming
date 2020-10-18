from typing import Callable
import requests

# Metaclass use case 1:
# * you can use a metaclass to enforce what kinds
#   of methods all children of that metaclass must
#   have to be valid

class MetaPerson(type):
    def __new__(cls, *args, **kwargs):
        """
        Called whenever a class is instantiated and
        it is called before the __init__ method
        """

        dict = args[2]
        # enforce the "speak" method requirement
        # for all classes that inherit from the
        # MetaPerson metaclass
        if 'speak' not in dict:
            raise Exception("person must speak")

        # you can modify and add methods before they
        # are passed to the actual class
        def metaify(func: Callable) -> Callable:
            def modified_func(self):
                print('\n*modified through metaclass')
                func(self)
            return modified_func

        new_dict = {f'_{k}': metaify(v) for k,v in dict.items() if 'run' in k}
        new_args = (args[0], args[1], {**dict, **new_dict})


        #print(new_args)
        return type.__new__(cls, *new_args, **kwargs)

class Person(metaclass=MetaPerson):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self):
        print(f'Hi, my name is {self.name}, I am {self.age} years old.')

    def run(self):
        print('I run')

p = Person(name='Jo', age=30)
p.speak()
p.run()
p._run()







r = requests.get('https://raw.githubusercontent.com/chousemath/metaprogramming/master/2020_10_17_0.txt')
exec(r.text)
from_internet()
