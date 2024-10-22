import random
from functools import singledispatch

class Lab:
    def __init__(self):
        pass

    def __call__(self, **args):
        methods = [getattr(self, method) for method in dir(self) if
                   callable(getattr(self, method)) and not method.startswith('_')]
        for method in methods:
            print(method.__name__)
            method()


    @staticmethod
    def _isValidateNumber(value: str, length:int = None) -> bool:
        if length == None:
            return value.isdigit()
        else:
            return value.isdigit() and len(value) == length


    

    
