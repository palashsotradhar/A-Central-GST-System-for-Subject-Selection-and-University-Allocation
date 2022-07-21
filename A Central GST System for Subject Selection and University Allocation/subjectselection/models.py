from django.db import models


class JNU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length = 100)

class IU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class KU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class COU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class JKKNIU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class BRUR_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class BU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class RUB_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class BDU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class SHU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class SUST_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class HSTU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class MBSTU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class NSTU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class JUST_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class PUST_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class BSMRSTU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class RMSTU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class BSFMSTU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class PSTU_Model(models.Model):
    group = models.CharField(max_length = 100)
    subject_name = models.CharField(max_length = 100)
    university_name = models.CharField(max_length = 100)
    combine = models.CharField(max_length=100)

class Counter_Model(models.Model):
    count = models.IntegerField()

