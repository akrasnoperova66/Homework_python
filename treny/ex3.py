from student import Student
from cursgroup import CorseGroup

student = Student("Анна", "Иванова", "30", "Инженер по тестированию")
classmate1 = Student("Антон", "Сидоров", "25", "Инженер по тестированию")
classmate2 = Student("Василий", "Петров", "28", "Инженер по тестированию") 
classmate3 = Student("Ангелина", "Васильева", "34", "Инженер по тестированию")

coursgroup = CorseGroup(student, [classmate1, classmate2, classmate3])

print(coursgroup)