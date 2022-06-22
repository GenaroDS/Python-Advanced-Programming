
class Course:
    def __init__(self, name : str, grade : str, credits : str):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits

class Courses:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name : str, grade : str, credits : str):
        if not name in self.__courses:
            self.__courses[name] = Course(name,grade,credits)
        elif name in self.__courses:
            if grade > self.__courses[name].grade():
                self.__courses[name] = Course(name,grade,credits)

    def search_course(self, name: str):
        if name in self.__courses:
            return self.__courses[name]
        else:
            return None
    
    def dictionary_length(self):
        return len(self.__courses)

    def dictionary_items(self):
        return self.__courses

class CoursesApplication:
    def __init__(self):
        self.__application = Courses()

    def add_course(self):
        course = input("course: ")    
        grade = input("grade: ")
        credits = input("credits: ")    
        self.__application.add_course(course, grade, credits)

    def search_course(self):
        course = input("course: ") 
        toPrint = self.__application.search_course(course)
        if toPrint == None:
            print("no entry for this course")
        else:
            print(f"{toPrint.name()} ({toPrint.credits()} cr) grade {toPrint.grade()}")

    def statistics(self):
        completedCourses = self.__application.dictionary_length()
        totalCredits = 0
        totalGrades = 0
        fives = ""
        fours = ""
        threes = ""
        twos = ""
        ones = ""
        for key, values in self.__application.dictionary_items().items():
            totalCredits += int(values.credits())
            totalGrades += int(values.grade())
            if int(values.grade()) == 5:
                fives += "x"
            elif int(values.grade()) == 4:
                fours += "x"
            elif int(values.grade()) == 3:
                threes += "x"
            elif int(values.grade()) == 2:
                twos += "x"
            elif int(values.grade()) == 1:
                ones += "x"
        print(f"{completedCourses} completed courses, a total of {totalCredits} credits")
        toPrint = totalGrades/completedCourses
        print(f"mean {toPrint:.1f}")
        print("grade distribution")
        print(f"5: {fives}")
        print(f"4: {fours}")
        print(f"3: {threes}")
        print(f"2: {twos}")
        print(f"1: {ones}")


    def help(self):
        print("1 add course")
        print("2 search course")
        print("3 statistics")
        print("0 exit")
    
    def execute(self):
        self.help()
        while (True):
            command = input("command: ")
            if command == "0":
                break
            if command == "1":
                self.add_course()
            if command == "2":
                self.search_course()
            if command == "3":
                self.statistics()
aplication = CoursesApplication()
aplication.execute()