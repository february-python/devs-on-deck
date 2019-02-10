# Generated by Django 2.1.5 on 2019-02-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devs', '0001_initial'),
        ('orgs', '0002_auto_20190209_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pos_dev', models.ManyToManyField(related_name='pos_dev', to='devs.Dev')),
                ('pos_org', models.ManyToManyField(related_name='pos_org', to='orgs.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255)),
                ('developer', models.ManyToManyField(related_name='dev', to='devs.Dev')),
                ('position', models.ManyToManyField(related_name='pos', to='orgs.Position')),
            ],
        ),
    ]