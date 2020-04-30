class Login:

    def menu(self):
        print('Bem vindo\n')

        while True:
            opc = int(input('[1] - Sign in\n [2] - Sign Up\n[3] - Exit\n'))

            if opc not in (1, 2, 3):
                continue

            if opc == 1:
                pass

            elif opc == 2:
                pass

            else:
                pass

    def sign_up(self):
        while True:
            name = input('Informe o seu nome completo: ')
            email = input('Informe o seu email: ')
            senha = input('Informe a sua senha: ')
            nSenha = input('Confirme a sua senha: ')

            if senha != nSenha:
                print('As senhas não coincidem!')
                continue

    def sign_in(self):
        pass
