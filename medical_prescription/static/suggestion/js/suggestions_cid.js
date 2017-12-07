$('#id_cid_id').change(function() {
  $('.suggestions_cid').empty();

  var csrf_token = $('.modal-body [name="csrfmiddlewaretoken"]').val();
  var jsonText = {};
  jsonText["csrfmiddlewaretoken"] = csrf_token;
  jsonText["id"] = $(this).val();

  var suggestion = $("#modal-view").attr("data-suggestion");
  $.ajax({
    url: suggestionsCid,
    type: 'POST',
    data: jsonText,
    traditional: true,
    dataType: 'json',
    success: function(result) {
      if (result.status == "success") {
        if (result['data']) {
          jQuery.each(result['data'], function(i, value) {

            var medicines = add_itens("Medicamentos", value.medicines);
            var exams = add_itens("Exames", value.exams);
            var recommendations = add_itens("Recomendações", value.recommendations);
            var url_suggestion = suggestion.replace('None', value.id);
            console.log(url_suggestion);

            $('.suggestions_cid').append(
      ` <div class="box box-primary box-solid">
          <div class="box-header with-border">
            <h3 class="box-title">${value.patient}</h3>

            <div class="box-tools pull-right">
              <input type="button" class="js-show-suggestion btn btn-secondary" data-url="${url_suggestion}" value="Visualizar"></input>
            </div>
          </div>
          <div class="box-body">
            ${medicines} ${exams} ${recommendations}
          </div>
        </div>`);
          });
        }
      }
    }
  });
});


function add_itens(name, itens) {
  var list_itens = "";

  if (itens.length == 0) {
    return list_itens;
  }

  list_itens = "<b>" + name + "</b><br><ol>"
  console.log(itens);
  for (var item in itens) {
    if (itens.hasOwnProperty(item)) {
      list_itens += "<li>" + itens[item].name + "</li>";
    }
  }
  list_itens += "</ol>";
  return list_itens;
}
