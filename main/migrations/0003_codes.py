# Generated by Django 3.2.14 on 2022-12-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_student_visibility'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('admin', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
            ],
        ),
    ]
