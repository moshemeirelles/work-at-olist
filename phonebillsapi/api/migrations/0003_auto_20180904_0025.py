# Generated by Django 2.1 on 2018-09-04 00:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180904_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callrecord',
            name='destination',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '12345678910'. 10 to 11 digits allowed.", regex='\\d{10,11}')]),
        ),
        migrations.AlterField(
            model_name='callrecord',
            name='source',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '12345678910'. 10 to 11 digits allowed.", regex='\\d{10,11}')]),
        ),
    ]
