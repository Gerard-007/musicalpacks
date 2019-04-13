from django.contrib import admin

# Register your models here.
from categories.models import Category
from categories.forms import CategoryAdminForm

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['updated', 'timestamp']
    list_display = ['title', 'updated', 'timestamp']
    readonly_fields = ['updated', 'timestamp', 'short_title']
    search_fields = ['title']
    form = CategoryAdminForm

    def short_title(self, obj):
        return obj.title[:5]

admin.site.register(Category, CategoryAdmin)
