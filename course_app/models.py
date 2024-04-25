#KMA COURSE RELATED ALL MODELS
from django.db import models

#PROGRAM MODE MODEL FOR SELECTING ONLINE,OFFLINE OR HYBRID MODE OF CLASS
class ProgramModeModel(models.Model):
    mode_name=models.CharField(max_length=100)

#SUBJECT MODEL 
class SubjectModel(models.Model):
    subject_name=models.CharField(max_length=100)

#CENTER MODEL FOR SELECTING THE LOCATION
class CenterModel(models.Model):
    center_name=models.CharField(max_length=100)

#BATCH MODEL
class BatchModel(models.Model):
    batch_name=models.CharField(max_length=100)

#SEMESTER MODEL
class SemesterModel(models.Model):
    semester=models.CharField(max_length=100)

#PROGRAM MODEL THAT REFER SEMESTER MODEL ONLY IF IT APPLICABLE
class ProgramModel(models.Model):
    program_name=models.CharField(max_length=100)
    semesterKey=models.ForeignKey(SemesterModel,on_delete=models.CASCADE)

#COURSE MODEL THAT REFER PROGRAM MODEL,SUBJECT MODEL,BATCH MODEL AND CENTER MODEL
class CourseModel(models.Model):
    programKey=models.ForeignKey(ProgramModel,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=100)
    subjectKey=models.ForeignKey(SubjectModel,on_delete=models.CASCADE)
    batchKey=models.ForeignKey(BatchModel,on_delete=models.CASCADE)
    centerKey=models.ManyToManyField(CenterModel,on_delete=models.CASCADE)#FOR EACH COURSE HAS MULTIPLE CENTER AND FOR EACH CENTER HAS MULTPLE COURSE SO HERE USE MANYTOMANYFIELD