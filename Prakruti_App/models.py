from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    UserName = models.CharField(max_length=20, default='')
    # User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Middle_name = models.CharField(max_length=20, default='')
    Phone_No = models.BigIntegerField(default=0)
    Age = models.IntegerField(default=0)
    Gender = models.CharField(max_length=10, default='')
    P_Prakruti = models.CharField(max_length=7, default='')
    S_Prakruti = models.CharField(max_length=7, default='')
    Img = models.ImageField(null=True, blank=True, upload_to="Prakruti_App/Users_images/",
                            default="Prakruti_App/Users_images/user1.jpg")


class Appointments(models.Model):
    U_id = models.BigIntegerField(default=0)
    Date = models.DateField(null=True)
    TimeSlot = models.CharField(max_length=20, default='')
    Status_A = models.BooleanField(default=False)
    Status_R = models.BooleanField(default=False)
    P_med = models.TextField(default='')


class M_remedy(models.Model):
    Name = models.CharField(max_length=20, default='')
    Desc = models.TextField(default='')
    Category = models.TextField(default='')
    Content = models.TextField(default='')
    Quantity = models.IntegerField(default=0)
    Price = models.IntegerField(default=0)
    Img = models.ImageField(
        null=True, blank=True, upload_to="Prakruti_App/Med_images/",  default="Prakruti_App/Med_images/mr1.jpg")


class H_remedy(models.Model):
    Name = models.CharField(max_length=20, default='')
    Desc = models.TextField(default='')
    Accessories = models.TextField(default='')
    Img = models.ImageField(
        null=True, blank=True, upload_to="Prakruti_App/Hom_images/",  default="Prakruti_App/Hom_images/hr1.jpg")


class Blogs(models.Model):
    Title = models.CharField(max_length=20, default='')
    Type = models.CharField(max_length=20, default='')
    Content = models.TextField(default='')
    Date = models.DateField(null=True)
    file = models.FileField(null=True, blank=True,
                            upload_to="Prakruti_App/Blogs/", default="Prakruti_App/Blogs/hr1.jpg")


class Orders(models.Model):
    o_id = models.IntegerField(default=0,primary_key=True)
    UserName = models.CharField(max_length=20, default='')
    Date = models.DateField()
    Time = models.TimeField()
    Address = models.CharField(default="",max_length=100,null=True)
    Status = models.BooleanField(default=False)
    Price = models.IntegerField(default=0)


class Med_per_ord(models.Model):
    o_id = models.IntegerField(default=0)
    m_id = models.IntegerField(default=0)
    m_qt = models.IntegerField(default=0)
    U_name = models.CharField(default="",max_length=100,null=True)


class Cart(models.Model):
    Username = models.CharField(max_length=20, default='')
    p_id = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)


class Prakruti_Quetions(models.Model):
    que = models.TextField(default='')
    choice1 = models.TextField(default='')
    choice2 = models.TextField(default='')
    choice3 = models.TextField(default='')
    choice4 = models.TextField(default='')


class Complaint_Quetions(models.Model):
    que = models.TextField(default='')
    choice1 = models.TextField(default='')
    choice2 = models.TextField(default='')
    prakruti = models.TextField(default='')


class Prakruti_Quetions_Ans(models.Model):
    u_id = models.IntegerField(default=0)
    age = models.TextField(default='')
    ans1 = models.TextField(default='')
    ans2 = models.TextField(default='')
    ans3 = models.TextField(default='')
    ans4 = models.TextField(default='')
    ans5 = models.TextField(default='')
    ans6 = models.TextField(default='')
    ans7 = models.TextField(default='')
    ans8 = models.TextField(default='')
    ans9 = models.TextField(default='')
    ans10 = models.TextField(default='')
    ans11 = models.TextField(default='')
    ans12 = models.TextField(default='')
    ans13 = models.TextField(default='')
    ans14 = models.TextField(default='')
    ans15 = models.TextField(default='')
    ans16 = models.TextField(default='')
    ans17 = models.TextField(default='')
    ans18 = models.TextField(default='')
    ans19 = models.TextField(default='')
    ans20 = models.TextField(default='')
    ans21 = models.TextField(default='')
    ans22 = models.TextField(default='')
    ans23 = models.TextField(default='')