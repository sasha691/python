from utilit import LabLib
from utilit import Student, Human
from collections import Counter, defaultdict
from itertools import combinations
import random, math

class Lab3(LabLib.Lab):
    
    @staticmethod
    def task1(nums: list = None) -> bool:
        try:
            if nums == None:
                n = int(input("Введіть кількість "))
                nums = [int(input("Введіть елемент ") for _ in range(n))]
        except ValueError as e:
            print(f"Невірно введене значення: {e}")
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                return False
        return True
    
    def task2():
        nums = [random.randint(1, 9) for _ in range(100)]
        countStart = sum(1 for num in nums if 1 <= num <= 3)
        countMidl = sum(1 for num in nums if 4 <= num <= 6)
        countEnd = sum(1 for num in nums if 7 <= num <= 9)
        print(f"Start: {countStart}\nMidl: {countMidl}\nEnd: {countEnd}")

    @staticmethod
    def task3():
        nums = [random.randint(1, 100) for _ in range(50)]
        print(f'max: {max(nums)}')
        nums.pop(2)
        nums.sort()
        nums.insert(3, 1111)
        print([num * 3 if num < 10 else num for num in nums])

    def task4(self):
        try:
            n = int(input("Ведіть кількість: "))
            students = [Student.Student() for _ in range(n)]

            maleName = [student.name for student in students if student.gender == 'male']
            femaleName = [student.name for student in students if student.gender == 'female']

            mostCommonMaleName = Counter(maleName).most_common(1)
            mostCommonFemaleName = Counter(femaleName).most_common(1)
            print("Найбільш поширене чоловіче ім'я: ", mostCommonMaleName[0][0] if mostCommonMaleName else "Немає")
            print("Найбільш поширене жіноче ім'я: ", mostCommonFemaleName[0][0] if mostCommonFemaleName else "Немає")

            ages = [student.getAge() for student in students]
            mostCommonAge = Counter(ages).most_common(1)[0][0]
            studentsWithCommonAge = [student.getFullName() for student in students if student.age == mostCommonAge]
            print(f"Студенти з найпоширенішим віком (прізвища та ініціали): {studentsWithCommonAge}")
        except ValueError as e:
            print(f"Сталась помилка {e}")

    def task5(self):
        try:
            n = int(input("Ведіть кількість: "))
            lst = [random.randint(0, 1) for _ in range(n)]
            maxLen, start, end, currentLen, currentStart = 0
            for i, value in enumerate(lst):
                if value == 1:
                    if currentLen == 0:
                        currentStart = i 
                    currentLen += 1 
                else:
                    if currentLen > maxLen:
                        maxLen = currentLen
                        start = currentStart
                        end = i - 1
                    currentLen = 0  
            if currentLen > maxLen:
                maxLen = currentLen
                start = currentStart
                end = len(lst) - 1

            return maxLen, start, end

        except ValueError as e:
            print(f"Сталась помилка {e}")

    def task6(self, numPoints = 100, xRange = (-10, 10), yRange = (-10, 10)):
        points = [(random.uniform(*xRange), random.uniform(*yRange)) for _ in range(numPoints)]

        bestCircle, maxCount = self._findCircleWithMostPoints(points)

        if bestCircle:
            print(f"Центр кола: {bestCircle[0]}, Радіус: {bestCircle[1]}")
            print(f"Максимальна кількість точок на колі: {maxCount}")
        else:
            print("Не вдалося знайти коло.")

    def _findCircleWithMostPoints(self, points):
        maxCount = 0
        bestCircle = None

        for A, B, C in combinations(points, 3):
            center, radius = self._calculateCircleCenterAndRadius(A, B, C)
            if center is None:
                continue
            
            count = self._countPointsCircle(points, center, radius)
            if count > maxCount:
                maxCount = count
                bestCircle = (center, radius)

        return bestCircle, maxCount

    @staticmethod
    def _calculateCircleCenterAndRadius(A, B, C):
        x1, y1 = A
        x2, y2 = B
        x3, y3 = C
        det = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
        if det == 0:
            return None, None
        xCenter = ((y2 - y3)*(x1**2 + y1**2 - x3**2 - y3**2) + 
                (y3 - y1)*(x2**2 + y2**2 - x3**2 - y3**2)) / (2 * det)
        yCenter = ((x3 - x2)*(x1**2 + y1**2 - x3**2 - y3**2) + 
                (x1 - x3)*(x2**2 + y2**2 - x3**2 - y3**2)) / (2 * det)
        radius =  math.sqrt((xCenter - x1)**2 + (yCenter - y1)**2)
        return (xCenter, yCenter), radius

    @staticmethod    
    def _countPointsCircle(points, center, radius, epsilon = 1e-6):
        count = 0
        for point in points:
            distance = math.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)
            if abs(distance - radius) < epsilon:
                count += 1
        return count
    
    def task7(self, sentence: str = None, letter: str = 'a', startPos: int = 1):
        if sentence == None:
            sentence = input("Введіть речення")

        words = sentence.split()

        shortestWord = min(words, key=len)
        shortestLength = len(shortestWord)
        shortestPosition = words.index(shortestWord) + 1 
        print(f'найкоротше слово речення, його довжину та позицію у реченні: {shortestWord} {shortestLength} {shortestPosition}')

        longestWord = max(words, key=len)
        longestLength = len(longestWord)
        longestPosition = words.index(longestWord) + 1 
        print(f'найдовше слово речення, його довжину та позицію у реченні: {longestWord} {longestLength} {longestPosition}')

        occurrences = sentence[startPos:].count(letter)
        print(f"кількість входжень заданої літери, починаючи з заданої позиції {occurrences}")

        vowels = "аеєиіїоуюяaeiou"
        wordVowelCount = [(word, sum(1 for char in word.lower() if char in vowels)) for word in words]
        mostVowelsWord = max(wordVowelCount, key=lambda x: x[1])[0]
        print(f'слово, що містить найбільшу кількість голосних літер {mostVowelsWord}')

    def task8(self):
        try:
            n = int(input("Ведіть кількість: "))
            humans = [Human.Human() for _ in range(n)]

            addressMap = defaultdict(list)
            for human in humans:
                addressMap[human.address].append(human)
            result = []
            for address, group in addressMap.items():
                if len(group) > 1: 
                    cities = set(resident.city for resident in group)
                    if len(cities) > 1:  
                        result.extend(group)
            if result:
                print("Знайдено жителів з однаковою адресою в різних містах:")
                for resident in result:
                    print(resident)
            else:
                print("Жителів з однаковою адресою в різних містах не знайдено.")
        except ValueError as e:
            print(f"Сталась помилка {e}")

    def task9(self):
        try:
            n = int(input("Ведіть кількість: "))
            students = [Student.Student() for _ in range(n)]
            print(f"Студенти з заборгованостями: {[student for student in students if student.isHasFailures()]}")
            best_subject_index, best_average = self.findBestSubject(students)
            print(f"Предмет, який було здано краще (предмет {best_subject_index}) має середню оцінку {best_average:.2f}")
            print(f"Студенти, що склали всі іспити на 4 і 5: {[student for student in students if student.isPassedAllExams()]}") 
        except ValueError as e:
            print(f"Сталась помилка {e}")

    @staticmethod
    def findBestSubject(students):
        subject_scores = [0] * len(students[0].grades)
        subject_counts = [0] * len(students[0].grades)

        for student in students:
            for i, grade in enumerate(student.grades):
                subject_scores[i] += grade
                subject_counts[i] += 1

        average_scores = [subject_scores[i] / subject_counts[i] for i in range(len(subject_scores))]
        best_subject_index = average_scores.index(max(average_scores))
        return best_subject_index + 1, average_scores[best_subject_index]
    
    def task10(self):
        try:
            n = int(input("Ведіть число: "))
        except ValueError as e:
            print(f"Сталась помилка {e}")
            return
        a, b = 0, 1
        fibonacci_numbers = [] 
        while b <= n:
            fibonacci_numbers.append(b)  
            a, b = b, a + b 

        print(f"Числа Фібоначчі до {n}:", fibonacci_numbers)
        print(f"Загальна кількість чисел Фібоначчі: {len(fibonacci_numbers)}")