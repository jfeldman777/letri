# Generated by Django 4.1.6 on 2023-02-02 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Army',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('army', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.army')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.region')),
            ],
        ),
    ]
