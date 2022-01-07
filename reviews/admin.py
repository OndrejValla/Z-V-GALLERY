from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = (
        'title',
        'product',
        'user',
        'rating',
        'date_added',
    )

    list_display = (
        'title',
        'product',
        'user',
        'rating',
        'date_added',
    )

    ordering = ('-date_added',)


admin.site.register(Review, ReviewAdmin)
