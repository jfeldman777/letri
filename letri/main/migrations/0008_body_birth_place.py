# Generated by Django 4.1.6 on 2023-02-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_body_birth_date_body_death_date_body_flag_done_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='body',
            name='birth_place',
            field=models.TextField(blank=True, null=True, verbose_name='место рождения'),
        ),
    ]
