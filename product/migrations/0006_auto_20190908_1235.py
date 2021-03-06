# Generated by Django 2.2.5 on 2019-09-08 07:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0005_auto_20190908_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nicename', models.CharField(max_length=50)),
                ('user_registered', models.DateTimeField()),
                ('display_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
