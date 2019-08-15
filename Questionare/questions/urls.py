from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('submit',views.submit),
    path('continue',views.form),
    path('data.csv',views.data)
]