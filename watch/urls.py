from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/create/',views.create_profile,name = 'create_profileUrl'),
    url(r'^business/view',views.view_business,name = 'viewbusinessUrl'),
    url(r'^business/',views.business,name = 'business'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^post/',views.post,name = 'post'),
    url(r'^leave/hood',views.leave_hood,name = 'leave_hoodUrl'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)