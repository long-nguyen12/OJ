# Generated by Django 2.2.17 on 2021-03-10 09:22

import django.core.validators
from django.db import migrations, models

import judge.models.problem_data
import judge.utils.problem_data


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0119_remove_py_cpp_checker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemdata',
            name='custom_checker',
            field=models.FileField(blank=True, null=True, storage=judge.utils.problem_data.ProblemDataStorage(), upload_to=judge.models.problem_data.problem_directory_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['cpp', 'py'])], verbose_name='custom checker file'),
        ),
    ]
