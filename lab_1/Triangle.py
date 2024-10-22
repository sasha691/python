import random

class Triangle:
    def __init__(self):
        self.triangle = self._generateTriangle()

    def _generateTriangle(selt):
        while True:
            triangle = [random.randint(0, 10) for _ in range(3)]
            if Triangle._isRealTriangle(triangle):
                break
        return triangle
        
    @staticmethod  
    def _isRealTriangle(triangle: list) -> bool:
        triangle = map(int, triangle)
        a, b, c = triangle
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or c + b <= a:
            return False
        return True