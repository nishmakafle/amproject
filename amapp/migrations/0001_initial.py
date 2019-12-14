# Generated by Django 3.0 on 2019-12-13 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=200)),
                ('deadline', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('semester', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=200)),
                ('roll_no', models.CharField(max_length=200)),
                ('class_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amapp.ClassRoom')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('class_room', 'roll_no')},
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignment_status', models.CharField(choices=[('Started', 'Started'), ('Completed', 'Completed'), ('Checked', 'Checked'), ('Not Submitted', 'Not Submitted')], default='Assigned', max_length=50)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('review', models.CharField(blank=True, max_length=200, null=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amapp.Assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amapp.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amapp.Program'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='class_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amapp.ClassRoom'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amapp.Student'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amapp.Teacher'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
