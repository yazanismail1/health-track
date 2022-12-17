from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeListView

urlpatterns = [
    path('', HomeListView.as_view(), name="home_notsigned"),
]