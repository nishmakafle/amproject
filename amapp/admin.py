from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Program, ClassRoom, Admin, Teacher,
                     Student, Assignment, Submission])
