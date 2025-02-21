chamados = []
contador_id = 1


def cadastrar_chamado(descricao, prioridade):
    global contador_id
    chamado = {
        'id': contador_id,
        'descricao': descricao,
        'prioridade': prioridade,
        'status': 'Aberto',
    }
    chamados.append(chamado)
    contador_id += 1
    print(f'Chamado {chamado['id']} inserido!')


def buscar_chamado(termo):
    resultado = []
    for i in chamados:
        if termo == str(i['id']) or termo.lower() in i['descricao'].lower():
            resultado.append(i)
    if resultado:
        for c in resultado:
            print(
                f'ID: {c['id']}, Descrição: {c['descricao']}, Prioridade: {c['prioridade']}, Status: {c['status']}')
    else:
        print('Nenhum chamado encontrado...')


def remover_chamado(id_chamado):
    for i in chamados:
        if i['id'] == id_chamado:
            chamados.remove(i)
            print(f'Chamado {id_chamado} removido!')
            return
    print(f'chamado {id_chamado} não encontrado')


def listar_chamados():
    if not chamados:
        print('Nenhum chamado cadastrado.')
    else:
        for c in sorted(chamados, key=lambda x: x['prioridade']):
            print(
                f'ID: {c['id']}, Descrição: {c['descricao']}, Prioridade: {c['prioridade']}, Status: {c['status']}')


def exibir_estadisticas():
    abertos = 0
    for i in chamados:
        if i['status'] == 'Aberto':
            abertos += 1
    finalizados = len(chamados) - abertos
    print(
        f'Total: {len(chamados)}, Chamados abertos: {abertos}, Chamados finalizados: {finalizados}')


def reverter_lista():
    chamados.reverse()
    print('Lista revertida!')


def limpar_lista():
    chamados.clear()
    print("Lista limpa!")


def finalizar_chamado(id_finalizar):
    for i in chamados:
        if i['id'] == id_finalizar:
            i['status'] = 'finalizado'
            print(f'Chamado {id_finalizar} finalizado!')
            return
    print(f'Chamado {id_finalizar} não encontrado')


while True:
    print("\n-+-+- Sistema de Chamados -+-+-")
    print("1. Cadastrar Chamado")
    print("2. Buscar Chamado")
    print("3. Remover Chamado")
    print("4. Listar Chamados")
    print("5. Exibir Estatísticas")
    print("6. Reverter Lista")
    print("7. Limpar Lista")
    print("8. Finalizar Chamado")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        descricao = input('Descrição: ')
        prioridade = int(input('Prioridade 1-3 (1 é maior e 3 menor): '))
        cadastrar_chamado(descricao, prioridade)
    elif opcao == '2':
        termo = input('Digite ID ou descrição: ')
        buscar_chamado(termo)
    elif opcao == '3':
        id_chamado = int(input('Digite o ID do chamado para remover: '))
        remover_chamado(id_chamado)
    elif opcao == '4':
        listar_chamados()
    elif opcao == '5':
        exibir_estadisticas()
    elif opcao == '6':
        reverter_lista()
    elif opcao == '7':
        desicao = input("Quer limpar a lista? (S/N): ")
        if desicao.lower() == 's':
            limpar_lista()
        elif desicao.lower() == 'n':
            continue
    elif opcao == '8':
        id_finalizar = int(input("Digite o ID do chamado para finalizar: "))
        finalizar_chamado(id_finalizar)
    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção invalida')
