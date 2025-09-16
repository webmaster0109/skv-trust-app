from django.contrib import admin
from .models import BannerSlider, SKVEventDetail, SKVNewsDetail, SKVHistory


class BannerSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'order')
    list_filter = ('is_active', 'order')
    search_fields = ('title', 'description')
    list_editable = ('is_active', 'order')
    list_per_page = 10
    ordering = ('order',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'is_active', 'order', 'image')}),
        ('Date Information', {'fields': ('created_at', 'updated_at')}),
    )

admin.site.register(BannerSlider, BannerSliderAdmin)

class SKVEventDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'slug')
    list_editable = ('is_active',)
    list_per_page = 10
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'description', 'image', 'event_initial_date', 'event_final_date', 'event_location', 'event_location_link', 'event_organizer', 'event_contact', 'event_email', 'is_active')}),
        ('Date Information', {'fields': ('created_at', 'updated_at')}),
    )

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(SKVEventDetail, SKVEventDetailAdmin)

class SKVNewsDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'slug')
    list_editable = ('is_active',)
    list_per_page = 10
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'body', 'image', 'is_active')}),
        ('Date Information', {'fields': ('created_at', 'updated_at')}),
        ('Author', {'fields': ('author',)}),
    )

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(SKVNewsDetail, SKVNewsDetailAdmin)

class SKVHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'is_active', 'order')
    list_filter = ('is_active', 'order', 'year')
    search_fields = ('title', 'year')
    list_editable = ('is_active', 'order')
    list_per_page = 10
    ordering = ('-order',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'year', 'image', 'is_active', 'order')}),
        ('Date Information', {'fields': ('created_at', 'updated_at')}),
    )

admin.site.register(SKVHistory, SKVHistoryAdmin)