// Sorting of drug forms.
$( function() {
  $("ul.list-medicine").sortable({
    connectWith: 'ul.list-medicine',
    axis: 'y'
  });
  $("ul.list-medicine").disableSelection();

  $("ul.list-exam").sortable({
    connectWith: 'ul.list-exam',
    axis: 'y'
  });
  $("ul.list-exam").disableSelection();

  $("ul.list-recommendation").sortable({
    connectWith: 'ul.list-recommendation',
    axis: 'y'
  });
  $("ul.list-recommendation").disableSelection();

});
