from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class BookInstanceAdmin(admin.ModelAdmin):
    pass


My_models = [Book, Genre, Author, BookInstance, BookLanguage]

admin.site.register(My_models)
admin.site.site_header = 'The Local Library'
admin.site.site_title = 'under procces'


