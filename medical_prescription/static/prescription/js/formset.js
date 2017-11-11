$.getScript("/static/prescription/js/autocomplete.js");

function updateElementIndex(el, prefix, ndx) {
  var id_regex = new RegExp('(' + prefix + '-\\d+)');
  var replacement = prefix + '-' + ndx;
  if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
  if (el.id) el.id = el.id.replace(id_regex, replacement);
  if (el.name) el.name = el.name.replace(id_regex, replacement);
}
// This function is used to add another form dynamically when the button is clicked.
// The parameters are:
//    selector: the div where the form will be added.
//    prefix: The form that will be cloned.
//    functionJson: The function to pass the data.
//    field: the field that will be used as reference.
function cloneMore(selector, prefix, functionJson, field) {
  var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
  var newElement = $(selector).clone(false);
  newElement.find(':input').each(function() {
    var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-');
    var id = 'id_' + name;
    $(this).attr({
      'name': name,
      'id': id
    }).val('').removeAttr('checked');
    $(this).prop("readonly", false);
    if (id.includes(field)) {
      autocompleteElement(this, functionJson, field);
    }
  });
  total++;
  $('#id_' + prefix + '-TOTAL_FORMS').val(total);
  $(selector).after(newElement);
  var conditionRow = $('.form-row:not(:last)');
  conditionRow.find('.btn.add-form-row')
    .removeClass('btn-success').addClass('btn-danger')
    .removeClass('add-form-row').addClass('remove-form-row')
    .html('<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>');
  return false;
}

function showHideForm(selector){
  $(selector).show();
}

function cloneOrShow(selector, prefix, functionJson, field){
  var verifyVisible = $(selector).is(":visible");
  if(verifyVisible){
    cloneMore(selector, prefix, functionJson, field);
  }else{
    showHideForm(selector);
  }
  return false;
}

// This function is used to delete a form dynamically when the button is clicked.
function deleteForm(prefix, text, btn) {
  var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
  console.log(total);
  if (total > 1) {
    btn.closest(text).remove();
    var forms = $(text);
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
      $(forms.get(i)).find(':input').each(function() {
        updateElementIndex(this, prefix, i);
      });
    }
    return false;
  } else if(total == 1){
    $(text).find(':input').each(function() {
      $(this).prop("readonly", false);
      $(this).val('');
    });
    btn.closest(text).hide();
    return false;
  }
}

// Calls add and remove forms.
$(document).ready(function() {

  // Method to clone medicine fields in the document
  $('#add_more').click(function() {
    cloneOrShow('div.table_medicine:last', 'form_medicine', autocompleteMedicine, "medicine");
  });

  // This function is responsable to remove medicine form.
   $("body").off("click").on("click",".remove-medicine",function() {
    deleteForm("form_medicine", ".table_medicine", $(this).parent());
  });

  // Method to clone exam fields in the document
  $('#add_more_exam').click(function() {
    cloneOrShow('div.table_exam:last', 'form_exam', autocompleteExam, "exam");
  });

  // This function is responsable to remove exam form.
   $("body").on("click",".remove-exam",function() {
    deleteForm("form_exam", ".table_exam", $(this).parent());
  });

  // Method to clone reccomendation fields in the document
  $('#add_more_reccomendation').click(function() {
    cloneOrShow('div.table_recommendation:last', 'form_reccomendation', "", "recommendation");
  });

  // This function is responsable to remove recommendation form.
   $("body").on("click",".remove-recommendation",function() {
    deleteForm("form_reccomendation", ".table_recommendation", $(this).parent());
  });

});
