# Generated by Django 4.1.5 on 2023-02-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, max_length=45, null=True)),
                ('lastname', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(blank=True, max_length=45, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('mobileno', models.CharField(blank=True, max_length=45, null=True)),
                ('usercol', models.CharField(blank=True, max_length=45, null=True)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('confirmpassword', models.CharField(blank=True, max_length=45, null=True)),
                ('isactive', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
