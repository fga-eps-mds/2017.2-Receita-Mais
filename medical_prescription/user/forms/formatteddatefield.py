# django
from django import forms


class FormattedDateField(forms.DateField):
    """
    Define format in field data.
    """

    widget = forms.DateInput(format='%d/%m/%Y')

    def __init__(self, *args, **kwargs):
        super(FormattedDateField, self).__init__(*args, **kwargs)
        self.input_formats = ('%d/%m/%Y',)
