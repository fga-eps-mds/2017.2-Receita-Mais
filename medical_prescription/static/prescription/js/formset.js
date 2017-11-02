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
  var newElement = $(selector).clone(false);
  var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
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

// This function is used to delete a form dynamically when the button is clicked.
function deleteForm(prefix, text, btn) {
  var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
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
  }
}

// This function is responsable to remove medicine form.
$(document).on('click', '.remove-medicine', function(e) {
  e.preventDefault();
  deleteForm('form', '.table_medicine', $(this).parent());
  return false;
});

// This function is responsable to remove recommendation form.
$(document).on('click', '.remove-recommendation', function(e) {
  e.preventDefault();
  deleteForm('form', '.table_recommendation ', $(this).parent());
  return false;
});


// Methods to clone fields in document.
$('#add_more').click(function() {
  cloneMore('div.table_medicine:last', 'form', autocompleteMedicine, "medicine");
});

$('#add_more_exam').click(function() {
  cloneMore('div.table_exam:last', 'form', autocompleteExam, "exam");
});

$('#add_more_reccomendation').click(function() {
  cloneMore('div.table_recommendation:last', 'form', "", "recommendation");
});
