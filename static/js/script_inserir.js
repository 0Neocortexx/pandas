function inserir() { 

        // Pega os dados do formulario
        pag_dado1 = document.getElementById('dado1').value;
        pag_dado2 = document.getElementById('dado2').value;

        // Colocar os dados em json
        dados = JSON.stringify({
            dado1: pag_dado1,
            dado2: pag_dado2,
        });

        // Fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/inserir', // Informa a rota requisitada
            type: 'POST', // O tipo de requisição
            dataType: 'json', // Os dados são recebidos em formato json
            contentType: 'application/json',
            data: dados,
            sucess: alert('Dados Enviados!'),
            error: alert('Erro ao contatar back-end'),
        })
    }