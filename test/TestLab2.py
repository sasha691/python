from lab_2 import Lab2
from utils import TestLib, Triangle

class TestLab2(TestLib.Test):
    def __init__(self):
        super().__init__(Lab2.Lab2())
        self.triangle = Triangle.Triangle()

    def testTask1CorrectPoint(self):
        x = 1
        y = 0
        return self.lab.task1(x, y)
    
    def testTask1NotCorrectPoint(self):
        x = 1
        y = 1
        return self.lab.task1(x, y)
    
    def testTask2(self):
        try:
            self.lab.task2('1111')
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def testTask3TriangleAcute(self):
        self.triangle.setTriangle("acute")
        return "acute" == self.lab.task3(self.triangle.getTriangle())
    
    def testTask3TriangleRight(self):
        self.triangle.setTriangle("right")
        return "right" == self.lab.task3(self.triangle.getTriangle())
    
    def testTask3TriangleObtuse(self):
        self.triangle.setTriangle("obtuse")
        return "obtuse" == self.lab.task3(self.triangle.getTriangle())

    def testTask4RealMove(self):
        x1 = 4
        y1 = 4
        x2 = 5
        y2 = 4
        move = [x1, y1, x2, y2]
        return self.lab.task4(move)
    
    def testTask4NotRealMove(self):
        x1 = 4
        y1 = 4
        x2 = 5
        y2 = 5
        move = [x1, y1, x2, y2]
        return not self.lab.task4(move)
    
    def testTask5ForInWhile(self):
        result1, result2 = self.lab.task5()
        return result1 == result2
    
    def testTask6Box(self):
        try:
            box1 = (1, 1, 10)
            box2 = (3, 3, 3)
            return not self.lab.task6(box1, box2)
        except Exception:
            return False
        
    def testTask7Rectangle(self):
        return self.lab.task7(['1','3','1','3'])
    
    def testTask8NumOfWord(self):
        try:
            self.lab.task8('142')
            return True
        except Exception:
            return False
        
    def testTask9OddNum(self):
        return False if self.lab.task9(10) == None else True
    
    def testTask10(self):
        try:
            self.lab.task10()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def testTask11(self):
        try:
            self.lab.task11()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False