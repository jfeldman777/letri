# Generated by Django 4.1.6 on 2023-02-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_letter_alter_body_army_alter_body_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='phone',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Contact Phone'),
        ),
    ]
