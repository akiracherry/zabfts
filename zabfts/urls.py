from zabfts import settings
from django.conf.urls import include, url
from django.contrib import admin
from zabfts.views import IndexView, ContactView, TourneyView, AboutView, FaqView, ProductsView
from django.conf.urls import patterns, include, url
from dancers.urls import urlpatterns as dancers_urls
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^tourney/$', TourneyView.as_view(), name='tourney'),
	url(r'^contact/$', ContactView.as_view(), name='contact'),
	url(r'^about/$', AboutView.as_view(), name='about'),
	url(r'^faq/$', FaqView.as_view(), name='faq'),
	url(r'^products/$', ProductsView.as_view(), name='products'),

	url(r'^admin/', admin.site.urls),	
	url(r'^files/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

#urlpatterns += [
#	url('^dancers/', include('dancers.urls'))
#]
urlpatterns += dancers_urls
#urlpatterns += staticfiles_urlpatterns()
