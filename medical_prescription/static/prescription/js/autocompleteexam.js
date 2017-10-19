
$('.exam-field').on("focus", function() {
  var value = $(this).val();
  console.log(this)
  $(this).autocomplete({
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
