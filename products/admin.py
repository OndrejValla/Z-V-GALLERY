from django.contrib import admin
from .models import Product, Project


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'project',
        'price',
        'image1',
        'image2',
        'image3',
    )

    ordering = ('project',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Project, ProjectAdmin)
