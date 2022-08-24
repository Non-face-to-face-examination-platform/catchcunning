from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from user.views import CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # user
    path('', include('user.urls')),

    path('email-confirmation-done/',
         TemplateView.as_view(
             template_name="account/email_cofirmation_done.html"),
         name="account_email_confirmation_done"
         ),
    path('password/change/',
         CustomPasswordChangeView.as_view(),  # allauth에 되기전에 먼저?
         name="account_password_change"
         ),
    path('', include('allauth.urls')),

    path('meeting/', include('meeting.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
