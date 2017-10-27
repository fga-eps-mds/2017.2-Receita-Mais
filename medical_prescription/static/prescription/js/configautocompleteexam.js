$.ui.autocomplete.prototype._renderItem = function(ul, item) {
  item.label = item.label.replace(new RegExp("(?![^&;]+;)(?!<[^<>]*)(" + $.ui.autocomplete.escapeRegex(this.term) + ")(?![^<>]*>)(?![^&;]+;)", "gi"), "<strong>$1</strong>");

  $img = $('<img>');
  $img.attr({
    src: 'https://mt.googleapis.com/vt/icon/name=icons/onion/73-hospitals.png',
    alt: item.label
  });

  var description = '<font size="2" color="gray">' + item.description + '</font>';

  return $("<li></li>")
    .data("item.autocomplete", item)
    .append($img)
    .append("<a>" + item.label + "</a>")
    .append(": <br>" + description + "")
    .appendTo(ul);
};
