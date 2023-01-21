# Generated by Django 4.1.4 on 2022-12-17 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=30)),
                ('surname', models.CharField(db_column='Surname', max_length=30)),
            ],
            options={
                'db_table': 'curators',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.PositiveSmallIntegerField(db_column='Building')),
                ('financing', models.DecimalField(db_column='Financing', decimal_places=2, max_digits=10)),
                ('name', models.CharField(db_column='Name', max_length=100, unique=True)),
            ],
            options={
                'db_table': 'departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=100, unique=True)),
            ],
            options={
                'db_table': 'faculties',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=10, unique=True)),
                ('year', models.PositiveIntegerField(db_column='Year')),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupsCurators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'groupscurators',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupsLectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'groupslectures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupsStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'groupsstudents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_column='Date')),
            ],
            options={
                'db_table': 'lectures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=30)),
                ('surname', models.CharField(db_column='Surname', max_length=30)),
                ('rating', models.PositiveSmallIntegerField(db_column='Rating')),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=100, unique=True)),
            ],
            options={
                'db_table': 'subjects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=30)),
                ('surname', models.CharField(db_column='Surname', max_length=30)),
                ('salary', models.DecimalField(db_column='Salary', decimal_places=2, max_digits=8)),
                ('isprofessor', models.BooleanField(db_column='IsProfessor')),
            ],
            options={
                'db_table': 'teachers',
                'managed': False,
            },
        ),
    ]