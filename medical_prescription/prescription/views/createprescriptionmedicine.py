# Django
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.forms import formset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django
from user.decorators import is_health_professional
from prescription.forms import (CreatePrescriptionForm,
                                MedicinePrescriptionForm,
                                RecommendationPrescriptionForm,
                                )
from prescription.models import (PrescriptionMedicine,
                                 PrescriptionHasManipulatedMedicine,
                                 PrescriptionHasMedicine,
                                 PrescriptionRecommendation,
                                 )


class CreatePrescriptionMedicine(FormView):
    """
    Responsible for rendering to fields.
    """
    template_name = 'show_prescription_medicine.html'
    # Defines that this form will have multiple instances.
    MedicinePrescriptionFormSet = formset_factory(MedicinePrescriptionForm)
    RecommendationPrescriptionFormSet = formset_factory(RecommendationPrescriptionForm)

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(CreatePrescriptionMedicine, self).dispatch(*args, **kwargs)

    # Creates the prescription object.
    def create_prescription_medicine(self, form):
        """
        Creates the base of the prescription
        """
        patient_id = form.cleaned_data.get('patient_id')
        cid_id = form.cleaned_data.get('cid_id')

        prescription_medicine_object = PrescriptionMedicine(patient_id=patient_id, cid_id=cid_id)
        prescription_medicine_object.save()
        return prescription_medicine_object


    def create_prescription_has_manipulated_medicine(self, medicine_id, quantity, posology, prescription_medicine):
        prescription_has_manipulatedmedicine_object = PrescriptionHasManipulatedMedicine(
            manipulated_medicine_id=medicine_id,
            posology=posology, quantity=quantity,
            prescription_medicine=prescription_medicine)

        prescription_has_manipulatedmedicine_object.save()

    def create_prescription_has_medicine(self, medicine_id, quantity, posology, prescription_medicine):
        prescription_has_medicine_object = PrescriptionHasMedicine(
            medicine_id=medicine_id,
            posology=posology, quantity=quantity,
            prescription_medicine=prescription_medicine)

        prescription_has_medicine_object.save()

    def add_medicine_in_prescription(self, atomic_form, prescription_medicine):
        """
        Defines which type of drug will be added to the prescription and adds it.
        """

        medicine_type = atomic_form.cleaned_data.get('medicine_type')
        medicine_id = atomic_form.cleaned_data.get('medicine_id')
        quantity = atomic_form.cleaned_data.get('quantity')
        posology = atomic_form.cleaned_data.get('posology')

        if medicine_type == 'medicine':
            self.create_prescription_has_medicine(medicine_id,
                                                  quantity,
                                                  posology,
                                                  prescription_medicine)
        elif medicine_type == 'manipulated_medicine':
            self.create_prescription_has_manipulated_medicine(medicine_id,
                                                              quantity,
                                                              posology,
                                                              prescription_medicine)
        else:
            # Nothing to do.
            pass

    def add_recommendation_in_prescription(self, formrecommendation, prescription_object):
        """
        Add recomendation to prescription
        """

        recommendation = formrecommendation.cleaned_data.get('recommendation')

        prescription_recommendation_object = PrescriptionRecommendation(
            prescription=prescription_object,recommendation=recommendation)

        prescription_recommendation_object.save()



    def get(self, request, *args, **kwargs):
        """
        Rendering form in view.
        """
        form = CreatePrescriptionForm(request.GET or None)
        formset = self.MedicinePrescriptionFormSet(request.GET or None)
        formrecommendation = self.RecommendationPrescriptionFormSet(request.GET or None)

        data = dict()
        context = {'form': form,
                   'formset': formset,
                   'formrecommendation': formrecommendation,
                   }
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        # Json to communication Ajax.
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        """
        Save data in the form in database.
        """
        form = CreatePrescriptionForm(request.POST or None)
        formset = self.MedicinePrescriptionFormSet(request.POST or None)
        formrecommendation = self.RecommendationPrescriptionFormSet(request.POST or None)
        data = dict()

        # Checks whether the completed forms are valid.

        default_is_valid = False
        atomic_is_valid = False
        formRecommendation_is_valid = False
        if form.is_valid():
            default_is_valid = True
            if formset.is_valid():
                atomic_is_valid = True
                prescription_medicine_object = self.create_prescription_medicine(form)

                for atomic_form in formset:
                    self.add_medicine_in_prescription(atomic_form, prescription_medicine_object)

                if formrecommendation.is_valid():
                    formRecommendation_is_valid = True
                    for recommendationField in formrecommendation:
                        self.add_recommendation_in_prescription(recommendationField, prescription_medicine_object)


        data['form_is_valid'] = default_is_valid and atomic_is_valid and formRecommendation_is_valid
        context = {'form': form,
                   'formset': formset,
                   'formrecommendation': formrecommendation}
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        # Json to communication Ajax.
        return JsonResponse(data)
