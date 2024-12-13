from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django.contrib.auth.models import User
from .models import ProfileParent, ProfileChild

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',  # Ganti dengan class CSS yang Anda gunakan
                'placeholder': field.label,  # Opsional: Gunakan label sebagai placeholder
            })

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Kolom yang ingin diedit dari model User

class detailForm(forms.ModelForm):
    class Meta:
        model = ProfileChild
        fields = ['nama_lengkap', 'pendidikan', 'umur', 'bidang_minat']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileParent
        fields = ['avatar', 'pekerjaan','nomor_telepon', 'alamat']

    # def __init__(self, *args, **kwargs):
    #     # Pass the user instance if available
    #     user = kwargs.pop('user', None)
    #     super().__init__(*args, **kwargs)

    #     # Set the initial value of the fullname field
    #     if user:
    #         self.fields['fullname'].initial = f"{user.first_name} {user.last_name}".strip()
