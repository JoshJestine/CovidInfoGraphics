from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index),
    path('room/', views.room),
    path('lobby/', views.lobby),
    path('get_token/', views.getToken),
    path('chatroom/', views.chatroom),
    path('dynamic/', views.dynamic),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)