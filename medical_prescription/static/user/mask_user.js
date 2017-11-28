$(document).ready(function($) {

  //Creating mascara for form fields
  var $date_of_birth = $("#id_date_of_birth");
  $date_of_birth.mask('00/00/0000');
  var $phone = $("#id_phone");
  $phone.mask('(00) 0000-00000');
});
