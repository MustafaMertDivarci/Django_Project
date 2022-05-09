from django.contrib import admin
from .models import Course, Category
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','available','category')
#Admin alanında name ve available alanı oluşturdum.
    list_filter = ('available',)
    search_fields= ('name','description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}