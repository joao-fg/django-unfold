from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from example.models import Tag


class TagToolAdmin(admin.ModelAdmin):
    def tool_view(self, request):
        return HttpResponse("ok")


tag_tool_admin = TagToolAdmin(Tag, admin.site)

urlpatterns = [
    # Custom admin view wrapped by AdminSite.admin_view(), the same pattern
    # used by ModelAdmin.get_urls() overrides (constance, custom tools, etc.).
    path(
        "secret-panel/tag-tool/",
        admin.site.admin_view(tag_tool_admin.tool_view),
        name="tag_tool",
    ),
    path("secret-panel/", admin.site.urls),
]
