$(function(){
  $("#send_email").autocomplete({
    source: "ajax/autocomplete_email/",
    minLenght: 3,
    create: function() {
      $(this).data('ui-autocomplete')._renderItem = function(ul, item) {
        item.label = item.label.replace(new RegExp("(?![^&;]+;)(?!<[^<>]*)(" + $.ui.autocomplete.escapeRegex(this.term) + ")(?![^<>]*>)(?![^&;]+;)", "gi"), "<strong>$1</strong>");
        return $("<li></li>")
               .data("item.autocomplete", item)
               .append(item.name + "  - " + "<a>" + item.value + "</a>")
               .appendTo(ul);
      };
    },
    select: function(event, ui) {
       $("#send_email").val(ui.item.value);
    },
})
});
