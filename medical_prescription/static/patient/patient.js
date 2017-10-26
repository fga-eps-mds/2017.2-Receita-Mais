  $(document).ready(function($) {

    //Criando mascara para os campos do formulário
    var $id_CPF = $("#id_CPF_document");
    $id_CPF.mask('000.000.000-00', {reverse: true});
    var $date_of_birth = $("#id_date_of_birth");
    $date_of_birth.mask('00/00/0000');
    var $phone = $("#id_phone");
    $phone.mask('(00) 0000-00000');
    function limpa_formulário_cep() {
      // Limpa valores do formulário de cep.
      $("#rua").val("");
      $("#bairro").val("");
      $("#cidade").val("");
      $("#id_UF").val("");
    }

    //Quando o campo cep perde o foco.
    $("#id_CEP").blur(function() {

      //Nova variável "cep" somente com dígitos.
      var cep = $(this).val().replace(/\D/g, '');

      //Verifica se campo cep possui valor informado.
      if (cep != "") {

        //Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if (validacep.test(cep)) {

          //Preenche os campos com "..." enquanto consulta webservice.
          $("#id_complement").val("Buscando...");
          $("#id_neighborhood").val("Buscando...");
          $("#id_city").val("Buscando...");
          $("#id_UF").val("Buscando...");

          //Consulta o webservice viacep.com.br/
          $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function(dados) {

            if (!("erro" in dados)) {
              //Atualiza os campos com os valores da consulta.
              $("#id_complement").val(dados.logradouro);
              $("#id_neighborhood").val(dados.bairro);
              $("#id_city").val(dados.localidade);
              $("#id_UF").val(dados.uf);
            } //end if.
            else {
              //CEP pesquisado não foi encontrado.
              limpa_formulário_cep();
              alert("CEP não encontrado.");
            }
          });
        } //end if.
        else {
          //cep é inválido.
          limpa_formulário_cep();
          alert("Formato de CEP inválido.");
        }
      } //end if.
      else {
        //cep sem valor, limpa formulário.
        limpa_formulário_cep();
      }
    });
  });
