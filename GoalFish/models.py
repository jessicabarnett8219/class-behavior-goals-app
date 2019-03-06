from django.contrib.auth.models import User
from django.db import models

class Score(models.Model):
    value = models.IntegerField()

class Goal(models.Model):
    description = models.CharField(max_length=250)

class GradeLevel(models.Model):
    grade = models.CharField(max_length=1)

    def __str__(self):
        return self.grade

class Student(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    gradeLevel = models.ForeignKey(
        GradeLevel,
        on_delete=models.CASCADE,
    )
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    classroomTeacher = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName, self.lastName

class Evaluation(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    score = models.ForeignKey(
        Score,
        on_delete=models.CASCADE,
    )
    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    schoolWeek = models.IntegerField()
