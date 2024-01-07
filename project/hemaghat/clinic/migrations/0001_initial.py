# Generated by Django 4.2.8 on 2024-01-07 11:10

import clinic.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact_info', models.CharField(max_length=200)),
                ('services', models.TextField()),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, validators=[clinic.validators.username_validation])),
                ('email', models.EmailField(max_length=200, validators=[clinic.validators.email_validation])),
                ('password', models.CharField(max_length=200, validators=[clinic.validators.password_validation])),
                ('user_type', models.CharField(choices=[('Doctor', 'Doctor'), ('Patient', 'Patient'), ('Secretary', 'Secretary')], max_length=10)),
                ('logged_in', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], max_length=10)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.appointment')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.clinic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.user')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_id', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.user')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.clinic'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.user'),
        ),
    ]
