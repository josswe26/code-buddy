# Generated by Django 3.2 on 2022-03-22 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20220307_0051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='votes_count',
            new_name='votes_score',
        ),
    ]
