from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView

from example.models import Tag

from unfold.views import UnfoldModelAdminViewMixin


class TagToolAdmin(admin.ModelAdmin):
    def tool_view(self, request):
        return HttpResponse("ok")


tag_tool_admin = TagToolAdmin(Tag, admin.site)


class TagFixerView(UnfoldModelAdminViewMixin, TemplateView):
    title = "Tag fixer"
    permission_required = ("example.change_tag",)
    template_name = "unfold/index.html"


urlpatterns = [
    # Custom admin view wrapped by AdminSite.admin_view(), the same pattern
    # used by ModelAdmin.get_urls() overrides (constance, custom tools, etc.).
    path(
        "secret-panel/tag-tool/",
        admin.site.admin_view(tag_tool_admin.tool_view),
        name="tag_tool",
    ),
    # Class-based view with its own permission_required, the pattern
    # recommended by unfold's docs for custom admin pages.
    path(
        "secret-panel/tag-fixer/",
        admin.site.admin_view(TagFixerView.as_view(model_admin=tag_tool_admin)),
        name="tag_fixer_tool",
    ),
    path("secret-panel/", admin.site.urls),
]
