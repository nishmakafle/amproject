# Generated by Django 3.0 on 2019-12-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default=1, upload_to='teacher'),
            preserve_default=False,
        ),
    ]