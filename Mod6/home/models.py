from django.db import models
from datetime import date
# Create your models here.

class Scholarship(models.Model):
    scholarshipID = models.CharField(max_length=100)
    denomination = models.CharField(max_length=255)
    referred_studies = models.CharField(max_length=255)
    minimum_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    criteria = models.CharField(max_length=255)
class School(models.Model):
    schoolID = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    school_type = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_phone_1 = models.CharField(max_length=255)
    contact_phone_2 = models.CharField(max_length=255)

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_type = models.IntegerField(default=1)
    ##User type maps to numbers that each represent the user type
    ##IE donor = 1, applicant = 2
    address = models.CharField(max_length=255)
    phone_1 = models.CharField(max_length=255)
    phone_2 = models.CharField(max_length=255)
    date_of_birth_day = models.CharField(max_length=2)
    date_of_b6irth_month = models.CharField(max_length=2)
    date_of_birth_year = models.CharField(max_length=4)
    city_of_birth = models.CharField(max_length=255)
    province_of_birth = models.CharField(max_length=255)
    country_of_birth = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    marital_status=models.IntegerField()
    number_of_children=models.IntegerField(default=0)
    occupation = models.CharField(max_length=255)
    employer_name = models.CharField(max_length=255)
    employer_address = models.CharField(max_length=255)
    

class Student_Scholarship(models.Model):
    scholarshipID = models.ForeignKey(Scholarship, on_delete=models.DO_NOTHING)
    username = models.ForeignKey(User, models.DO_NOTHING)
    awarded_on = models.DateField(default=date.today)
    delivery_method = models.CharField(max_length=255)
    award_justification = models.CharField(max_length=255)
    awarded_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Scholarship_Donation(models.Model):
    scholarshipID = models.ForeignKey(Scholarship, on_delete=models.DO_NOTHING)
    donorID = models.ForeignKey(User, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    academic_year = models.DecimalField(max_digits=10, decimal_places=2)



class Student_Education(models.Model):
    schoolID = models.ForeignKey(School, models.DO_NOTHING)
    username = models.ForeignKey(User, models.DO_NOTHING)
    year_attended = models.CharField(max_length=4)
    class_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    degree  = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    dismissed = models.IntegerField(default=0)
    dismissal_reason  = models.CharField(max_length=255)

class Student_Hollow_Year(models.Model):
    username = models.ForeignKey(User, models.DO_NOTHING)
    hollow_year = models.CharField(max_length=255)
    activities = models.CharField(max_length=255)


class Tuition_Fees(models.Model):
    schoolID = models.ForeignKey(School, models.DO_NOTHING)
    academic_level = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=255)
    tuition = models.CharField(max_length=255)
    clothing = models.CharField(max_length=255)
    furniture = models.CharField(max_length=255)
    books = models.CharField(max_length=255)
    misc = models.CharField(max_length=255)