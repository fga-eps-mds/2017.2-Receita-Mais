$('#id_cid_id').change(function(){
    $('.sugestions_cid').empty();

    var csrf_token = $('.modal-body [name="csrfmiddlewaretoken"]').val();
    var jsonText = {};
    jsonText["csrfmiddlewaretoken"] = csrf_token;
    jsonText["id"] = $(this).val();

    $.ajax({
        url: sugestionsCid,
        type: 'POST',
        data: jsonText,
        traditional: true,
        dataType: 'json',
        success: function(result){
            console.log(result)
            if (result.status == "success") {
                if (result['data']) {
                    jQuery.each(result['data'], function (i, value) {
                      console.log(value);
                        $('.sugestions_cid').append(
                            '<tr><td id="cid">'+value['cid']+'</td>' +
                            '<td id="id">'+value['id']+'</td></tr>');
                    });
                }
            }
        }
    });
});
