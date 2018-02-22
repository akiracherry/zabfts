#coding: utf-8
from django.contrib import admin
from dancers.models import Trainer, Ruk, St, La, Rank, Club, Dancer, Category, Article, Tour, Group, Atl

class TrainerAdmin(admin.ModelAdmin):
    list_display=('name','is_published',)
    list_display_links=('name',)
    list_editable=('is_published',)
    search_fields=('name',)

class RukAdmin(admin.ModelAdmin):
    list_display=('name','is_published',)
    list_display_links=('name',)
    list_editable=('is_published',)
    search_fields=('name',)

class StAdmin(admin.ModelAdmin):
    list_display=('name','is_published',)
    list_display_links=('name',)
    list_editable=('is_published',)
    search_fields=('name',)

class LaAdmin(admin.ModelAdmin):
    list_display=('name','is_published',)
    list_display_links=('name',)
    list_editable=('is_published',)
    search_fields=('name',)

class RankAdmin(admin.ModelAdmin):
    list_display=('name','is_published',)
    list_display_links=('name',)
    list_editable=('is_published',)
    search_fields=('name',)

class ClubAdmin(admin.ModelAdmin):
    list_display=('name','is_published',)
    list_display_links=('name',)
    list_editable=('is_published',)
    search_fields=('name',)

class DancerAdmin(admin.ModelAdmin):
    list_display=('numbs','fio','otch','date_birth','st','dst','la','dla','rank','drank','transl','club','city','strainer','reg','dper','partner','wdsf',)
    list_display_links=('fio',)
    list_editable=('date_birth','dst','dla','drank')
    list_filter=('club',)
    search_fields=('fio',)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','is_published',)
    list_display_links=('title',)
    list_editable=('is_published',)
    search_fields=('title',)

class ArticleAdmin(admin.ModelAdmin):
    list_display=('category','title','is_published',)
    list_display_links=('title',)
    list_editable=('is_published',)
    search_fields=('title',)

class TourAdmin(admin.ModelAdmin):
    list_display=('title','is_published',)
    list_display_links=('title',)
    list_editable=('is_published',)
    search_fields=('title',)

class GroupAdmin(admin.ModelAdmin):
    list_display=('tour','name','is_published',)
    list_display_links=('name',)
    list_editable=('is_published',)
    search_fields=('name',)

class AtlAdmin(admin.ModelAdmin):
    list_display=('dancer1','dancer2','is_published',)
    list_display_links=('dancer1','dancer2',)
    list_editable=('is_published',)

admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Ruk, RukAdmin)
admin.site.register(St, StAdmin)
admin.site.register(La, LaAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Dancer, DancerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Atl, AtlAdmin)
