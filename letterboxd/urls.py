from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_urls
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('cataloge.urls')),
    path('activate/<str:uidb64>/<str:token>/',
         views.activate_account, name='activate_account'),
    # Define this view.
    path('account-activated/', views.account_activated, name='account_activated'),
    # Define this view.
    path('activation-error/', views.activation_error, name='activation_error'),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
