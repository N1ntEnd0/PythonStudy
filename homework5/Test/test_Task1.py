import pytest

from Task1 import Homework, Student, Teacher


def test():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    assert teacher.last_name == "Daniil"
    assert student.first_name == "Petrov"

    expired_homework = teacher.create_homework("Learn functions", 0)
    assert str(expired_homework.deadline) == "0:00:00"
    assert expired_homework.text == "Learn functions"

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert str(oop_homework.deadline) == "5 days, 0:00:00"

    student.do_homework(oop_homework)
    assert student.do_homework(expired_homework) is None
