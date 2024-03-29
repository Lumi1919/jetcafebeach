# Generated by Django 3.2.6 on 2021-08-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlatDuJour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationsRestaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('numeroTel', models.CharField(blank=True, max_length=12, null=True)),
                ('mail', models.EmailField(blank=True, max_length=200, null=True)),
                ('nombreDePersonnes', models.IntegerField(blank=True, null=True)),
                ('tables', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
    ]
