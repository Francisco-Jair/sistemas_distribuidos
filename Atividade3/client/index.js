$(document).ready(function(){
    $(document).on('click','#btn', function(){
        var valor = $('#valor').val();

        if(valor != ''){
            var data =  JSON.stringify({
                login: valor
            })
            
            $.ajax({
              type: "POST",
              headers: {
                "accept": "application/json",
                "Access-Control-Allow-Origin": "*"
              },
              data: data,
              dataType: 'json',
              url: "http://localhost:8000/login",
              method: "POST",
            }).done(function(res) {
               // console.log(res);
               // $('div').append(res.nome);
               // window.location.href = `./file/caixa_entrada.html?user=${res.nome}`;
            });
      
        }
    });
});