$(function () {

    /* Functions */
    var modalIsCreated = false;

    var loadForm = function () {
        var btn = $(this);
        if (!modalIsCreated){
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            async: true,
            success: function (data) {
                $("#modal-prescription .modal-content").html("");
                $("#modal-prescription").modal("show");
                modalIsCreated = false;
                $("#modal-prescription .modal-content").html(data.html_form);
            }
        });
      }else{
        $("#modal-prescription").modal("show");
      }
    };

    var saveForm = function () {
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
                  $("#modal-prescription").modal("hide");
                }
                else {
                    $("#modal-prescription").modal("show");
                    $("#modal-prescription .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create prescription.
    $(".js-create-prescription").click(loadForm);
    $("#modal-prescription").on("submit", ".js-prescription-create-form", saveForm);

    // Update prescription.
    $("#prescription-table").on("click", ".js-update-prescription", loadForm);
    $("#modal-prescription").on("submit", ".js-prescription-update-form", saveForm);

    // Delete prescription.
    $("#prescription-table").on("click", ".js-delete-prescription", loadForm);
    $("#modal-prescription").on("submit", ".js-prescription-delete-form", saveForm);

    // Show prescription.
    $(".js-show-prescription").click(loadForm);

});
