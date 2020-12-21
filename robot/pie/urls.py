from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('move', views.direction, name='move'),
    path('inputCode', views.runCode, name='inputCode')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
