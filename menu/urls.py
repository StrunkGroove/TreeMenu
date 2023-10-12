from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),

    path('lvl1 1/', views.base, {'name': 'lvl1 1'}),
    path('lvl1 1/lvl2 1/', views.base, {'name': 'lvl2 1'}),
    path('lvl1 1/lvl2 1/lvl3 1/', views.base, {'name': 'lvl3 1'}),
    path('lvl1 1/lvl2 1/lvl3 2/', views.base, {'name': 'lvl3 2'}),
    path('lvl1 1/lvl2 1/lvl3 3/', views.base, {'name': 'lvl3 3'}),
    path('lvl1 1/lvl2 2/', views.base, {'name': 'lvl2 2'}),
    path('lvl1 1/lvl2 3/', views.base, {'name': 'lvl2 3'}),
    path('lvl1 2/', views.base, {'name': 'lvl1 2'}),
    path('lvl1 3/', views.base, {'name': 'lvl1 3'}),
    path('lvl1 1/lvl2 4/', views.base, {'name': 'lvl2 4'}),
    path('lvl1 1/lvl2 4/lvl3 4/', views.base, {'name': 'lvl3 4'}),
    path('lvl1 1/lvl2 5/', views.base, {'name': 'lvl2 5'}),
    path('lvl1 1/lvl2 5/lvl3 5/', views.base, {'name': 'lvl3 5'}),
    path('lvl1 4/', views.base, {'name': 'lvl1 4'}),
    path('lvl1 4/lvl2 6/', views.base, {'name': 'lvl2 6'}),
    path('lvl1 4/lvl2 6/lvl3 6/', views.base, {'name': 'lvl3 6'}),
    path('lvl1 4/lvl2 7/', views.base, {'name': 'lvl2 7'}),
    path('lvl1 4/lvl2 7/lvl3 7/', views.base, {'name': 'lvl3 7'}),

    path('one/', views.base, {'name': 'one'}),
    path('two/', views.base, {'name': 'two'}),
    path('one/four/', views.base, {'name': 'four'}),
    path('one/five/', views.base, {'name': 'five'}),
    path('one/six/', views.base, {'name': 'six'}),
    path('two/seven/', views.base, {'name': 'seven'}),
    path('two/eight/', views.base, {'name': 'eight'}),
    path('two/nine/', views.base, {'name': 'nine'}),
    path('one/four/ten/', views.base, {'name': 'ten'}),
    path('one/four/eleven/', views.base, {'name': 'eleven'}),
    path('one/four/twelve/', views.base, {'name': 'twelve'}),
]
