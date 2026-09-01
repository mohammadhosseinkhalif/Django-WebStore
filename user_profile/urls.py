from django.urls import path

from .views import (
    SelfProfileView,
    ProfileDetailView,
    InterestsListView,
    upload_avatar,
    upload_banner,
    update_description,
    SettingsView,
    UpdateUsernameView,
    UpdateProfileView,
    ChangePasswordView,
    delete_account,
    login_user,
    logout_user,
    signup_user,
)

urlpatterns = [
    # Public profile
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('self-profile/', SelfProfileView.as_view(), name='self_profile_view'),

    # Interests
    path('interests/', InterestsListView.as_view(), name='interests_view'),

    # File uploads (AJAX)
    path('profile/upload-avatar/', upload_avatar, name='upload_avatar'),
    path('profile/upload-banner/', upload_banner, name='upload_banner'),
    path('profile/update-description/', update_description, name='update_description'),

    # Settings and profile management
    path('settings/', SettingsView.as_view(), name='settings_view'),
    path('update_username/', UpdateUsernameView.as_view(), name='update_username'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('delete_account/', delete_account, name='delete_account'),

    # Authentication
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_user, name='signup'),
]