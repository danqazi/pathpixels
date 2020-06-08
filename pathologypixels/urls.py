from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from viewer import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='index'),
    path('viewer/', include('viewer.urls')),
]
