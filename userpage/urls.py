from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeSignedView
urlpatterns = [
path('', HomeSignedView.as_view(), name='home_signed'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)