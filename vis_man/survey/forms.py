from django import forms
from .models import Visitor
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class MainForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
            'nightstay',
            'planned_checkout'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': PhoneNumberPrefixWidget(attrs={'class': 'form-control'}, initial='AU'),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'nightstay': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'planned_checkout': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'role': 'Role',
            'nightstay': 'Are you planning to stay overnight?',
            'planned_checkout': 'Planned Checkout'
        }

    def __init__(self, exclude, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
        if not exclude['accomodation']:
            del self.fields['nightstay']


class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'emergency_first_name',
            'emergency_last_name',
            'emergency_phone',
            'emergency_relation'
        ]

        widgets = {
            'emergency_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_relation': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'emergency_first_name': 'Emergency Contact First Name',
            'emergency_last_name': 'Emergency Contact last Name',
            'emergency_phone': 'Emergency Contact Number',
            'emergency_relation': 'Relationship'
        }


class Signout(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'email',
            'phone_number'
        ]

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': PhoneNumberPrefixWidget(attrs={'class': 'form-control'}, initial='AU')
        }

        labels = {
            'email': 'Email',
            'phone_number': 'Phone Number'
        }

# class Signout(forms.Form):

#     email= forms.EmailField(label='Email')
#     phone_number= PhoneNumberField(region='AU')
#     email.widget.attrs.update({'class': 'form-control'})
#     phone_number.widget.attrs.update({'class': 'form-control'})
