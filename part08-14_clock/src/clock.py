# Write your solution here:
class Clock:
    def __init__(self, hours :int, minutes:int, seconds:int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def tick(self):
        self.seconds+=1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0
C:\Users\genar\AppData\Local\tmc\vscode\mooc-programming-22
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def set(self, hours :int, minutes:int):
        self.seconds = 0
        self.minutes = minutes
        self.hours = hours
