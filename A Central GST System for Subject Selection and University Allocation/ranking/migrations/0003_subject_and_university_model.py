# Generated by Django 3.1.7 on 2022-04-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0002_email_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_and_University_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.CharField(max_length=100, null=True)),
                ('student_university', models.CharField(max_length=100, null=True)),
                ('student_subject', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
