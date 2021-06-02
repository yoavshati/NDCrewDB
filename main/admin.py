from django.contrib import admin

from .models import *

class ItemInline(admin.TabularInline):
    model = TestItem

class TestAdmin(admin.ModelAdmin):
    model = Test
    inlines = [ItemInline]

admin.site.register(User)
admin.site.register(Test, TestAdmin)
admin.site.register(ReferanceItem)