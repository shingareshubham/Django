from django.urls import path
from .views import artile_list

urlpatterns = [
    path('artiles/', artile_list),
]