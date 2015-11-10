from django.contrib import admin

# Register your models here.

from .models import Article
from .models import Image
from .models import Contributor

admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Contributor)
