class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(message)
    
    def separator(self):
        self.log("-" * 40)