# Generated by Django 5.1.3 on 2024-12-12 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calendar',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('calendar_date', models.DateField(blank=True, null=True)),
                ('calendar_time', models.TimeField(blank=True, null=True)),
                ('calendar_event', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'school_calendar',
            },
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'school_faculties',
            },
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('student_level', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'school_levels',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('secretary', models.CharField(blank=True, max_length=45, null=True)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.faculties')),
            ],
            options={
                'db_table': 'school_departments',
            },
        ),
        migrations.CreateModel(
            name='Lecturers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('active', models.CharField(blank=True, max_length=5, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.departments')),
            ],
            options={
                'db_table': 'school_lecturers',
            },
        ),
        migrations.AddField(
            model_name='faculties',
            name='dean',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.lecturers'),
        ),
        migrations.AddField(
            model_name='departments',
            name='h_o_d',
            field=models.OneToOneField(blank=True, db_column='h_o_d', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.lecturers'),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('desription', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.departments')),
                ('lecturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.lecturers')),
            ],
            options={
                'db_table': 'school_courses',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('d_o_b', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('active', models.CharField(blank=True, max_length=5, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.departments')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.levels')),
            ],
            options={
                'db_table': 'school_students',
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('attendance', models.IntegerField(blank=True, null=True)),
                ('assignment', models.IntegerField(blank=True, null=True)),
                ('test_score', models.IntegerField(blank=True, null=True)),
                ('exam_scores', models.IntegerField(blank=True, null=True)),
                ('total_scores', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=1, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.courses')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.students')),
            ],
            options={
                'db_table': 'school_results',
            },
        ),
        migrations.CreateModel(
            name='Guardians',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('relationship', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('active', models.CharField(blank=True, max_length=5, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.students')),
            ],
            options={
                'db_table': 'school_guardians',
            },
        ),
    ]