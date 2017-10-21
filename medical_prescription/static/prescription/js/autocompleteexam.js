$('.exam-field').focus(function() {
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
					console.log(data.list)
          response(data.list);
        }
      });
    },
    minLength: 2
  });
});
