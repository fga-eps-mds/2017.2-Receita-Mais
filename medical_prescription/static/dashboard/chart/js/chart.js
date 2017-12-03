$(document).ready(function () {
  "use strict";

  $.ajax({
    url: chartData,
    type: 'GET',
    traditional: true,
    dataType: 'json',
    success: function(result) {
      console.log(result);
      var a = [
        {y: '2011', item1: 2666},
        {y: '2011', item1: 2778},
        {y: '2013', item1: 4912},
        {y: '2014', item1: 3767},
        {y: '2015', item1: 6810},
        {y: '2016', item1: 5670},
        {y: '2017', item1: 4820},
        {y: '2018', item1: 15073},
        {y: '2019', item1: 10687},
        {y: '2020', item1: 8432}
      ];
      console.log(a);
var line = new Morris.Line({
  element: 'line-chart',
  resize: true,
  data: result,
  xkey: 'name',
  ykeys: ['quantity'],
  labels: ['Quantity'],
  lineColors: ['#3c8dbc'],
  hideHover: 'auto',
  parseTime: false,
  xLabelMargin: 10
});}});
});
