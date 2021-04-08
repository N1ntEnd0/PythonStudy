"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    pass


class HomeworkResult:
    def __init__(self, author, homework, solution):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.author = author
        self.__homework = homework
        self.__solution = solution
        self.__created = datetime.datetime.today()

    @property
    def homework(self):
        return self.__homework

    @property
    def solution(self):
        return self.__solution

    @property
    def created(self):
        return self.__created


class Human:
    def __init__(self, last_name, first_name):
        self.__last_name = last_name
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def first_name(self):
        return self.__first_name


class Homework:
    def __init__(self, text, deadline):
        self.__text = text
        self.__deadline = datetime.timedelta(deadline)
        self.__created = datetime.datetime.today()

    @property
    def text(self):
        return self.__text

    @property
    def deadline(self):
        return self.__deadline

    @property
    def created(self):
        return self.__created

    def is_active(self):
        return datetime.datetime.today() - self.__created < self.__deadline


class Student(Human):
    def do_homework(self, hw, solution):
        if hw.is_active():
            return HomeworkResult(self, hw, solution)
        raise DeadlineError("You are late")


class Teacher(Human):
    homework_done = defaultdict(int)

    def check_homework(self, hwr):
        if len(hwr.solution) > 5:
            if hwr.homework not in Teacher.homework_done:
                Teacher.homework_done[hwr.homework] += 1
            return True
        return False

    @staticmethod
    def reset_results(*args):
        if len(args) == 0:
            Teacher.homework_done.clear()
        else:
            Teacher.homework_done.pop(args)

    def create_homework(self, text, deadline):
        return Homework(text, deadline)


if __name__ == "__main__":

    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
