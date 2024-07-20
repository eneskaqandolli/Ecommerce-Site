from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="shop/")),
    path("shop/", include("ecommerce.urls"), name="ecommerce"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
