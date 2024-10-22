class TestLib:
    def __init__(self, obj):
         self.lab = obj
         self.result = "Failed"
         self.allCurrentTest = 0
         self.allFailedTest = 0
         
    def __call__(self):
        methods = [getattr(self, method) for method in dir(self) if
                    callable(getattr(self, method)) and not method.startswith('_')]
        for method in methods:
                try: 
                    print(method.__name__)
                    if method():
                         self.result = "Current"
                         self.allCurrentTest += 1
                    else:
                         self.result = "Failed"
                         self.allFailedTest += 1
                    print(method.__name__, self.result)
                except Exception as e:
                    print(f"Failed {e}")
                    self.allFailedTest += 1
        print(f"\nAll test {self.allCurrentTest + self.allFailedTest}\nCurrent test {self.allCurrentTest}\
            \nFailed test {self.allFailedTest}")