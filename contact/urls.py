from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_form, name='submit_form'),
    path('submissions/', views.get_submissions, name='get_submissions'),
]
