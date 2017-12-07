//This functions are used to auto complete the fields when something is been inserted.

//This function receive:
//  element: The element that will be autocompleted.
//  functionJson: The function used to get the data.
//  field: The field where the element will be completed.
function autocompleteElement(element, functionJson, field) {
  $(element).autocomplete({
    source: functionJson,
    select: function(event, ui) {
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

// Customize the autocomplete pattern for medicine.
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

// Customize the autocomplete pattern for exam.
function autocomplete_exam(ul, item) {
    $img = $('<img>');
    $img.attr({
        alt: item.label
    });

    var description = '<font size="2" color="gray">' + item.description + '</font>';

    return $("<li></li>")
    .data("item.autocomplete", item)
    .append("<a>" + item.label + "</a>")
    .append(": <br>" + description + "")
    .appendTo(ul);
}

// Customize the autocomplete pattern for patient.
function autocomplete_patient(ul, item) {
  return $("<li></li>")
    .data("item.autocomplete", item)
    .append("<a>" + item.label + "</a>")
    .append(" - " + item.email)
    .appendTo(ul);
}

// Customize the autocomplete pattern for CID.
function autocomplete_cid(ul, item) {
  return $("<li></li>")
    .data("item.autocomplete", item)
    .append("<a>" + item.label + "</a>")
    .appendTo(ul);
}

// Customize the autocomplete pattern for CID.
function autocomplete_recommendation(ul, item) {
  return $("<li></li>")
    .data("item.autocomplete", item)
    .append("<a>" + item.label + "</a>")
    .appendTo(ul);
}

// Select the field to autocomplete custom.
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
    case 'recommendation':
      return autocomplete_recommendation(ul, item);
    default:
      return;
  }
}

// Select the id the specific field.
function select_type_field(element, field, ui) {
  switch (field) {
    case 'medicine':
      $(element).prop("readonly", true);
      $("#" + element.id + "_id").val(ui.item.id);
      $("#" + element.id + "_type").val(ui.item.type);
      break;
    case 'patient':
      document.getElementById("id_email").type = "text";
      $("#" + element.id + "_id").val(ui.item.id);
      $("#id_email").val(ui.item.email);
      break;
    case 'disease':
      $("#" + element.id + "_id").val(ui.item.id);
      break;
    case 'exam':
      $(element).prop("readonly", true);
      $("#" + element.id + "_type").val(ui.item.type);
      $("#" + element.id + "_id").val(ui.item.id);
      break;
    case 'cid':
      $("#" + element.id + "_id").val(ui.item.id);
      $("#" + element.id + "_id").trigger( "change" );
      break;
    case 'recommendation':
      $("#" + element.id + "_type").val(ui.item.type);
      $("#" + element.id + "_id").val(ui.item.id);
      break;
  }
}

// Set autocomplete in all medicines in form
function autocompleteAllMedicines(){
  var totalMedicines = $('#id_form_medicine-TOTAL_FORMS').val() - 1;
  for(medicineNumber=totalMedicines; medicineNumber>=0; medicineNumber--){
    autocompleteElement('#id_form_medicine-' + medicineNumber + '-medicine', autocompleteMedicine, "medicine");
  }
}

// Set autocomplete in all exams in form
function autocompleteAllExams(){
  var totalExams = $('#id_form_exam-TOTAL_FORMS').val() - 1;
  for(examNumber=totalExams; examNumber>=0; examNumber--){
    autocompleteElement('#id_form_exam-' + examNumber + '-exam', autocompleteExam, "exam");
  }
}

// Set autocomplete in all recommendations in form
function autocompleteAllRecommendations(){
  var totalRecommendations = $('#id_form_recommendation-TOTAL_FORMS').val() - 1;
  for(recommendationNumber=totalRecommendations; recommendationNumber>=0; recommendationNumber--){
    autocompleteElement('#id_form_recommendation-' + totalRecommendations + '-recommendation', autocompleteRecommendation, "recommendation");
  }
}

// Performs autocomplete in the specified fields.
var totalExam = $('#id_form_exam-TOTAL_FORMS').val() - 1;
autocompleteAllMedicines();
autocompleteAllExams();
autocompleteAllRecommendations();
autocompleteElement('#id_patient', autocompletePatient, "patient");
autocompleteElement('#id_cid', autocompleteCid, "cid");
