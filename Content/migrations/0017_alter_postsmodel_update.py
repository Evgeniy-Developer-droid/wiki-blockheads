# Generated by Django 4.1.5 on 2023-01-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0016_postsmodel_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsmodel',
            name='update',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
