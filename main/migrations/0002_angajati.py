# Generated by Django 4.0.3 on 2022-03-11 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='angajati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=15)),
                ('prenume', models.CharField(max_length=15)),
                ('varsta', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('O', 'O')], default='M', max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('data_nasterii', models.DateTimeField(default=django.utils.timezone.now)),
                ('nationalitate', models.CharField(max_length=45)),
                ('adresa', models.CharField(max_length=100)),
            ],
        ),
    ]
