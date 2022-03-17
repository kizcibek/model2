from django.contrib import admin

# Register your models here.
 #здесь регистрируются модели для их отображения в админ-проекте
import posts.models


admin.site.register(posts.models.Post)
admin.site.register(posts.models.Comment)