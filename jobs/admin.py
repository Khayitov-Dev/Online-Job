from django.contrib import admin
from jobs.models import StudentUser,Recruiter
# Register your models here.


@admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ['id','user','mobile','image','gender','type']
    list_filter = ['id','user','mobile','image','gender','type']
    search_fields = ['id','user','mobile','image','gender','type']
    # prepopulated_fields = {'slug':('name',)}


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ['id','user','mobile','image','gender','type','status']
    list_filter = ['id','user','mobile','image','gender','type','status']
    search_fields = ['id','user','mobile','image','gender','type','status']