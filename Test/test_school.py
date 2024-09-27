import pytest
from source.school import ClassRoom, Teacher, Student, ToManyStudent

# Fixtures for common objects in tests
@pytest.fixture
def professor_snape():
    return Teacher("Severus Snape")

@pytest.fixture
def harry():
    return Student("Harry Potter")

@pytest.fixture
def hermione():
    return Student("Hermione Granger")

@pytest.fixture
def ron():
    return Student("Ron Weasley")

@pytest.fixture
def hogwarts_classroom(professor_snape, harry, hermione, ron):
    return ClassRoom(teacher=professor_snape, students=[harry, hermione, ron], course_title="Potions")

# Tests
def test_add_student(hogwarts_classroom):
    luna = Student("Luna Lovegood")
    hogwarts_classroom.add_student(luna)
    assert luna in hogwarts_classroom.students

def test_remove_student(hogwarts_classroom):
    hogwarts_classroom.remove_student("Ron Weasley")
    assert not any(student.name == "Ron Weasley" for student in hogwarts_classroom.students)

def test_change_teacher(hogwarts_classroom):
    new_teacher = Teacher("Albus Dumbledore")
    hogwarts_classroom.change_teacher(new_teacher)
    assert hogwarts_classroom.teacher.name == "Albus Dumbledore"

def test_too_many_students(hogwarts_classroom):
    # Add 8 more students to hit the limit
    for i in range(7):
        hogwarts_classroom.add_student(Student(f"Student {i}"))

    with pytest.raises(ToManyStudent):
        hogwarts_classroom.add_student(Student("Neville Longbottom"))
