# Generated by Django 3.2.9 on 2022-07-28 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_resturantbranch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resturantbranch',
            name='resturant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.resturant'),
        ),
    ]
