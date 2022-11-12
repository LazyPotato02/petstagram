from django.urls import path, include
from petstagram.accounts import views
from petstagram.accounts.views import SignInView, SignUpView, SignOutView, UserDetailsView, UserEditView, UserDeleteView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='profile-details'),
        path('edit/', UserEditView.as_view(), name='profile-edit'),
        path('delete/', UserDeleteView.as_view(), name='profile-delete'),
    ]))

)