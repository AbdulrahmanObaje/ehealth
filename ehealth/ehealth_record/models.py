from django.contrib.auth.base_user import BaseUserManager
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class State(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class UserCustomManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('The given phonenumber must be set')
        user = self.model(phone_number=phone_number, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone_number, password, **extra_fields)

    def create_superuser(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone_number, password, **extra_fields)

class User(AbstractUser):
    # You have to remove 'username' and 'password'!
    username = None
    # password = None
    sex = models.CharField(max_length = 10, default='')
    role = models.CharField(max_length = 60, default='')
    email = models.EmailField(null=True, blank=True, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length = 60)
    is_owner = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
    dob = models.DateTimeField(null=True)
    image = models.ImageField(blank=True, null=True)
    data_join = models.DateTimeField(default=timezone.now)
    code_agency = models.IntegerField(null=True, blank=True, default=0)

    USERNAME_FIELD = 'email'
    # You must remove the 'phone_number' from REQUIRED_FIELDS!
    # Here you can't repeat in the REQUIRED_FIELDS the same field that you put in USERNAME_FIELD, you can add other: 'email', etc ...
    REQUIRED_FIELDS = []
    
    objects = UserCustomManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email
   
    
class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   marital_status = models.CharField(max_length = 10, default='')
   h_address = models.CharField(max_length = 200, default='')
   w_address = models.CharField(max_length = 200, default='')
   lga = models.CharField(max_length = 5, default=0)
   state = models.CharField(max_length = 5, default=0)
   country = models.CharField(max_length = 5, default=0)
   picture = models.ImageField(upload_to = 'img')

   class Meta:
      db_table = "profile"

class Ailment(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_patient', unique=False, verbose_name="Patient")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='related_state', verbose_name="State Residing", unique=False, blank=True, null=True)
    ailment = models.ForeignKey(Ailment, on_delete=models.CASCADE)
    diagnosis = models.CharField(null=True, blank=True, max_length=500)
    prescription = models.CharField(null=True, blank=True, max_length=500)
    added_by = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ailment

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment_user', unique=False, verbose_name="User")
    appointment_consultant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_appointment_consultant', verbose_name="Related Appointment Consultant", unique=False, blank=True, null=True)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    appointment_date = models.DateTimeField(default=timezone.now)
    added_by = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Appointment_Meta(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    appointment_date_time = models.DateTimeField()
    defered_date_time = models.DateTimeField()
    added_by = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

