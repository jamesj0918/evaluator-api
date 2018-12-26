from django.db import models


class Department(models.Model):
    DEPARTMENT_CHOICES = (
        ("컴퓨터공학과", "Computer Engineering"),
        ("소프트웨어과", "Software"),
        ("정보보호학과", "Information Security"),
        ("지능기전학과", "Intelligent Mechanics"),
        ("데이터사이언스", "Data Science"),
    )

    title = models.CharField(choices=DEPARTMENT_CHOICES, max_length=32)

    def __str__(self):
        return self.title


class Test(models.Model):
    LECTURE_CHOICES = (
        (0, "C프로그래밍및실습"),
        (1, "고급C프로그래밍및실습")
    )

    year = models.IntegerField(default=2018)
    semester = models.IntegerField(default=1)
    lecture_type = models.IntegerField(choices=LECTURE_CHOICES)

    def __str__(self):
        return str(self.year) + "-" + str(self.semester)


class Question(models.Model):
    question_num = models.CharField(max_length=8)
    points = models.IntegerField(default=0)
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, db_index=True, related_name="question", related_query_name="question")

    def __str__(self):
        return self.question_num


class Student(models.Model):
    student_id = models.CharField(max_length=8)
    name = models.CharField(max_length=16)
    grade = models.IntegerField(default=1)
    department = models.ForeignKey(Department, db_index=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id


class Lecture(models.Model):
    code = models.CharField(max_length=32, unique=True)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="lecture", related_query_name="lecture")

    def __str__(self):
        return self.code
