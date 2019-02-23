from django.contrib import admin
from .models import Post
from import_export import resources
from .models import Articleupload
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from django.urls import path, include # new
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

class ArticleuploadResource(resources.ModelResource):
    class Meta:
        model = Articleupload

@admin.register(Articleupload)
class ArticleuploadAdmin(ImportExportModelAdmin):
    pass

