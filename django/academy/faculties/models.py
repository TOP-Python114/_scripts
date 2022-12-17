from django.db import models


class Faculty(models.Model):
    name = models.CharField(db_column='Name', unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'faculties'


class Department(models.Model):
    building = models.PositiveSmallIntegerField(db_column='Building')
    financing = models.DecimalField(db_column='Financing', max_digits=10, decimal_places=2)
    name = models.CharField(db_column='Name', unique=True, max_length=100)
    faculty = models.ForeignKey(Faculty, models.CASCADE, db_column='FacultyId')

    class Meta:
        managed = False
        db_table = 'departments'


class Student(models.Model):
    name = models.CharField(db_column='Name', max_length=30)
    surname = models.CharField(db_column='Surname', max_length=30)
    rating = models.PositiveSmallIntegerField(db_column='Rating')

    class Meta:
        managed = False
        db_table = 'students'


class Curator(models.Model):
    name = models.CharField(db_column='Name', max_length=30)
    surname = models.CharField(db_column='Surname', max_length=30)

    class Meta:
        managed = False
        db_table = 'curators'


class Subject(models.Model):
    name = models.CharField(db_column='Name', unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'subjects'


class Teacher(models.Model):
    name = models.CharField(db_column='Name', max_length=30)
    surname = models.CharField(db_column='Surname', max_length=30)
    salary = models.DecimalField(db_column='Salary', max_digits=8, decimal_places=2)
    isprofessor = models.BooleanField(db_column='IsProfessor')
    subjects = models.ManyToManyField(Subject, through='Lecture')

    class Meta:
        managed = False
        db_table = 'teachers'


class Lecture(models.Model):
    date = models.DateField(db_column='Date')
    subject = models.ForeignKey(Subject, models.CASCADE, db_column='SubjectId')
    teacher = models.ForeignKey(Teacher, models.CASCADE, db_column='TeacherId')

    class Meta:
        managed = False
        db_table = 'lectures'


class Group(models.Model):
    name = models.CharField(db_column='Name', unique=True, max_length=10)
    year = models.PositiveIntegerField(db_column='Year')
    department = models.ForeignKey(Department, models.CASCADE, db_column='DepartmentId')
    students = models.ManyToManyField(Student, through='GroupsStudents')
    curators = models.ManyToManyField(Curator, through='GroupsCurators')
    lectures = models.ManyToManyField(Lecture, through='GroupsLectures')

    class Meta:
        managed = False
        db_table = 'groups'


class GroupsStudents(models.Model):
    student = models.ForeignKey(Student, models.CASCADE, db_column='StudentId')
    group = models.ForeignKey(Group, models.CASCADE, db_column='GroupId')

    class Meta:
        managed = False
        db_table = 'groupsstudents'


class GroupsCurators(models.Model):
    curator = models.ForeignKey(Curator, models.CASCADE, db_column='CuratorId')
    group = models.ForeignKey(Group, models.CASCADE, db_column='GroupId')

    class Meta:
        managed = False
        db_table = 'groupscurators'


class GroupsLectures(models.Model):
    lecture = models.ForeignKey(Lecture, models.CASCADE, db_column='LectureId')
    group = models.ForeignKey(Group, models.CASCADE, db_column='GroupId')

    class Meta:
        managed = False
        db_table = 'groupslectures'
