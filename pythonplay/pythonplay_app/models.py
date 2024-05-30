from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Achievement(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'achievement')

    def __str__(self):
        return f'{self.user.username} - {self.achievement.title}'


class Taskcompletions(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task = models.ForeignKey('Tasks', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'task')

    def __str__(self):
        return '%s%s' % (self.user, self.task)


class Tasks(models.Model):
    taskid = models.AutoField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description_theory = models.TextField(db_column='description_theory', blank=True, null=True)  # Field name made lowercase.
    description_task = models.TextField(db_column='description_task', blank=True, null=True)  # Field name made lowercase.
    description_goals = models.TextField(db_column='description_goals', blank=True, null=True)  # Field name made lowercase.
    difficulty = models.IntegerField(db_column='Difficulty')  # Field name made lowercase.

    def __str__(self):
        return self.name





class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    experience = models.IntegerField()

    def __str__(self):
        return self.username