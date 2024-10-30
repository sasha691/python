import random
from utilit import Human

class Student(Human.Human):
    def __init__(self, numSubjects: int = 3) -> None:
        super().__init__()
        self.course = random.randint(1, 5)
        self.group = self.fake.random_int(min=1, max=10)
        self.grades = [self.fake.random_int(min=1, max=5) for _ in range(numSubjects)] 
        
    def __str__(self):
        return f"{self.lastname} (Group: {self.group}, Grades: {self.grades})"
    
    def isHasFailures(self):
        return any(grade < 3 for grade in self.grades)
    
    def isPassedAllExams(self):
        return all(grade >= 4 for grade in self.grades)