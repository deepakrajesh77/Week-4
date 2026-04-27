from django.contrib import admin
from .models import Course, Lesson, Student, CourseDetail

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'price', 'status')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(CourseDetail)