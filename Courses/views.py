from django.shortcuts import render, redirect
from django.contrib import messages

from Courses.models import Course
from .forms import CourseForm
# Create your views here.
def ListView(request):  
    courses = Course.objects.all()  
    return render(request,"CoursesList.html",{'courses':courses}) 


# Create your views here.
def DetailView(request, title):  
    print(type(id))
    course_detail = Course.objects.filter(title=title).first()
    print(course_detail.id)
    return render(request,"CourseDetails.html",{'course':course_detail}) 


  
def CreateView(request): 
    print(request.method)
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect("courses:listCourses") 
    else:
        form = CourseForm()
    context = {'form': form}
    return render(request, "AddCourse.html", context) 


def UpdateView(request):
    print( request.POST)
    if request.method == "POST":
        if 'course_title' in request.POST and 'course_description' in request.POST:
            title = request.POST.get('course_title')
            description = request.POST.get('course_description')

            updatedtitle = request.POST.get('title')
            updateddescription = request.POST.get('description')
            
            courseToUpdate = Course.objects.filter(title=title).first()
            
           
            courseToUpdate.title = updatedtitle if updatedtitle != '' else courseToUpdate.title
            courseToUpdate.description = updateddescription if updateddescription else None


            return redirect('courses:listCourses')  
            
            
        selected_courses = request.POST.getlist('selected_courses')
        print("Selected courses for update:", selected_courses)

        
        if len(selected_courses) != 1:
            messages.error(request, 'You must select exactly one course to update.')
            return redirect('courses:listCourses')  
        
        courseDetail = Course.objects.filter(title__in=selected_courses).first()
        print("Course to update:", courseDetail)
    
    else:
        courseDetail = None
    
    return render(request, "UpdateCourse.html", context={'course': courseDetail})




def DeleteView(request):
    if request.method == "POST":
        selected_courses = request.POST.getlist('selected_courses')
        
        # Delete selected courses based on title
        courses_to_delete = Course.objects.filter(title__in=selected_courses)
        deleted_count, _ = courses_to_delete.delete()

        if deleted_count:
            messages.success(request, f'{deleted_count} course(s) successfully deleted!')
        else:
            messages.error(request, 'No courses were selected or nothing was deleted.')

        return redirect('courses:listCourses')  # Adjust the redirect path as needed
    
    # Render page again if method isn't POST
    return render(request,"CoursesList.html", {'courses': Course.objects.all()})