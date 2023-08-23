# Generated by Django 4.2.4 on 2023-08-21 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('periodity', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно')], max_length=50)),
                ('action', models.CharField(max_length=100, verbose_name='действие')),
                ('length', models.IntegerField(verbose_name='продолжительность в мин')),
                ('reward', models.CharField(max_length=100, verbose_name='вознаграждение')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='приятная?')),
                ('is_public', models.BooleanField(default=True, verbose_name='публичная?')),
                ('linked_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.habit')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ['owner'],
            },
        ),
    ]
