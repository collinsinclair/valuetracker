from django.contrib import admin

from .models import Category, Activity, Entry


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user  # Set default user on creation
        super().save_model(request, obj, form, change)


class ActivityAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)


class EntryAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Entry, EntryAdmin)
