from django.contrib import admin
from pythonplay_app.models import Users, Achievements, Achievementslist, Tasks, Taskcompletions
# Register your models here.

admin.site.register(Users)
admin.site.register(Achievements)
admin.site.register(Achievementslist)
admin.site.register(Tasks)
admin.site.register(Taskcompletions)

