from utilit import LabLib
from utilit.MorseCode import MorseCode
from functools import wraps
from urllib.parse import urlparse, parse_qs
import os

class Lab4(LabLib.Lab):
    @staticmethod
    def task1(number: int = None):
        if number is None:
            number = int(input("Введіть число: "))
        if number <= 1:
            print(False)
            return False
        if number <= 3:
            print(True)
            return True
        if number % 2 == 0 or number % 3 == 0:
            print(False)
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                print(False)
                return False
            i += 6
        print(True)
        return True

    def task2(self):
        happy_numbers = []
        for num in range(100_000, 1_000_000):
            first_half = num // 1000
            second_half = num % 1000
            if self._sum_of_digits(first_half) == self._sum_of_digits(second_half):
                happy_numbers.append(num)
        return happy_numbers

    @staticmethod
    def _sum_of_digits(number):
        return sum(int(digit) for digit in str(number))
    
    @staticmethod
    def task3():
        message = input('Введіть текст: ')
        print(MorseCode.decrypt(message))

    @staticmethod
    def task4(input_filename: str = 'README.md', output_filename: str = 'README.md', key: str = 'wwwwwww') -> None:
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()
        key_length = len(key)
        encrypted_content = ''.join(
            chr(ord(char) ^ ord(key[i % key_length])) for i, char in enumerate(content)
        )
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(encrypted_content)

    def task5(self):
        number = 53829
        print("Сума цифр:", self._sum_of_digits(number))
        print("Кількість цифр:", self._count_digits(number))
        print("Максимальна цифра:", self._max_digit(number))
        print("Мінімальна цифра:", self._min_digit(number))

    def _sum_of_digits(self, n: int) -> int:
        n = abs(n) 
        if n == 0:
            return 0
        return n % 10 + self._sum_of_digits(n // 10)

    def _count_digits(self, n: int) -> int:
        n = abs(n) 
        if n < 10:
            return 1
        return 1 + self._count_digits(n // 10)

    def _max_digit(self, n: int) -> int:
        n = abs(n) 
        if n < 10:
            return n
        return max(n % 10, self._max_digit(n // 10))

    def _min_digit(self, n: int) -> int:
        n = abs(n)
        if n < 10:
            return n
        return min(n % 10, self._min_digit(n // 10))
    
    @staticmethod
    def task6(*arg_types, **kwarg_types):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for i, (arg, expected_type) in enumerate(zip(args, arg_types)):
                    if not isinstance(arg, expected_type):
                        raise TypeError(f"Аргумент {i + 1} має бути типу {expected_type.__name__}, але отримано {type(arg).__name__}")

                for key, expected_type in kwarg_types.items():
                    if key in kwargs and not isinstance(kwargs[key], expected_type):
                        raise TypeError(f"Аргумент '{key}' має бути типу {expected_type.__name__}, але отримано {type(kwargs[key]).__name__}")
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @staticmethod
    def task7(n = 100):
        if n < 2:
            return False
        
        divisors_sum = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
        return divisors_sum == n

    def task8(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Виникла помилка: {e.__class__.__name__}: {e}")
        return wrapper
    
    @staticmethod
    def task9():
        row = [1]
        while True:
            yield row
            row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

    @staticmethod
    def task10(url: str = 'https://google.com'):
        parsed_url = urlparse(url)
        result = {
            'scheme': parsed_url.scheme,
            'domain': parsed_url.netloc,
            'path': parsed_url.path,
            'params': parsed_url.params,
            'query': parse_qs(parsed_url.query),
            'fragment': parsed_url.fragment
        }
        print(result)
        return result
    
    def task11(self, directory = './lab_4', extension = '.py'):
        found_files = []
        
        for entry in os.listdir(directory):
            path = os.path.join(directory, entry)
            
            if os.path.isfile(path) and path.endswith(extension):
                found_files.append(path)
            
            elif os.path.isdir(path):
                found_files.extend(self.task11(path, extension))
        print(found_files)
        return found_files
