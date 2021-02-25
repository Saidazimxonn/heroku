from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Doctor(models.Model):

    name = models.CharField('Name', max_length=100)
    specialist = models.CharField('Specialist', max_length=100)
    image = models.ImageField('Image', upload_to ='uploads')
    info = models.TextField('Info') 

    def __str__(self):
        return self.name


class Patient(models.Model):
    DAY_WORK = [
        ('day', 'Day'),
        ('sunday', 'Sunday'),
        ('monday', 'Monday'), 
    ]

    TIME_WORK =[
        ('am', 'AM'),
        ('pm', 'PM'),
    ]

    name = models.CharField('Name', max_length=100, help_text='Your Name')
    phone = models.CharField('Phone', help_text='Phone', max_length=50)
    email = models.EmailField('Email',help_text='Email Address')
    day = models.CharField('Day', choices=DAY_WORK,default='D', max_length=10)
    time = models.CharField('Time', choices=TIME_WORK, default='A', max_length=10)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    message = models.TextField('Message',help_text='Your Message...', null=True, blank=True)
   
    def __str__(self):
        return self.name

class Message(models.Model):

    name = models.CharField('Name',max_length=100)
    email = models.EmailField('Email Address')
    phone = models.CharField('Phone',max_length=50)
    subject = models.CharField('Subject', max_length=50)
    message = models.TextField('Message')

    def __str__(self):
        return self.name

class Email(models.Model):

    email = models.EmailField('Email')

    def __str__(self):
        return self.email