# Generated by Django 4.2.4 on 2023-08-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_habit_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodity',
            field=models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], max_length=50),
        ),
    ]