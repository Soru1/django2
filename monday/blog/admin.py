from django.contrib import admin
from .models import Article, Comment

# Прежде чем мы выведем наши посты, нам необходимо эти посты создать. В свою очередь, сделаем мы это через админку,
# поэтому добавьте модель Article в admin.py:

admin.site.register(Comment)
admin.site.register(Article)
