from django.urls import path
from .views import PoolView

urlpatterns = [
    path("", PoolView.as_view(), name='main_page')
]
