from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/', permanent=False), name='home'),  # Redirect root URL to login
    path('', include('inventory.urls')),
    path(
        'login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'
    ),
    path(
        'logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
