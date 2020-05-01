import json
from os import system


class Login:

    def menu(self):
        print('Bem vindo\n')

        while True:
            print('[1] - Sign in\n[2] - Sign Up\n[3] - Exit\n')
            opc = int(input('Escolha: '))

            if opc not in (1, 2, 3):
                system('clear')
                continue

            if opc == 1:
                system('clear')
                self.sign_in()

            elif opc == 2:
                system('clear')
                self.sign_up()

            else:
                break

    def sign_up(self):
        while True:
            name = input('Informe o seu nome completo: ')
            idade = input('Informe sua idade: ')
            email = input('Informe o seu email: ')
            senha = input('Informe a sua senha: ')
            nSenha = input('Confirme a sua senha: ')

            if senha != nSenha:
                print('As senhas não coincidem!')
                continue

            while True:
                system('clear')

                print('\nConfirme suas informações')
                print(f'Nome: {name}\nIdade: {idade}\nEmail: {email}')
                opc = int(input('[1] - Prosseguir\n[2] - Refazer cadastro\n'))

                if opc not in (1, 2):
                    continue

                if opc == 2:
                    return

                dic = {}
                dic[email] = {}
                dic[email].update(
                    {'nome': name, 'idade': idade, 'senha': senha})

                self.save_json(dic)
                print('Inscrito com sucesso.')
                return

    def sign_in(self):
        email = input('Email: ')
        senha = input('Senha: ')

        login = self.checkLogin(email, senha)

        system('clear')
        if login:
            print('Você está cadastrado.')

        else:
            print('Credenciais incorretas.')

    def save_json(self, dic):

        with open('cadastros.json', 'a+') as file:
            file.seek(0, 0)

            # Ler o json existente no arquivo
            json_atual = file.read()

            # Ver se o arquivo não está vazio
            if json_atual:
                # Converter o json do arquivo em dicionario
                dic_atual = json.loads(json_atual)

                dic_atual.update(dic)

            else:
                dic_atual = dic

            # Limpar o arquivo
            file.seek(0, 0)
            file.truncate()

            file.write(json.dumps(dic_atual, indent=True))

    def checkLogin(self, email, password):

        with open('cadastros.json', 'a+') as file:
            file.seek(0, 0)

            dic = file.read()

            if dic:

                dic_atual = json.loads(dic)

                if email not in dic_atual:
                    return False

                if password != dic_atual[email]['senha']:
                    return False

                file.seek(0, 0)
                return True

            else:
                print('Não há usuários cadastrados.')

            file.seek(0, 0)
