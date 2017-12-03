$(document).ready(function($) {

  var $cpf = $("#id_CPF_document");
  $cpf.mask('00000000000');

  var $cep = $("#id_CEP");
  $cep.mask('00000000');

  function clean_form_cep() {
    // Cleans cep form values.
    $("#id_complement").val("");
    $("#id_neighborhood").val("");
    $("#id_city").val("");
    $("#id_UF").val("");
  }

  //When the cep field loses focus.
  $("#id_CEP").blur(function() {

    //New variable "cep" with digits only.
    var cep = $(this).val().replace(/\D/g, '');


    if (cep != "") {

      //Regular expression to validate the CEP.
      var validationcep = /^[0-9]{8}$/;

      // Validate the format of the CEP.
      if (validationcep.test(cep)) {

        // Fill fields while querying API.
        $("#id_complement").val("Buscando...");
        $("#id_neighborhood").val("Buscando...");
        $("#id_city").val("Buscando...");
        $("#id_UF").val("Buscando...");

        // Check the webservice viacep.com.br/
        $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function(dados) {

          if (!("erro" in dados)) {
            // Refreshes fields with query values.
            $("#id_complement").val(dados.logradouro);
            $("#id_neighborhood").val(dados.bairro);
            $("#id_city").val(dados.localidade);
            $("#id_UF").val(dados.uf);
          } //end if.
          else {
            clean_form_cep();
            alert("CEP não encontrado.");
          }
        });
      } //end if.
      else {
        clean_form_cep();
        alert("Formato de CEP inválido.");
      }
    } //end if.
    else {
      // no value, clean form.
      clean_form_cep();
    }
  });
});
