from django.urls import path,include
from .import views
#from .views import course_list, CourseList, CourseDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
   # path('', views.home_view),
    path('course/<str:name>/', views.detail_view),
    #path('courses/', course_list),
    #path('courses/api/', CourseList.as_view()),
    #path('courses/api/<int:pk>/', CourseDetail.as_view()),
    path('', include(router.urls)),
]