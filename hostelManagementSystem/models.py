#declared the class
from django.db import models
from django.contrib.auth.models import User

class Hostel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hostel_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    
    def __str__(self):
        return f"Room {self.room_number} - {self.hostel.name}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

class HostelReviews(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review of {self.hostel.name} by {self.student.user.username}"
