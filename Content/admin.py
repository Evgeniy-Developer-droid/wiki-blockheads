from django.contrib import admin
from .models import PostsModel, CommentsModel, Settings
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('base',)


admin.site.register(PostsModel, PostAdmin)
admin.site.register(CommentsModel)


class SettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False


admin.site.register(Settings, SettingsAdmin)

