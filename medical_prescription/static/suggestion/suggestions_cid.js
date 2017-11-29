$('#id_cid_id').change(function() {
  $('.suggestions_cid').empty();

  var csrf_token = $('.modal-body [name="csrfmiddlewaretoken"]').val();
  var jsonText = {};
  jsonText["csrfmiddlewaretoken"] = csrf_token;
  jsonText["id"] = $(this).val();

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

            $('.suggestions_cid').append(
        `<div>
             <div class="col-md-6">
                     <div class="panel-group" id="accordion">
                       <div class="panel panel-default">
                         <div class="panel-heading">
                           <div class="row">
                             <div class="col-sm-10">
                               <h4 class="panel-title">
                                 <a data-toggle="collapse" data-parent="#accordion" href="#collapse1"></a>
                                  ${value.patient}
                               </h4>
                             </div>
                             <div class="col-sm-2">
                               <a href='#'><i class="fa fa-print"></i></a>
                             </div>
                           </div>
                         </div>
                         <div id="collapse1" class="panel-collapse collapse in">
                             <div class="row">
                               <div  class="col-md-8">
                               ${medicines} ${exams} ${recommendations}
                               </div>
                             </div>

                         </div>
                       </div>
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

  for (var item in itens) {
    if (itens.hasOwnProperty(item)) {
      list_itens += "<li>" + itens[item].name + "</li>";
    }
  }
  list_itens += "</ol>";
  return list_itens;
}
