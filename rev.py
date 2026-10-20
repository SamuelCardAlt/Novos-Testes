import flet as ft


def main(page: ft.Page):

    # Janela principal
    page.title = "EmprestaAqui"
    page.window.width = 800
    page.window.height = 700
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    # Lista para armazenar os empréstimos durante a execução
    emprestimos = []

    # Campos do formulário
    responsavel = ft.TextField(
        label="Nome do responsável",
        hint_text="Digite o nome completo",
        prefix_icon=ft.Icons.PERSON,
        expand=True,
    )

    equipamento = ft.Dropdown(
        label="Equipamento",
        hint_text="Selecione um equipamento",
        options=[
            ft.dropdown.Option("Notebook"),
            ft.dropdown.Option("Projetor"),
            ft.dropdown.Option("Multímetro"),
        ],
        expand=True,
    )

    quantidade = ft.TextField(
        label="Quantidade",
        hint_text="Digite um número inteiro",
        prefix_icon=ft.Icons.NUMBERS,
        keyboard_type=ft.KeyboardType.NUMBER,
        expand=True,
    )

    # Mensagem de retorno
    mensagem = ft.Text(
        "",
        size=14,
        weight=ft.FontWeight.BOLD,
    )

    # Texto que mostra o total de unidades emprestadas
    total_texto = ft.Text(
        "Total de unidades emprestadas: 0",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE,
    )

    # Tabela de empréstimos
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Responsável")),
            ft.DataColumn(ft.Text("Equipamento")),
            ft.DataColumn(ft.Text("Quantidade")),
        ],
        rows=[],
    )

    # Atualiza a tabela e o total de unidades
    def atualizar_tabela():
        tabela.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(item["responsavel"])),
                    ft.DataCell(ft.Text(item["equipamento"])),
                    ft.DataCell(ft.Text(str(item["quantidade"]))),
                ]
            )
            for item in emprestimos
        ]

        total = sum(
            item["quantidade"] for item in emprestimos
        )

        total_texto.value = (
            f"Total de unidades emprestadas: {total}"
        )

        page.update()

    # Registra um novo empréstimo
    def registrar_emprestimo(e):

        nome = (
            responsavel.value.strip()
            if responsavel.value
            else ""
        )

        item = equipamento.value

        qtd_texto = (
            quantidade.value.strip()
            if quantidade.value
            else ""
        )

        # Validação do responsável
        if not nome:
            mensagem.value = "Informe o nome do responsável."
            mensagem.color = ft.Colors.RED
            page.update()
            return

        # Validação do equipamento
        if not item:
            mensagem.value = "Selecione um equipamento."
            mensagem.color = ft.Colors.RED
            page.update()
            return

        # Validação da quantidade
        try:
            qtd = int(qtd_texto)

        except ValueError:
            mensagem.value = (
                "A quantidade deve ser um número inteiro válido."
            )
            mensagem.color = ft.Colors.RED
            page.update()
            return

        if qtd <= 0:
            mensagem.value = (
                "A quantidade deve ser maior que zero."
            )
            mensagem.color = ft.Colors.RED
            page.update()
            return

        # Armazena o empréstimo válido
        emprestimos.append(
            {
                "responsavel": nome,
                "equipamento": item,
                "quantidade": qtd,
            }
        )

        mensagem.value = (
            f"Empréstimo registrado com sucesso para {nome}!"
        )
        mensagem.color = ft.Colors.GREEN

        # Limpa os campos após o registro
        responsavel.value = ""
        equipamento.value = None
        quantidade.value = ""

        # Atualiza a tabela e o total
        atualizar_tabela()

    # Limpa os campos do formulário
    def limpar_campos(e):
        responsavel.value = ""
        equipamento.value = None
        quantidade.value = ""
        mensagem.value = ""

        page.update()

    # Título
    titulo = ft.Text(
        "EmprestaAqui",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE,
    )

    subtitulo = ft.Text(
        "Cadastro e consulta de empréstimos do laboratório",
        size=15,
        color=ft.Colors.GREY,
    )

    # Formulário de cadastro
    formulario = ft.Column(
        controls=[
            ft.Text(
                "Cadastrar empréstimo",
                size=20,
                weight=ft.FontWeight.BOLD,
            ),

            responsavel,
            equipamento,
            quantidade,

            ft.Row(
                controls=[
                    ft.Button(
                        "Registrar empréstimo",
                        icon=ft.Icons.SAVE,
                        on_click=registrar_emprestimo,
                        bgcolor=ft.Colors.BLUE,
                        color=ft.Colors.WHITE,
                    ),

                    ft.OutlinedButton(
                        "Limpar campos",
                        icon=ft.Icons.CLEAR,
                        on_click=limpar_campos,
                    ),
                ],
                wrap=True,
            ),

            mensagem,
        ],
        spacing=12,
    )

    # Área de consulta dos empréstimos
    consulta = ft.Column(
        controls=[
            ft.Text(
                "Empréstimos registrados",
                size=20,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Row(
                controls=[tabela],
                scroll=ft.ScrollMode.AUTO,
            ),

            total_texto,
        ],
        spacing=12,
    )

    # Monta a interface principal
    page.add(
        titulo,
        subtitulo,
        ft.Divider(),
        formulario,
        ft.Divider(),
        consulta,
    )


# Executa o aplicativo
ft.run(main)
