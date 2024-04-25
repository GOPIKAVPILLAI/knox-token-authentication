
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

    def _create_user(self,email,role,password,**extra_fields):
        if not email:
            raise ValueError("User must have an Email address")
        now=timezone.now()
        email = self.normalize_email(email)
        user=self.model(
           
            email=email,
            # is_staff=is_staff,
            is_active=True,
            # is_superuser=is_superuser,
            role=role,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,email,role,password,**extra_fields):
        return self._create_user(email,role,password,is_staff=False, is_superuser=False,**extra_fields)
    
    def create_superuser(self,email,role,password,**extra_fields):
        user=self._create_user(email,role,password,is_staff=True, is_superuser=True,**extra_fields)
        return user
    
    

class User(AbstractBaseUser,PermissionsMixin):
    ADMIN=1
    STUDENT=2
    FACULTY=3
    MODERATOR=4
    ROLE_choice = (
        (ADMIN,"Admin"),
        (STUDENT,"Student"),
        (FACULTY,"Faculty"),
        (MODERATOR,"Moderator")
    )
    email=models.EmailField(max_length=254,unique=True)
    role=models.PositiveSmallIntegerField(choices=ROLE_choice)
    name=models.CharField(max_length=254,null=True,blank=True)
    is_staff=models.BooleanField(default=False,null=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    last_login=models.DateTimeField(null=True,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD='email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=["role"]
    objects=UserManager()
    
    def get_absolute_url(self):
        return "/core/%i/" % (self.pk)
    def is_admin(self):
        return self.role == self.ADMIN
    def is_student(self):
        return self.role == self.STUDENT
    def is_faculty(self):
        return self.role == self.FACULTY
    def is_moderator(self):
        return self.role == self.MODERATOR