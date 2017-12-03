# django
from django import forms

# local django
from exam.models import CustomExam
from exam.validators import CustomExamValidator
from exam import constants


class UpdateCustomExamForm(forms.ModelForm):
        """
        Form to edit a custom exam.
        """
        name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

        class Meta:
            # Define model to form.
            model = CustomExam
            fields = ('description', 'name',)

        def get_pk(self, pk):
            self.pk = pk

        def clean(self):
            """
            Get Custom Exam fields.
            """
            description = self.cleaned_data.get('description')
            name = self.cleaned_data.get('name')

            exists = CustomExam.objects.get(pk=self.pk)

            name_base = CustomExam.objects.filter(name=name)

            if name_base.exists() and exists.name != name:
                raise forms.ValidationError({'name': [(constants.NAME_EXISTS)]})

            # Verify validations in form.
            self.validator_all(description, name)

        def validator_all(self, description, name):
            """
            Checks validator in all fields.
            """

            validator = CustomExamValidator()

            validator.validator_name_update(name)
            validator.validator_description(description)
