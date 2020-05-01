import json


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
            idade = input('Informe sua idade: ')
            email = input('Informe o seu email: ')
            senha = input('Informe a sua senha: ')
            nSenha = input('Confirme a sua senha: ')

            if senha != nSenha:
                print('As senhas não coincidem!')
                continue

            while True:
                print('Confirme suas informações')
                print(f'Nome: {name}\nIdade: {idade}\nEmail: {email}')
                opc = int(input('[1] - Prosseguir\n[2] - Refazer cadastro\n'))

                if opc not in (1, 2):
                    continue

                if opc == 2:
                    return

                dic[name] = {}
                dic[name].update({'email': email, 'idade': idade})

    def sign_in(self):
        pass

    def save_json(self, dic):

        with open('cadastros.json', 'a+') as file:
            file.seek(0, 0)

            # Ler o json existente no arquivo
            json_atual = file.read()

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
