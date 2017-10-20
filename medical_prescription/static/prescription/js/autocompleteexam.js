// $(document).ready(function(){
// 	$("#id_exam").keyup(function(){
// 		$.ajax({
//       url: "ajax/autocomplete_exam/",
//       dataType: "json",
// 		beforeSend: function(){
// 			$(this).css("background","#FFF");
// 		},
// 		success: function(data){
// 			console.log(data.list)
// 		}
// 		});
// 	});
// });
// //To select country name
// function selectCountry(val) {
// $("#id_exam").val(val);
// $("#suggesstion-box").hide();
// }

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
					console.log("------------------------")
					console.log(data.list)
          response(data.list);
        }
      });
    },
    minLength: 2
  });
});
