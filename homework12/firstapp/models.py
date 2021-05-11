from django.db import models


class Human(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)


class Homework(models.Model):
    text = models.TextField()
    deadline = models.DateField()


class HomeworkResult(models.Model):
    author = models.ForeignKey(Human, on_delete=models.CASCADE)
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE)
    solution = models.TextField()



