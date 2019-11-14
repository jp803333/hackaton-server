from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('v',views.voiceRequest.as_view())
]