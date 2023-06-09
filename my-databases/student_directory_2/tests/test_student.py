from lib.student import *

"""
student construct with id, name and cohort_id
"""
def test_student_construct():
    student = Student(1, "Student1", 1)
    assert student.id == 1
    assert student.name == "Student1"
    assert student.cohort_id == 1

"""
Test the format as string
"""
def test_format_as_string():
    student = Student(1, "Student1", 1)
    assert str(student) == "1 - Student1 - 1"