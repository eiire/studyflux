# Generated by Django 3.1.2 on 2021-07-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm',
            name='code',
            field=models.IntegerField(default=False),
        ),
    ]
