from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseSerializer

def home_view(request):
    context = {
        'title': 'Welcome to Klaw Courses',
        'user_name': 'Deepak',
        'courses': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'courses/course_list.html', context)


def detail_view(request, name):
    return HttpResponse(f"Course Name: {name}")

@api_view(['GET', 'POST'])
def course_list(request):

    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseList(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    def get(self, request, pk):
        course = self.get_object(pk)
        if not course:
            return Response({"error": "Not found"}, status=404)

        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)
        if not course:
            return Response({"error": "Not found"}, status=404)

        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        course = self.get_object(pk)
        if not course:
            return Response({"error": "Not found"}, status=404)

        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)