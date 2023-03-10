# Generated by Django 4.1.6 on 2023-02-02 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_body_image_alter_body_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MobiType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Rang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='body',
            name='education',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.education'),
        ),
        migrations.AddField(
            model_name='body',
            name='mobitype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.mobitype'),
        ),
        migrations.AddField(
            model_name='body',
            name='rang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.rang'),
        ),
    ]
