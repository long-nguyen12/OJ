# Generated by Django 2.2.17 on 2021-01-06 05:44
# Formatted by Thuc Le to follow flake8
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0115_add_custom_cpp_checker'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='is_polygon_problem',
            field=models.BooleanField(
                default=False, help_text='Is the problem statement copied from polygon html?', verbose_name='polygon problem '),
        ),
        migrations.AlterField(
            model_name='problemtranslation',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('vi', 'Vietnamese')],
                                   max_length=7, verbose_name='language'),
        ),
    ]
