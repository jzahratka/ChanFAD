# Generated by Django 2.2.24 on 2021-11-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdb', models.CharField(max_length=4)),
                ('species', models.CharField(max_length=50)),
                ('geneName', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('ion', models.CharField(max_length=3)),
                ('icn3d', models.TextField(max_length=5000)),
                ('submitter', models.CharField(max_length=50)),
                ('uniprot', models.CharField(max_length=6)),
                ('channelpedia', models.CharField(max_length=1000)),
                ('dateSubmission', models.DateTimeField()),
            ],
        ),
    ]
