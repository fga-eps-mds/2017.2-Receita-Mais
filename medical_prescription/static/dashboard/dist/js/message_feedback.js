
function feedback(path){
      var csrf_token = $('.main-header [name="csrfmiddlewaretoken"]').val();
      var data = {};
      data["csrfmiddlewaretoken"] = csrf_token;;

      var list_messages = document.getElementById("notify_responses");
      var cont_messages = document.getElementById("cont_responses");
      $.ajax({
        url: path,
        type: "POST",
        data: data,
        dataType: 'json',
        success: function(data){
            data = JSON.parse(data);
            var cont = 0;
            for(i in data){
              cont ++;
              var element = document.createElement("li");
              var link = document.createElement("a");
              var text = document.createTextNode(data[i]['text']);

              link.appendChild(text);
              element.appendChild(link);

              list_messages.appendChild(element);

            }
            cont_messages.appendChild(document.createTextNode(cont));

        }
      });
}
