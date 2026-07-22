"""
URL configuration for zaban_derslik_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from lessons.views import grade_admin_redirect

urlpatterns = [
    # Must come before the admin catch-all: stable per-number grade links
    # used by the Jazzmin sidebar (independent of DB primary keys).
    path('admin/sinif/<int:number>/', grade_admin_redirect, name='grade-admin-redirect'),
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    path('api/', include('lessons.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
