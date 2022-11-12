from django.contrib import admin
# Register your models here.
from django.contrib.auth import admin as auth_admin, get_user_model

from petstagram.accounts.forms import UserCreateForm, UserEditForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
