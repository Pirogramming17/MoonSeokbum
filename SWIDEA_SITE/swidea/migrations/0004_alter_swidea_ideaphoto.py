# Generated by Django 4.0.6 on 2022-07-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swidea', '0003_alter_swidea_ideachoice_alter_swidea_ideaphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swidea',
            name='ideaphoto',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='아이디어사진'),
        ),
    ]
