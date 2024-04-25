from django.db import models
from course_app.models import ProgramModel,CourseModel,BatchModel,ProgramModeModel

#CURRICULUM MODEL IS USED TO SELECT THE STUDENT ENROLLED PROGRAM,COURSE,BATCH AND THE PROGRAM MODE
class CurriculumModel(models.Model):
    enrolled_program=models.ForeignKey(ProgramModel,on_delete=models.CASCADE)
    enrolled_course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    enrolled_batch=models.ForeignKey(BatchModel,on_delete=models.CASCADE)
    enrolled_program_mode=models.ForeignKey(ProgramModeModel,on_delete=models.CASCADE)

#STUDENT PROFILE MODEL IS USED TO STORE THE ALL THE DETAILS ABOUT A STUDENT
class StudentProfileModel(models.Model):
    student_name=models.CharField(max_length=50)
    student_contact=models.IntegerField()
    student_dob=models.DateField()
    student_address=models.TextField()
    student_photo=models.ImageField()
    student_signature=models.ImageField()

#STUDENT MODEL THAT REFER STUDENT PROFILE MODEL AND CURRICULUM MODEL
class StudentModel(models.Model):
    student_uid=models.CharField(max_length=50)
    student_email=models.EmailField()
    student_aadhar_number=models.IntegerField()
    student_sslc_number=models.IntegerField()
    curriculumKey=models.ForeignKey(CurriculumModel,on_delete=models.CASCADE)
    student_profileKey=models.OneToOneField(StudentProfileModel,on_delete=models.CASCADE)#FOR EACH STUDENT HAS EXACTLY ONE PROFILE SO USE ONETOONEFIELD


