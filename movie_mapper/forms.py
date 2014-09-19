from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from cards.models import Player


# class EmailUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(max_length=30, required=True)
#     last_name = forms.CharField(max_length=30, required=True)
#     phone = forms.CharField(max_length=12, help_text="Format should be: 650-111-2222")
#
#     class Meta:
#         model = Player
#         fields = ("username", "first_name", "last_name", "email", "phone", "password1", "password2")
#
#     def clean_username(self):
#         # Since User.username is unique, this check is redundant,
#         # but it sets a nicer error message than the ORM. See #13147.
#         username = self.cleaned_data["username"]
#         try:
#             Player.objects.get(username=username)
#         except Player.DoesNotExist:
#             return username
#         raise forms.ValidationError(
#             self.error_messages['duplicate_username'],
#             code='duplicate_username',
#         )


class SimpleInput(forms.Form):
    question = forms.CharField(max_length=120)


# class PickOne(forms.Form):
#     question = forms.ChoiceField(max_length=120)