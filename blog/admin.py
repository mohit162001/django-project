from django.contrib import admin
from blog.models import ArticleModel,ContactModel
# Register your models here.

admin.site.register(ArticleModel)
admin.site.register(ContactModel)

