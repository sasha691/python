import math
import datetime
import re
from utils import LabLib, Triangle

class Lab1(LabLib.Lab):
    @staticmethod
    def task1(x = None):
        if x == None:
            x = input("x = ")
        try:
            x = int(x)
            a = math.exp(-x) - x * math.sin(x) - math.log(x) ** 2
            b = math.log10(abs(math.cos(x))) + (math.cos(x ** 2 - 1) / math.sin(x ** 2 -1))
            z = a / b
            print(f"z = {z:.2f}")
            return f"{z:.2f}"
        except ValueError:
            print("Невірно введене значення")
            return
        except ZeroDivisionError:
            print("Здійснено ділення на нуль")
            return
        
    def task2(self, triangle: list = None):
        try:
            if triangle == None:
                triangle = [int(input('Введіть сторону трикутника')) for _ in range(3)]
            if not Triangle.Triangle.isRealTriangle(triangle):
                print("Трикутник неможливий")
                return
            triangle = map(int, triangle)
            a, b, c = triangle
            p = (a + b + c) / 2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"Площа трикутника дорівнює {s:.2f}")
            return s
        except ValueError as e:
            print(f"Невірно введене значення: {e}")
            return
        
    def task3(self, tiket: str = None) -> int:
        if tiket == None:
            tiket = input("Введіть шестизначний номер: ")
        if not self._isValidateNumber(tiket, 6):
            print("Невірний білет")
            return
        result = sum(map(int, tiket[:3])) == sum(map(int, tiket[3:]))
        print(f"Щасливий квиток {tiket}? {result}")
        return result   

    def task4(self, minutes: str = None) -> list:
        if minutes == None:
            minutes = input("X = ")
        if not self._isValidateNumber(minutes):
            print("не число")
        minutes = int(minutes)
        hour = minutes // 60
        minutes = minutes % 60
        print(f"{hour} годин {minutes} хвилин")
        return hour, minutes
    
    @staticmethod
    def task5(birthd: str = None) -> int:
        if birthd == None:
            birthd = input("Введіть дату народження в у форматі «день-місяць-рік»: ")
        try:
            day, month, year = map(int, birthd.split('-'))
            date = datetime.date(year, month, day)
        except ValueError:
            print("невірні дані")
            return
        now = datetime.datetime.now().date()
        result = now - date
        result = result.days // 365
        print(result)
        return result
        
    def task6(self, temperature: str = None) -> str:
        if temperature == None:
            temperature = input("Введіть температуру у форматі «37.00C»: ")
        pattern = r"^-?\d{1,3}(?:[.,]\d{1,2})?[CF]$"
        if not re.search(pattern, temperature):
            print("Невірно введене значення")
            return
        temperature = temperature.replace(',', '.')
        if re.search(r"F$", temperature):
            result = f"{self._findFahrenheit(temperature):.2f}F"
        else:
            result = f"{self._findCelsius(temperature):.2f}C"
        print(result)
        return result

    @staticmethod
    def _findFahrenheit(value: str) -> float:
        temperature = float(value[:-1])
        fahrenheit = (temperature * 9 / 5) + 32
        return fahrenheit
    
    @staticmethod
    def _findCelsius(value: str) -> float:
        temperature = float(value[:-1])
        celsius = (temperature - 32) * 5 / 9
        return celsius
    
    def task7(self, speed: str = None) -> int:
        speedList = {
            "1": "meter",
            "2": "kilometer"
        }
        speedFunctions = {
            "meter": self._convertToMeters,
            "kilometer": self._convertToKilometers
        }
        if speed == None:
            speed = input("введіть швидкість: ")
        type = self._inputTypeConvertSpeed(speedList)
        if type in speedFunctions:
            result = speedFunctions[type](speed)
            print(f"Конвертована швидкість: {result}")
            return result
        else:
            print("Невірний тип швидкості!")
            return

    def _inputTypeConvertSpeed(self, dictionary):
        type = input(f"введіть потрібну розмірність({', '.join(dictionary.values())}) за замовчуванням 1 : ")
        if self._isValidateNumber(type) and type in dictionary:
            return dictionary[type]
        print("Виникла помилка. Буде використано значення за замовчуванням")
        return dictionary["1"]
    
    def _convertToMeters(self, speed: str) -> float:
        speedNum = float(speed)
        return speedNum * 1000

    def _convertToKilometers(self, speed: str) -> float:
        speedNum = float(speed)
        return speedNum / 1000

    def task8(self, sity1: tuple = None, sity2: tuple = None) -> float:
        try:
            sity1 = sity1 if sity1 is not None else self._initSity()
            sity2 = sity2 if sity2 is not None else self._initSity()

            lat1Radian = math.radians(sity1[0])
            lon1Radian = math.radians(sity1[1])
            lat2Radian = math.radians(sity2[0])
            lon2Radian = math.radians(sity2[1])

            dlat = lat2Radian - lat1Radian
            dlon = lon2Radian - lon1Radian

            a = math.sin(dlat / 2) ** 2 + math.cos(lat1Radian) * math.cos(lat2Radian) * math.sin(dlon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            return 6371.0 * c
        except Exception:
            print('Невірно введенні значення')
            return

    @staticmethod
    def _initSity() -> tuple:
        lat = float(input("Введіть широту міста: "))
        lon = float(input("Введіть довготу міста: "))
        return (lat, lon)
    
    def task9(self, num: int = None) -> list:
        try:
            if num == None:
                num = int(input("Введіть межу: "))
            primeNums = self._findPrimeNumber(num)
            print(f"Прості числа у діапазоні від 1 до {num}: {primeNums}")
        except ValueError:
            print("Неправильне значення")
            return
        
    @staticmethod
    def _isPrime(num: int) -> bool:
     if num < 2:
          return False
     for i in range(2, int(math.sqrt(num) + 1)):
          if num % i == 0:
               return False
     return True

    def _findPrimeNumber(self, limit: int) -> list:
        if limit <= 0:
            raise ValueError
        listNum = [i for i in range(2, limit) if self._isPrime(i)]
        return listNum
    
    @staticmethod
    def task10(apple: int = None) -> None:
        if apple == None:
            apple = int(input("Введіть кількість"))
        if apple < 0:
            print("Помилка")
            return
        print(f"Кількість повних упаковок: {apple // 6}")
        print(f"Залишок яблук поза упаковками: {apple % 6}")