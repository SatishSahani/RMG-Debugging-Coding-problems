from django.contrib import admin
from .models import Book

class MemberAdmin(admin.ModelAdmin):
    list_display="BookName","AuthorName","Price"

admin.site.register(Book,MemberAdmin)
