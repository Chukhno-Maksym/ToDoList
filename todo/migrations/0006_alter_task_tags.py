# Generated by Django 4.1 on 2025-01-31 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='todo.tag'),
        ),
    ]
