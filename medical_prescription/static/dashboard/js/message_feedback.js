
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
              var list_from = document.createElement("li");
              var list_link = document.createElement("li");

              var text_user_from = document.createTextNode('De: '+ data[i]['user_from']);
              var text = document.createTextNode(data[i]['text']);

              var lu = document.createElement("ul");


              lu.setAttribute("style","list-style-type: none");
              lu.setAttribute("class", "container-fluid");
              list_from.setAttribute("class", "label label-success");
              list_from.setAttribute("style", "font-size:10px;");
              list_link.setAttribute("style", "color: gray;padding-left:10px;font-size:15px;");

              element.appendChild(lu);
              lu.appendChild(list_from);
              lu.appendChild(list_link);


              list_from.appendChild(text_user_from);
              // list_link.appendChild("<textarea readonly>"+ text +"</textarea>");
              list_link.appendChild(text);

              list_messages.appendChild(element);

            }
            cont_messages.appendChild(document.createTextNode(cont));

        }
      });
}
