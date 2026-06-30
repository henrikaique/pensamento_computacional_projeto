'''
>>projeto industria de automoveis
'''
 # Inicializando as variáveis para o Produto 1 (vazio)
p1_nome = "Porshe 911 Turbo S"
p1_estoque = 5
p1_preco = 2.125000
p1_ano = "10/02/2026"
p1_descrição = "Carro Esportivo que pode te entergar mais de 700 cavalos de potência." 

# Inicializando as variáveis para o Produto 2 (vazio)
p2_nome = "Chevrolet Corvette C7"
p2_estoque = 2
p2_preco = 700.000
p2_ano = "14/01/2019"
p2_descricao = "Carro SuperEsportivo de tração traseira que pode te entregar um motor v8 chegando de 0 a 100 em 3 segundos"

# Inicializando as variáveis para o Produto 3 (vazio)
p3_nome = "Nissan Skyline GT-R R34"
p3_estoque = 2
p3_preco = 2.000000
p3_ano = "15/02/2002"
p3_descricao = "Carro Esportivo "


#Ufa, quebrei a maldição
# print('Olá, Mundo!')
while True:
    print('-' * 48 + '\n')
    print('Bem-vindo ao Sistema de vendas - industria de automoveis!\n')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Realizar vendas')
    print('4 - Buscar veiculos')
    print('5 - Buscar por Ano')
    print('6 - Financiamento ')
    print('7 - Estoque')
    print('8 - Agenda de visitas')
    print('9 - Sobre')
    print('0 - Sair do Sistema')
    print('\n------------------------------------------\n')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == '1':
        print('Cadastrando produto...\n')
    # faça a logica para cadastrae produto aqui,
    ## e somente a inserção dos dados usando input e os tipos de dados.
    if  p1_nome == "Porshe 911 Turbo S":
        p1_nome == input('Digite o nome do produto: ')
        p1_estoque = int(input('Digite a quantidade em estoque: '))
        p1_preco = float(input('Digite o preço do produto: '))
        p1_ano = input('Digite o ano do produto: ')
        p1_descricao = input('Digite a descrição do produto: ')
        print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')

    elif p2_nome == "Chevrolet Corvette C7":
        p2_nome = input('Digite o nome do produto: ')
        p2_estoque = int(input('Digite a quantidade em estoque: '))
        p2_preco = float(input('Digite o preço do produto: '))
        p2_ano = input('Digite a validade do produto: ')    
        p2_descricao = input('Digite a descrição do produto: ')
        print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')

    elif p3_nome == "Nissan Skyline GT-R R34":
        p3_nome = input('Digite o nome do produto: ')
        p3_estoque = int(input('Digite a quantidade em estoque: '))
        p3_preco = float(input('Digite o preço do produto: '))
        p3_validade = input('Digite a validade do produto: ')    
        p3_descricao = input('Digite a descrição do produto: ')
        print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')
        

    elif opcao == '2':
        print('Listando produtos...')   
    if p1_nome == "Porshe 911 Turbo S" and p2_nome == "Chevrolet Corvette C7" and p3_nome == "Nissan Skyline GT-R R34":
        
       
# Mostra o Produto 1 se ele existir
        if p1_nome != "Porshe 911 Turbo S":
                print(f"Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")

                print(f"Validade: {p1_ano} | Descrição: {p1_descricao}")

                print('🔥' * 30)

            # Mostra o Produto 2 se ele existir
    if p2_nome != "Chevrolet Corvette C7":

                print(f"Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")

                print(f"Validade: {p2_ano} | Descrição: {p2_descricao}")

                print('🔥' * 30)    

             # Mostra o Produto 3 se ele existir
    if p3_nome != "Nissan Skyline GT-R R34":

                print(f"Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")

                print(f"Validade: {p3_validade} | Descrição: {p3_descricao}")

                print('🔥' * 30)          

    elif opcao == '3':
        print('Realizando venda...') 
        
    if p1_nome == "Porshe 911 Turbo S" and p2_nome == "Chevrolet Corvette C7" and p3_nome == "Nissan Skyline GT-R R34":
            print(f'Não há produtos cadastrados para realizar vendas.')

    else:
            nome_venda = input('Digite o nome do produto que deseja vender: ')

            # Testamos o nome digitado contra o Produto 1
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "Porshe 911 Turbo S":
                qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')

                     # Testamos contra o Produto 2
            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "Chevrolet Corvette C7":
                qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))
                if qtd_venda <= p2_estoque:
                    p2_estoque -= qtd_venda
                    total = qtd_venda * p2_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')

                    # Testamos contra o Produto 3
            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "Nissan Skyline GT-R R34":
                qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))
                if qtd_venda <= p3_estoque:
                    p3_estoque -= qtd_venda
                    total = qtd_venda * p3_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')

            else:
                print('🔥 Erro: Produto não encontrado!')






