from django.contrib import admin
from .models import RoomCategory, RoomCategoryImage, Room


# Inline model to show multiple images within RoomCategory admin
class RoomCategoryImageInline(admin.TabularInline):
    model = RoomCategoryImage
    extra = 1
    fields = ('image', 'caption',)

# Admin for RoomCategory with inline images


@admin.register(RoomCategory)
class RoomCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    inlines = [RoomCategoryImageInline]

# Admin for Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name',)
