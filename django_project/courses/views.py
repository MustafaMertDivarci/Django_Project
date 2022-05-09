from django.shortcuts import render
# Kursları dinamik olarak gösterebilimek için models' a ihtiyacım var
from . models import Course, Category

# Create your views here.
def course_list(request):

    # ORM yapıları ile dinamik bir şekilde veritabanından bilgilerimizi alıyoruz.
    courses = Course.objects.all().order_by('-date')

    context= {
        'courses':courses
    }

    return render(request, 'courses.html',context)

def course_detail(request, category_slug, course_id):
    # courses/models.py dosyasındaki Course class' ındaki category'i 
    # " category=models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)"
    #                           (->Category<-) class'ındaki slug özelliğini alabilmek için
    # iki tane alttan tire yapmam gerek '__'   --->category__slug
    # Query Set olduğu için __ kullanıldı.
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    
    context= {
        'course':course
    }
    return render(request, 'course.html', context)

