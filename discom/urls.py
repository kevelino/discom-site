from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from vitrine.views import RobotsTxtView


sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vitrine.urls', namespace='site')),
    path("robots.txt", RobotsTxtView.as_view(content_type="text/plain"), name="robots"),
    path('rosetta/', include('rosetta.urls')),
    re_path(r"^static/(?P<path>.*)$", serve, {'document_root':settings.STATIC_ROOT}),
    re_path(r"^media/(?P<path>.*)$", serve, {'document_root':settings.MEDIA_ROOT}),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

handler404 = 'vitrine.views.page404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)