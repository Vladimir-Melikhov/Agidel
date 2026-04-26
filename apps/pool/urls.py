from django.urls import path
from .views import PoolView, PoliticView

urlpatterns = [
    path("", PoolView.as_view(), name='main_page'),
    path("politics/", PoliticView.as_view(), name='politics')
]
