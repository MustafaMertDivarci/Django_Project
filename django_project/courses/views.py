from django.shortcuts import render
# Kursları dinamik olarak gösterebilimek için models' a ihtiyacım var
from . models import Course

# Create your views here.
def course_list(request):

    # ORM yapıları ile dinamik bir şekilde veritabanından bilgilerimizi alıyoruz.
    courses = Course.objects.all().order_by('-date')

    context= {
        'courses':courses
    }

    return render(request, 'courses.html',context)
