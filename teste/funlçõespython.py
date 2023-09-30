class Estudante:
    def __init__(self, nome="", email="", matricula=0, curso=""):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.curso = curso
        self.cursos = []

    def __str__(self):
        return f"Nome: {self.nome}\nEmail: {self.email}\nMatricula: {self.matricula}\nCurso: {self.curso}"



def menu():
    estudantes = []
    while True:
        try:
            print(" 1 - Adicionar estudante\n 2 - Editar estudante\n 3 - Listar Cursos do estudante\n 4 - Editar cursos do estudante\n 5 - Mostrar estudantes\n 6 - Sair")
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite a opção certa :) ")
            menu()   
        if opcao == 1:
            try:
                nome = input("Digite o nome do estudante: ")
                email = input("Digite o email do estudante: ")
                matricula = int(input("Digite a matricula do estudante: "))
                curso = input("Digite o curso do estudante: ")
                estudante = Estudante(nome, email, matricula, curso)
                print("Você deseja adicionar cursos ao estudante ? 1 - Sim 2 - Nao")
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    i = int(input("Quantos cursos deseja adicionar? "))            
                    cursos = []
                    for j in range(i):
                        nomecurso = input("Qual o nome do curso: ")
                        estudante.cursos.append(nomecurso)
                estudantes.append(estudante)
            except ValueError:
                print("Opção invalida, tente novamente")
                menu()            

        elif opcao == 2:
            try:
                matricula = int(input("Digite a matricula do estudante: "))
                for estudante in estudantes:
                    if estudante.matricula == matricula:
                        nome = input("Digite o nome do estudante: ")
                        email = input("Digite o email do estudante: ")
                        matricula = int(input("Digite a matricula do estudante: "))
                        curso = input("Digite o curso do estudante: ")
                        estudante.nome = nome
                        estudante.email = email
                        estudante.matricula = matricula
                        estudante.curso = curso
                    else:
                        print("Estudante não encontrado")
            except ValueError:
                print("Somente numeros")
                menu()   
        elif opcao == 3:
            try:
                matricula = int(input("Digite a matricula do estudante: "))
                for estudante in estudantes:
                    if estudante.matricula == matricula:
                        for i in estudante.cursos:
                            print(f"O {estudante.nome} está matriculado no curso: ",i)
                    else:
                        print("Estudante não encontrado")
            except ValueError:
                print("Somente numeros, na matricula, tente novamente")
                menu()   
        elif opcao == 4:
            try: 
                matricula = int(input("Digite a matricula do estudante: "))
                for estudante in estudantes:
                    if estudante.matricula == matricula:
                        print(" 1 - Se deseja incrementar cursos ao aluno\n 2 - Se deseja decrementar cursos ao aluno")
                        opc = int(input("Escolha uma opção: "))
                        if opc == 1:
                            i = int(input("Quantos cursos deseja adicionar? "))
                            for j in range(i):
                                nomecurso = input("Qual o nome do curso: ")
                                estudante.cursos.append(nomecurso)
                        elif opc == 2:
                            i = int(input("Quantos cursos deseja remover? "))
                            for j in range(i):
                                nomecurso = input("Qual o nome do curso: ")
                                estudante.cursos.remove(nomecurso)
                    else:
                        print("Estudante não encontrado")
            except ValueError:
                print("Somente numeros, na matricula, tente novamente")
                menu()   
        elif opcao == 5:
            for estudante in estudantes:
                print(estudante)
        elif opcao == 6:
            break
        else:
            print("Opção Invalida")
menu()
