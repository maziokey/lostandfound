# Generated by Django 2.1.1 on 2018-10-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0003_auto_20180930_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('AVAILABLE', 'Available'), ('PICKED UP', 'Picked Up')], default='AVAILABLE', max_length=12),
        ),
    ]