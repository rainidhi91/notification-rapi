"""p_notification_rapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import debug_toolbar
from django.urls import path, include
# from a_template.sitemaps import StaticViewSitemap, PostSitemap
# from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static

# sitemaps = {
#     'static': StaticViewSitemap,
#     'post': PostSitemap,
# }

urlpatterns = [
    path('api/secret/legit/admin/', admin.site.urls),
    path("api/secret/legit/admin/", include('loginas.urls')),
    path('api/secret/legit/admin/defender/', include('defender.urls')),
    path('api/admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('api/__debug__/', include(debug_toolbar.urls)),
    path('api/', include("a_notification_rapi.api.urls")),
    # path('api/sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]

# URL Pattern for Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)