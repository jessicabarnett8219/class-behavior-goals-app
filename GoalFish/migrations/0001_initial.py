# Generated by Django 2.1.7 on 2019-03-16 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('schoolWeek', models.IntegerField()),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('score3', models.IntegerField()),
                ('score4', models.IntegerField()),
                ('score5', models.IntegerField()),
                ('score6', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='GradeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('classroomTeacher', models.CharField(max_length=50)),
                ('avatar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goalfish.Avatar')),
                ('gradeLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goalfish.GradeLevel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='goal1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal1', to='goalfish.Goal'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='goal2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal2', to='goalfish.Goal'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='goal3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal3', to='goalfish.Goal'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='goal4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal4', to='goalfish.Goal'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='goal5',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal5', to='goalfish.Goal'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='goal6',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal6', to='goalfish.Goal'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goalfish.Student'),
        ),
    ]
