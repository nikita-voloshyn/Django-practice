# Generated by Django 4.2.4 on 2023-09-19 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("age", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="ContactData",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("data_type", models.CharField(max_length=20)),
                ("data_value", models.CharField(max_length=100)),
                ("contact", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="application.contact")),
            ],
        ),
    ]
