from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', include('amapp.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
