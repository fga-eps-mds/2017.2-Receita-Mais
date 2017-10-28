# Django
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.forms import formset_factory

# Local Django
from prescription.forms import (CreatePrescriptionExamForm,
                                ExamPrescriptionForm
                                )
from prescription.models import (PrescriptionDefaultExam,
                                 PrescriptionCustomExam,
                                 Prescription
                                 )


class CreatePrescriptionExamView(FormView):
    """
    Responsible for rendering to fields.
    """
    template_name = 'show_prescription.html'
    # Defines that this form will have multiple instances.
    ExamPrescriptionFormSet = formset_factory(ExamPrescriptionForm)

    def create_base_prescription(self, form):
        """
        Creates the base of the prescription
        """
        patient_id = form.cleaned_data.get('patient_id')
        cid_id = form.cleaned_data.get('cid_id')

        prescription_base_object = Prescription(patient_id=patient_id, cid_id=cid_id)
        prescription_base_object.save()
        return prescription_base_object

    def create_many_to_many_exam(self, form, exam_prescription):
        """
        Defines which type of exam will be added to the prescription and create it.
        """

        exam_type = form.cleaned_data.get('exam_type')

        if exam_type == 'default_exam':
            id_tuss = form.cleaned_data.get('id_tuss')
            self.create_prescription_default_exam(exam_prescription,
                                                  id_tuss)
        elif exam_type == 'custom_exam':
            name = form.cleaned_data.get('name')
            self.create_prescription_custom_exam(exam_prescription,
                                                 name)
        else:
            # Nothing to do.
            pass

    def create_prescription_default_exam(self, prescription, id_tuss):
        prescription_default_exam_object = PrescriptionDefaultExam(
            prescription=prescription,
            id_tuss=id_tuss
            )

        prescription_default_exam_object.save()

    def create_prescription_custom_exam(self, prescription, name):
        prescription_custom_exam_object = PrescriptionCustomExam(
            prescription=prescription,
            name=name
            )

        prescription_custom_exam_object.save()

    def get(self, request, *args, **kwargs):
        """
        Rendering form in view.
        """
        form = CreatePrescriptionExamForm(request.GET or None)
        formset = self.ExamPrescriptionFormSet(request.GET or None)

        data = dict()
        context = {'form': form,
                   'formset': formset}
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        # Json to communication Ajax.
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        """
        Save data in the form in database.
        """
        form = CreatePrescriptionExamForm(request.POST or None)
        formset = self.ExamPrescriptionFormSet(request.POST or None)
        data = dict()

        form_is_validated = True

        if not form.is_valid():
            form_is_validated = False
            if not formset.is_valid():
                form_is_validated = False
            else:
                prescription_base_object = self.create_base_prescription(form)

        data['form_is_valid'] = form_is_validated
        context = {'form': form,
                   'formset': formset}
        data['html_form'] = render_to_string(self.template_name, context, request)
        # Json to communication Ajax.
        return JsonResponse(data)
