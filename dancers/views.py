from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView, View
from .models import Club, Dancer, Tour, Atl, Article
from .forms import AtlForm


class ClubList(ListView):
	template_name = 'dancers/club_list.html'
	model = Club
	queryset = model.objects.filter(is_published=True)
	context_object_name = 'clubs'

class ClubItem(DetailView):
	template_name = 'dancers/club_item.html'
	model = Club
	queryset = model.objects.filter(is_published=True)
	context_object_name = 'club'

class DancerList(ListView):
	template_name = 'dancers/dancer_list.html'
	model = Dancer
	context_object_name = 'dancers'

class TourItem(DetailView):
	template_name = 'dancers/tour_item.html'
	model = Tour
	queryset = model.objects.filter(is_published=True)
	context_object_name = 'tour'

class AtlAdd(TemplateView):
	template_name = 'dancers/atl_add.html'

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form = AtlForm()
		context['form'] = form
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		data = request.POST.copy()
		print dir(request)
		form = AtlForm(data, request.FILES)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect(reverse('atl_list'))
		context['form'] = form
		return self.render_to_response(context)

class AtlAddAjax(View):
	def post(self, request, *args, **kwargs):
		data = request.POST.copy()
		form = AtlForm(data)
		if form.is_valid():
			atl = form.save()
			return HttpResponse('success')
		t = loader.get_template('dancers/atl_form.html')
		c = Context({'form': form})
		return HttpResponse(t.render(c))

class ArticleAll(ListView):
    template_name = 'about.html'
    model = Article
    queryset = model.objects.all().order_by('pub_date').reverse().filter(is_published=True)
    context_object_name = 'articles'