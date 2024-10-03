from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('measurements/', views.measurements, name='measurements'),
    path('measurements/<int:id>/details/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
#    # Only add this in development (Django automatically handles static files in production)
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)