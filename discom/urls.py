from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    # re_path(r"^static/(?P<path>.*)$", serve, {'document_root':settings.STATIC_ROOT}),
    # re_path(r"^media/(?P<path>.*)$", serve, {'document_root':settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('vitrine.urls', namespace='site')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)