import random
import re
from lab_1 import Lab1, Triangle
from utilit import TestLib

class TestLab1(TestLib.TestLib):

    def __init__(self):
        super().__init__(Lab1.Lab1())

    @staticmethod
    def testTask1RandomNumber():
        num = random.randint(0, 10)
        result = Lab1.Lab1.task1(num)
        return False if result == None else True
    
    def testTask2RealTriangle(self):
        triangle = Triangle.Triangle().triangle
        result = self.lab.task2(triangle)
        return False if result == None else True
    
    def testTask3CurrentLuckyTiket(self):
        tiket = "444444"
        return True if self.lab.task3(tiket) == True else False
    
    def testTask3CurrentUnluckyTiket(self):
        tiket = "444555"
        return True if self.lab.task3(tiket) == False else False
    
    def testTask3NotCurrentTiket(self):
        tiket = "55555"
        return self.lab.task3(tiket) == None
            
    
    def testTask4FormatTime(self):
        minutes = random.randint(360, 600)
        minutes = str(minutes)
        try:
            result = self.lab.task4(minutes)
            return True if 0 <= result[0] <= 23 and 0 <= result[1] <= 59 else False
        except ValueError:
            return False
        
    def testTask5CurrentData(self):
        birthd = "31-12-2004"
        return isinstance(self.lab.task5(birthd), int)
        
    def testTask6Celsius(self):
        temperature = "32.2C"
        pattern = r"^-?\d{1,3}(?:[.,]\d{1,2})?[C]$"
        return re.search(pattern, self.lab.task6(temperature))
    
    def testTask6Fahrenheit(self):
        temperature = "32.2F"
        pattern = r"^-?\d{1,3}(?:[.,]\d{1,2})?[F]$"
        return re.search(pattern, self.lab.task6(temperature))
    
    def testTask7SpeedKilometr(self):
        speed = "60"
        result = self.lab.task7(speed)
        return False if result == None or float(speed) <= 0 else True

    def testTask8SityDistance(self):
        sity1 = (5, 4)
        sity2 = (3, 5)
        distance = self.lab.task8(sity1, sity2)
        return True if distance is not None and distance >= 0 else False
    
    def testTask9PrimeNumbers(self):
        num = 20
        currentResult = [2, 3, 5, 7, 11, 13, 17, 19]
        primes = self.lab.task9(num)
        return primes == currentResult
    
    def testTask10CorrectData(self):
        apple = 10
        try:
            Lab1.Lab1.task10(apple)
            return True
        except Exception:
            return False
        
