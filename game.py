import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha o refrigerante certo!")
    resposta_correta = "Guaraná"
    
    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "GUARANA"
        else:
            mensagem.value = "Resposta Errada"     
        page.update()
    
    page.title = "Game: Adivinhe a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors = "#C78B8B"

    page.add(
      ft.Column(
          controls=[
              ft.Text(
                  "Adivinhe a Imagem",
                  size=24,
                  weight="bold"    
                  ),
                  ft.Image(
                      src="images/hornet.jpeg",
                      height=200
                  ),
                  ft.Row(
                      controls=[
                          ft.Button(
                              content="Guaraná",
                              on_click=verificar_resposta,
                              bgcolor="#DEAFAF",
                              color="white"
                          ),
                          ft.Button(
                              content="Pepsi",
                              on_click=verificar_resposta,
                              bgcolor="#DEAFAF",
                              color="white"
                          ),
                          ft.Button(
                              content="Coca-Cola",
                              on_click=verificar_resposta,
                              bgcolor="#DEAFAF",
                              color="white"
                          ),
                      ],
                      alignment=ft.MainAxisAlignment.CENTER
                  ),
                  mensagem
          ],
          horizontal_alignment=ft.CrossAxisAlignment.CENTER
      )
    )

ft.run(main)