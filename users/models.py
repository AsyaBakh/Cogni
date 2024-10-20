from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
  name_role = models.CharField(max_length=45)

  def __str__(self):
    return self.name_role

class MBTI_type(models.Model):
  name_of_type = models.CharField(max_length=45)

  def __str__(self):
    return self.name_of_type

class CustomUser(AbstractUser):
  name = models.CharField(max_length=45, blank=True)
  description = models.CharField(max_length=45, blank=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=45)
  image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True)
  type_mbti = models.CharField(max_length=4, blank=True)
  id_role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
  id_MBTI_type = models.ForeignKey(MBTI_type, on_delete=models.CASCADE, null=True, blank=True)

  groups = models.ManyToManyField(
    'auth.Group',
    verbose_name='groups',
    blank=True,
    related_name='custom_user_set',
  )
  user_permissions = models.ManyToManyField(
    'auth.Permission',
    verbose_name='user permissions',
    blank=True,
    related_name='custom_user_set',
  )
  def __str__(self):
    return self.username

class Article(models.Model):
  article_name = models.CharField(max_length=128)
  article_body = models.CharField(max_length=1024)
  id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

  def __str__(self):
    return self.article_name

class MBTI_question(models.Model):
  question = models.CharField(max_length=45)

  def __str__(self):
    return self.question

class Tag(models.Model):
  name_tag = models.CharField(max_length=45)

  def __str__(self):
    return self.name_tag

class UserTags(models.Model):
  id_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('id_tag', 'id_user')
