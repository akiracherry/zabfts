from django.conf.urls import url
from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt 
from views import ClubList, ClubItem, DancerList, TourItem, AtlAdd, AtlAddAjax, ArticleAll

urlpatterns = patterns('',
	url(r'^club-list/$', ClubList.as_view(), name='club_list'),
	url(r'^club/(?P<pk>\d+)/$', ClubItem.as_view(), name='club_item'),
	url(r'^dancer-list/$', DancerList.as_view(), name='dancer_list'),
	url(r'^article-all/$', ArticleAll.as_view(), name='article_all'),

	url(r'^tour/(?P<pk>\d+)/$', TourItem.as_view(), name='tour_item'),

	url(r'^atl-add/$', AtlAdd.as_view(), name='atl_add'),
    url(r'^atl-add-ajax/$', csrf_exempt(AtlAddAjax.as_view()), name='atl_add_ajax'),

)