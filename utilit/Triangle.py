import random

class Triangle:
    _typeChecks = {
        'acute': lambda t: sum(sorted(t)[:2])**2 > sorted(t)[-1]**2,
        'right': lambda t: sum(sorted(t)[:2])**2 == sorted(t)[-1]**2,
        'obtuse': lambda t: sum(sorted(t)[:2])**2 < sorted(t)[-1]**2,
        'any': lambda t: True
    }

    def __init__(self, typeTriangle = 'any'): 
        if typeTriangle not in self._typeChecks:
            raise ValueError(f"Недійсний тип трикутника: {typeTriangle}. Допустимі типи: {', '.join(self._typeChecks.keys())}")
        self.typeTriangle = typeTriangle
        self.triangle = self._generateTriangle()

    def _generateTriangle(self) -> list:
        attempts = 0
        maxAttempts = 300
        while attempts < maxAttempts:
            triangle = [random.randint(0, 20) for _ in range(3)]
            if self.isRealTriangle(triangle) and self._typeChecks[self.typeTriangle](triangle):
                return triangle
            attempts += 1
        raise RuntimeError("Не вдалося згенерувати трикутник за допустимими умовами")
        
    @staticmethod  
    def isRealTriangle(triangle: list) -> bool:
        triangle = list(map(int, triangle))
        a, b, c = sorted(triangle)
        return a > 0 and b > 0 and c > 0 and a + b > c
    
    def getTriangle(self):
        return self.triangle
    
    @staticmethod
    def determineTypeTriangle(triangle: list) -> str:
        a, b, c = sorted(triangle)
        if not Triangle.isRealTriangle(triangle):
            print("Трикутник неможливий")
            return
        elif a**2 + b**2 > c**2:
            print("Трикутник гострокутний")
            return "acute"
        elif a**2 + b**2 == c**2:
            print("Трикутник прямокутний")
            return "right"
        else:
            print("Трикутник тупокутний")
            return "obtuse"
    
    def setTriangle(self, typeTriangle: str = "any"):
        if typeTriangle not in self._typeChecks:
            raise ValueError(f"Недійсний тип трикутника: {typeTriangle}. Допустимі типи: {', '.join(self._typeChecks.keys())}")
        self.typeTriangle = typeTriangle
        self.triangle = self._generateTriangle()