from django import forms


class FormattedDateField(forms.DateField):
    widget = forms.DateInput(format='%d/%m/%Y')

    def __init__(self, *args, **kwargs):
        super(FormattedDateField, self).__init__(*args, **kwargs)
        self.input_formats = ('%d/%m/%Y',)
