from django.contrib import admin
from user.models import UserProfile
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# class UserProfileInline(admin.StackedInline):
#     model =  UserProfile
#     can_delete = False


# class AccountUserAdmin(AuthUserAdmin):
#     def add_view(self, *args, **kwargs):
#         self.inlines = []
#         return super(AccountUserAdmin, self).add_view(*args, **kwargs)

#     def change_view(self, *args, **kwargs):
#         self.inlines = [UserProfileInline]
#         return super(AccountUserAdmin, self).change_view(*args, **kwargs)

#AccountUserAdmin)

# class CustomeUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets, (
#             'Additional Info',
#             {
#                 'fields': (
#                     'age',
#                     'nickname'
#                 )
#             }
#         )
#     )


# admin.site.register(get_user_model(), CustomeUserAdmin) 


fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'age', 'nickname')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(get_user_model(), UserAdmin)