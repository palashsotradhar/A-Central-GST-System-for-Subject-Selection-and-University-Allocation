from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length = 100)
    subject_seat_number = models.IntegerField()

class Email_Model(models.Model):
    email_name = models.CharField(max_length = 100,null=True)

class Subject_and_University_Model(models.Model):
    student_email = models.CharField(max_length=100,null=True)
    student_university = models.CharField(max_length=100,null=True)
    student_subject = models.CharField(max_length=100,null=True)

class Subject_and_University_Model2(models.Model):
    student_email = models.CharField(max_length=100,null=True)
    student_university = models.CharField(max_length=100,null=True)
    student_subject = models.CharField(max_length=100,null=True)
    ranking_score = models.CharField(max_length=100, null=True)
    ranking_registration_number = models.CharField(max_length=100, null=True)
    ranking_username = models.CharField(max_length=100, null=True)
    ranking_group = models.CharField(max_length=100,null=True)

