from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('ktweet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('ktweet.urls')),  # Map root URL to ktweet.urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
