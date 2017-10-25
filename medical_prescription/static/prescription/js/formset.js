function autocomplete_patient(ul, item){
  $.ui.autocomplete.prototype._renderItem = function(ul, item) {
      item.label = item.label.replace(new RegExp("(?![^&;]+;)(?!<[^<>]*)(" + $.ui.autocomplete.escapeRegex(this.term) + ")(?![^<>]*>)(?![^&;]+;)", "gi"), "<strong>$1</strong>");
    
      return $("<li></li>")
        .data("item.autocomplete", item)
        .append("<a>" + item.label + "</a>")
        .appendTo(ul);
    };
  }

function updateElementIndex(el, prefix, ndx) {
  var id_regex = new RegExp('(' + prefix + '-\\d+)');
  var replacement = prefix + '-' + ndx;
  if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
  if (el.id) el.id = el.id.replace(id_regex, replacement);
  if (el.name) el.name = el.name.replace(id_regex, replacement);
}

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
    if (id.includes(field)){
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

function autocompleteElement(element, functionJson, field) {
  $(element).autocomplete({
    source: functionJson,
    select: function(event, ui) {
      $(this).prop("readonly", true);
    },
    minLength: 2, 
    create: function() {
            $(this).data('ui-autocomplete')._renderItem  = function (ul, item) {
              return autocomplete_patient(ul, item);
            };
  }
  });
};

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
