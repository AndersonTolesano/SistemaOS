// $( "#btncontato").click(function(){
//     let nome = $("#id_nome_contato").val();
//     let telefone = $("#id_telefone_contato").val();
//     let email = $("#id_email_contato").val();
//
//     $.ajax({
//         type: 'POST',
//         url: '/salvar/contato/',
//         dataType: 'json',
//         data: {
//             'nome': nome,
//             'telefone': telefone,
//             'email': email,
//
//         },  success: function (data){
//             if (data.sucesso) {
//                 alert('Contato salvo com sucesso')
//             }
//             else if (data.error) {
//                 alert('Favor preencha os campos')
//             }
//         }
//     })
// });