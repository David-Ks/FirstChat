from django.contrib import admin
from chat import urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
