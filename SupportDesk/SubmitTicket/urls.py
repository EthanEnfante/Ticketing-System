from django.urls import path
from . import views

app_name = 'SubmitTicket'
urlpatterns = [
    path("", views.index, name='index')
]