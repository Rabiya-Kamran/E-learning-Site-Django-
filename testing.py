import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ElearningSite.settings')  # Replace 'ELearningSite' with your project name
django.setup()


from Courses.models import Course
print(Course.objects.all())
