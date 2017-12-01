
function feedback(path){

      var csrf_token = $('.main-header [name="csrfmiddlewaretoken"]').val();
      var data = {};
      data["csrfmiddlewaretoken"] = csrf_token;;

      var list_messages = document.getElementById("notify_responses");

      $.ajax({
        url: path,
        type: "POST",
        data: data,
        dataType: 'json',
        success: function(data){

            data = JSON.parse(data);

            for(i in data){

              var element = document.createElement("li");
              var link = document.createElement("a");
              var text = document.createTextNode(data[i]['text']);

              link.appendChild(text);
              element.appendChild(link);

              list_messages.appendChild(element);

            }

        }
      });
}
