from django.contrib.auth.models import User, Group
from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Program(TimeStamp):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


SEMESTER = (
    ('I', 'I'),
    ('II', 'II'),
    ('III', 'III'),
    ('IV', 'IV'),
    ('V', 'V'),
    ('VI', 'VI'),
    ('VII', 'VII'),
    ('VIII', 'VIII'),
)


class ClassRoom(TimeStamp):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50, choices=SEMESTER)

    def __str__(self):
        return self.program.title + " Semester " + self.semester


class Admin(TimeStamp):
    full_name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name="Admin")
        self.user.groups.add(group)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Teacher(TimeStamp):
    full_name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teacher')

    def save(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name="Teacher")
        self.user.groups.add(group)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Student(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='student')

    def save(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name="Student")
        self.user.groups.add(group)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ['class_room', 'roll_no']

    def __str__(self):
        return self.full_name


class Assignment(TimeStamp):
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to=200)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title


ASSIGNMENT_STATUS = (
    ('Started', 'Started'),
    ('Completed', 'Completed'),
    ('Checked', 'Checked'),
    ('Not Submitted', 'Not Submitted'),
)


class Submission(TimeStamp):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    assignment_status = models.CharField(
        max_length=50, choices=ASSIGNMENT_STATUS, default="Assigned")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True)
    file_upload_date = models.DateTimeField(null=True, blank=True)
    review = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.assignment.title
