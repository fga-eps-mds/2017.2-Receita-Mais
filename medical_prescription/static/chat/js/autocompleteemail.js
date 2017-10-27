$(function(){
  var value = $(this).val();
  $("#send_email").autocomplete({
    source: function(request, response){
      $.ajax({
          url: "ajax/autocomplete_email/",
          dataType: "json",
          data: {
            'search': request.term
          },
          success:function(data){
            response(data.list)
          }
      });
    },
    minLenght: 3
  });
});
