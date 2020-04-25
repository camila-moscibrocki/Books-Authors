# Generated by Django 3.0.5 on 2020-04-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('edition', models.FloatField()),
                ('publication_year', models.IntegerField()),
                ('author', models.ManyToManyField(to='authors.Author')),
            ],
        ),
    ]