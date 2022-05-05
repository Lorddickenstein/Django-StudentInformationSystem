from django.utils.translation import gettext_lazy as _
from django.db import models
# from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, user_id, first_name, last_name, sex, birthday, age, branch, is_regular, password=None, **extra_fields):
        """
        Creates and saves a User.
        """
        if not email:
            raise ValueError('Users must have an email address')

        extra_fields.setdefault('middle_name', '')
        extra_fields.setdefault('address', '')

        user = self.model(
            email=self.normalize_email(email),
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            birthday=birthday,
            age=age,
            branch=branch,
            is_regular=is_regular,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_staffuser(self, email, user_id, first_name, last_name, sex, birthday, age, branch, is_regular, password, **extra_fields):
        """
        Creates and saves a staff user.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            birthday=birthday,
            age=age,
            branch=branch,
            is_regular=is_regular,
            **extra_fields,
        )
        user.staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, user_id, first_name, last_name, sex, birthday, age, branch, is_regular, password=None, **extra_fields):
        """
        Creates and saves a superuser.
        """
        user = self.create_user(
            email,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            birthday=birthday,
            age=age,
            branch=branch,
            is_regular=is_regular,
            password=password,
            **extra_fields,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser):

    class SexOptions(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    class BranchOptions(models.TextChoices):
        MANILA = 'MN', _('Manila')
        TAGUIG = 'TC', _('Taguig City')
        QUEZON_CITY = 'QC', _('Quezon City')
        SAN_JUAN_CITY = 'SJ', _('San Juan City')
        PARANAQUE_CITY = 'PC', _('Paranaque City')

    user_id = models.CharField('User ID', max_length=15, primary_key=True)
    email = models.EmailField('Email Address', max_length=120, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    is_regular = models.BooleanField(default=True)
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80)
    address = models.CharField(max_length=200, blank=True)
    sex = models.CharField(max_length=1, choices=SexOptions.choices)
    birthday = models.DateField()
    age = models.IntegerField()
    branch = models.CharField(max_length=2, choices=BranchOptions.choices)
    mobile_num = models.CharField(max_length=11)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'birthday', 'age', 'branch', 'sex', 'is_regular']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.middle_name[0]}. {self.last_name}'
    
    def get_first_name(self):
        return self.first_name
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin


class Subject(models.Model):

    sub_code = models.CharField('Subject Code', max_length=10, null=False, primary_key=True)
    year_level = models.IntegerField()
    description = models.CharField(max_length=120)
    units = models.IntegerField()

    def __str__(self):
        return self.description


class Grades(models.Model):

    # User = settings.AUTH_USER_MODEL

    stud_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Student ID', related_name='grades_student')
    sub_code = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Subject Code')
    admin_id = models.ForeignKey(UserProfile, on_delete=models.SET_DEFAULT, default='', verbose_name='Faculty', related_name='grades_faculty')
    final_grade = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.final_grade


class Department(models.Model):

    # Use = settings.AUTH_USER_MODEL

    dep_id = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=120)

    def get_id(self):
        return self.dep_id

    def __str__(self):
        return self.description


class Schedule(models.Model):

    # UserProfile = settings.AUTH_USER_MODEL

    stud_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Student ID', related_name='schedule_student')
    day_sched = models.CharField(max_length=5)
    time_sched = models.CharField(max_length=30)
    admin_id = models.ForeignKey(UserProfile, on_delete=models.SET_DEFAULT, default='', verbose_name='Faculty', related_name='schedule_faculty')

    def __str__(self):
        return f'{self.day_sched} {self.time_sched}'