from django.db import models
# Create your models here.
class Doctor(models.Model):
   name = models.CharField(max_length=50)


   def __str__(self):
       return f'{ self.pk } 번 의사 { self.name }'



class Patient(models.Model):
   name = models.CharField(max_length=50)
   doctors = models.ManyToManyField(Doctor, related_name='patients')



   def __str__(self):
       return f'{ self.pk } 번 환자 { self. name }'



# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


#     def __str__(self):
#         return f'{self.doctor.id}번 의사의 {self.patient.id}번 환자'