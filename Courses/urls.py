from django.urls import path
from . import views



app_name = 'courses' 
urlpatterns=[
    path('listCourses/',views.ListView, name='listCourses'),
   path('courseDetails/<str:title>',views.DetailView, name='courseDetails'),
    path('addCourse/',views.CreateView, name='addCourse'),
     path('deleteCourse/',views.DeleteView, name='deleteCourse'),
     path('updateCourse/',views.UpdateView, name='updateCourse'),
    
]