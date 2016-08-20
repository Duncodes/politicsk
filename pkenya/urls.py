# coding: utf-8
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from pkenya.core import views as core_views
from pkenya.authentication import views as pkenya_auth_views
from pkenya.activities import views as activities_views
from pkenya.search import views as search_views
from pkenya.themes import views as pkenya_theme_views
from pkenya.diplomats import views as regions_view

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^admin/', include(admin.site.urls),name='admin'),
    url(r'^regions',regions_view.regions,name='regions'),
    url(r'^diplomat/(?P<region>[^/]+)/$',regions_view.viewdiplomats,name='diplomat'),
    url(r'^login', auth_views.login, {'template_name': 'core/login.html'},name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', pkenya_auth_views.signup, name='signup'),
    url(r'^signupp/$', pkenya_auth_views.signupp, name='signupp'),
    url(r'^themes/$',pkenya_theme_views.themes,name='themes'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^network/$', core_views.network, name='network'),
    url(r'^feeds/', include('pkenya.feeds.urls')),
    url(r'^questions/', include('pkenya.questions.urls')),
    url(r'^articles/', include('pkenya.articles.urls')),
    url(r'^messages/', include('pkenya.messenger.urls')),
    url(r'^notifications/$', activities_views.notifications,
        name='notifications'),
    url(r'^notifications/last/$', activities_views.last_notifications,
        name='last_notifications'),
    url(r'^notifications/check/$', activities_views.check_notifications,
        name='check_notifications'),
    url(r'^about',core_views.about,name='about'),
    url(r'^help',core_views.help,name='help'),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
