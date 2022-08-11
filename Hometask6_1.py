class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and 
            course in self.courses_in_progress and 
            course in lecturer.lecture_grades):
            lecturer.lecture_grades[course].append(grade)
            
    def find_mean(self, grades):
        _sum = 0
        length = 0
        for course in grades:
            _sum += sum(grades[course])
            length += len(grades[course])
        if length == 0: return 0
        return _sum / length
    
    def __str__(self) -> str:
        result = (f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.find_mean(self.grades)}
Курсы в процессе обучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
''')
        return result
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Вы сравниваете студента с кем-то другим")
            return
        return self.find_mean(self.grades) < other.find_mean(other.grades)
        
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        
class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}
        
    def add_lecture(self, course):
        self.lecture_grades[course] = []
    def find_mean(self, lecture_grades):
        _sum = 0
        length = 0
        for course in lecture_grades:
            _sum += sum(lecture_grades[course])
            length += len(lecture_grades[course])
        if length == 0: return 0
        return _sum / length 
    def __str__(self) -> str:
        result = (f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.find_mean(self.lecture_grades)}''')
        return result
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Вы сравниваете лектора с кем-то другим")
            return
        return (self.find_mean(self.lecture_grades) < 
                other.find_mean(other.lecture_grades))
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and 
            course in self.courses_attached and 
            course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self) -> str:
        result = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return result
best_student = Student('Elena', 'Golovach', 'Female')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['English', 'Java']

not_the_best_student = Student('Tom', 'Cruise', 'Scientologyst')
not_the_best_student.courses_in_progress += ['Python', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']

brilliant_reviewer = Reviewer('David', 'Duchovny')
brilliant_reviewer.courses_attached += ['Python', 'Git']


awesome_lecturer = Lecturer('David', 'Hasselhoff')
awesome_lecturer.add_lecture('Python')

ultra_lecturer = Lecturer('Han', 'Solo')
ultra_lecturer.add_lecture('Python')

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(not_the_best_student, 'Python', 3)
cool_reviewer.rate_hw(not_the_best_student, 'Git', 4)

brilliant_reviewer.rate_hw(best_student, 'Python', 9)
brilliant_reviewer.rate_hw(best_student, 'Git', 10)
brilliant_reviewer.rate_hw(not_the_best_student, 'Python', 2)
brilliant_reviewer.rate_hw(not_the_best_student, 'Git', 1)

best_student.rate_lecture(awesome_lecturer, 'Python', 9)
best_student.rate_lecture(awesome_lecturer, 'Git', 8)
best_student.rate_lecture(ultra_lecturer, 'Python', 10)
best_student.rate_lecture(ultra_lecturer, 'Git', 10)
not_the_best_student.rate_lecture(awesome_lecturer, 'Python', 2)
not_the_best_student.rate_lecture(awesome_lecturer, 'Git', 3)
not_the_best_student.rate_lecture(ultra_lecturer, 'Python', 1)
not_the_best_student.rate_lecture(ultra_lecturer, 'Git', 1)

def calculate_mean_hw(students, course):
    summary = 0
    length = 0
    for student in students:
        for grade in student.grades:
            if grade == course:
                summary += student.find_mean(student.grades)
                length += 1
    return summary / length
print(calculate_mean_hw([best_student, not_the_best_student], 'Python'))

def calculate_mean_lectures(lecturers, course):
    summary = 0
    length = 0
    for lecturer in lecturers:
        for grade in lecturer.lecture_grades:
            if grade == course:
                summary += lecturer.find_mean(lecturer.lecture_grades)
                length += 1
    return summary / length
print(calculate_mean_lectures([awesome_lecturer, ultra_lecturer], 'Python')) 