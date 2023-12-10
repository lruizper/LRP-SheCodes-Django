# Generated by Django 4.2.2 on 2023-12-09 04:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="profile_pic",
            field=models.URLField(blank=True, null=True, verbose_name="profile-pic"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
