# AUTHORS:
# MATHEUS DE ALMEIDA BOAVA                                                
# TAÍS MAYME FERRARI                                                      
# RAFAEL RODRIGUES PICHIBINSKI                                            
                                    
import npyscreen


class LoginForm(npyscreen.FormBaseNew):
    def create(self):
        altura, largura = self.useable_space()
        box_altura = 8
        box_largura = 50
        box_rely = int((altura - box_altura) / 2) - 2
        box_relx = int((largura - box_largura) / 2)

        titulo_ascii = r"""

██╗   ██╗███╗   ██╗██╗ ██████╗    ██████╗  █████╗ ███╗   ██╗██╗  ██╗
██║   ██║████╗  ██║██║██╔════╝    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
██║   ██║██╔██╗ ██║██║██║  ███╗   ██████╔╝███████║██╔██╗ ██║█████╔╝ 
██║   ██║██║╚██╗██║██║██║   ██║   ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ 
╚██████╔╝██║ ╚████║██║╚██████╔╝██╗██████╔╝██║  ██║██║ ╚████║██║  ██╗
 ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                                    
COOPERATIVA DE CRÉDITO E ECONOMIA MÚTUA UNIGUAÇU LTDA
Av. Brasil, 1234 - Centro - São Miguel do Iguaçu/PR
CNPJ 79.378.841/0001-97 - Telefone: (45) 3528-1234         
"""
        for i, linha in enumerate(titulo_ascii.splitlines()):
            self.add(npyscreen.FixedText, value=linha, editable=False, relx=max(2, int((largura - len(linha)) / 2)), rely=10 + i, color='GOOD')

        self.login_box = self.add(
            npyscreen.BoxTitle,
            name="Acesso do Cooperado",
            relx=box_relx,
            rely=box_rely,
            max_width=box_largura,
            max_height=box_altura - 1,
            editable=False
        )

        self.username = self.add(
            npyscreen.TitleText,
            name="Matrícula:",
            relx=box_relx + 2,
            rely=box_rely + 2,
            width=box_largura - 4
        )
        self.password = self.add(
            npyscreen.TitlePassword,
            name="Senha:",
            relx=box_relx + 2,
            rely=box_rely + 4,
            width=box_largura - 4
        )

        botao_texto = " [Acessar Sistema] "
        botao_largura = len(botao_texto)
        relx_central = int((largura - botao_largura) / 2)

        self.ok_button = self.add(
            npyscreen.ButtonPress,
            name=botao_texto,
            relx=relx_central-3,
            rely=box_rely + box_altura + 1,
        )
        self.ok_button.whenPressed = self.executar_login

    def beforeEditing(self):
        self.username.value = ""
        self.password.value = ""

    def executar_login(self):
        if self.username.value == "admin" and self.password.value == "admin":
            self.parentApp.logged_user = self.username.value
            self.parentApp.setNextForm("DASHBOARD")
            self.editing = False
        else:
            npyscreen.notify_confirm("Usuário ou senha inválidos!", title="Erro de Login")

class DashboardForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, value="DASHBOARD", editable=False, relx=2, rely=1, color='GOOD')
        self.add(npyscreen.FixedText, value="MENU DE OPÇÕES", editable=False, relx=2, rely=3)
        altura, largura = self.useable_space()
        margem_lateral = 4
        largura_total = largura - margem_lateral

        # Botões individuais
        self.botao_logout = self.add(
            npyscreen.ButtonPress,
            name="Logout",
            relx=4,
            rely=5
        )
        self.botao_logout.whenPressed = self.acao_logout

        texto_instrucoes = [
            "INSTRUÇÕES DO DASHBOARD",
            "",
            "Logout:",
            "  - Retorna à tela de login.",
        ]

        self.detalhes = self.add(
            npyscreen.BoxTitle,
            name="Instruções",
            values=texto_instrucoes,
            relx=50,
            rely=5,
            max_height=altura - 8,
            width=largura_total - 80,
            editable=False
        )

    def acao_logout(self):
        self.parentApp.setNextForm("MAIN")
        self.editing = False

    def beforeEditing(self):
        self.name = f"COOPERATIVA DE CRÉDITO E ECONOMIA MÚTUA UNIGUAÇU LTDA | Usuário: {self.parentApp.logged_user}"

class LoginApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.logged_user = None
        self.addForm("MAIN", LoginForm, name="COOPERATIVA DE CRÉDITO E ECONOMIA MÚTUA UNIGUAÇU LTDA")
        self.addForm("DASHBOARD", DashboardForm)

if __name__ == '__main__':
    # Mensagem de boas-vindas e instruções básicas do sistema
    input(
        "\n" +
        "╔" + "═" * 78 + "╗\n" +
        "║{:^78}║\n".format("Inicializando...") +
        "╟" + "─" * 78 + "╢\n" +
        "║{:78}║\n".format("Este sistema usa uma interface em modo texto.") +
        "║{:78}║\n".format("Maximize a janela para melhor experiência.") +
        "║{:78}║\n".format("") +
        "╟" + "─" * 78 + "╢\n" +
        "║{:78}║\n".format("Trabalho apresentado no contexto da disciplina de") +
        "║{:78}║\n".format("Paradigmas de Linguagens de Programação do curso de") +
        "║{:78}║\n".format("Bacharelado em Engenharia de Software da Faculdade Uniguaçu.") +
        "║{:78}║\n".format("") +
        "╟" + "─" * 78 + "╢\n" +
        "║{:^78}║\n".format("Acadêmicos") +
        "║{:78}║\n".format("") +
        "║{:78}║\n".format(" - MATHEUS DE ALMEIDA BOAVA") +
        "║{:78}║\n".format(" - TAÍS MAYME FERRARI") +
        "║{:78}║\n".format(" - RAFAEL RODRIGUES PICHIBINSKI") +
        "║{:78}║\n".format("") +
        "╚" + "═" * 78 + "╝\n" +
        "\nSão Miguel do Iguaçu/PR, 30 de junho de 2025.\n" +
        "\nPressione ENTER para iniciar...\n"
    )

    # Inicia o aplicativo de login
    try:
        app = LoginApp()
        app.run()

    # Caso a janela do terminal seja muito pequena, exibe uma mensagem de erro.
    # Isso evita que o usuário veja uma tela de erro padrão do npyscreen, o que interfere na experiência do usuário.
    except npyscreen.wgwidget.NotEnoughSpaceForWidget:
        print("\n[ERRO] A janela do terminal está muito pequena para rodar o sistema.")
        input("Pressione ENTER para sair...")
