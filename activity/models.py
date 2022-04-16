from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return f'/blog/tag/{self.slug}'


class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Categories'

class Act(models.Model):
  title = models.CharField(max_length=30) #제목
  apply = models.CharField(max_length=500) #홈페이지
  number = models.IntegerField() #모집인원
  content = models.TextField() #상세내용

  start_at = models.DateField() #시작일
  end_at = models.DateField() #마감일

  poster_image = models.ImageField(upload_to='activity/images/%Y/%m/%d/', blank=True) #포스터 이미지

  category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
  tag = models.ManyToManyField(Tag, null=True, blank=True)
  
  def __str__(self):
    return f'[{self.pk}]{self.title}'

  def get_absolute_url(self):
    return f'/activity/{self.pk}/'



  