#coding: utf-8
import datetime
from django.db import models
from django.core.urlresolvers import reverse

class Trainer(models.Model):
	name = models.CharField(max_length=200)
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)
	
	class Meta:
		verbose_name = u'Тренер'
		verbose_name_plural = u'Тренеры'

	def __unicode__(self):
		return self.name

class Ruk(models.Model):
	name = models.CharField(max_length=200)
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)
	
	class Meta:
		verbose_name = u'Руководитель'
		verbose_name_plural = u'Руководители'

	def __unicode__(self):
		return self.name

class St(models.Model):
	name = models.CharField(max_length=5)
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)
	
	class Meta:
		verbose_name = u'st'
		verbose_name_plural = u'sts'

	def __unicode__(self):
		return self.name

class La(models.Model):
	name = models.CharField(max_length=5)
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)
	
	class Meta:
		verbose_name = u'la'
		verbose_name_plural = u'las'

	def __unicode__(self):
		return self.name

class Rank(models.Model):
	name = models.CharField(max_length=50)
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)
	
	class Meta:
		verbose_name = u'Разряд'
		verbose_name_plural = u'Разряды'

	def __unicode__(self):
		return self.name

class Club(models.Model):
	name = models.CharField(max_length=200)
	ruk = models.ForeignKey(Ruk, verbose_name=u'Ст.тренер')
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)

	class Meta:
		verbose_name = u'Клуб'
		verbose_name_plural = u'Клубы'

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('club_item', kwargs={'pk': self.pk})

	def get_all_dancers(self):
		return Dancer.objects.select_related().filter(club=self)

	def get_dancers_count(self):
		return len(self.get_all_dancers())


class Dancer(models.Model):
	numbs = models.CharField(max_length=20, verbose_name=u'№ Кн.')
	fio = models.CharField(max_length=200, verbose_name=u'Фамилия Имя')
	otch = models.CharField(max_length=200, verbose_name=u'Отчество')
	date_birth = models.DateField(verbose_name=u'Дата рождения')
	st = models.ForeignKey(St, verbose_name=u'ST')
	dst = models.DateField(max_length=20, null=True, verbose_name=u'Д.ST')
	la = models.ForeignKey(La, verbose_name=u'LA')
	dla = models.DateField(max_length=20, null=True, verbose_name=u'Д.LA')
	rank = models.ForeignKey(Rank, null=True, verbose_name=u'Разряд', blank=True)
	drank = models.DateField(max_length=20, null=True, verbose_name=u'Д.Разряд', blank=True)
	transl = models.CharField(max_length=50, verbose_name=u'Транслит')
	club = models.ForeignKey(Club, verbose_name=u'Клуб')
	city = models.CharField(max_length=20, default='Чита', verbose_name=u'Город')
	strainer = models.ForeignKey(Ruk, verbose_name=u'Ст.тренер')
	trainer = models.ManyToManyField(Trainer, verbose_name=u'Тренер')
	reg = models.IntegerField(default=75, verbose_name=u'Регион')
	dper = models.DateField(max_length=20, null=True, verbose_name=u'Переход', blank=True)
	partner = models.CharField(max_length=50, verbose_name=u'Партнер', blank=True)
	wdsf =  models.CharField(max_length=50, verbose_name=u'WDSF MIN', blank=True)
    
	class Meta:
		verbose_name = u'Танцор'
		verbose_name_plural = u'Танцоры'

	def get_all_trainers(self):
		return Trainer.objects.select_related().filter(dancer=self)

class Category(models.Model):
    date_add = models.DateTimeField(verbose_name=u'Дата добавления', default=datetime.datetime.now)
    title = models.CharField(verbose_name=u'Название', max_length=300)
    is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)

    class Meta:
        ordering = ['-date_add']
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return '%s' % self.title

	def get_all_articles(self):
		return Article.objects.all().order_by('-date_add')[:9]

def file_path_image(instance, filename):
    return os.path.join('images', 'news',  translify(filename).replace(' ', '_'))

class Article(models.Model):
	category = models.ForeignKey(Category, verbose_name=u'Категория')
	date_add = models.DateTimeField(verbose_name=u'Дата добавления', default=datetime.datetime.now)
	title = models.CharField(verbose_name=u'Заголовок', max_length=300)
	text = models.TextField(verbose_name=u'Описание', blank=True)
	image = models.FileField(verbose_name=u'Изображение', upload_to=file_path_image, blank=True)
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)

	class Meta:
		ordering = ['-date_add']
		verbose_name = u'Новость'
		verbose_name_plural = u'Новости'

	def __unicode__(self):
		return self.title

	def __str__(self):
		return '%s' % self.title

class Tour(models.Model):
	date = models.DateTimeField(verbose_name=u'Дата проведения', default=datetime.datetime.now)
	title = models.CharField(verbose_name=u'Заголовок', max_length=300)
	vidtor = models.CharField(verbose_name=u'Вид турнира', max_length=300)
	text = models.TextField(verbose_name=u'Описание', blank=True)
	doptext = models.TextField(verbose_name=u'Дополнительное описание', blank=True)
	reg = models.CharField(verbose_name=u'Регистрация открыта до:', max_length=300)
	vid = models.CharField(max_length=30, verbose_name=u'Вид',default='Открытый турнир')
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)


	class Meta:
		verbose_name = u'Турнир'
		verbose_name_plural = u'Турниры'

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tour_item', kwargs={'pk': self.pk})

	def get_all_groups(self):
		return Group.objects.select_related().filter(tour=self)
	
	def get_all_tours(self):
		return Tour.objects.all().order_by('date')[:3]
	
	def get_atls_count(self):
		return len(self.get_all_alts())

#	def get_all_dancers(self):
#		return Dancer.objects.select_related().filter(dancer1='dancer.numbs')
	
	def get_all_dancers(self):
		return Dancer.objects.all()

class Group(models.Model):
	tour = models.ForeignKey(Tour, verbose_name=u'Группа')
	name = models.CharField(verbose_name=u'Заголовок', max_length=300)
	date = models.DateTimeField(verbose_name=u'Дата проведения', default=datetime.datetime.now)
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)

	def get_all_atls(self):
		return Atl.objects.select_related().filter(group=self).order_by('-group')
    
	def __unicode__(self):
		return self.name


class Atl(models.Model):
	group = models.ManyToManyField(Group, verbose_name=u'Турнир')
	dancer1 = models.CharField(max_length=20, verbose_name=u'Партнер 1')
	dancer2 = models.CharField(max_length=20, verbose_name=u'Партнер 2')
	email = models.TextField(verbose_name=u'email', max_length=50)
	is_published = models.BooleanField(verbose_name=u'Опубликовать', default=True)

	class Meta:
		verbose_name = u'Зарегистрированный танцор'
		verbose_name_plural = u'Зарегистрированные танцоры'
