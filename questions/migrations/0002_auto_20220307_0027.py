# Generated by Django 3.2 on 2022-03-07 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'replies'},
        ),
        migrations.RenameField(
            model_name='question',
            old_name='updated_on',
            new_name='last_updated',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='updated_on',
            new_name='last_updated',
        ),
    ]
