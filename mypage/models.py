from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()

  created_at = models.DateField()

  head_image = models.ImageField(upload_to='mypage/images/%Y/%m/%d/', blank=True)
  file_upload = models.FileField(upload_to='mypage/files/%Y/%m/%d/', blank=True)
  def __str__(self):
    return f'[{self.pk}]{self.title}'

  def get_absolute_url(self):
    return f'/mypage/{self.pk}/'