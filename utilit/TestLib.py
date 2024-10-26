class Test:
    def __init__(self, obj):
         self.lab = obj
         self.result = "Failed"
         self.allSuccessfulTest = 0
         self.allFailedTest = 0
         
    def __call__(self):
        RED = "\033[91m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RESET = "\033[0m"

        methods = [getattr(self, method) for method in dir(self) if
                    callable(getattr(self, method)) and not method.startswith('_')]
        for method in methods:
                try: 
                    print(f"{YELLOW}{method.__name__}{RESET}")
                    if method():
                         self.result = f"{GREEN}Successful{RESET}"
                         self.allSuccessfulTest += 1
                    else:
                         self.result = f"{RED}Failed{RESET}"
                         self.allFailedTest += 1
                    print(method.__name__, self.result)
                except Exception as e:
                    print(f"Failed {e}")
                    self.allFailedTest += 1
        print(f"\nAll test {self.allSuccessfulTest + self.allFailedTest}\nSccessful test: {GREEN}{self.allSuccessfulTest}{RESET}\
            \nFailed test: {RED}{self.allFailedTest}{RESET}")