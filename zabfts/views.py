#coding: utf-8
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
	template_name = 'index.html'

class ContactView(TemplateView):
	template_name = 'contact.html'

class TourneyView(TemplateView):
	template_name = 'tourney.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class FaqView(TemplateView):
	template_name = 'faq.html'

class ProductsView(TemplateView):
	template_name = 'products.html'