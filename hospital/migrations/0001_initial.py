# Generated by Django 3.0.3 on 2020-02-16 10:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'hospital_admin',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('pictures', models.ImageField(upload_to='department/')),
            ],
            options={
                'db_table': 'hospital_department',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('speciality', models.CharField(max_length=120)),
                ('picture', models.ImageField(upload_to='experts/')),
            ],
            options={
                'db_table': 'hospital_doctor',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening')], max_length=10)),
                ('note', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='hospital.Doctor')),
            ],
        ),
    ]
