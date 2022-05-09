from django.db import models

# Create your models here.

# Many-to-one Relationships için hazırlıyorum.
class Category(models.Model):
    name= models.CharField(max_length=50, null=True)
    #slug = URL kısmının daha anlamlı gözükmesi için kullanılıyor.
    slug = models.SlugField(max_length=50, unique=True, null=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=200, unique = True, verbose_name="Kursun Adı", help_text="Kurs adını yazınız")
    category=models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    image=models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default.gif")
    date=models.DateTimeField(auto_now=True)
    available= models.BooleanField(default=True)

    def __str__(self):
        return self.name
