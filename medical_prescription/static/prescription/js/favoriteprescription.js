function getCookie(name) {
  /*
  This function was implemented in order to return the csrtoken value that is used in the ajax function bellow.
  */
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
return cookieValue;
}
var csrftoken = getCookie('csrftoken');


$(document).on('click', '.post-likes', function(){
  /*
  the following ajax function was implemented to avoid refreshing the page everytime the user favorite or unfavorite a prescription.
  */
    var class_span = $(this).find('span').attr("class");
    console.log(class_span);
    var cookieValue = null;

    if (class_span == 'fa fa-star'){
        $(this).find('span').removeClass('fa fa-star');
        $(this).find('span').addClass('fa fa-star-o');
        $(this).find('span').css('color', 'black');
    }
    else {
        $(this).find('span').removeClass('fa fa-star-o');
        $(this).find('span').addClass('fa fa-star');
        $(this).find('span').css('color', 'orange');
    }

    var url = $(this).attr("url-prescription");

    $.ajax({
        url: url,
        type: "POST",
        dataType: "json",
        data: { csrfmiddlewaretoken: getCookie('csrftoken') },
    });
});
