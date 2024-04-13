from django.urls import path
from . import views

urlpatterns = [
      path('data1/', views.websocket_view_sync, name='data'),
       path('data/', views.receive_data, name='receive_data'),
]