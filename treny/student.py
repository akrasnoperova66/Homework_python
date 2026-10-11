class Student():
    def __init__(self, name, soname, age, curs):
        self.name = name
        self.soname = soname
        self.age = age
        self.curs = curs

    def __str__(self):
        return f"{self.name} {self.soname} , {self.age} лет, {self.curs} курс"