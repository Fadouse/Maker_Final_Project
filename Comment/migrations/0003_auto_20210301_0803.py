# Generated by Django 3.1.7 on 2021-03-01 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20210301_0513'),
        ('Comment', '0002_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Post.post'),
        ),
    ]
