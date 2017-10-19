var counter = 1;

var limit = 3;

function addInput(divName){
    if (counter == limit)  {
        alert("You have reached the limit of adding " + counter + " inputs");
    }
    else {
        var i = $('div[id^="'+ divName +'"]:last');
        var $div = $('div[id^="'+ divName +'"]:last');
        var $klon = $div.clone().appendTo($div);
        //var newdiv = document.createElement('div');
        //newdiv.innerHTML = "Entry " + (counter + 1) + " <br><input type='text' name='myInputs[]'>";
        //document.getElementById(divName).appendChild(newdiv);
        //$div.after( $klon.text('klon'+num) );
        counter++;
    }
}
