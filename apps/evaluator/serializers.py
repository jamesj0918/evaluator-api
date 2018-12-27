from rest_framework.serializers import ModelSerializer

from .models import Department, Test, Question, Student, Lecture


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'title',
        )


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test,
        fields = (
            'year',
            'semester',
            'lecture_type',
        )


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'question_id',
            'points',
            'test',
        )


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'student_id',
            'name',
            'grade',
            'department',
        )


class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = (
            'code',
            'student',
        )
