$(function () {

    /* Functions */
    var modalIsCreated = false;

    function loadForm(event) {
        var btn = $(this);
        $(event.data.id_modal).modal({
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
                $(event.data.id_modal + " .modal-content").html("");
                $(event.data.id_modal).modal("show");
                modalIsCreated = false;
                $(event.data.id_modal + " .modal-content").html(data.html_form);
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


    /* Binding */

    // Create prescription.
    $(".js-create-prescription").click({id_modal: "#modal-prescription"}, loadForm);
    $("#modal-prescription").on("submit", ".js-prescription-create-form",{id_modal: "#modal-prescription"}, saveForm);

    // Update prescription.
    $("#prescription-table").on("click", ".js-update-prescription", {id_modal: "#modal-prescription"}, loadForm);
    $("#modal-prescription").on("submit", ".js-prescription-update-form", {id_modal: "#modal-prescription"}, saveForm);

    // Delete prescription.
    $("#prescription-table").on("click", ".js-delete-prescription", {id_modal: "#modal-prescription"}, loadForm);
    $("#modal-prescription").on("submit", ".js-prescription-delete-form", {id_modal: "#modal-prescription"}, saveForm);

    // Show prescription.
    $(".js-show-prescription").click({id_modal: "#modal-prescription"}, loadForm);
});
