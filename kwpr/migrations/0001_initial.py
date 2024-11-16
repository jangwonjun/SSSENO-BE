# Generated by Django 5.1.3 on 2024-11-16 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor', models.CharField(max_length=45)),
                ('college', models.CharField(max_length=45)),
                ('department', models.CharField(max_length=45)),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('photo', models.CharField(blank=True, max_length=45, null=True)),
                ('number', models.CharField(blank=True, max_length=45, null=True)),
                ('lab', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('subject1', models.CharField(blank=True, max_length=45, null=True)),
                ('subject2', models.CharField(blank=True, max_length=45, null=True)),
                ('subject3', models.CharField(blank=True, max_length=45, null=True)),
                ('repu1', models.IntegerField(default=0)),
                ('repu2', models.IntegerField(default=0)),
                ('repu3', models.IntegerField(default=0)),
                ('repu4', models.IntegerField(default=0)),
                ('repu5', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'info',
            },
        ),
    ]
