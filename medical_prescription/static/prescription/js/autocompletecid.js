$(function() {
  var value = $(this).val();
  $("#id_cid").autocomplete({
    source: function(request, response) {
      $.ajax({
        url: "ajax/autocomplete_cid/",
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
