# Generated by Django 4.0.6 on 2022-07-15 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('openyear', models.IntegerField(verbose_name='개봉년도')),
                ('genre', models.CharField(max_length=50, verbose_name='장르')),
                ('score', models.IntegerField(verbose_name='별점')),
                ('runningtime', models.IntegerField(verbose_name='러닝타임')),
                ('content', models.TextField(verbose_name='리뷰')),
                ('director', models.CharField(max_length=50, verbose_name='감독')),
                ('actor', models.CharField(max_length=50, verbose_name='배우')),
            ],
        ),
    ]