from student import Student

class CorseGroup():
    def __init__(self, student, classmates):
        self.student = student
        self.classmates = classmates

    def __str__(self):
        classmates_str = ""
        for classmate in self.classmates:
            classmates_str += classmate
        
        if classmates_str.endswith(", "):
            classmates_str = classmates_str[:-2]
        return f"{self.student} учится вместе с: {classmates_str}"