from django.contrib import admin
from django.urls import path, include, re_path

from core.urls import urlpatterns as core_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^', include(core_patterns)),
]
