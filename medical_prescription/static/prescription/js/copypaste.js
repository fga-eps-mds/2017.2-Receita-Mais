$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-prescription .modal-content").html("");
        $("#modal-prescription").modal("show");
      },
      success: function (data) {
        $("#modal-prescription .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#prescription-table tbody").html(data.html_prescription_list);
          $("#modal-prescription").modal("hide");
        }
        else {
          $("#modal-prescription .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create prescription
  $(".js-create-prescription").click(loadForm);
  $("#modal-prescription").on("submit", ".js-prescription-create-form", saveForm);

  // Update prescription
  $("#prescription-table").on("click", ".js-update-prescription", loadForm);
  $("#modal-prescription").on("submit", ".js-prescription-update-form", saveForm);

  // Delete prescription
  $("#prescription-table").on("click", ".js-delete-prescription", loadForm);
  $("#modal-prescription").on("submit", ".js-prescription-delete-form", saveForm);

});
