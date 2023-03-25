"""
    HW2: Student, Marks, Undergraduate, and Postgraduate Classes
    Author: Taylor Hancock
    Date: 02/10/2023
"""


class Marks:
    def __init__(self, gpa: float, with_honors: bool):
        self.gpa = gpa
        self.with_honors = with_honors


class Student:
    def __init__(self, name: str, student_id: int, student_name: str, marks: Marks):
        self.name = name
        self.student_id = student_id
        self.student_name = student_name
        self.marks = marks


class Undergraduate(Student):
    def __init__(self, name: str, student_id: int, student_name: str, marks: Marks, sat_score: Marks):
        super().__init__(name, student_id, student_name, marks)
        self.sat_score = sat_score


class Postgraduate(Student):
    def __init__(self, name: str, student_id: int, student_name: str, marks: Marks, bachelors_gpa: Marks):
        super().__init__(name, student_id, student_name, marks)
        self.bachelors_gpa = bachelors_gpa


if __name__ == '__main__':
    # Create some data
    x = Undergraduate("Taylor", 172942, "Taylor Hancock", Marks(4.0, True), Marks(1600, True))
    y = Postgraduate("John", 101101, "John Doe", Marks(3.5, True), Marks(3.9, False))
    z = Undergraduate("Mario", 1234, "Mario Mario", Marks(3.0, False), Marks(1100, True))
    a = Undergraduate("Luigi", 4321, "Luigi Mario", Marks(3.2, True), Marks(1305, False))
    b = Postgraduate("Sample", 111111, "Sample Text", Marks(2.2, False), Marks(3.0, True))
    c = Student("Jane", 10010, "Jane Doe", Marks(4.0, True))

    list_of_students = [x, y, z, a, b, c]

    # Print each student and info about them (if they are instances and subclasses)
    for student in list_of_students:
        print(f"{student.name} is a {type(student).__name__} with a {student.marks.gpa} GPA.")
        print(f"    They are an instance of Marks: {isinstance(student, Marks)}")
        print(f"    They are an instance of Student: {isinstance(student, Student)}")
        print(f"    They are an instance of Undergraduate: {isinstance(student, Undergraduate)}")
        print(f"    They are an instance of Postgraduate: {isinstance(student, Postgraduate)}")
        print(f"    They are a subclass of Object: {issubclass(type(student), object)}")
