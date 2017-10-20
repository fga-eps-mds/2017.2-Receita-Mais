$(function() {
  var value = $(this).val();
  $("#id_patient").autocomplete({
    source: function(request, response) {
      $.ajax({
        url: "ajax/autocomplete_patient/",
        dataType: "json",
        data: {
          'search': request.term
        },
        success: function(data) {
          console.log(data.list)
          response(data.list);
        }
      });
    },
    minLength: 2
  });
});
