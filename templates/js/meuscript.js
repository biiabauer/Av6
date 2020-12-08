$(function() { 
    
    function exibir_livros() {
        mostrar_conteudo('TabelaLivros')
        $.ajax({
            url: 'http://localhost:5000/listar_livros',
            method: 'GET',
            dataType: 'json', 
            success: listar, 
            error: function(problema) {
                alert("erro ao ler dados, verifique o backend");
            }
        });
         
        function listar (livros) {
            $('#corpoTabelaLivros').empty();
            mostrar_conteudo("cadastroLivros");      
            for (var i in livros) { 
                lin = '<tr id="linha_'+livros[i].id+'">' + 
                '<td>' + livros[i].nome + '</td>' + 
                '<td>' + livros[i].autor + '</td>' + 
                '<td>' + livros[i].ano_publi + '</td>' + 
                '<td><a href=# id="excluir_' + livros[i].id + '" ' + 
                  'class="excluir_livro"><img src="img/excluir.png" '+
                  'alt="Excluir livro" title="Excluir livros" height=20 width= 20></a>' + 
                '</td>' + 
                '</tr>';
                $('#corpoTabelaLivros').append(lin);
            }
        }
    }

    function mostrar_conteudo(identificador) {
        $("#cadastroLivros").addClass('invisible');
        $("#cadastroLeitor").addClass('invisible');
        $("#cadastroBiblioteca").addClass('invisible');
        $("#cadastroLeitura").addClass('invisible');
        $("#conteudoInicial").addClass('invisible');
        $("#"+identificador).removeClass('invisible');      
    }

    $(document).on("click", "#linkListarLivros", function() {
        exibir_livros();
    });
    
    $(document).on("click", "#linkInicio", function() {
        mostrar_conteudo("conteudoInicial");
    });

    $(document).on("click", "#btIncluirLivro", function() {
        nome = $("#campoNome").val();
        autor = $("#campoAutor").val();
        ano_publi = $("#campoAno").val();
        var dados = JSON.stringify({ nome: nome, autor: autor, ano_publi: ano_publi });
        $.ajax({
            url: 'http://localhost:5000/incluir_livro',
            type: 'POST',
            dataType: 'json', 
            contentType: 'application/json', 
            data: dados, 
            success: livroIncluida, 
            error: erroAoIncluir
        });
        function livroIncluida (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Música incluída com sucesso!");
                nome = $("#campoNome").val();
                autor = $("#campoautor").val();
                ano_publi = $("#campoAno").val();
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

    $('#modalIncluirLivro').on('hide.bs.modal', function (e) {
        if (! $("#cadastroLivros").hasClass('invisible')) {
            exibir_livros();
        }
    });

    mostrar_conteudo("conteudoInicial");

    $(document).on("click", ".excluir_livro", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_";
        var id_livro = componente_clicado.substring(nome_icone.length);
        $.ajax({
            url: 'http://localhost:5000/excluir_livro/'+id_livro,
            type: 'DELETE', 
            dataType: 'json', 
            success: livroExcluida, 
            error: erroAoExcluir
        });
        function livroExcluida (retorno) {
            if (retorno.resultado == "ok") { 
                $("#linha_" + id_livro).fadeOut(1000, function(){
                    alert("Livro removido com sucesso!");
                });
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoExcluir (retorno) {
            alert("erro ao excluir dados, verifique o backend: ");
        }
    });

    function exibir_leitor() {
        $.ajax({
            url: 'http://localhost:5000/listar_leitor',
            method: 'GET',
            dataType: 'json', 
            success: listar, 
            error: function(problema) {
                alert("erro ao ler dados, verifique o backend: ");
            }
        });

        function listar (leitor) {
            $('#corpoTabelaLeitor').empty();
            mostrar_conteudo("cadastroLeitor");      
            for (var i in leitor) {
                lin = '<tr id="linha_leitor_'+leitor[i].id+'">' + 
                '<td>' + leitor[i].nome + '</td>' + 
                // dados da profissao
                '<td>' + leitor[i].livro.nome + '</td>' + 
                '<td>' + leitor[i].livro.autor + '</td>' + 
                '<td>' + leitor[i].livro.ano_publi + '</td>' + 
                '<td><a href=# id="excluir_leitor_' + leitor[i].id + '" ' + 
                  'class="excluir_leitor"><img src="img/excluir.png" height=20 width= 20'+
                  'alt="Excluir leitor" title="Excluir leitor" ></a>' + 
                '</td>' + 
                '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaLeitor').append(lin);
            }
        }
    }

    // código para mapear o click do link Exames Realizados
    $(document).on("click", "#linkListarLeitor", function() {
        exibir_leitor();
    });

    function exibir_biblioteca() {
        $.ajax({
            url: 'http://localhost:5000/listar_biblioteca',
            method: 'GET',
            dataType: 'json', 
            success: listar, 
            error: function(problema) {
                alert("erro ao ler dados, verifique o backend: ");
            }
        });

        function listar (biblioteca) {
            $('#corpoTabelaBiblioteca').empty();
            mostrar_conteudo("cadastroBiblioteca");      
            for (var i in biblioteca) {
                lin = '<tr id="linha_biblioteca_'+biblioteca[i].id+'">' + 
                '<td>' + biblioteca[i].nome + '</td>' + 
                // dados da profissao
                '<td>' + biblioteca[i].livro.nome + '</td>' + 
                '<td>' + biblioteca[i].livro.autor + '</td>' + 
                '<td>' + biblioteca[i].livro.ano_publi + '</td>' + 
                '<td><a href=# id="excluir_biblioteca_' + biblioteca[i].id + '" ' + 
                  'class="excluir_biblioteca"><img src="img/excluir.png" height=20 width= 20'+
                  'alt="Excluir biblioteca" title="Excluir biblioteca" ></a>' + 
                '</td>' + 
                '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaBiblioteca').append(lin);
            }
        }
    }

    // código para mapear o click do link Exames Realizados
    $(document).on("click", "#linkListarBiblioteca", function() {
        exibir_biblioteca();
    });

    function exibir_leitura() {
        $.ajax({
            url: 'http://localhost:5000/listar_leitura',
            method: 'GET',
            dataType: 'json', 
            success: listar, 
            error: function(problema) {
                alert("erro ao ler dados, verifique o backend: ");
            }
        });

        function listar (leitura) {
            $('#corpoTabelaLeitura').empty();
            mostrar_conteudo("cadastroLeitura");      
            for (var i in leitura) {
                lin = '<tr id="linha_leitura_'+leitura[i].id+'">' + 
                // dados da profissao
                '<td>' + leitura[i].id + '</td>' + 
                '<td><a href=# id="excluir_leitura_' + leitura[i].id + '" ' + 
                  'class="excluir_leitura"><img src="img/excluir.png" height=20 width= 20'+
                  'alt="Excluir leitura" title="Excluir leitura" ></a>' + 
                '</td>' + 
                '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaLeitura').append(lin);
            }
        }
    }

    // código para mapear o click do link Exames Realizados
    $(document).on("click", "#linkListarLeitura", function() {
        exibir_leitura();
    });



});
