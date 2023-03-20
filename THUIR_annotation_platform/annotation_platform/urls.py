from django.urls import include, path

from django.contrib import admin
from . import views

# from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

admin.autodiscover()

urlpatterns += [ 
    # Examples:
    # url(r'^$', 'annotation_platform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user_system.urls')),
    path('task/', include('task_manager.urls')),
    path('', views.index),
]
