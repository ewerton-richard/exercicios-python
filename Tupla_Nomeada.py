from collections import namedtuple


def cadastro():
    cadastrando = namedtuple('Funcionario', ['Matrícula', 'Nome', 'Departamento', 'Cargo'])
    matricula = (input('\nDigite a matrícula do funcionário a ser cadastrado: ')).upper()
    nome = input('Digite o nome completo do funcionário: ').upper()
    departamento = input('Digite o departamento atuante: ').upper()
    cargo = input('Digite o cargo ocupado: ').upper()
    print(f'\nOk. O funcionário "{nome}" foi cadastrado.')
    livro.append(cadastrando(matricula, nome, departamento, cargo))


def consulta_matricula():
    consulta = str(input('\nOk. Por favor, digite a matrícula: '))
    verificador = False
    for funcionarios in livro:
        if consulta == (funcionarios[0]):
            verificador = True
            return (funcionarios)
    if not verificador:
        return ('\nFuncionário não encontrado. Retornando ao menu...')


def deletar():
    apagar = str(input('\nDigite a matrícula do funcionário que será deletado: ')).upper()
    verificador = False
    for funcionarios in livro:
        if apagar == (funcionarios[0]):
            livro.remove(funcionarios)
            verificador = True
            return (f'\nO funcionário com a matrícula {apagar} foi removido do banco de dados.')
    if not verificador:
        return ('Funcionário não encontrado. Retornando ao menu...\n')


def consulta_chave(opcao):
    encontrados = []
    while True:
        busca = str(input('\nAgora digite o termo a ser pesquisado ou sair para cancelar: ')).upper()
        verificador = False

        if busca.lower() == 'sair':
            break

        for funcionarios in livro:
            if busca in funcionarios[opcao - 1]:
                encontrados.append(funcionarios)
                verificador = True

        if not verificador:
            print('Funcionário não encontrado.')
        else:
            break
    return sorted(encontrados, key=lambda funcionario: funcionario[1])


livro = []
while True:
    escolha = int(input('\n-----------------------------MENU----------------------------\n1 para cadastrar funcionário,'
                        '\n2 para listar todos os funcionários,\n3 para consultar funcionário por matrícula,'
                        '\n4 para consultar funcionário utilizando uma informação imprecisa,\n5 para apagar funcionário'
                        '\n0 para sair\n-->: '))

    if escolha == 1:
        cadastro()

    elif escolha == 2:
        if not livro:
            print('\nNenhum funcionário cadastrado. Retornando ao Menu...')
        else:
            print('\nOs funcionários cadastrados são:\n')
            for i in sorted(livro, key=lambda funcionario: funcionario[1]):
                print(i)

    elif escolha == 3:
        if not livro:
            print('\nNenhum funcionário cadastrado. Retornando ao Menu...')
            continue
        print(consulta_matricula())

    elif escolha == 4:
        if not livro:
            print('\nNenhum funcionário cadastrado. Retornando ao Menu...')
            continue
        while True:
            opcao = int(input('\nDigite:\n1 para consultar utilizando a matrícula,\n2 para consultar utilizando o nome,'
                              '\n3 para consultar utilizando o departamento,\n4 para pesquisar utilizando o cargo,'
                              '\n0 para cancelar\n-->: '))
            if opcao > 4 or opcao < 0:
                print('Opção inválida. Por favor, selecione uma das opções listadas.')
                continue
            else:
                break
        if opcao == 0:
            print('Cancelando a consulta e retornado ao Menu...')
            continue
        funcionarios = (consulta_chave(opcao))
        print('\nOs funcinários que correspondem a essa pesquisa são:\n')
        for itens in funcionarios:
            print(itens)

    elif escolha == 5:
        print(deletar())

    elif escolha == 0:
        print('\nEncerrando...')
        break
