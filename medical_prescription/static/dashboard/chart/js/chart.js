// This function is intended to request the application data for the chart.
$(document).ready(function() {
  "use strict";

  $.ajax({
    url: chartData,
    type: 'GET',
    traditional: true,
    dataType: 'json',
    success: function(result) {
      var line = new Morris.Line({
        element: 'line-chart',
        resize: true,
        data: result,
        xkey: 'name',
        ykeys: ['quantity'],
        labels: ['Quantity'],
        lineColors: ['#3c8dbc'],
        hideHover: 'auto',
        parseTime: false
      });
    }
  });
});
