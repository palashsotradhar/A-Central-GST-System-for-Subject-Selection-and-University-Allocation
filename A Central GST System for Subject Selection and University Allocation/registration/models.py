from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Registration_Model(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    student_name = models.CharField(max_length = 100,blank=False)
    father_name = models.CharField(max_length=100,blank=False)
    mother_name = models.CharField(max_length=100,blank=False)
    student_contact_no = models.IntegerField(blank=False)
    parent_contact = models.IntegerField(blank=False)
    student_email = models.EmailField(max_length=70,blank=False,unique=True)
    relationship = models.CharField(max_length=100,blank=False)
    present_adress = models.CharField(max_length=100,blank=False)
    parmanent_adress = models.CharField(max_length=100,blank=False)
    District = models.CharField(max_length=100,blank=False)
    upazila = models.CharField(max_length=100,blank=False)
    postal_zip = models.IntegerField(blank=False)
    exam_namessc = models.CharField(max_length=100,blank=False)
    passing_yearssc = models.IntegerField(blank=False)
    gpassc =  models.CharField(max_length=100,blank=False)
    ssc_roll_number = models.IntegerField()
    ssc_registration_number = models.IntegerField(blank=False)
    boardssc = models.CharField(max_length=100,blank=False)
    sscgroup = models.CharField(max_length=100,blank=False,null=True)
    exam_namehsc = models.CharField(max_length=100,blank=False)
    passing_yearhsc = models.IntegerField(blank=False)
    gpahsc =  models.CharField(max_length=100,blank=False)
    hsc_roll_number = models.IntegerField(blank=False)
    hsc_registration_number = models.IntegerField(blank=False)
    boardhsc = models.CharField(max_length=100,blank=False)
    hsc_group = models.CharField(max_length=100,blank=False,null=True)
    exam_score = models.FloatField(null=True)


# @receiver(post_save,sender = User)
# def create_user_profile(sender,instance,created,**kwarg):
#     if created:
#         Registration_Model.objects.create(user = instance)
#
# @receiver(post_save,sender = User)
# def save_user_profile(sender,instance,**kwarg):
#     instance.Registration_Model.save()






