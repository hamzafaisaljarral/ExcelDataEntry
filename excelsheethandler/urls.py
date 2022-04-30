from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [

    path('', views.Import_csv, name="Import_csv"),
    path('create/', login_required(views.CreateEmployeeView.as_view()), name='create'),
]