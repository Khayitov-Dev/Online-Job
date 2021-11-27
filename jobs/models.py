from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BaseInfo(models.Model):


    """
    Bu class Asosiy ma'lumot tarqatuvchi class.
    """


    GENDER = (
        ('male','male'),
        ('female','female'),
        ('unknown','unknown'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    image = models.ImageField(upload_to='student/')
    gender = models.CharField(max_length=30, choices=GENDER,null=True)
    type = models.CharField(max_length=255,null=True)




    def __str__(self):
        return self.user.username


    class Meta:
        abstract = True

        

class StudentUser(BaseInfo):
    class Meta:
        verbose_name_plural = "StudentUser"



class Recruiter(BaseInfo):
    STATUS = (
        ('active','active'),
        ('inactive','inactive'),
        ('pending','pending'),
    )
    status = models.CharField(max_length=30, choices=STATUS)
    

    class Meta:
        verbose_name_plural = "Recruiter"