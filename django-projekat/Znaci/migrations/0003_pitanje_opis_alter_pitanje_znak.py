# Generated by Django 4.0.2 on 2022-02-11 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Znaci', '0002_rename_netacan_odg1_pitanje_netacni_odg1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitanje',
            name='opis',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pitanje',
            name='znak',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
