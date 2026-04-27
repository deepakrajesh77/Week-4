from django.db import models

class ActiveCourseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="ACTIVE")


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_filled = models.IntegerField(default=0)
    total_seats = models.IntegerField()
    status = models.CharField(max_length=20, default="DRAFT")

    objects = models.Manager()
    active_objects = ActiveCourseManager()

    def __str__(self):
        return self.course_name


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=200)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons"
    )

    def __str__(self):
        return self.lesson_name


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.student_name


class CourseDetail(models.Model):
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE
    )
    syllabus = models.TextField()

    def __str__(self):
        return self.course.course_name