# Generated by Django 4.0.3 on 2022-03-16 17:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='bookmanage',
            fields=[
                ('bookid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=50)),
                ('bookimage', models.CharField(max_length=1000)),
                ('bookgenary', models.CharField(max_length=50)),
                ('bookdescription', models.TextField(max_length=600)),
                ('bookratingid', models.CharField(max_length=150)),
                ('bookpdf', models.FileField(max_length=20, upload_to='')),
                ('dateofadd', models.CharField(max_length=50)),
                ('authorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmanage.author')),
            ],
        ),
    ]
