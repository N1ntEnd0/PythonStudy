import pytest

from Task2 import (DeadlineError, Homework, HomeworkResult, Human, Student,
                   Teacher)


def test_exeption_in_HomeworkResult():
    student = Student("Roman", "Petrov")
    with pytest.raises(TypeError):
        HomeworkResult(student, "error", "solution")


def test_check_homework():
    teacher1 = Teacher("Daniil", "Shadrin")
    teacher2 = Teacher("Aleksandr", "Smetanin")
    student = Student("Lev", "Sokolov")
    hw = teacher2.create_homework("Learn OOP", 1)
    result_1 = student.do_homework(hw, "I have done this hw")
    teacher2.check_homework(result_1)
    temp_1 = teacher2.homework_done
    teacher1.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2
    Teacher.reset_results()


def test_reset_results():
    teacher = Teacher("Daniil", "Shadrin")
    oop_hw = teacher.create_homework("Learn OOP", 1)
    docs_hw = teacher.create_homework("Read docs", 5)
    student = Student("Lev", "Sokolov")
    result_1 = student.do_homework(oop_hw, "I have done this hw")
    result_2 = student.do_homework(docs_hw, "I have done this hw")
    teacher.check_homework(result_1)
    teacher.check_homework(result_2)
    assert len(Teacher.homework_done) == 2
    Teacher.reset_results(oop_hw)
    assert len(Teacher.homework_done) == 1
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0
