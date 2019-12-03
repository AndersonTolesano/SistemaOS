$( "#btnsolicitante").click (function() {
    let nome = $("#id_nome").val();
    let email = $("#id_email").val();
    let telefone = $("#id_telefone").val();
    let setor = $("#id_setor").val();
    console.log(nome);
    console.log(email);
    console.log(telefone);
    console.log(setor);

    $.ajax ({
        type: 'POST',
        url: '/salvar/solicitante/',
        dataType: 'json',
        data: {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'setor': setor,
        }, success: function (data) {
            if (data.sucesso){
                alert(
                    'Cadastro Cadastrado com sucesso'
                )
            }
            else if (data.error){
                alert(
                    'Favor preencha os campos'
                )
            }
        }
    })
});