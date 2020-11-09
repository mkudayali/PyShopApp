from django.contrib.auth.models import User
from django.db import models
from threading import current_thread
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
from django.utils.timezone import now
from django.conf import settings

from pyshop import settings

_requests = {}


def get_username():
    t = current_thread()
    if t not in _requests:
         return None
    return _requests[t]


# Project Class
from pip._internal.utils import datetime


class Projects(models.Model):
    ProjectName = models.CharField(max_length=255)
    Description = models.TextField(max_length=2048, default="", blank=True)
    ContactName = models.CharField(max_length=255)
    Email = models.EmailField()
    ContactNumber = models.CharField(max_length=12)
    SpecialNotes = models.TextField(max_length=2048, default="", blank=True)
    Status = models.BooleanField(default=True)

    def __str__(self):
        return self.ProjectName

class Employees(models.Model):
    EmpName = models.CharField(max_length=500)
    EmpID = models.CharField(max_length=10)
    Designation = models.CharField(max_length=200)
    CurrentlyEmployed = models.BooleanField(default=True)
    Mobile = models.CharField(max_length=12)
    PersonalEmail = models.EmailField(blank=True)
    OfficialEmail = models.EmailField(blank=True)
    StartDate = models.DateField()
    EndDate = models.DateField(default="1989-01-01", blank=True)
    Address = models.CharField(blank=True, max_length= 300)
    Education = models.CharField(blank=True, max_length=200)
    Experience = models.CharField(blank=True, max_length= 100)
    SkillSet = models.TextField(max_length=3000, blank=True)


class Day(models.Model):
    Date = models.DateField(blank=True)
    Description = models.TextField(max_length=3000)


#class CurrentUserDjango(models.User):


class Timesheets(models.Model):
    EmpUser = models.CharField(default=CurrentUserField().default, editable = None, max_length=100)
    ProjectName = models.ForeignKey(Projects, default=0, verbose_name="Select Project", on_delete=models.SET_DEFAULT)
    StartPeriod = models.DateField(default=now)
    EndPeriod = models.DateField(default=now)
    Day1 = models.IntegerField(default=0, blank=True)
    Day2 = models.IntegerField(default=0, blank=True)
    Day3 = models.IntegerField(default=0, blank=True)
    Day4 = models.IntegerField(default=0, blank=True)
    Day5 = models.IntegerField(default=0, blank=True)
    Day6 = models.IntegerField(default=0, blank=True)
    Day7 = models.IntegerField(default=0, blank=True)
    Notes = models.TextField(max_length=5000, blank=True)


class TimeSheetMain(models.Model):
    EmpUser = models.CharField(default=CurrentUserField().default, editable = None, max_length=100)
    SubmitDate = models.DateField(default=now)


class TimeSheetDate(models.Model):
    show = models.ForeignKey(
        TimeSheetMain, on_delete=models.CASCADE, related_name="photos"
    )
    ProjectName = models.ForeignKey(Projects, default=0, verbose_name="Select Project", on_delete=models.SET_DEFAULT)
    date = models.DateField(default=now)
    hours = models.IntegerField(default=0, blank=False)
    instructions = models.TextField(blank=True)
