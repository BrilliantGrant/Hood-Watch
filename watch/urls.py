from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/create',views.create_profile,name = 'create_profileUrl'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)