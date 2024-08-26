from django.contrib import admin
from .models import *

# Register your models here.


class Tag_Admin(admin.ModelAdmin):
    list_filter = ("caption",)
    list_display = ("caption",)

class Author_Admin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name")
    list_display = ("first_name", "last_name")


class All_Posts_Admin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "date", "tag")
    list_display = ("title", "author", "date")


class  Comment_Admin(admin.ModelAdmin):
    list_display = ("username", "rating", "post")
    list_filter = ("post","rating") 


admin.site.register(All_Posts, All_Posts_Admin)
admin.site.register(Author, Author_Admin)
admin.site.register(Tag, Tag_Admin)

admin.site.register(Comment, Comment_Admin)