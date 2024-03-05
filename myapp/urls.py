from django.contrib import admin
from .import views
from django.urls import path

urlpatterns = [
    path('',views.task,name = 'task'),
    path('A/',views.new,name = 'new'),
    path('B/',views.home,name = 'home'),
    path('R/',views.res,name = 'res'),
    path('N/',views.new_file,name = 'new_file'),
    path('T/',views.index,name = 'index'),
    path('1',views.task1,name = 'task1'),
    path('2',views.task2,name = 'task2'),
    path('3',views.task3,name = 'task3'),
    path('4',views.task4,name = 'task4'),

]