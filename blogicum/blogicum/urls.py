from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import CreateView
from blog.form import CustomUserCreationForm
from django.conf import settings
from django.conf.urls.static import static

handler404 = "pages.views.page_not_found"
handler500 = "pages.views.internal_server_err"

urlpatterns = [
    path("", include("blog.urls", namespace="blog")),
    path("auth/", include("django.contrib.auth.urls")),
    path(
        "auth/registration/",
        CreateView.as_view(
            template_name="registration/registration_form.html",
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy("blog:index"),
        ),
        name="registration",
    ),
    path("pages/", include("pages.urls", namespace="pages")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
