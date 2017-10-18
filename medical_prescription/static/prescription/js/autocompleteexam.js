$(function() {
  var value = $(this).val();
  $("#id_exam").autocomplete({
    source: function(request, response) {
      $.ajax({
        url: "ajax/autocomplete_exam/",
        dataType: "json",
        data: {
          'search': request.term
        },
        success: function(data) {
          response(data.list);
        }
      });
    },
    minLength: 2
  });
});
