$('#id_cid_id').change(function(){
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
        success: function(result){
            if (result.status == "success") {
                if (result['data']) {
                    jQuery.each(result['data'], function (i, value) {
                        console.log("Começa");
                        console.log(value.medicines);
                        console.log("For");
                        var medicines = "<b>Medicamentos:</b><br><ol>", exams = "<b>Exames:</b><br><ol>";
                        for (var item in value.medicines) {
                            if (value.medicines.hasOwnProperty(item)) {
                                console.log(value.medicines[item].name);
                                medicines += "<li>" + value.medicines[item].name + "</li>";
                            }
                        }
                        for (var item in value.exams) {
                            if (value.exams.hasOwnProperty(item)) {
                                console.log(value.exams[item].name);
                                exams += "<li>" + value.exams[item].name + "</li>";
                            }
                        }

                        medicines  += "</ol>";
                        exams += "</ol>";

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
                                                                `+ value.patient +`
                                                           </h4>
                                                         </div>
                                                         <div class="col-sm-2">
                                                           <a href='#'><i class="fa fa-print"></i></a>
                                                         </div>
                                                       </div>
                                                     </div>
                                                     <div id="collapse1" class="panel-collapse collapse in">
                                                         <div class="row">
                                                           <div class="col-sm-1">

                                                           </div>
                                                           <div  class="col-md-8">
                                                           `+ medicines + exams +`
                                                           </div>
                                                         </div>

                                                     </div>
                                                   </div>
                                                 </div>
                                               </div>`
                        );
                    });
                }
            }
        }
    });
});
