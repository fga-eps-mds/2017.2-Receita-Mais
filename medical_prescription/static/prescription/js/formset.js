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
function deleteForm(prefix, btn) {
  var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
  if (total > 1) {
    btn.closest('.form-row').remove();
    var forms = $('.form-row');
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
      $(forms.get(i)).find(':input').each(function() {
        updateElementIndex(this, prefix, i);
      });
    }
  }
  return false;
}

// This functions are responsable to call the functions when the button is clicked.
$(document).on('click', '.add-form-row', function(e) {
  e.preventDefault();
  cloneMore('.form-row:last', 'form');
  return false;
});

$(document).on('click', '.remove-form-row', function(e) {
  e.preventDefault();
  deleteForm('form', $(this));
  return false;
});

//This functions are used to auto complete the fields when something is been inserted.

//This function receive:
//  element: The element that will be autocompleted.
//  functionJson: The function used to get the data.
//  field: The field where the element will be completed.
function autocompleteElement(element, functionJson, field) {
  $(element).autocomplete({
    source: functionJson,
    select: function(event, ui) {
      $(this).prop("readonly", true);
      select_type_field(this, field, ui);
    },
    minLength: 2,
    create: function() {
      $(this).data('ui-autocomplete')._renderItem = function(ul, item) {
        item.label = item.label.replace(new RegExp("(?![^&;]+;)(?!<[^<>]*)(" + $.ui.autocomplete.escapeRegex(this.term) + ")(?![^<>]*>)(?![^&;]+;)", "gi"), "<strong>$1</strong>");
        return select_field(ul, item, field);
      };
    }
  });
};

function autocomplete_medicine(ul, item) {
  $img = $('<img>');
  $img.attr({
    src: 'https://mt.googleapis.com/vt/icon/name=icons/onion/73-hospitals.png',
    alt: item.label
  });

  var description = '<font size="2" color="gray">' + item.description + '</font>';
  return $("<li></li>")
    .data("item.autocomplete", item)
    .append($img)
    .append("<a>" + item.label + "</a>")
    .append(": <br>" + description + "")
    .appendTo(ul);
}

function autocomplete_patient(ul, item) {
  return $("<li></li>")
    .data("item.autocomplete", item)
    .append("<a>" + item.label + "</a>")
    .appendTo(ul);
}

function autocomplete_cid(ul, item) {
  return $("<li></li>")
    .data("item.autocomplete", item)
    .append("<a>" + item.label + "</a>")
    .appendTo(ul);
}

function select_field(ul, item, field) {
  switch (field) {
    case 'medicine':
      return autocomplete_medicine(ul, item);
    case 'patient':
      return autocomplete_patient(ul, item);
    case 'disease':
      return autocomplete_disease(ul, item);
    case 'exam':
      return autocomplete_exam(ul, item);
    case 'cid':
      return autocomplete_cid(ul, item);
    default:
      return;
  }
}

function select_type_field(element, field, ui) {
  switch (field) {
    case 'medicine':
      $("#" + element.id + "_id").val(ui.item.id);
      $("#" + element.id + "_type").val(ui.item.type);
      break;
    case 'patient':
      $("#" + element.id + "_id").val(ui.item.id);
      break;
    case 'disease':
      $("#" + element.id + "_id").val(ui.item.id);
      break;
    case 'exam':
      $("#" + element.id + "_id").val(ui.item.id);
      break;
    case 'cid':
      $("#" + element.id + "_id").val(ui.item.id);
      break;
    case 'recommendation':
      $("#" + element.id + "_id").val(ui.item.id);
      break;
  }
}
