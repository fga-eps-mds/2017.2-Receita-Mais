$(document).ready(function($) {
  //Creating mascara for form fields
  var $date_of_birth = $("#id_date_of_birth");
  $date_of_birth.mask('00/00/0000');

  maskPhone( form.phone );

});

function maskPhone( field ) {

  function treat( value,  isOnBlur ) {

    value = value.replace(/\D/g,"");
    value = value.replace(/^(\d{2})(\d)/g,"($1)$2");

    if( isOnBlur ) {

      value = value.replace(/(\d)(\d{4})$/,"$1-$2");
    } else {

      value = value.replace(/(\d)(\d{3})$/,"$1-$2");
    }
    return value;
  }

  field.onkeypress = function (evt) {

    var code = (window.event)? window.event.keyCode : evt.which;
    var value = this.value
    this.value = treat(value, false);
  }

  field.onblur = function() {

    var value = this.value;
    if( value.length < 11 ) {
      this.value = ""
    }else {
      this.value = treat( this.value, true );
    }
  }

  field.maxLength = 14;
}
