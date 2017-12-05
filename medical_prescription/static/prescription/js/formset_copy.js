$.getScript("/static/prescription/js/formset.js");

// This function is responsable to remove medicine form.
$(document).on('click','#add_more_medicine_copy', function(){
  cloneOrShow($('div.table_medicine:last'), 'form_medicine', autocompleteMedicine, "medicine");
});

// Method to clone medicine fields in the document
$(document).on('click','.remove-medicine', function(){
  deleteForm("form_medicine", ".table_medicine", $(this).parent());
});

// Method to clone exam fields in the document
$(document).on('click','#add_more_exam_copy', function(){
    cloneOrShow('div.table_exam:last', 'form_exam', autocompleteExam, "exam");
});

// This function is responsable to remove exam form.
$(document).on('click','.remove-exam', function(){
  deleteForm("form_exam", ".table_exam", $(this).parent());
});

// Method to clone recomendation fields in the document
$(document).on('click','#add_more_recomendation_copy', function(){
cloneOrShow('div.table_recommendation:last', 'form_recommendation',autocompleteRecommendation, "recommendation");
});

// This function is responsable to remove recommendation form.
$(document).on('click','.remove-recommendation', function(){
  deleteForm("form_recomendation", ".table_recommendation", $(this).parent());
});
