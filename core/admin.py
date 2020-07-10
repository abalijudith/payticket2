from django.contrib import admin

# Register your models here.

from .models import User
from django.contrib.auth.admin import UserAdmin
from django import forms

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',"password","is_staff","type","first_name","last_name","is_active","avatar")


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomAdmin(UserAdmin):
    add_form = UserCreationForm


    list_display = ('email',"first_name","date_joined","is_staff")
    ordering = ('email',)
    fieldsets = ((None,{'fields':('email',"password","is_staff","first_name","last_name","is_active","avatar")}),)
    add_fieldsets=((None,{'fields':('email',"password","is_staff","first_name","last_name","is_active","avatar")}),)
    search_fields = ('email',)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
admin.site.register(User,CustomAdmin)