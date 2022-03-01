from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path( "", include('base.urls')),
    path('accounts/', include('accounts.urls'))
]

handler404 = 'base.views.error_404'