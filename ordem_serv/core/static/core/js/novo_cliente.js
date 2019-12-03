$( "#botao" ).click(function() {
  let razaoSocial = $("#id_razao_social").val();
  let fantasia = $("#id_fantasia").val();
  let fone1 = $("#id_fone1").val();
  let fone2 = $("#id_fone2").val();
  let celular = $("#id_celular").val();
  let email = $("#id_email").val();
  let cnpj = $("#id_cnpj").val();
  let ie = $("#id_ie").val();
  let ativo = $("#id_ativo").val();

  $.ajax({
      type: 'POST',
      url: '/salvar/cliente/',
      dataType: 'json',
      data: {
          'razaoSocial': razaoSocial,
          'fantasia': fantasia,
          'fone1': fone1,
          'fone2': fone2,
          'celular': celular,
          'email': email,
          'cnpj': cnpj,
          'ie': ie,
          'ativo': ativo,
      }, success: function (data) {
          if (data.error){
              alert(
                  'Favor preencha os campos'
              )
          }
          else if (data.sucesso){
              alert(
                  'Cliente salvo com sucesso'
              )
          }
          else if (data.falha){
              alert(
                  'falha no preenchimento'
              )
          } else if (data.existe) {
              alert('Cliente com esse CNPJ já cadastrado no sistema!')
          }
      }
  })
});