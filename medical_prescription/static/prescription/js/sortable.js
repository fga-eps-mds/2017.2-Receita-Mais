$( function() {
  $("ul.list-medicine").sortable({
    connectWith: 'ul',
    axis: 'y'
  });
  $("ul.list-medicine").disableSelection();
});
