var counter = 1;

var limit = 3;

function addInput(divName, input_name){
        var $div = $('input[id^="'+ divName +'"]:last');
        var $klon = $div.clone(true).attr('id', "#"+divName).insertAfter("#"+divName);
        counter++;
}
