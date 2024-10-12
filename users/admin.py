from django.contrib import admin
from .models import  Role, MBTI_type, CustomUser, Article, MBTI_question, Tag, UserTags

admin.site.register(Role)
admin.site.register(MBTI_type)
admin.site.register(CustomUser)
admin.site.register(Article)
admin.site.register(MBTI_question)
admin.site.register(Tag)
admin.site.register(UserTags)
# Register your models here.
