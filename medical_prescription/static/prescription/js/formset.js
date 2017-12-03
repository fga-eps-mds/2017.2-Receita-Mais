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
    if (id.endsWith(field)) {
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
  if (total > 1) {
    btn.closest(text).remove();
    var forms = $(text);
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
      $(forms.get(i)).find(':input').each(function() {
        updateElementIndex(this, prefix, i);
      });
    }
    return true;
  } else if(total == 1){
    $(text).find(':input').each(function() {
      $(this).prop("readonly", false);
      $(this).val('');
    });
    btn.closest(text).hide();
    return true;
  }
}
