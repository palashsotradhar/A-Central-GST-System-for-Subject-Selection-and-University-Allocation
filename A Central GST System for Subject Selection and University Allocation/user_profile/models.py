from django.db import models

class Selected_Subject_Model(models.Model):
    # group = models.CharField(max_length = 100)
    choosen_number = models.IntegerField(null=True)
    subject_name = models.CharField(max_length = 100,null=True)
    university_name = models.CharField(max_length = 100,null=True)
    email = models.EmailField(max_length=100,null=True)
