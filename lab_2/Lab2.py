from utils import LabLib, Triangle
import math
import numpy as np

class Lab2(LabLib.Lab):
    
    @staticmethod
    def task1(x: float = None, y: float = None) -> bool:
        try:
            if x == None or y == None:
                x = float(input('x = '))
                y = float(input('y = '))
            if x**2 + y**2 <= 2**2 and x**2 + y**2 >= 1 and y >= 0:
                print("Точка входить в діапазон")
                return True
            else:
                print("Точка не входить в діапазон")
                return False
        except ValueError:
            print("Невірні значення")

    def task2(self, num: str = None):
        if num == None:
            num = input("Введіть число: ")
        if not self._isValidateNumber(num, 4):
            print("Невірне введення")
            return
        print(f"містить цифру 5: {num in '5'}")
        print(f"складається лише з непарних чисел: {all(int(i) % 2 != 0 for i in num)}")
        print(f"сума його цифр більша за число 10: {sum(int(i) for i in num) > 10}")
        print(f"сума його перших двох цифр менша за суму наступних двох цифр: \
              {sum(map(int, num[:2])) < sum(map(int, num[2:]))}")

    def task3(self, triangle: list = None):
        try:
            if triangle == None:
                triangle = [int(input('Введіть сторону трикутника')) for _ in range(3)]
            return Triangle.Triangle.determineTypeTriangle(triangle)
        except ValueError as e:
            print(f"Невірно введене значення: {e}")

    @staticmethod
    def task4(move: list = None) -> bool:
        try:
            if move == None:
                move = [int(input("Введіть положення")) for _ in range(4)]
            if not all(map(lambda x: 0 < x <= 8, move)):
                raise ValueError("Усі числа повинні бути в межах від 1 до 8")
            x1, y1, x2, y2  = move
            if x1 == x2 or y1 == y2:
                print("YES")
                return True
            else:
                print("NO")
                return False
        except Exception as e:
            print(f"Невірно введене значення: {e}")
            return
        
    def task5(self) -> list:
        x = 0.3
        print(self._taskFor(x), self._taskWhile(x))
        return [self._taskFor(x), self._taskWhile(x)]

    @staticmethod
    def _taskFor(x: int) -> float:
        result = 0
        for j in range(1, 11):
            for i in range(1, 6):
                result += (i**2 + x**i + 1) / (math.factorial(j) + i**2)
        return result

    @staticmethod   
    def _taskWhile(x: int) -> float:
        result = 0
        j = 1
        while j <= 10:
            i = 1
            while i <= 5:
                result += (i**2 + x**i + 1) / (math.factorial(j) + i**2)
                i += 1 
            j += 1
        return result
    
    def task6(self, box1: tuple = None, box2: tuple = None):
        try:
            if box1 == None or box2 == None:
                A, B, C = map(int, input('Введіть розміри першої коробки (A1 B1 C1): ').split())
                box1 = (A, B, C)
                A, B, C = map(int, input('Введіть розміри другої коробки (A1 B1 C1): ').split())
                box2 = (A, B, C)
            if box1 == box2:
                print('Коробки однакові')
                return True
            elif self._canFit(box1, box2):
                print("Першу коробку можна покласти в другу")
                return box1
            elif self._canFit(box2, box1):
                print("Другу коробку можна покласти в першу")
                return box2
            else:
                print('Коробки не розміщуються одна в одну')
                return False
        except Exception as e:
            print(f"Невірний ввід {e}")

    @staticmethod
    def _canFit(box1: tuple, box2: tuple) -> bool:
        return all(b1 <= b2 for b1, b2 in zip(sorted(box1), sorted(box2)))
    
    def task7(self, sides: list = None):
        if sides == None:
            sides = [input("Введіть довжину відрізка") for _ in range(4)]
        try:
            if not all(map(self._isValidateNumber, sides)):
                raise ValueError()
            sides = sorted(list(map(int, sides)))
            if sides[0] == sides[1] and sides[2] == sides[3]:
                print('З цих відрізків можна утворити прямокутник')
                return True
            else:
                print("З цих відрізків не можна утворити прямокутник")
                return False
        except ValueError:
            print("Невірно введене значення")

    def task8(self, num: str = None):
        if num == None:
            num = input("Введіть 3 значне число")
        try:
            if not self._isValidateNumber(num, 3):
                raise ValueError()
            h, t, u = list(map(int, num))
            word = []
            word.append(self._hundreds[h])
            if t == 1 and u > 0:
                word.append(self._teens[u])
            else:
                word.append(self._tens[t])
            word.append(self._units[u])
            print(' '.join(word).strip())
        except ValueError as e:
            print(f"Невірно введене значення: {e}")

    def task9(self, num: int = None):
        try:
            if num == None:
                num = int(input("n = "))
            if num <= 0:
                raise ValueError()
            result = 1
            for i in range(1, num + 1, 2):
                result *= i
            print(f"Добуток простих чисел = {result}")
            return result
        except ValueError as e:
            print(f"Невірно введене значення: {e}")

    def task10(self):
        print(" x       |  sin(x)")
        print("-------------------")
        x = 0
        while x <= 1:
            y = math.sin(x)
            print(f"{x:.1f}     |  {y:.5f}")
            x += 0.1

    def task11(self):
        try:
            n = int(input("Введіть кількість елементів"))
            nums = [int(input("Введіть елемент")) for _ in range(n)]
        except ValueError as e:
            print(f"Невірно введене значення: {e}")
            return
        minNum = min(nums)
        indices = [2**i - 1 for i in range(len(nums)) if 2**i - 1 < len(nums)]
        elements = [nums[i] for i in indices]
        maxNum = max(elements)
        print(f"max: {maxNum}")
        print(f"min: {minNum}")

        nums = np.array(nums)
        values, counts = np.unique(nums, return_counts=True)
        maxCount = counts.max()
        modeValues = values[counts == maxCount]
        if maxCount > 1:
            print("Мода послідовності:", modeValues)
        else:
            print("Мода відсутня (усі елементи унікальні).")

        medianValue = np.median(nums)
        print("Медіана послідовності:", medianValue)

        mean = np.mean(nums)
        stdDev = np.std(nums)
        threeSigmaUpper = mean + 3 * stdDev
        threeSigmaLower = mean - 3 * stdDev

        anomalies = nums[(nums > threeSigmaUpper) | (nums < threeSigmaLower)]
        if anomalies.size > 0:
            print("Аномальні значення, що виходять за межі 3 сигм:", anomalies)
        else:
            print("Аномальні значення відсутні.")
        