# Generated by Django 4.2.11 on 2024-04-28 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='grade',
            new_name='subject',
        ),
    ]
