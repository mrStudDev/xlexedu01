from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import random
from django.utils.text import slugify

class CategorySocialModel(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app_home:home-view')

class TagSocialModel(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('app_home:home-view')

class ArticlesSocialModel(models.Model):
    title = models.CharField(max_length=155)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    key_words = models.CharField(max_length=255, default="Artigos")
    category = models.ForeignKey(CategorySocialModel, null=True, blank=True, on_delete=models.SET_NULL)
    content_social = models.TextField(blank=True, null=True)
    meta_description = models.TextField(max_length=160)
    keyword = models.CharField(max_length=255)
    tags = models.ManyToManyField('TagSocialModel', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    old_url = models.SlugField(blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    last_updated = models.DateTimeField(auto_now=True)
    code = models.PositiveIntegerField(unique=True, blank=True, null=True)
    views = models.IntegerField(default=0)
    indexable = models.BooleanField(default=True)  # Novo campo para SEO

    def is_indexable(self):
        return self.indexable    


    def generate_unique_code(self):
        code = random.randint(100000, 999999)
        while ArticlesSocialModel.objects.filter(code=code).exists():
            code = random.randint(100000, 999999)
        return code

    def save(self, *args, **kwargs):
        # Gera um código único se não existir
        if not self.code:
            self.code = self.generate_unique_code()
        # Gera um slug a partir do título se o slug não existir
        if not self.slug:
            self.slug = slugify(self.title)
        super(ArticlesSocialModel, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} | {self.author} | {self.views}"


    def get_absolute_url(self):
        return reverse('app_edu_social:article-social-single', kwargs={'slug': self.slug})

    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(ArticlesSocialModel, self).save(*args, **kwargs)