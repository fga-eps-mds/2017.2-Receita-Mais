
$(document).on('click','.js-show-suggestion', function(){
  $("#modal-prescription").modal("hide");
  loadForm(this, "#modal-view");
});

$(document).on('click','.btn-return-modal', function(){
  $("#modal-prescription").modal("hide");
  $("#modal-prescription").modal("show");
});

    /* Functions */
    var modalIsCreated = false;

    function loadForm(event, id_modal) {
        var btn = $(event);
        $(id_modal).modal({
          backdrop: 'static',
          keyboard: false
        })
        if (!modalIsCreated){
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            async: true,
            success: function (data) {
                $(id_modal + " .modal-content").html("");
                $(id_modal).modal("show");
                modalIsCreated = false;
                $(id_modal + " .modal-content").html(data.html_form);
            }
        });
      }else{
        $(id_modal).modal("show");
      }
    };

    function saveForm(event) {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            async: true,
            success: function (data) {
                if (data.form_is_valid) {
                  modalIsCreated = false;
                  $(event.data.id_modal).modal("hide");
                }
                else {
                    $(event.data.id_modal).modal("show");
                    $(event.data.id_modal + " .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };
