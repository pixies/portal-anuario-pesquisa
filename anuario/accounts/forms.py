from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

User = get_user_model()

class AccountLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # if not user:
        #     self.add_error('username', forms.ValidationError("Esse username não existe"))
        # elif not user.check_password(password):
        #     self.add_error('password', forms.ValidationError("A senha não confere"))
        # elif not user.is_active:
        #     raise forms.ValidationError("Esse usuário foi desativado")
        
        return super(AccountLoginForm, self).clean(*args, **kwargs)


class RegisterAccountForm(forms.ModelForm):
    attrs = {'class': 'input'} # Classe para se integrar com o framework Bulma.
    
    username = forms.CharField(widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(label='Informe seu e-mail', widget=forms.EmailInput(attrs=attrs))
    email2 = forms.EmailField(label='Confirme seu e-mail', widget=forms.EmailInput(attrs=attrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs), required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("E-mail já registrado")

        return email



    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError('Os e-mails são diferentes!')

        return email2

    def save(self, commit=True):
        user = super(RegisterAccountForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user