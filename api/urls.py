from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', ProfileListApiVeiw.as_view(), name='profiles'),
    path('post/', PostListApiVeiw.as_view(), name='posts'),
    path('profile/<int:pk>', ProfileRetry.as_view(), name='profile_update'),
    path('post/<int:pk>', PostRetry.as_view(), name='posts_update'),

]