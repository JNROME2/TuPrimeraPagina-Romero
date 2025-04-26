from django.urls import path
from .views import UserRegisterView, UserLoginView, logout_view, AvatarUpdateView, UserChangeView

app_name = 'accounts'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path('upload-avatar/', AvatarUpdateView.as_view(), name='upload-avatar'),
    path('edit/', UserChangeView.as_view(), name='edit'),
]