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


    _units = {0: "", 1: "один", 2: "два", 3: "три", 4: "чотири", 
             5: "п'ять", 6: "шість", 7: "сім", 8: "вісім", 9: "дев'ять"}
    
    _teens = {0: "десять", 1: "одинадцять", 2: "дванадцять", 3: "тринадцять", 
             4: "чотирнадцять", 5: "п'ятнадцять", 6: "шістнадцять", 
             7: "сімнадцять", 8: "вісімнадцять", 9: "дев'ятнадцять"}
    
    _tens = {0: "", 1: "десять", 2: "двадцять", 3: "тридцять", 
            4: "сорок", 5: "п'ятдесят", 6: "шістдесят", 
            7: "сімдесят", 8: "вісімдесят", 9: "дев’яносто"}
    
    _hundreds = {0: "", 1: "сто", 2: "двісті", 3: "триста", 
                4: "чотириста", 5: "п'ятсот", 6: "шістсот", 
                7: "сімсот", 8: "вісімсот", 9: "дев'ятсот"}


    
