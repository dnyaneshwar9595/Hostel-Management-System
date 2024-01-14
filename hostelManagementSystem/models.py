# i created this
from django.db import models
from django.db.models import UniqueConstraint


#declared the class

class HostelDataClass(models.Model):
    rollnumber = models.CharField(max_length=255)
    studentname = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    hoastelalloted = models.CharField(max_length=255)
    roomno = models.IntegerField(primary_key=True)
    floorno = models.IntegerField()
    # UniqueConstraint(fields=['hoastelalloted', 'roomno'], name='PRIMARY_KEY')

    class Meta:
        db_table = "hosteldata"

class HostelReviews(models.Model):
    rollnumber = models.CharField(max_length=255,primary_key=True)
    studentname = models.CharField(max_length=255)
    hostelnum = models.CharField(max_length=255)
    review = models.CharField(max_length=1000)
    # hostelimages = models.ImageField(upload_to="", default="")

    class Meta:
        db_table = "hostelreviews"