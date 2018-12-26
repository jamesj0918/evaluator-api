from django.db import models


class Department(models.Model):
    Department_Choices = (
        ("컴퓨터공학과", "Computer Engineering"),
        ("소프트웨어과", "Software"),
        ("정보보호학과", "Information Security"),
        ("지능기전학과", "Intelligent Mechanics"),
        ("데이터사이언스", "Data Science"),
    )

    title = models.CharField(choices=Department_Choices, max_length=32)

    def __str__(self):
        return self.title


class Question(models.Model):
    question_num = models.CharField(max_length=8)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.question_num


class Test(models.Model):
    Lecture_Choices = (
        (0, "C프로그래밍및실습"),
        (1, "고급C프로그래밍및실습")
    )

    year = models.IntegerField(default=2018)
    semester = models.IntegerField(default=1)
    lecture_type = models.IntegerField(choices=Lecture_Choices)

    questions = models.ManyToManyField(Question)

    def __str__(self):
        return str(self.year) + "-" + str(self.semester)


class Student(models.Model):
    student_id = models.CharField(max_length=8)
    name = models.CharField(max_length=16)
    grade = models.IntegerField(default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    test = models.ManyToManyField(Test, blank=True, null=True)

    def __str__(self):
        return self.student_id

