import flet as ft 

def main (page: ft.Page):
    #janela principal
    page.title = "EmprestaAqui"
    page.window,width = 800
    page.window.height =700
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    #lista para armazenar os emprestimos durante a execução
    emprestimos - []

    #campos do formulario
    responsavel = ft.TextField(
        label = "Nome do responável",
        hint_text = "Digite o nome completo",
        prefix_icon = ft.Icons.PERSON,
        expand = True,
    )

    equipamento = ft.Dropdown(
        label = "equipamento",
        hint_text = "selecione um equipamento",
        options = [
            ft.dropdown.Option("Notebook"),
            ft.dropdown.Option("Projetor"),
            ft.dropdown.Option("Multímetro"),

        ],
        prefix_icon = ft.Icons.COMPUTER,
        expand = True,
    )
    quantidade = ft.TextField(
        label = "quantidade",
        hint_text = "Digite um número inteiro",
        prefix_icon = ft.Icons.NUMBERS,
        keyboard_type = ft.KeyboardType.NUMBER,
        expand = True
    )
    mensagem = ft.Text(
        "",
        size = 14,
         weight=ft.FontWeight.BOLD,
    )
    total_texto=ft.Text(
        "Total de unidades empretadas: 0 ",
        size = 20,
        weight = ft.FontWeight.BOLD,
        color = ft.Colors.BLUE,
    )
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Responsável")),
            ft.DataColumn(ft.Text("Equipamento")),
            ft.DataColumn(ft.Text("Quantidade")),
        ],
        rows = [],
        expand = True,
    )
