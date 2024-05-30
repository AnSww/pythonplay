from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Achievements(models.Model):
    achievename = models.CharField(db_column='AchieveName', primary_key=True, max_length=255)  # Field name made lowercase.
    goal = models.CharField(max_length=255)
    reward = models.CharField(max_length=255)

    def __str__(self):
        return self.achievename


class Achievementslist(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase. The composite primary key (UserID, AchieveName) found, that is not supported. The first column is selected.
    achievename = models.ForeignKey(Achievements, models.DO_NOTHING, db_column='AchieveName')  # Field name made lowercase.

    def __str__(self):
        return '%s%s' %(self.achievename, self.userid)


class Tasks(models.Model):
    taskid = models.AutoField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    difficulty = models.IntegerField(db_column='Difficulty')  # Field name made lowercase.

    def __str__(self):
        return self.name


class Taskcompletions(models.Model):
    userid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    taskid = models.ForeignKey('Tasks', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('userid', 'taskid')

    def __str__(self):
        return '%s%s' % (self.userid, self.taskid)


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    experience = models.IntegerField()

    def __str__(self):
        return self.username