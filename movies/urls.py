from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'movie_mapper.views.test', name='test'),
    url(r'^profile/$', 'movie_mapper.views.profile', name='profile'),
    url(r'^faq/$', 'movie_mapper.views.faq', name='faq'),
    url(r'^movies/$', 'movie_mapper.views.movie_list', name='movie_list'),
    url(r'^movies/search/$', 'movie_mapper.views.search_movie', name='search_movie'),
    url(r'^movies/add/$', 'movie_mapper.views.add_movie', name='add_movie'),
    url(r'^locations/$', 'movie_mapper.views.location_list', name='location_list'),
    url(r'^locations/add/$', 'movie_mapper.views.add_location', name='add_location'),

    url(r'^map/u\'(?P<movie_id>\d+)\'/$', 'movie_mapper.views.map_view', name='map_view'),

    url(r'^register/$', 'movie_mapper.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

)
