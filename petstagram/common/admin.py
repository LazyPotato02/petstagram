from django.contrib import admin

# Register your models here.
from petstagram.common.models import PhotoComment


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass