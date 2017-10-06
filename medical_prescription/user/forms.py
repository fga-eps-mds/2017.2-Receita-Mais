import re
from datetime import date

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from user.models import HealthProfessional, Patient, User

from . import constants


class UserLoginForm(forms.Form):
    '''
    Login Form.
    '''

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                           'placeholder': '* Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control s-form-v3__input',
                                                                 'placeholder': '* Senha'}))


class FormattedDateField(forms.DateField):
    widget = forms.DateInput(format='%d/%m/%Y')

    def __init__(self, *args, **kwargs):
        super(FormattedDateField, self).__init__(*args, **kwargs)
        self.input_formats = ('%d/%m/%Y',)


class UserForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                         'placeholder': '* João da Silva '}))
    date_of_birth = FormattedDateField(widget=forms.DateInput(attrs={'class': 'form-control s-form-v3__input',
                                                                     'placeholder': '*Ex: dd/mm/aaaa'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control s-form-v3__input',
                                                                 'placeholder': '*********'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control s-form-v3__input',
                                                                         'placeholder': '*********'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control s-form-v3__input',
                                                            'placeholder': '* exemplo@exemplo.com'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                          'placeholder': '* (xx)xxxxx-xxxx'}))
    sex = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control s-form-v3__input'}), choices=constants.SEX_CHOICE)

    class Meta:
        model = User
        fields = [
            'name', 'email', 'date_of_birth', 'phone', 'sex', 'password'
        ]


class HealthProfessionalForm(UserForm):
    crm = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                        'placeholder': '* 00000'}))
    crm_state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control s-form-v3__input',
                                                             'placeholder': '* Crm'}), choices=constants.UF_CHOICE)

    class Meta:
        model = HealthProfessional
        fields = ('name', 'email', 'date_of_birth', 'phone', 'sex', 'crm', 'crm_state', 'password',)

    def clean(self):
        crm = self.cleaned_data.get('crm')
        crm_state = self.cleaned_data.get('crm_state')
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        email_from_database = User.objects.filter(email=email)

        # TODO(Mateus) Refactor date calculation.
        today = date.today()
        try:
            born = today.year - date_of_birth.year - \
                ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        except:
            raise forms.ValidationError(constants.DATE_OF_BIRTH_FORMAT)

        crm_from_database = HealthProfessional.objects.filter(crm=crm)
        crm_state_from_database = HealthProfessional.objects.filter(crm_state=crm_state)

        # Validating CRM
        if crm is not None and len(crm) != constants.CRM_LENGTH:
            raise forms.ValidationError({'crm': [_(constants.CRM_SIZE)]})
        elif crm_state is not None and len(crm_state) != constants.CRM_STATE_LENGTH:
            raise forms.ValidationError({'crm_state': [_(constants.CRM_STATE_SIZE)]})
        elif crm_from_database.exists() and crm_state_from_database.exists():
            raise forms.ValidationError({'crm_state': [_(constants.CRM_EXIST)]})
        elif not crm.isdigit():
            raise forms.ValidationError({'crm': [_(constants.CRM_FORMAT)]})

        # Validating email
        elif email_from_database.exists():
            raise ValidationError({'email': [_(constants.EMAIL_EXISTS)]})
        elif email is None:
            raise forms.ValidationError("email inválido")
        elif len(email) > constants.EMAIL_MAX_LENGTH:
            raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})
        elif len(email) < constants.EMAIL_MIN_LENGTH:
            raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})

        # Validating password.
        elif len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif not password.isalnum():
            raise forms.ValidationError({'password': [_(constants.PASSWORD_FORMAT)]})
        elif password != password_confirmation:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_MATCH)]})

        # Validating name.
        elif name is not None and len(name) > constants.NAME_MAX_LENGHT:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and not all(x.isalpha() or x.isspace() for x in name):
            raise forms.ValidationError({'name': [_(constants.NAME_FORMAT)]})

        # Validating phone number.
        elif phone is not None and len(phone) > constants.PHONE_NUMBER_FIELD_LENGTH_MAX:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_SIZE)]})
        elif phone is not None and len(phone) < constants.PHONE_NUMBER_FIELD_LENGTH_MIN:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_SIZE)]})
        elif not phone.isdigit():
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_FORMAT)]})

        # Validating date of birth.
        elif born < constants.DATE_OF_BIRTH_MIN:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_ERROR)]})


# form to reset password User
class ResetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control s-form-v4__input g-padding-l-0--xs',
                                                            'placeholder': '* exemplo@exemplo.com'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_from_database = User.objects.filter(email=email)

        if email_from_database.exists():
            pass
        else:
            raise forms.ValidationError('this email is not registered')
        return super(ResetPasswordForm, self).clean(*args, **kwargs)


class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
                               label='')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(
                            attrs={'placehold': 'password confirmation'}),
                            label='')

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if(password != password_confirmation):
            raise forms.ValidationError('As senhas devem ser iguais')
        else:
            # Nothing to do.
            pass

        return super(ConfirmPasswordForm, self).clean(*args, **kwargs)


class PatientForm(UserForm):
    id_document = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                                'placeholder': '* 00000'}))
    id_document_state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control s-form-v3__input',
                                                                     'placeholder': '* Crm'}), choices=constants.UF_CHOICE)
    date_of_birth = FormattedDateField(initial=date.today)

    class Meta:
        model = Patient
        fields = [
                'name', 'email', 'date_of_birth', 'phone', 'sex',
                'id_document', 'password'
                ]

    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        id_document = self.cleaned_data.get('id_document')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        today = date.today()
        try:
            born = today.year - date_of_birth.year - \
                ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        except:
            raise forms.ValidationError(constants.DATE_OF_BIRTH_FORMAT)

        email_from_database = User.objects.filter(email=email)

        # Validating email.
        if email_from_database.exists():
            raise ValidationError(constants.EMAIL_EXISTS)
        elif email is None:
            raise forms.ValidationError("email inválido")
        elif len(email) > constants.EMAIL_MAX_LENGTH:
            raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})
        elif len(email) < constants.EMAIL_MIN_LENGTH:
            raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})

        # Validating password.
        elif len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif not password.isalnum():
            raise forms.ValidationError({'password': [_(constants.PASSWORD_FORMAT)]})
        elif password != password_confirmation:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_MATCH)]})

        # Validating name.
        elif name is not None and len(name) > constants.NAME_MAX_LENGHT:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and not all(x.isalpha() or x.isspace() for x in name):
            raise forms.ValidationError({'name': [_(constants.NAME_FORMAT)]})

        # Validating phone number.
        elif phone is not None and len(phone) > constants.PHONE_NUMBER_FIELD_LENGTH_MAX:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_SIZE)]})
        elif phone is not None and len(phone) < constants.PHONE_NUMBER_FIELD_LENGTH_MIN:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_SIZE)]})
        elif not phone.isdigit():
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_FORMAT)]})

        # Validating id document.
        elif id_document is not None and len(id_document) < constants.ID_DOCUMENT_MIN_LENGTH:
            raise forms.ValidationError({'id_document': [_(constants.ID_DOCUMENT_SIZE)]})
        elif id_document is not None and len(id_document) > constants.ID_DOCUMENT_MAX_LENGTH:
            raise forms.ValidationError({'id_document': [_(constants.ID_DOCUMENT_SIZE)]})
        elif not id_document.isdigit():
            raise forms.ValidationError({'id_document': [_(constants.ID_DOCUMENT_FORMAT)]})

        # Validating date of birth.
        elif born < constants.DATE_OF_BIRTH_MIN_PATIENT:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_PATIENT_ERROR)]})


class UpdateUserForm(forms.ModelForm):

    date_of_birth = FormattedDateField(initial=date.today)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'name', 'date_of_birth', 'phone', 'sex', 'password'
        ]

    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        today = date.today()
        try:
            born = today.year - date_of_birth.year - \
                ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        except:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_FORMAT)]})

        # Validating password.
        if len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif not password.isalnum():
            raise forms.ValidationError({'password': [_(constants.PASSWORD_FORMAT)]})
        elif password != password_confirmation:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_MATCH)]})

        # Validating name.
        elif name is not None and len(name) > constants.NAME_MAX_LENGHT:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and not all(x.isalpha() or x.isspace() for x in name):
            raise forms.ValidationError({'name': [_(constants.NAME_FORMAT)]})

        # Validating phone number.
        elif phone is not None and len(phone) > constants.PHONE_NUMBER_FIELD_LENGTH_MAX:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_SIZE)]})
        elif phone is not None and len(phone) < constants.PHONE_NUMBER_FIELD_LENGTH_MIN:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_SIZE)]})
        elif phone is not None and not phone.isdigit():
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_FORMAT)]})
        elif phone is not None and len(phone) > constants.PHONE_NUMBER_FIELD_LENGTH_MAX:
            raise forms.ValidationError(constants.PHONE_NUMBER_SIZE)

        # Validating date of birth.
        elif born < constants.DATE_OF_BIRTH_MIN_PATIENT:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_PATIENT_ERROR)]})
