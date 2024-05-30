from django.urls import path
from .views import (HomePageView, LetsgoPageView, LoginPageView, roadmapPageView, Level_0_View, \
    Level_1_View, run_code, Level_2_View, Level_3_View, Level_18_View, Level_19_View, Level_20_View, check_code,
                    get_completed_tasks_count)

urlpatterns = (
    path('', HomePageView.as_view(), name='home'),
    path('letsgo', LetsgoPageView.as_view(), name='letsgo'),
    path('login', LoginPageView.as_view(), name='login'),
    path('roadmap', roadmapPageView, name='roadmap'),
    path('level0', Level_0_View.as_view(), name='level0'),
    path('level1', Level_1_View.as_view(), name='level1'),
    path('level2', Level_2_View.as_view(), name='level2'),
    path('level3', Level_3_View.as_view(), name='level3'),
    path('level18', Level_18_View.as_view(), name='level18'),
    path('level19', Level_19_View.as_view(), name='level19'),
    path('level20', Level_20_View.as_view(), name='level20'),
    path('run_code/', run_code, name='run_code'),
    path('check_code/', check_code, name='check_code'),
    path('api/completed-tasks-count/', get_completed_tasks_count, name='completed_tasks_count'),
)
