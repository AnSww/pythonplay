from django.contrib import admin
from pythonplay_app.models import Users, Achievement, UserAchievement, Tasks, Taskcompletions
# Register your models here.

admin.site.register(Users)
admin.site.register(Achievement)
admin.site.register(UserAchievement)
admin.site.register(Tasks)
admin.site.register(Taskcompletions)

